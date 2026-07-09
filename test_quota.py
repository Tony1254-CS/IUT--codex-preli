import urllib.request
import urllib.error
import json
from datetime import datetime, timedelta, timezone

BASE_URL = "http://localhost:8000"

def _future(hours: int) -> str:
    return (datetime.now(timezone.utc) + timedelta(hours=hours)).replace(
        minute=0, second=0, microsecond=0
    ).isoformat()

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
            return response.status, response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode('utf-8')
    except Exception as e:
        return 0, str(e)

def test_quota():
    org = "test_quota_org2"
    make_request("POST", "/auth/register", json_body={"org_name": org, "username": "admin", "password": "pw"})
    st, body = make_request("POST", "/auth/login", json_body={"org_name": org, "username": "admin", "password": "pw"})
    token = json.loads(body)["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    st, body = make_request("POST", "/rooms", headers=headers, json_body={"name": "Room Q", "capacity": 10, "hourly_rate_cents": 1000})
    room_id = json.loads(body)["id"]
    
    print("Booking 1:", make_request("POST", "/bookings", headers=headers, json_body={"room_id": room_id, "start_time": _future(1), "end_time": _future(2)})[0])
    print("Booking 2:", make_request("POST", "/bookings", headers=headers, json_body={"room_id": room_id, "start_time": _future(3), "end_time": _future(4)})[0])
    print("Booking 3:", make_request("POST", "/bookings", headers=headers, json_body={"room_id": room_id, "start_time": _future(5), "end_time": _future(6)})[0])
    
    st, body = make_request("POST", "/bookings", headers=headers, json_body={"room_id": room_id, "start_time": _future(7), "end_time": _future(8)})
    print("Booking 4:", st, body)

if __name__ == "__main__":
    test_quota()
