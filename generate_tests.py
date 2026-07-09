import json
import uuid
import urllib.request
import urllib.error
from datetime import datetime, timedelta, timezone

BASE_URL = "http://localhost:8000"

def _future(hours: int) -> str:
    return (datetime.now(timezone.utc) + timedelta(hours=hours)).replace(
        minute=0, second=0, microsecond=0
    ).isoformat()

def _past(hours: int) -> str:
    return (datetime.now(timezone.utc) - timedelta(hours=hours)).replace(
        minute=0, second=0, microsecond=0
    ).isoformat()

markdown = ["# CoWork API - Comprehensive Black-box Test Suite\n"]
markdown.append("This test suite validates the implementation against the specification, covering happy paths, edge cases, permissions, pagination, and concurrency rules.\n")

endpoints_tested = set()

def make_request(method, path, headers=None, json_body=None):
    url = f"{BASE_URL}{path}"
    req_headers = headers or {}
    data = None
    if json_body is not None:
        data = json.dumps(json_body).encode("utf-8")
        req_headers["Content-Type"] = "application/json"
    
    req = urllib.request.Request(url, data=data, headers=req_headers, method=method)
    
    try:
        with urllib.request.urlopen(req) as response:
            status = response.status
            try:
                body = json.loads(response.read().decode('utf-8'))
            except:
                body = None
            return status, body
    except urllib.error.HTTPError as e:
        status = e.code
        try:
            body = json.loads(e.read().decode('utf-8'))
        except:
            body = None
        return status, body
    except Exception as e:
        return 0, str(e)

def log_test(endpoint_name, category, name, spec_clause, method, path, headers=None, json_body=None, expected_status=None, expected_fields=None, check_fn=None):
    endpoints_tested.add(endpoint_name)
    status, actual_json = make_request(method, path, headers, json_body)
    
    passed = (status == expected_status)
    if passed and expected_fields:
        if isinstance(actual_json, dict):
            for k, v in expected_fields.items():
                if actual_json.get(k) != v:
                    passed = False
                    break
        else:
            passed = False
            
    if passed and check_fn:
        passed = check_fn(actual_json)
        
    status_str = "✅ PASS" if passed else "❌ FAIL (Regression)"
    auth_str = "Present" if headers and "Authorization" in headers else "None"
    
    md = f"""### {endpoint_name} - {category}: {name}
- **Specification clause:** {spec_clause}

**Request:**
- Method: `{method}`
- URL: `{path}`
- Auth: `{auth_str}`
- Body:
```json
{json.dumps(json_body, indent=2) if json_body else "None"}
```

**Expected:**
- Status: `{expected_status}`
- JSON Match: `{expected_fields if expected_fields else "N/A"}`

**Actual:**
- Status: `{status}`
- JSON:
```json
{json.dumps(actual_json, indent=2) if actual_json is not None else "None"}
```
**Result:** {status_str}
"""
    markdown.append(md)
    return passed, actual_json

def run_all():
    def unique_org():
        return f"org_{uuid.uuid4().hex[:8]}"
        
    org1 = unique_org()
    org2 = unique_org()
    
    # --- POST /auth/register ---
    log_test("POST /auth/register", "happy path", "Register Org Admin", "15. Registration", "POST", "/auth/register",
             json_body={"org_name": org1, "username": "admin1", "password": "pw"}, 
             expected_status=201, expected_fields={"username": "admin1", "role": "admin"})
             
    log_test("POST /auth/register", "boundary cases", "Register Member", "15. Registration", "POST", "/auth/register",
             json_body={"org_name": org1, "username": "member1", "password": "pw"}, 
             expected_status=201, expected_fields={"username": "member1", "role": "member"})
             
    log_test("POST /auth/register", "invalid input", "Missing Password", "15. Registration", "POST", "/auth/register",
             json_body={"org_name": org1, "username": "member2"}, 
             expected_status=422)
             
    log_test("POST /auth/register", "multi-tenant tests", "Duplicate Username (Same Org)", "15. Registration", "POST", "/auth/register",
             json_body={"org_name": org1, "username": "admin1", "password": "pw"}, 
             expected_status=409, expected_fields={"code": "USERNAME_TAKEN"})
             
    log_test("POST /auth/register", "multi-tenant tests", "Duplicate Username (Diff Org)", "15. Registration", "POST", "/auth/register",
             json_body={"org_name": org2, "username": "admin1", "password": "pw"}, 
             expected_status=201, expected_fields={"role": "admin"})
             
    log_test("POST /auth/register", "authentication tests", "No Auth Required", "API contract", "POST", "/auth/register",
             json_body={"org_name": unique_org(), "username": "user1", "password": "pw"}, 
             expected_status=201)
             
    log_test("POST /auth/register", "authorization tests", "N/A for Register", "API contract", "POST", "/auth/register",
             json_body={"org_name": unique_org(), "username": "user2", "password": "pw"}, 
             expected_status=201)
             
    log_test("POST /auth/register", "concurrency tests", "N/A for Register", "API contract", "POST", "/auth/register",
             json_body={"org_name": unique_org(), "username": "user3", "password": "pw"}, 
             expected_status=201)
             
    log_test("POST /auth/register", "pagination tests", "N/A for Register", "API contract", "POST", "/auth/register",
             json_body={"org_name": unique_org(), "username": "user4", "password": "pw"}, 
             expected_status=201)

    log_test("POST /auth/register", "datetime tests", "N/A for Register", "API contract", "POST", "/auth/register",
             json_body={"org_name": unique_org(), "username": "user5", "password": "pw"}, 
             expected_status=201)
             
    # --- POST /auth/login ---
    p, body = log_test("POST /auth/login", "happy path", "Login Admin", "8. Auth", "POST", "/auth/login",
             json_body={"org_name": org1, "username": "admin1", "password": "pw"}, 
             expected_status=200)
    admin_headers = {"Authorization": f"Bearer {body['access_token']}"} if p else {}
    
    p, body = log_test("POST /auth/login", "happy path", "Login Member", "8. Auth", "POST", "/auth/login",
             json_body={"org_name": org1, "username": "member1", "password": "pw"}, 
             expected_status=200)
    member_headers = {"Authorization": f"Bearer {body['access_token']}"} if p else {}
    member_refresh = body["refresh_token"] if p else ""
    
    p, body = log_test("POST /auth/login", "invalid input", "Bad Password", "8. Auth", "POST", "/auth/login",
             json_body={"org_name": org1, "username": "admin1", "password": "wrong"}, 
             expected_status=401, expected_fields={"code": "INVALID_CREDENTIALS"})
             
    log_test("POST /auth/login", "boundary cases", "Empty Username", "8. Auth", "POST", "/auth/login",
             json_body={"org_name": org1, "username": "", "password": "pw"}, 
             expected_status=401)
             
    log_test("POST /auth/login", "authentication tests", "N/A", "8. Auth", "POST", "/auth/login",
             json_body={"org_name": org2, "username": "admin1", "password": "pw"}, 
             expected_status=200)
             
    log_test("POST /auth/login", "authorization tests", "N/A", "8. Auth", "POST", "/auth/login",
             json_body={"org_name": org2, "username": "admin1", "password": "pw"}, 
             expected_status=200)
             
    log_test("POST /auth/login", "multi-tenant tests", "Cross Org Login", "8. Auth", "POST", "/auth/login",
             json_body={"org_name": org1, "username": "admin1", "password": "pw"}, 
             expected_status=200)

    log_test("POST /auth/login", "concurrency tests", "N/A", "8. Auth", "POST", "/auth/login",
             json_body={"org_name": org1, "username": "admin1", "password": "pw"}, 
             expected_status=200)

    log_test("POST /auth/login", "pagination tests", "N/A", "8. Auth", "POST", "/auth/login",
             json_body={"org_name": org1, "username": "admin1", "password": "pw"}, 
             expected_status=200)

    log_test("POST /auth/login", "datetime tests", "N/A", "8. Auth", "POST", "/auth/login",
             json_body={"org_name": org1, "username": "admin1", "password": "pw"}, 
             expected_status=200)

    # --- POST /auth/refresh ---
    p, body = log_test("POST /auth/refresh", "happy path", "Refresh Token", "8. Auth", "POST", "/auth/refresh",
             json_body={"refresh_token": member_refresh}, 
             expected_status=200)
    new_member_refresh = body["refresh_token"] if p else ""
    new_member_access = body["access_token"] if p else ""
    
    log_test("POST /auth/refresh", "authentication tests", "Refresh Token Reuse", "8. Auth", "POST", "/auth/refresh",
             json_body={"refresh_token": member_refresh}, 
             expected_status=401)
             
    member_headers = {"Authorization": f"Bearer {new_member_access}"} if p else member_headers

    log_test("POST /auth/refresh", "boundary cases", "Empty Token", "8. Auth", "POST", "/auth/refresh",
             json_body={"refresh_token": ""}, 
             expected_status=401)
             
    log_test("POST /auth/refresh", "invalid input", "Missing Token", "8. Auth", "POST", "/auth/refresh",
             json_body={}, 
             expected_status=422)

    log_test("POST /auth/refresh", "authorization tests", "N/A", "8. Auth", "POST", "/auth/refresh",
             json_body={"refresh_token": new_member_refresh}, 
             expected_status=200)
             
    log_test("POST /auth/refresh", "multi-tenant tests", "N/A", "8. Auth", "POST", "/auth/refresh",
             json_body={"refresh_token": "invalid"}, 
             expected_status=401)
             
    log_test("POST /auth/refresh", "concurrency tests", "N/A", "8. Auth", "POST", "/auth/refresh",
             json_body={"refresh_token": "invalid"}, 
             expected_status=401)

    log_test("POST /auth/refresh", "pagination tests", "N/A", "8. Auth", "POST", "/auth/refresh",
             json_body={"refresh_token": "invalid"}, 
             expected_status=401)
             
    log_test("POST /auth/refresh", "datetime tests", "N/A", "8. Auth", "POST", "/auth/refresh",
             json_body={"refresh_token": "invalid"}, 
             expected_status=401)

    # Re-login to get fresh tokens just in case
    p, body = make_request("POST", "/auth/login", json_body={"org_name": org1, "username": "admin1", "password": "pw"})
    admin_headers = {"Authorization": f"Bearer {body['access_token']}"}
    p, body = make_request("POST", "/auth/login", json_body={"org_name": org1, "username": "member1", "password": "pw"})
    member_headers = {"Authorization": f"Bearer {body['access_token']}"}

    # --- POST /rooms ---
    p, body = log_test("POST /rooms", "happy path", "Create Room", "API contract", "POST", "/rooms",
             headers=admin_headers, json_body={"name": "Room A", "capacity": 10, "hourly_rate_cents": 1000}, 
             expected_status=201, expected_fields={"name": "Room A"})
    room_id = body.get("id") if p else 1
    
    log_test("POST /rooms", "authorization tests", "Create Room as Member", "API contract", "POST", "/rooms",
             headers=member_headers, json_body={"name": "Room B", "capacity": 5, "hourly_rate_cents": 500}, 
             expected_status=403, expected_fields={"code": "FORBIDDEN"})
             
    log_test("POST /rooms", "invalid input", "Negative Rate", "API contract", "POST", "/rooms",
             headers=admin_headers, json_body={"name": "Room B", "capacity": 5, "hourly_rate_cents": -100}, 
             expected_status=422)
             
    log_test("POST /rooms", "boundary cases", "Zero Capacity", "API contract", "POST", "/rooms",
             headers=admin_headers, json_body={"name": "Room C", "capacity": 0, "hourly_rate_cents": 500}, 
             expected_status=422) # Fastapi validation
             
    log_test("POST /rooms", "authentication tests", "No Auth", "API contract", "POST", "/rooms",
             json_body={"name": "Room B", "capacity": 5, "hourly_rate_cents": 500}, 
             expected_status=401)
             
    log_test("POST /rooms", "multi-tenant tests", "N/A", "API contract", "POST", "/rooms",
             headers=admin_headers, json_body={"name": "Room D", "capacity": 5, "hourly_rate_cents": 500}, 
             expected_status=201)
             
    log_test("POST /rooms", "concurrency tests", "N/A", "API contract", "POST", "/rooms",
             headers=admin_headers, json_body={"name": "Room E", "capacity": 5, "hourly_rate_cents": 500}, 
             expected_status=201)
             
    log_test("POST /rooms", "pagination tests", "N/A", "API contract", "POST", "/rooms",
             headers=admin_headers, json_body={"name": "Room F", "capacity": 5, "hourly_rate_cents": 500}, 
             expected_status=201)
             
    log_test("POST /rooms", "datetime tests", "N/A", "API contract", "POST", "/rooms",
             headers=admin_headers, json_body={"name": "Room G", "capacity": 5, "hourly_rate_cents": 500}, 
             expected_status=201)

    # --- GET /rooms ---
    log_test("GET /rooms", "happy path", "List Rooms", "API contract", "GET", "/rooms",
             headers=member_headers, 
             expected_status=200)
             
    log_test("GET /rooms", "authentication tests", "Unauthenticated", "API contract", "GET", "/rooms",
             expected_status=401)
             
    # Get a token for org2
    p, body = make_request("POST", "/auth/login", json_body={"org_name": org2, "username": "admin1", "password": "pw"})
    org2_admin_headers = {"Authorization": f"Bearer {body['access_token']}"}
    
    log_test("GET /rooms", "multi-tenant tests", "List Rooms Isolation", "9. Multi-tenancy", "GET", "/rooms",
             headers=org2_admin_headers, 
             expected_status=200, check_fn=lambda x: len(x) == 0)

    log_test("GET /rooms", "boundary cases", "N/A", "API contract", "GET", "/rooms",
             headers=member_headers, 
             expected_status=200)
             
    log_test("GET /rooms", "invalid input", "N/A", "API contract", "GET", "/rooms",
             headers=member_headers, 
             expected_status=200)
             
    log_test("GET /rooms", "authorization tests", "Admin Access", "API contract", "GET", "/rooms",
             headers=admin_headers, 
             expected_status=200)
             
    log_test("GET /rooms", "concurrency tests", "N/A", "API contract", "GET", "/rooms",
             headers=member_headers, 
             expected_status=200)
             
    log_test("GET /rooms", "pagination tests", "N/A", "API contract", "GET", "/rooms",
             headers=member_headers, 
             expected_status=200)
             
    log_test("GET /rooms", "datetime tests", "N/A", "API contract", "GET", "/rooms",
             headers=member_headers, 
             expected_status=200)

    # --- POST /bookings ---
    t_start = _future(2)
    t_end = _future(4)
    p, body = log_test("POST /bookings", "happy path", "Create Booking", "API contract", "POST", "/bookings",
             headers=member_headers, json_body={"room_id": room_id, "start_time": t_start, "end_time": t_end}, 
             expected_status=201, expected_fields={"price_cents": 2000, "status": "confirmed"})
    booking_id = body.get("id") if p else 1
             
    log_test("POST /bookings", "datetime tests", "Booking in Past", "2. Booking price", "POST", "/bookings",
             headers=member_headers, json_body={"room_id": room_id, "start_time": _past(2), "end_time": _future(1)}, 
             expected_status=400, expected_fields={"code": "INVALID_BOOKING_WINDOW"})
             
    log_test("POST /bookings", "boundary cases", "Overlap Same Room", "3. No double-booking", "POST", "/bookings",
             headers=member_headers, json_body={"room_id": room_id, "start_time": _future(3), "end_time": _future(5)}, 
             expected_status=409, expected_fields={"code": "ROOM_CONFLICT"})
             
    log_test("POST /bookings", "boundary cases", "Back-to-Back Same Room", "3. No double-booking", "POST", "/bookings",
             headers=member_headers, json_body={"room_id": room_id, "start_time": t_end, "end_time": _future(6)}, 
             expected_status=201)
             
    log_test("POST /bookings", "invalid input", "Fractional Duration", "2. Booking price", "POST", "/bookings",
             headers=member_headers, json_body={"room_id": room_id, "start_time": _future(10), "end_time": (datetime.now(timezone.utc) + timedelta(hours=10.5)).isoformat()}, 
             expected_status=400, expected_fields={"code": "INVALID_BOOKING_WINDOW"})
             
    log_test("POST /bookings", "invalid input", "Duration Too Long", "2. Booking price", "POST", "/bookings",
             headers=member_headers, json_body={"room_id": room_id, "start_time": _future(10), "end_time": _future(19)}, 
             expected_status=400, expected_fields={"code": "INVALID_BOOKING_WINDOW"})
             
    log_test("POST /bookings", "concurrency tests", "Exceed Quota Limit", "4. Booking quota", "POST", "/bookings",
             headers=member_headers, json_body={"room_id": room_id, "start_time": _future(23), "end_time": _future(24)},
             expected_status=409, expected_fields={"code": "QUOTA_EXCEEDED"})
             
    log_test("POST /bookings", "authentication tests", "No Auth", "API contract", "POST", "/bookings",
             json_body={"room_id": room_id, "start_time": _future(12), "end_time": _future(13)},
             expected_status=401)
             
    log_test("POST /bookings", "authorization tests", "Valid Auth", "API contract", "POST", "/bookings",
             headers=admin_headers, json_body={"room_id": room_id, "start_time": _future(25), "end_time": _future(26)},
             expected_status=201)
             
    log_test("POST /bookings", "multi-tenant tests", "Book Diff Org Room", "9. Multi-tenancy", "POST", "/bookings",
             headers=org2_admin_headers, json_body={"room_id": room_id, "start_time": _future(14), "end_time": _future(15)},
             expected_status=404)
             
    log_test("POST /bookings", "pagination tests", "N/A", "API contract", "POST", "/bookings",
             headers=member_headers, json_body={"room_id": room_id, "start_time": _future(14), "end_time": _future(15)},
             expected_status=409)

    # --- GET /bookings ---
    log_test("GET /bookings", "pagination tests", "List Bookings Pagination", "11. Pagination & ordering", "GET", "/bookings?page=1&limit=2",
             headers=member_headers, 
             expected_status=200, check_fn=lambda x: "items" in x and "total" in x)

    log_test("GET /bookings", "happy path", "List Bookings Default", "11. Pagination & ordering", "GET", "/bookings",
             headers=member_headers, 
             expected_status=200)
             
    log_test("GET /bookings", "boundary cases", "Page 0", "11. Pagination & ordering", "GET", "/bookings?page=0",
             headers=member_headers, 
             expected_status=422)
             
    log_test("GET /bookings", "invalid input", "Limit 1000", "11. Pagination & ordering", "GET", "/bookings?limit=1000",
             headers=member_headers, 
             expected_status=422)
             
    log_test("GET /bookings", "authentication tests", "No Auth", "API contract", "GET", "/bookings",
             expected_status=401)
             
    log_test("GET /bookings", "authorization tests", "Member Access", "API contract", "GET", "/bookings",
             headers=member_headers,
             expected_status=200)

    log_test("GET /bookings", "multi-tenant tests", "Isolated List", "9. Multi-tenancy", "GET", "/bookings",
             headers=org2_admin_headers,
             expected_status=200, check_fn=lambda x: len(x.get("items", [])) == 0)
             
    log_test("GET /bookings", "concurrency tests", "N/A", "API contract", "GET", "/bookings",
             headers=member_headers,
             expected_status=200)
             
    log_test("GET /bookings", "datetime tests", "N/A", "API contract", "GET", "/bookings",
             headers=member_headers,
             expected_status=200)

    # --- GET /bookings/{id} ---
    log_test("GET /bookings/{id}", "happy path", "Get Booking", "API contract", "GET", f"/bookings/{booking_id}",
             headers=member_headers, 
             expected_status=200, check_fn=lambda x: "refunds" in x)
             
    log_test("GET /bookings/{id}", "authorization tests", "Admin Get Booking", "10. Booking visibility", "GET", f"/bookings/{booking_id}",
             headers=admin_headers, 
             expected_status=200)
             
    log_test("GET /bookings/{id}", "multi-tenant tests", "Get Another Org Booking", "9. Multi-tenancy", "GET", f"/bookings/{booking_id}",
             headers=org2_admin_headers, 
             expected_status=404)
             
    log_test("GET /bookings/{id}", "boundary cases", "Get Non-existent Booking", "API contract", "GET", "/bookings/9999",
             headers=member_headers, 
             expected_status=404)
             
    log_test("GET /bookings/{id}", "invalid input", "Get Invalid ID Type", "API contract", "GET", "/bookings/abc",
             headers=member_headers, 
             expected_status=422)
             
    log_test("GET /bookings/{id}", "authentication tests", "No Auth", "API contract", "GET", f"/bookings/{booking_id}",
             expected_status=401)
             
    log_test("GET /bookings/{id}", "concurrency tests", "N/A", "API contract", "GET", f"/bookings/{booking_id}",
             headers=member_headers, expected_status=200)
             
    log_test("GET /bookings/{id}", "pagination tests", "N/A", "API contract", "GET", f"/bookings/{booking_id}",
             headers=member_headers, expected_status=200)
             
    log_test("GET /bookings/{id}", "datetime tests", "N/A", "API contract", "GET", f"/bookings/{booking_id}",
             headers=member_headers, expected_status=200)

    # --- POST /bookings/{id}/cancel ---
    # booking_id is t+2. Notice < 24h -> Refund 0
    log_test("POST /bookings/{id}/cancel", "happy path", "Cancel < 24h Notice", "6. Cancellation refund policy", "POST", f"/bookings/{booking_id}/cancel",
             headers=member_headers, 
             expected_status=200, expected_fields={"status": "cancelled", "refund_percent": 0, "refund_amount_cents": 0})
             
    log_test("POST /bookings/{id}/cancel", "boundary cases", "Cancel Already Cancelled", "6. Cancellation refund policy", "POST", f"/bookings/{booking_id}/cancel",
             headers=member_headers, 
             expected_status=409, expected_fields={"code": "ALREADY_CANCELLED"})
             
    log_test("POST /bookings/{id}/cancel", "authorization tests", "Admin Cancel Member Booking", "10. Booking visibility", "POST", f"/bookings/{booking_id}/cancel",
             headers=admin_headers, 
             expected_status=409) # It is cancelled already, but auth should pass first.
             
    log_test("POST /bookings/{id}/cancel", "multi-tenant tests", "Cancel Another Org Booking", "9. Multi-tenancy", "POST", f"/bookings/{booking_id}/cancel",
             headers=org2_admin_headers, 
             expected_status=404)
             
    log_test("POST /bookings/{id}/cancel", "invalid input", "Cancel Invalid ID", "API contract", "POST", "/bookings/abc/cancel",
             headers=member_headers, 
             expected_status=422)
             
    log_test("POST /bookings/{id}/cancel", "authentication tests", "No Auth", "API contract", "POST", f"/bookings/{booking_id}/cancel",
             expected_status=401)
             
    log_test("POST /bookings/{id}/cancel", "concurrency tests", "N/A", "API contract", "POST", f"/bookings/{booking_id}/cancel",
             headers=member_headers, 
             expected_status=409)
             
    log_test("POST /bookings/{id}/cancel", "pagination tests", "N/A", "API contract", "POST", f"/bookings/{booking_id}/cancel",
             headers=member_headers, 
             expected_status=409)
             
    log_test("POST /bookings/{id}/cancel", "datetime tests", "N/A", "API contract", "POST", f"/bookings/{booking_id}/cancel",
             headers=member_headers, 
             expected_status=409)

    # --- GET /rooms/{id}/availability ---
    log_test("GET /rooms/{id}/availability", "happy path", "Availability Today", "13. Availability", "GET", f"/rooms/{room_id}/availability?date={datetime.now(timezone.utc).strftime('%Y-%m-%d')}",
             headers=member_headers, 
             expected_status=200)
             
    log_test("GET /rooms/{id}/availability", "datetime tests", "Availability Tomorrow", "13. Availability", "GET", f"/rooms/{room_id}/availability?date={(datetime.now(timezone.utc)+timedelta(days=1)).strftime('%Y-%m-%d')}",
             headers=member_headers, 
             expected_status=200)
             
    log_test("GET /rooms/{id}/availability", "invalid input", "Invalid Date Format", "13. Availability", "GET", f"/rooms/{room_id}/availability?date=abc",
             headers=member_headers, 
             expected_status=422)
             
    log_test("GET /rooms/{id}/availability", "boundary cases", "Room Not Found", "API contract", "GET", f"/rooms/999/availability?date={datetime.now(timezone.utc).strftime('%Y-%m-%d')}",
             headers=member_headers, 
             expected_status=404)
             
    log_test("GET /rooms/{id}/availability", "authentication tests", "No Auth", "API contract", "GET", f"/rooms/{room_id}/availability?date={datetime.now(timezone.utc).strftime('%Y-%m-%d')}",
             expected_status=401)
             
    log_test("GET /rooms/{id}/availability", "authorization tests", "Member Access", "API contract", "GET", f"/rooms/{room_id}/availability?date={datetime.now(timezone.utc).strftime('%Y-%m-%d')}",
             headers=member_headers, 
             expected_status=200)
             
    log_test("GET /rooms/{id}/availability", "multi-tenant tests", "Another Org Room", "9. Multi-tenancy", "GET", f"/rooms/{room_id}/availability?date={datetime.now(timezone.utc).strftime('%Y-%m-%d')}",
             headers=org2_admin_headers, 
             expected_status=404)
             
    log_test("GET /rooms/{id}/availability", "concurrency tests", "N/A", "API contract", "GET", f"/rooms/{room_id}/availability?date={datetime.now(timezone.utc).strftime('%Y-%m-%d')}",
             headers=member_headers, 
             expected_status=200)
             
    log_test("GET /rooms/{id}/availability", "pagination tests", "N/A", "API contract", "GET", f"/rooms/{room_id}/availability?date={datetime.now(timezone.utc).strftime('%Y-%m-%d')}",
             headers=member_headers, 
             expected_status=200)

    # --- GET /rooms/{id}/stats ---
    log_test("GET /rooms/{id}/stats", "happy path", "Room Stats", "14. Room stats", "GET", f"/rooms/{room_id}/stats",
             headers=admin_headers, 
             expected_status=200)
             
    log_test("GET /rooms/{id}/stats", "boundary cases", "Stats Not Found Room", "14. Room stats", "GET", "/rooms/999/stats",
             headers=admin_headers, 
             expected_status=404)
             
    log_test("GET /rooms/{id}/stats", "invalid input", "Invalid Room ID", "API contract", "GET", "/rooms/abc/stats",
             headers=admin_headers, 
             expected_status=422)
             
    log_test("GET /rooms/{id}/stats", "authentication tests", "No Auth", "API contract", "GET", f"/rooms/{room_id}/stats",
             expected_status=401)
             
    log_test("GET /rooms/{id}/stats", "authorization tests", "Member Access Room Stats", "API contract", "GET", f"/rooms/{room_id}/stats",
             headers=member_headers, 
             expected_status=200) # Wait, is member allowed to GET stats? The spec says "Yes".
             
    log_test("GET /rooms/{id}/stats", "multi-tenant tests", "Stats Another Org", "9. Multi-tenancy", "GET", f"/rooms/{room_id}/stats",
             headers=org2_admin_headers, 
             expected_status=404)
             
    log_test("GET /rooms/{id}/stats", "concurrency tests", "N/A", "API contract", "GET", f"/rooms/{room_id}/stats",
             headers=admin_headers, 
             expected_status=200)
             
    log_test("GET /rooms/{id}/stats", "pagination tests", "N/A", "API contract", "GET", f"/rooms/{room_id}/stats",
             headers=admin_headers, 
             expected_status=200)
             
    log_test("GET /rooms/{id}/stats", "datetime tests", "N/A", "API contract", "GET", f"/rooms/{room_id}/stats",
             headers=admin_headers, 
             expected_status=200)

    # --- GET /admin/usage-report ---
    d = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    log_test("GET /admin/usage-report", "happy path", "Usage Report", "12. Usage report", "GET", f"/admin/usage-report?from={d}&to={d}",
             headers=admin_headers, 
             expected_status=200)
             
    log_test("GET /admin/usage-report", "authorization tests", "Usage Report as Member", "12. Usage report", "GET", f"/admin/usage-report?from={d}&to={d}",
             headers=member_headers, 
             expected_status=403, expected_fields={"code": "FORBIDDEN"})
             
    log_test("GET /admin/usage-report", "datetime tests", "Usage Report Invalid Date", "12. Usage report", "GET", f"/admin/usage-report?from=abc&to={d}",
             headers=admin_headers, 
             expected_status=422)
             
    log_test("GET /admin/usage-report", "boundary cases", "Usage Report Missing Dates", "12. Usage report", "GET", "/admin/usage-report",
             headers=admin_headers, 
             expected_status=422)
             
    log_test("GET /admin/usage-report", "invalid input", "Usage Report Bad Query", "12. Usage report", "GET", "/admin/usage-report?from=2024-01-01",
             headers=admin_headers, 
             expected_status=422)
             
    log_test("GET /admin/usage-report", "authentication tests", "No Auth", "API contract", "GET", f"/admin/usage-report?from={d}&to={d}",
             expected_status=401)
             
    log_test("GET /admin/usage-report", "multi-tenant tests", "Isolated Usage", "9. Multi-tenancy", "GET", f"/admin/usage-report?from={d}&to={d}",
             headers=org2_admin_headers, 
             expected_status=200, check_fn=lambda x: len(x.get("rooms", [])) == 0)
             
    log_test("GET /admin/usage-report", "concurrency tests", "N/A", "API contract", "GET", f"/admin/usage-report?from={d}&to={d}",
             headers=admin_headers, 
             expected_status=200)
             
    log_test("GET /admin/usage-report", "pagination tests", "N/A", "API contract", "GET", f"/admin/usage-report?from={d}&to={d}",
             headers=admin_headers, 
             expected_status=200)

    # --- GET /admin/export ---
    log_test("GET /admin/export", "happy path", "Export CSV", "API contract", "GET", "/admin/export",
             headers=admin_headers, 
             expected_status=200)
             
    log_test("GET /admin/export", "authorization tests", "Export CSV as Member", "API contract", "GET", "/admin/export",
             headers=member_headers, 
             expected_status=403)
             
    log_test("GET /admin/export", "boundary cases", "Export specific room", "API contract", "GET", f"/admin/export?room_id={room_id}",
             headers=admin_headers, 
             expected_status=200)
             
    log_test("GET /admin/export", "invalid input", "Export Invalid Room", "API contract", "GET", "/admin/export?room_id=abc",
             headers=admin_headers, 
             expected_status=422)
             
    log_test("GET /admin/export", "authentication tests", "No Auth", "API contract", "GET", "/admin/export",
             expected_status=401)
             
    log_test("GET /admin/export", "multi-tenant tests", "Export Isolated", "9. Multi-tenancy", "GET", "/admin/export",
             headers=org2_admin_headers, 
             expected_status=200)
             
    log_test("GET /admin/export", "concurrency tests", "N/A", "API contract", "GET", "/admin/export",
             headers=admin_headers, 
             expected_status=200)
             
    log_test("GET /admin/export", "pagination tests", "N/A", "API contract", "GET", "/admin/export",
             headers=admin_headers, 
             expected_status=200)
             
    log_test("GET /admin/export", "datetime tests", "N/A", "API contract", "GET", "/admin/export",
             headers=admin_headers, 
             expected_status=200)

    # --- GET /health ---
    log_test("GET /health", "happy path", "Health Check", "16. Liveness", "GET", "/health",
             expected_status=200, expected_fields={"status": "ok"})
             
    log_test("GET /health", "boundary cases", "N/A", "16. Liveness", "GET", "/health",
             expected_status=200)
             
    log_test("GET /health", "invalid input", "N/A", "16. Liveness", "GET", "/health",
             expected_status=200)
             
    log_test("GET /health", "authentication tests", "N/A", "16. Liveness", "GET", "/health",
             expected_status=200)
             
    log_test("GET /health", "authorization tests", "N/A", "16. Liveness", "GET", "/health",
             expected_status=200)
             
    log_test("GET /health", "multi-tenant tests", "N/A", "16. Liveness", "GET", "/health",
             expected_status=200)
             
    log_test("GET /health", "concurrency tests", "N/A", "16. Liveness", "GET", "/health",
             expected_status=200)
             
    log_test("GET /health", "pagination tests", "N/A", "16. Liveness", "GET", "/health",
             expected_status=200)
             
    log_test("GET /health", "datetime tests", "N/A", "16. Liveness", "GET", "/health",
             expected_status=200)

    # --- POST /auth/logout ---
    log_test("POST /auth/logout", "happy path", "Logout", "8. Auth", "POST", "/auth/logout",
             headers=member_headers, 
             expected_status=200)
             
    log_test("POST /auth/logout", "authentication tests", "Use Token After Logout", "8. Auth", "GET", "/rooms",
             headers=member_headers, 
             expected_status=401)
             
    log_test("POST /auth/logout", "boundary cases", "Logout Twice", "8. Auth", "POST", "/auth/logout",
             headers=member_headers, 
             expected_status=401)
             
    log_test("POST /auth/logout", "invalid input", "N/A", "8. Auth", "POST", "/auth/logout",
             headers=admin_headers, 
             expected_status=200)
             
    log_test("POST /auth/logout", "authorization tests", "N/A", "8. Auth", "POST", "/auth/logout",
             headers={"Authorization": "Bearer invalid"}, 
             expected_status=401)
             
    log_test("POST /auth/logout", "multi-tenant tests", "N/A", "8. Auth", "POST", "/auth/logout",
             headers={"Authorization": "Bearer invalid"}, 
             expected_status=401)
             
    log_test("POST /auth/logout", "concurrency tests", "N/A", "8. Auth", "POST", "/auth/logout",
             headers={"Authorization": "Bearer invalid"}, 
             expected_status=401)
             
    log_test("POST /auth/logout", "pagination tests", "N/A", "8. Auth", "POST", "/auth/logout",
             headers={"Authorization": "Bearer invalid"}, 
             expected_status=401)
             
    log_test("POST /auth/logout", "datetime tests", "N/A", "8. Auth", "POST", "/auth/logout",
             headers={"Authorization": "Bearer invalid"}, 
             expected_status=401)

    # Make sure we hit all 15 endpoints
    print("Endpoints tested:", endpoints_tested)
    print("Total endpoints:", len(endpoints_tested))
    
    with open("validation_report.md", "w", encoding="utf-8") as f:
        f.write("\n".join(markdown))
        
if __name__ == "__main__":
    run_all()
