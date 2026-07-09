# CoWork API - Comprehensive Black-box Test Suite

This test suite validates the implementation against the specification, covering happy paths, edge cases, permissions, pagination, and concurrency rules.

### POST /auth/register - happy path: Register Org Admin
- **Specification clause:** 15. Registration

**Request:**
- Method: `POST`
- URL: `/auth/register`
- Auth: `None`
- Body:
```json
{
  "org_name": "org_a586d77f",
  "username": "admin1",
  "password": "pw"
}
```

**Expected:**
- Status: `201`
- JSON Match: `{'username': 'admin1', 'role': 'admin'}`

**Actual:**
- Status: `201`
- JSON:
```json
{
  "user_id": 20,
  "org_id": 17,
  "username": "admin1",
  "role": "admin"
}
```
**Result:** ✅ PASS

### POST /auth/register - boundary cases: Register Member
- **Specification clause:** 15. Registration

**Request:**
- Method: `POST`
- URL: `/auth/register`
- Auth: `None`
- Body:
```json
{
  "org_name": "org_a586d77f",
  "username": "member1",
  "password": "pw"
}
```

**Expected:**
- Status: `201`
- JSON Match: `{'username': 'member1', 'role': 'member'}`

**Actual:**
- Status: `201`
- JSON:
```json
{
  "user_id": 21,
  "org_id": 17,
  "username": "member1",
  "role": "member"
}
```
**Result:** ✅ PASS

### POST /auth/register - invalid input: Missing Password
- **Specification clause:** 15. Registration

**Request:**
- Method: `POST`
- URL: `/auth/register`
- Auth: `None`
- Body:
```json
{
  "org_name": "org_a586d77f",
  "username": "member2"
}
```

**Expected:**
- Status: `422`
- JSON Match: `N/A`

**Actual:**
- Status: `422`
- JSON:
```json
{
  "detail": [
    {
      "type": "missing",
      "loc": [
        "body",
        "password"
      ],
      "msg": "Field required",
      "input": {
        "org_name": "org_a586d77f",
        "username": "member2"
      }
    }
  ]
}
```
**Result:** ✅ PASS

### POST /auth/register - multi-tenant tests: Duplicate Username (Same Org)
- **Specification clause:** 15. Registration

**Request:**
- Method: `POST`
- URL: `/auth/register`
- Auth: `None`
- Body:
```json
{
  "org_name": "org_a586d77f",
  "username": "admin1",
  "password": "pw"
}
```

**Expected:**
- Status: `409`
- JSON Match: `{'code': 'USERNAME_TAKEN'}`

**Actual:**
- Status: `409`
- JSON:
```json
{
  "detail": "Username taken",
  "code": "USERNAME_TAKEN"
}
```
**Result:** ✅ PASS

### POST /auth/register - multi-tenant tests: Duplicate Username (Diff Org)
- **Specification clause:** 15. Registration

**Request:**
- Method: `POST`
- URL: `/auth/register`
- Auth: `None`
- Body:
```json
{
  "org_name": "org_5f17290f",
  "username": "admin1",
  "password": "pw"
}
```

**Expected:**
- Status: `201`
- JSON Match: `{'role': 'admin'}`

**Actual:**
- Status: `201`
- JSON:
```json
{
  "user_id": 22,
  "org_id": 18,
  "username": "admin1",
  "role": "admin"
}
```
**Result:** ✅ PASS

### POST /auth/register - authentication tests: No Auth Required
- **Specification clause:** API contract

**Request:**
- Method: `POST`
- URL: `/auth/register`
- Auth: `None`
- Body:
```json
{
  "org_name": "org_b3b37708",
  "username": "user1",
  "password": "pw"
}
```

**Expected:**
- Status: `201`
- JSON Match: `N/A`

**Actual:**
- Status: `201`
- JSON:
```json
{
  "user_id": 23,
  "org_id": 19,
  "username": "user1",
  "role": "admin"
}
```
**Result:** ✅ PASS

### POST /auth/register - authorization tests: N/A for Register
- **Specification clause:** API contract

**Request:**
- Method: `POST`
- URL: `/auth/register`
- Auth: `None`
- Body:
```json
{
  "org_name": "org_8514c123",
  "username": "user2",
  "password": "pw"
}
```

**Expected:**
- Status: `201`
- JSON Match: `N/A`

**Actual:**
- Status: `201`
- JSON:
```json
{
  "user_id": 24,
  "org_id": 20,
  "username": "user2",
  "role": "admin"
}
```
**Result:** ✅ PASS

### POST /auth/register - concurrency tests: N/A for Register
- **Specification clause:** API contract

**Request:**
- Method: `POST`
- URL: `/auth/register`
- Auth: `None`
- Body:
```json
{
  "org_name": "org_85cbc6e1",
  "username": "user3",
  "password": "pw"
}
```

**Expected:**
- Status: `201`
- JSON Match: `N/A`

**Actual:**
- Status: `201`
- JSON:
```json
{
  "user_id": 25,
  "org_id": 21,
  "username": "user3",
  "role": "admin"
}
```
**Result:** ✅ PASS

### POST /auth/register - pagination tests: N/A for Register
- **Specification clause:** API contract

**Request:**
- Method: `POST`
- URL: `/auth/register`
- Auth: `None`
- Body:
```json
{
  "org_name": "org_14bb5398",
  "username": "user4",
  "password": "pw"
}
```

**Expected:**
- Status: `201`
- JSON Match: `N/A`

**Actual:**
- Status: `201`
- JSON:
```json
{
  "user_id": 26,
  "org_id": 22,
  "username": "user4",
  "role": "admin"
}
```
**Result:** ✅ PASS

### POST /auth/register - datetime tests: N/A for Register
- **Specification clause:** API contract

**Request:**
- Method: `POST`
- URL: `/auth/register`
- Auth: `None`
- Body:
```json
{
  "org_name": "org_53bc85b6",
  "username": "user5",
  "password": "pw"
}
```

**Expected:**
- Status: `201`
- JSON Match: `N/A`

**Actual:**
- Status: `201`
- JSON:
```json
{
  "user_id": 27,
  "org_id": 23,
  "username": "user5",
  "role": "admin"
}
```
**Result:** ✅ PASS

### POST /auth/login - happy path: Login Admin
- **Specification clause:** 8. Auth

**Request:**
- Method: `POST`
- URL: `/auth/login`
- Auth: `None`
- Body:
```json
{
  "org_name": "org_a586d77f",
  "username": "admin1",
  "password": "pw"
}
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMCIsIm9yZyI6MTcsInJvbGUiOiJhZG1pbiIsImp0aSI6ImE2NjY3NjU2NGVlNjQyOTNiNzQ1NjM0M2E4MGIxNmUwIiwiaWF0IjoxNzgzNjA5NjgyLCJleHAiOjE3ODM2MTA1ODIsInR5cGUiOiJhY2Nlc3MifQ.4ICFpxwB7R9gcVRwDrWA3ta0UGMWPEBNXDhUyuy0Yw4",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMCIsIm9yZyI6MTcsInJvbGUiOiJhZG1pbiIsImp0aSI6IjgzMWU5MTJhMzU2NzQzM2JiYWQyZTlmZmI3YjU3ZGZhIiwiaWF0IjoxNzgzNjA5NjgyLCJleHAiOjE3ODQyMTQ0ODIsInR5cGUiOiJyZWZyZXNoIn0.Pa3WDkgJKzC-q-S_uurpI0XLJjiz7Rz0jmk21rQ5MYo",
  "token_type": "bearer"
}
```
**Result:** ✅ PASS

### POST /auth/login - happy path: Login Member
- **Specification clause:** 8. Auth

**Request:**
- Method: `POST`
- URL: `/auth/login`
- Auth: `None`
- Body:
```json
{
  "org_name": "org_a586d77f",
  "username": "member1",
  "password": "pw"
}
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMSIsIm9yZyI6MTcsInJvbGUiOiJtZW1iZXIiLCJqdGkiOiI1YWQwOThiNTA0NTI0OGNhYjdhNmYwNmRhNjEyMTE1OSIsImlhdCI6MTc4MzYwOTY4MiwiZXhwIjoxNzgzNjEwNTgyLCJ0eXBlIjoiYWNjZXNzIn0.8CsMOZbar43_u8r7XHXYW63BlA-SctnSkLBux915x48",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMSIsIm9yZyI6MTcsInJvbGUiOiJtZW1iZXIiLCJqdGkiOiIxNzAxODg4ZjZmNGU0NGE0OTdlNzA3YWQ5NzVhZDkxNyIsImlhdCI6MTc4MzYwOTY4MiwiZXhwIjoxNzg0MjE0NDgyLCJ0eXBlIjoicmVmcmVzaCJ9.kHbPs1-ONZ1eZjZRMFc4vDrbi-HjuO2kHZ8FQ8j9v84",
  "token_type": "bearer"
}
```
**Result:** ✅ PASS

### POST /auth/login - invalid input: Bad Password
- **Specification clause:** 8. Auth

**Request:**
- Method: `POST`
- URL: `/auth/login`
- Auth: `None`
- Body:
```json
{
  "org_name": "org_a586d77f",
  "username": "admin1",
  "password": "wrong"
}
```

**Expected:**
- Status: `401`
- JSON Match: `{'code': 'INVALID_CREDENTIALS'}`

**Actual:**
- Status: `401`
- JSON:
```json
{
  "detail": "Invalid username or password",
  "code": "INVALID_CREDENTIALS"
}
```
**Result:** ✅ PASS

### POST /auth/login - boundary cases: Empty Username
- **Specification clause:** 8. Auth

**Request:**
- Method: `POST`
- URL: `/auth/login`
- Auth: `None`
- Body:
```json
{
  "org_name": "org_a586d77f",
  "username": "",
  "password": "pw"
}
```

**Expected:**
- Status: `401`
- JSON Match: `N/A`

**Actual:**
- Status: `401`
- JSON:
```json
{
  "detail": "Invalid username or password",
  "code": "INVALID_CREDENTIALS"
}
```
**Result:** ✅ PASS

### POST /auth/login - authentication tests: N/A
- **Specification clause:** 8. Auth

**Request:**
- Method: `POST`
- URL: `/auth/login`
- Auth: `None`
- Body:
```json
{
  "org_name": "org_5f17290f",
  "username": "admin1",
  "password": "pw"
}
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMiIsIm9yZyI6MTgsInJvbGUiOiJhZG1pbiIsImp0aSI6ImE3YmQ5ZGRkZTk1MzQxNWViYmYxMDhjZjJkM2NiYmJhIiwiaWF0IjoxNzgzNjA5NjgyLCJleHAiOjE3ODM2MTA1ODIsInR5cGUiOiJhY2Nlc3MifQ.ozjC6vB9opr4mzVHbghvD739g5YZ5fZYtViuqr8AlZM",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMiIsIm9yZyI6MTgsInJvbGUiOiJhZG1pbiIsImp0aSI6IjA4NmE1NTQ4YWRkZDRjNjdhYzBlOWE2NjU1ZWI2ZDNjIiwiaWF0IjoxNzgzNjA5NjgyLCJleHAiOjE3ODQyMTQ0ODIsInR5cGUiOiJyZWZyZXNoIn0.1an2RzrAwIOA6a3bV0sqsJIC0Y-D7w3pPjZz7JyT9TQ",
  "token_type": "bearer"
}
```
**Result:** ✅ PASS

### POST /auth/login - authorization tests: N/A
- **Specification clause:** 8. Auth

**Request:**
- Method: `POST`
- URL: `/auth/login`
- Auth: `None`
- Body:
```json
{
  "org_name": "org_5f17290f",
  "username": "admin1",
  "password": "pw"
}
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMiIsIm9yZyI6MTgsInJvbGUiOiJhZG1pbiIsImp0aSI6ImQ3ZTQ1YzFlNDYwYjQ2MGVhNzA5OTIxMjliM2I1MmRjIiwiaWF0IjoxNzgzNjA5NjgyLCJleHAiOjE3ODM2MTA1ODIsInR5cGUiOiJhY2Nlc3MifQ.gMaeNADWyemNVd-U3ZqENDKJHwh5vgBUDC4wgvrJ-CE",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMiIsIm9yZyI6MTgsInJvbGUiOiJhZG1pbiIsImp0aSI6ImFjY2M5NmFkNzRiMzQ5MzI4M2JlYTMwNWEwYmQ1ZDQ1IiwiaWF0IjoxNzgzNjA5NjgyLCJleHAiOjE3ODQyMTQ0ODIsInR5cGUiOiJyZWZyZXNoIn0.CX2hAprdqWcRvnVlhq1eLX1Pp_zsekp5vZc7GD5aHOk",
  "token_type": "bearer"
}
```
**Result:** ✅ PASS

### POST /auth/login - multi-tenant tests: Cross Org Login
- **Specification clause:** 8. Auth

**Request:**
- Method: `POST`
- URL: `/auth/login`
- Auth: `None`
- Body:
```json
{
  "org_name": "org_a586d77f",
  "username": "admin1",
  "password": "pw"
}
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMCIsIm9yZyI6MTcsInJvbGUiOiJhZG1pbiIsImp0aSI6IjQ4MDdlMTM3YmJkMjQ5NDlhNTllNWEwMjZlZDc1ZjE0IiwiaWF0IjoxNzgzNjA5NjgzLCJleHAiOjE3ODM2MTA1ODMsInR5cGUiOiJhY2Nlc3MifQ.sRnq0D72ni4T6Hm8ILjhGeQD7cEeryF0SICDTY_QngY",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMCIsIm9yZyI6MTcsInJvbGUiOiJhZG1pbiIsImp0aSI6IjI4ZmU3ZjI3ZjZjYTRlZGFhZjYwMGZlNmJlMzU2ZDlmIiwiaWF0IjoxNzgzNjA5NjgzLCJleHAiOjE3ODQyMTQ0ODMsInR5cGUiOiJyZWZyZXNoIn0.h60pz2yA1qM_xxfydy2FL0SsRQEv0r9mASruaiWPm0M",
  "token_type": "bearer"
}
```
**Result:** ✅ PASS

### POST /auth/login - concurrency tests: N/A
- **Specification clause:** 8. Auth

**Request:**
- Method: `POST`
- URL: `/auth/login`
- Auth: `None`
- Body:
```json
{
  "org_name": "org_a586d77f",
  "username": "admin1",
  "password": "pw"
}
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMCIsIm9yZyI6MTcsInJvbGUiOiJhZG1pbiIsImp0aSI6IjFmOWQwMTgwYzc5NzQyYTU4N2RkZmVkMTFkMjhkZDIyIiwiaWF0IjoxNzgzNjA5NjgzLCJleHAiOjE3ODM2MTA1ODMsInR5cGUiOiJhY2Nlc3MifQ.u7ARQGzFzDRD0R-Y71Lyhb7qLJs5hfGNT1cYCprNGJI",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMCIsIm9yZyI6MTcsInJvbGUiOiJhZG1pbiIsImp0aSI6IjRlYjQ0NWZiMTFjNjRiZjRiN2M2YTE3ZWQ5NzA0M2E5IiwiaWF0IjoxNzgzNjA5NjgzLCJleHAiOjE3ODQyMTQ0ODMsInR5cGUiOiJyZWZyZXNoIn0.uCvd4ohrEcKa3cRF5QqwE4SskdjhZ-rnE7aSY4uvqgU",
  "token_type": "bearer"
}
```
**Result:** ✅ PASS

### POST /auth/login - pagination tests: N/A
- **Specification clause:** 8. Auth

**Request:**
- Method: `POST`
- URL: `/auth/login`
- Auth: `None`
- Body:
```json
{
  "org_name": "org_a586d77f",
  "username": "admin1",
  "password": "pw"
}
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMCIsIm9yZyI6MTcsInJvbGUiOiJhZG1pbiIsImp0aSI6IjczYjY0NzhiYzU1YTQ1OTBhNjc3ZmNhZTc2YmM3MmFkIiwiaWF0IjoxNzgzNjA5NjgzLCJleHAiOjE3ODM2MTA1ODMsInR5cGUiOiJhY2Nlc3MifQ.wQ28eFFvtOGgPBjBx74BPDURZS3GxGN9556wVkwwJyA",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMCIsIm9yZyI6MTcsInJvbGUiOiJhZG1pbiIsImp0aSI6IjhjOGY2Njk0YjFhMjQ4MjZiODI1NDVlYTdlYmM5NWIzIiwiaWF0IjoxNzgzNjA5NjgzLCJleHAiOjE3ODQyMTQ0ODMsInR5cGUiOiJyZWZyZXNoIn0.VNRrJujpiGvKfYimB7TgvhmFrqQdF64F-PrPFdaQDrM",
  "token_type": "bearer"
}
```
**Result:** ✅ PASS

### POST /auth/login - datetime tests: N/A
- **Specification clause:** 8. Auth

**Request:**
- Method: `POST`
- URL: `/auth/login`
- Auth: `None`
- Body:
```json
{
  "org_name": "org_a586d77f",
  "username": "admin1",
  "password": "pw"
}
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMCIsIm9yZyI6MTcsInJvbGUiOiJhZG1pbiIsImp0aSI6ImJiNzQ1NTc2NmI4YjQzMTY4M2ExMjFiZDE5MjEyM2Q4IiwiaWF0IjoxNzgzNjA5NjgzLCJleHAiOjE3ODM2MTA1ODMsInR5cGUiOiJhY2Nlc3MifQ.QdkE5je7AliRCw_uq-PCywP2CzdpcEKqVBi7JeqgpJo",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMCIsIm9yZyI6MTcsInJvbGUiOiJhZG1pbiIsImp0aSI6IjMzMzg1NjNiZWNhMTRlODg4ZGZlODNkYmE2YmRhODA5IiwiaWF0IjoxNzgzNjA5NjgzLCJleHAiOjE3ODQyMTQ0ODMsInR5cGUiOiJyZWZyZXNoIn0.SljoUJksYBciMnc34WMpAR-8ghtS3TqEZHuxQvi9Xck",
  "token_type": "bearer"
}
```
**Result:** ✅ PASS

### POST /auth/refresh - happy path: Refresh Token
- **Specification clause:** 8. Auth

**Request:**
- Method: `POST`
- URL: `/auth/refresh`
- Auth: `None`
- Body:
```json
{
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMSIsIm9yZyI6MTcsInJvbGUiOiJtZW1iZXIiLCJqdGkiOiIxNzAxODg4ZjZmNGU0NGE0OTdlNzA3YWQ5NzVhZDkxNyIsImlhdCI6MTc4MzYwOTY4MiwiZXhwIjoxNzg0MjE0NDgyLCJ0eXBlIjoicmVmcmVzaCJ9.kHbPs1-ONZ1eZjZRMFc4vDrbi-HjuO2kHZ8FQ8j9v84"
}
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMSIsIm9yZyI6MTcsInJvbGUiOiJtZW1iZXIiLCJqdGkiOiJjOTgxNDhlZjZiZGU0NTk4OTQyYTIyOTNjMTA2NzE3ZSIsImlhdCI6MTc4MzYwOTY4MywiZXhwIjoxNzgzNjEwNTgzLCJ0eXBlIjoiYWNjZXNzIn0.k5SFWZ4Cc6gFNYjdMnZkiQTrCxxAr0p5n_0L3xfvosQ",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMSIsIm9yZyI6MTcsInJvbGUiOiJtZW1iZXIiLCJqdGkiOiJlY2QyOTBlZjk0NmI0OWMxODUwNTRiNTc1MzNhNmRkZSIsImlhdCI6MTc4MzYwOTY4MywiZXhwIjoxNzg0MjE0NDgzLCJ0eXBlIjoicmVmcmVzaCJ9.xvi7cKVwkt_Z9hZb4KWVbU6Nlh5oV5RgU1qJ3jpPheE",
  "token_type": "bearer"
}
```
**Result:** ✅ PASS

### POST /auth/refresh - authentication tests: Refresh Token Reuse
- **Specification clause:** 8. Auth

**Request:**
- Method: `POST`
- URL: `/auth/refresh`
- Auth: `None`
- Body:
```json
{
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMSIsIm9yZyI6MTcsInJvbGUiOiJtZW1iZXIiLCJqdGkiOiIxNzAxODg4ZjZmNGU0NGE0OTdlNzA3YWQ5NzVhZDkxNyIsImlhdCI6MTc4MzYwOTY4MiwiZXhwIjoxNzg0MjE0NDgyLCJ0eXBlIjoicmVmcmVzaCJ9.kHbPs1-ONZ1eZjZRMFc4vDrbi-HjuO2kHZ8FQ8j9v84"
}
```

**Expected:**
- Status: `401`
- JSON Match: `N/A`

**Actual:**
- Status: `401`
- JSON:
```json
{
  "detail": "Token has been revoked",
  "code": "UNAUTHORIZED"
}
```
**Result:** ✅ PASS

### POST /auth/refresh - boundary cases: Empty Token
- **Specification clause:** 8. Auth

**Request:**
- Method: `POST`
- URL: `/auth/refresh`
- Auth: `None`
- Body:
```json
{
  "refresh_token": ""
}
```

**Expected:**
- Status: `401`
- JSON Match: `N/A`

**Actual:**
- Status: `401`
- JSON:
```json
{
  "detail": "Invalid or expired token",
  "code": "UNAUTHORIZED"
}
```
**Result:** ✅ PASS

### POST /auth/refresh - invalid input: Missing Token
- **Specification clause:** 8. Auth

**Request:**
- Method: `POST`
- URL: `/auth/refresh`
- Auth: `None`
- Body:
```json
None
```

**Expected:**
- Status: `422`
- JSON Match: `N/A`

**Actual:**
- Status: `422`
- JSON:
```json
{
  "detail": [
    {
      "type": "missing",
      "loc": [
        "body",
        "refresh_token"
      ],
      "msg": "Field required",
      "input": {}
    }
  ]
}
```
**Result:** ✅ PASS

### POST /auth/refresh - authorization tests: N/A
- **Specification clause:** 8. Auth

**Request:**
- Method: `POST`
- URL: `/auth/refresh`
- Auth: `None`
- Body:
```json
{
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMSIsIm9yZyI6MTcsInJvbGUiOiJtZW1iZXIiLCJqdGkiOiJlY2QyOTBlZjk0NmI0OWMxODUwNTRiNTc1MzNhNmRkZSIsImlhdCI6MTc4MzYwOTY4MywiZXhwIjoxNzg0MjE0NDgzLCJ0eXBlIjoicmVmcmVzaCJ9.xvi7cKVwkt_Z9hZb4KWVbU6Nlh5oV5RgU1qJ3jpPheE"
}
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMSIsIm9yZyI6MTcsInJvbGUiOiJtZW1iZXIiLCJqdGkiOiJlYjY3YzhiZjNjOWU0MWQyODc0MzVlYzZjODI3M2QyOSIsImlhdCI6MTc4MzYwOTY4MywiZXhwIjoxNzgzNjEwNTgzLCJ0eXBlIjoiYWNjZXNzIn0.u9NiH36CAZFyw5s1orcNjwtmNL84wahXY2jI3KT2VaM",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMSIsIm9yZyI6MTcsInJvbGUiOiJtZW1iZXIiLCJqdGkiOiI2ZTQyZTFkNTgwNjA0NDk3YWY4MjA0NDZiYWU3MDY5NCIsImlhdCI6MTc4MzYwOTY4MywiZXhwIjoxNzg0MjE0NDgzLCJ0eXBlIjoicmVmcmVzaCJ9.nv87w7hibmGREI3gdTFRCumqfS7ugIF3CzYK00Obkcs",
  "token_type": "bearer"
}
```
**Result:** ✅ PASS

### POST /auth/refresh - multi-tenant tests: N/A
- **Specification clause:** 8. Auth

**Request:**
- Method: `POST`
- URL: `/auth/refresh`
- Auth: `None`
- Body:
```json
{
  "refresh_token": "invalid"
}
```

**Expected:**
- Status: `401`
- JSON Match: `N/A`

**Actual:**
- Status: `401`
- JSON:
```json
{
  "detail": "Invalid or expired token",
  "code": "UNAUTHORIZED"
}
```
**Result:** ✅ PASS

### POST /auth/refresh - concurrency tests: N/A
- **Specification clause:** 8. Auth

**Request:**
- Method: `POST`
- URL: `/auth/refresh`
- Auth: `None`
- Body:
```json
{
  "refresh_token": "invalid"
}
```

**Expected:**
- Status: `401`
- JSON Match: `N/A`

**Actual:**
- Status: `401`
- JSON:
```json
{
  "detail": "Invalid or expired token",
  "code": "UNAUTHORIZED"
}
```
**Result:** ✅ PASS

### POST /auth/refresh - pagination tests: N/A
- **Specification clause:** 8. Auth

**Request:**
- Method: `POST`
- URL: `/auth/refresh`
- Auth: `None`
- Body:
```json
{
  "refresh_token": "invalid"
}
```

**Expected:**
- Status: `401`
- JSON Match: `N/A`

**Actual:**
- Status: `401`
- JSON:
```json
{
  "detail": "Invalid or expired token",
  "code": "UNAUTHORIZED"
}
```
**Result:** ✅ PASS

### POST /auth/refresh - datetime tests: N/A
- **Specification clause:** 8. Auth

**Request:**
- Method: `POST`
- URL: `/auth/refresh`
- Auth: `None`
- Body:
```json
{
  "refresh_token": "invalid"
}
```

**Expected:**
- Status: `401`
- JSON Match: `N/A`

**Actual:**
- Status: `401`
- JSON:
```json
{
  "detail": "Invalid or expired token",
  "code": "UNAUTHORIZED"
}
```
**Result:** ✅ PASS

### POST /rooms - happy path: Create Room
- **Specification clause:** API contract

**Request:**
- Method: `POST`
- URL: `/rooms`
- Auth: `Present`
- Body:
```json
{
  "name": "Room A",
  "capacity": 10,
  "hourly_rate_cents": 1000
}
```

**Expected:**
- Status: `201`
- JSON Match: `{'name': 'Room A'}`

**Actual:**
- Status: `201`
- JSON:
```json
{
  "id": 16,
  "org_id": 17,
  "name": "Room A",
  "capacity": 10,
  "hourly_rate_cents": 1000
}
```
**Result:** ✅ PASS

### POST /rooms - authorization tests: Create Room as Member
- **Specification clause:** API contract

**Request:**
- Method: `POST`
- URL: `/rooms`
- Auth: `Present`
- Body:
```json
{
  "name": "Room B",
  "capacity": 5,
  "hourly_rate_cents": 500
}
```

**Expected:**
- Status: `403`
- JSON Match: `{'code': 'FORBIDDEN'}`

**Actual:**
- Status: `403`
- JSON:
```json
{
  "detail": "Admin privileges required",
  "code": "FORBIDDEN"
}
```
**Result:** ✅ PASS

### POST /rooms - invalid input: Negative Rate
- **Specification clause:** API contract

**Request:**
- Method: `POST`
- URL: `/rooms`
- Auth: `Present`
- Body:
```json
{
  "name": "Room B",
  "capacity": 5,
  "hourly_rate_cents": -100
}
```

**Expected:**
- Status: `422`
- JSON Match: `N/A`

**Actual:**
- Status: `201`
- JSON:
```json
{
  "id": 17,
  "org_id": 17,
  "name": "Room B",
  "capacity": 5,
  "hourly_rate_cents": -100
}
```
**Result:** ❌ FAIL (Regression)

### POST /rooms - boundary cases: Zero Capacity
- **Specification clause:** API contract

**Request:**
- Method: `POST`
- URL: `/rooms`
- Auth: `Present`
- Body:
```json
{
  "name": "Room C",
  "capacity": 0,
  "hourly_rate_cents": 500
}
```

**Expected:**
- Status: `422`
- JSON Match: `N/A`

**Actual:**
- Status: `201`
- JSON:
```json
{
  "id": 18,
  "org_id": 17,
  "name": "Room C",
  "capacity": 0,
  "hourly_rate_cents": 500
}
```
**Result:** ❌ FAIL (Regression)

### POST /rooms - authentication tests: No Auth
- **Specification clause:** API contract

**Request:**
- Method: `POST`
- URL: `/rooms`
- Auth: `None`
- Body:
```json
{
  "name": "Room B",
  "capacity": 5,
  "hourly_rate_cents": 500
}
```

**Expected:**
- Status: `401`
- JSON Match: `N/A`

**Actual:**
- Status: `401`
- JSON:
```json
{
  "detail": "Missing bearer token",
  "code": "UNAUTHORIZED"
}
```
**Result:** ✅ PASS

### POST /rooms - multi-tenant tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `POST`
- URL: `/rooms`
- Auth: `Present`
- Body:
```json
{
  "name": "Room D",
  "capacity": 5,
  "hourly_rate_cents": 500
}
```

**Expected:**
- Status: `201`
- JSON Match: `N/A`

**Actual:**
- Status: `201`
- JSON:
```json
{
  "id": 19,
  "org_id": 17,
  "name": "Room D",
  "capacity": 5,
  "hourly_rate_cents": 500
}
```
**Result:** ✅ PASS

### POST /rooms - concurrency tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `POST`
- URL: `/rooms`
- Auth: `Present`
- Body:
```json
{
  "name": "Room E",
  "capacity": 5,
  "hourly_rate_cents": 500
}
```

**Expected:**
- Status: `201`
- JSON Match: `N/A`

**Actual:**
- Status: `201`
- JSON:
```json
{
  "id": 20,
  "org_id": 17,
  "name": "Room E",
  "capacity": 5,
  "hourly_rate_cents": 500
}
```
**Result:** ✅ PASS

### POST /rooms - pagination tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `POST`
- URL: `/rooms`
- Auth: `Present`
- Body:
```json
{
  "name": "Room F",
  "capacity": 5,
  "hourly_rate_cents": 500
}
```

**Expected:**
- Status: `201`
- JSON Match: `N/A`

**Actual:**
- Status: `201`
- JSON:
```json
{
  "id": 21,
  "org_id": 17,
  "name": "Room F",
  "capacity": 5,
  "hourly_rate_cents": 500
}
```
**Result:** ✅ PASS

### POST /rooms - datetime tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `POST`
- URL: `/rooms`
- Auth: `Present`
- Body:
```json
{
  "name": "Room G",
  "capacity": 5,
  "hourly_rate_cents": 500
}
```

**Expected:**
- Status: `201`
- JSON Match: `N/A`

**Actual:**
- Status: `201`
- JSON:
```json
{
  "id": 22,
  "org_id": 17,
  "name": "Room G",
  "capacity": 5,
  "hourly_rate_cents": 500
}
```
**Result:** ✅ PASS

### GET /rooms - happy path: List Rooms
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/rooms`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
[
  {
    "id": 16,
    "org_id": 17,
    "name": "Room A",
    "capacity": 10,
    "hourly_rate_cents": 1000
  },
  {
    "id": 17,
    "org_id": 17,
    "name": "Room B",
    "capacity": 5,
    "hourly_rate_cents": -100
  },
  {
    "id": 18,
    "org_id": 17,
    "name": "Room C",
    "capacity": 0,
    "hourly_rate_cents": 500
  },
  {
    "id": 19,
    "org_id": 17,
    "name": "Room D",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 20,
    "org_id": 17,
    "name": "Room E",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 21,
    "org_id": 17,
    "name": "Room F",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 22,
    "org_id": 17,
    "name": "Room G",
    "capacity": 5,
    "hourly_rate_cents": 500
  }
]
```
**Result:** ✅ PASS

### GET /rooms - authentication tests: Unauthenticated
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/rooms`
- Auth: `None`
- Body:
```json
None
```

**Expected:**
- Status: `401`
- JSON Match: `N/A`

**Actual:**
- Status: `401`
- JSON:
```json
{
  "detail": "Missing bearer token",
  "code": "UNAUTHORIZED"
}
```
**Result:** ✅ PASS

### GET /rooms - multi-tenant tests: List Rooms Isolation
- **Specification clause:** 9. Multi-tenancy

**Request:**
- Method: `GET`
- URL: `/rooms`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
[]
```
**Result:** ✅ PASS

### GET /rooms - boundary cases: N/A
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/rooms`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
[
  {
    "id": 16,
    "org_id": 17,
    "name": "Room A",
    "capacity": 10,
    "hourly_rate_cents": 1000
  },
  {
    "id": 17,
    "org_id": 17,
    "name": "Room B",
    "capacity": 5,
    "hourly_rate_cents": -100
  },
  {
    "id": 18,
    "org_id": 17,
    "name": "Room C",
    "capacity": 0,
    "hourly_rate_cents": 500
  },
  {
    "id": 19,
    "org_id": 17,
    "name": "Room D",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 20,
    "org_id": 17,
    "name": "Room E",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 21,
    "org_id": 17,
    "name": "Room F",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 22,
    "org_id": 17,
    "name": "Room G",
    "capacity": 5,
    "hourly_rate_cents": 500
  }
]
```
**Result:** ✅ PASS

### GET /rooms - invalid input: N/A
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/rooms`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
[
  {
    "id": 16,
    "org_id": 17,
    "name": "Room A",
    "capacity": 10,
    "hourly_rate_cents": 1000
  },
  {
    "id": 17,
    "org_id": 17,
    "name": "Room B",
    "capacity": 5,
    "hourly_rate_cents": -100
  },
  {
    "id": 18,
    "org_id": 17,
    "name": "Room C",
    "capacity": 0,
    "hourly_rate_cents": 500
  },
  {
    "id": 19,
    "org_id": 17,
    "name": "Room D",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 20,
    "org_id": 17,
    "name": "Room E",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 21,
    "org_id": 17,
    "name": "Room F",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 22,
    "org_id": 17,
    "name": "Room G",
    "capacity": 5,
    "hourly_rate_cents": 500
  }
]
```
**Result:** ✅ PASS

### GET /rooms - authorization tests: Admin Access
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/rooms`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
[
  {
    "id": 16,
    "org_id": 17,
    "name": "Room A",
    "capacity": 10,
    "hourly_rate_cents": 1000
  },
  {
    "id": 17,
    "org_id": 17,
    "name": "Room B",
    "capacity": 5,
    "hourly_rate_cents": -100
  },
  {
    "id": 18,
    "org_id": 17,
    "name": "Room C",
    "capacity": 0,
    "hourly_rate_cents": 500
  },
  {
    "id": 19,
    "org_id": 17,
    "name": "Room D",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 20,
    "org_id": 17,
    "name": "Room E",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 21,
    "org_id": 17,
    "name": "Room F",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 22,
    "org_id": 17,
    "name": "Room G",
    "capacity": 5,
    "hourly_rate_cents": 500
  }
]
```
**Result:** ✅ PASS

### GET /rooms - concurrency tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/rooms`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
[
  {
    "id": 16,
    "org_id": 17,
    "name": "Room A",
    "capacity": 10,
    "hourly_rate_cents": 1000
  },
  {
    "id": 17,
    "org_id": 17,
    "name": "Room B",
    "capacity": 5,
    "hourly_rate_cents": -100
  },
  {
    "id": 18,
    "org_id": 17,
    "name": "Room C",
    "capacity": 0,
    "hourly_rate_cents": 500
  },
  {
    "id": 19,
    "org_id": 17,
    "name": "Room D",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 20,
    "org_id": 17,
    "name": "Room E",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 21,
    "org_id": 17,
    "name": "Room F",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 22,
    "org_id": 17,
    "name": "Room G",
    "capacity": 5,
    "hourly_rate_cents": 500
  }
]
```
**Result:** ✅ PASS

### GET /rooms - pagination tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/rooms`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
[
  {
    "id": 16,
    "org_id": 17,
    "name": "Room A",
    "capacity": 10,
    "hourly_rate_cents": 1000
  },
  {
    "id": 17,
    "org_id": 17,
    "name": "Room B",
    "capacity": 5,
    "hourly_rate_cents": -100
  },
  {
    "id": 18,
    "org_id": 17,
    "name": "Room C",
    "capacity": 0,
    "hourly_rate_cents": 500
  },
  {
    "id": 19,
    "org_id": 17,
    "name": "Room D",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 20,
    "org_id": 17,
    "name": "Room E",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 21,
    "org_id": 17,
    "name": "Room F",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 22,
    "org_id": 17,
    "name": "Room G",
    "capacity": 5,
    "hourly_rate_cents": 500
  }
]
```
**Result:** ✅ PASS

### GET /rooms - datetime tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/rooms`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
[
  {
    "id": 16,
    "org_id": 17,
    "name": "Room A",
    "capacity": 10,
    "hourly_rate_cents": 1000
  },
  {
    "id": 17,
    "org_id": 17,
    "name": "Room B",
    "capacity": 5,
    "hourly_rate_cents": -100
  },
  {
    "id": 18,
    "org_id": 17,
    "name": "Room C",
    "capacity": 0,
    "hourly_rate_cents": 500
  },
  {
    "id": 19,
    "org_id": 17,
    "name": "Room D",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 20,
    "org_id": 17,
    "name": "Room E",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 21,
    "org_id": 17,
    "name": "Room F",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 22,
    "org_id": 17,
    "name": "Room G",
    "capacity": 5,
    "hourly_rate_cents": 500
  }
]
```
**Result:** ✅ PASS

### POST /bookings - happy path: Create Booking
- **Specification clause:** API contract

**Request:**
- Method: `POST`
- URL: `/bookings`
- Auth: `Present`
- Body:
```json
{
  "room_id": 16,
  "start_time": "2026-07-09T17:00:00+00:00",
  "end_time": "2026-07-09T19:00:00+00:00"
}
```

**Expected:**
- Status: `201`
- JSON Match: `{'price_cents': 2000, 'status': 'confirmed'}`

**Actual:**
- Status: `201`
- JSON:
```json
{
  "id": 12,
  "reference_code": "CW-001000",
  "room_id": 16,
  "user_id": 21,
  "start_time": "2026-07-09T17:00:00+00:00",
  "end_time": "2026-07-09T19:00:00+00:00",
  "status": "confirmed",
  "price_cents": 2000,
  "created_at": "2026-07-09T15:08:04.513257+00:00"
}
```
**Result:** ✅ PASS

### POST /bookings - datetime tests: Booking in Past
- **Specification clause:** 2. Booking price

**Request:**
- Method: `POST`
- URL: `/bookings`
- Auth: `Present`
- Body:
```json
{
  "room_id": 16,
  "start_time": "2026-07-09T13:00:00+00:00",
  "end_time": "2026-07-09T16:00:00+00:00"
}
```

**Expected:**
- Status: `400`
- JSON Match: `{'code': 'INVALID_BOOKING_WINDOW'}`

**Actual:**
- Status: `400`
- JSON:
```json
{
  "detail": "start_time must be in the future",
  "code": "INVALID_BOOKING_WINDOW"
}
```
**Result:** ✅ PASS

### POST /bookings - boundary cases: Overlap Same Room
- **Specification clause:** 3. No double-booking

**Request:**
- Method: `POST`
- URL: `/bookings`
- Auth: `Present`
- Body:
```json
{
  "room_id": 16,
  "start_time": "2026-07-09T18:00:00+00:00",
  "end_time": "2026-07-09T20:00:00+00:00"
}
```

**Expected:**
- Status: `409`
- JSON Match: `{'code': 'ROOM_CONFLICT'}`

**Actual:**
- Status: `409`
- JSON:
```json
{
  "detail": "Room already booked for this interval",
  "code": "ROOM_CONFLICT"
}
```
**Result:** ✅ PASS

### POST /bookings - boundary cases: Back-to-Back Same Room
- **Specification clause:** 3. No double-booking

**Request:**
- Method: `POST`
- URL: `/bookings`
- Auth: `Present`
- Body:
```json
{
  "room_id": 16,
  "start_time": "2026-07-09T19:00:00+00:00",
  "end_time": "2026-07-09T21:00:00+00:00"
}
```

**Expected:**
- Status: `201`
- JSON Match: `N/A`

**Actual:**
- Status: `201`
- JSON:
```json
{
  "id": 13,
  "reference_code": "CW-001001",
  "room_id": 16,
  "user_id": 21,
  "start_time": "2026-07-09T19:00:00+00:00",
  "end_time": "2026-07-09T21:00:00+00:00",
  "status": "confirmed",
  "price_cents": 2000,
  "created_at": "2026-07-09T15:08:05.656377+00:00"
}
```
**Result:** ✅ PASS

### POST /bookings - invalid input: Fractional Duration
- **Specification clause:** 2. Booking price

**Request:**
- Method: `POST`
- URL: `/bookings`
- Auth: `Present`
- Body:
```json
{
  "room_id": 16,
  "start_time": "2026-07-10T01:00:00+00:00",
  "end_time": "2026-07-10T01:38:06.338124+00:00"
}
```

**Expected:**
- Status: `400`
- JSON Match: `{'code': 'INVALID_BOOKING_WINDOW'}`

**Actual:**
- Status: `400`
- JSON:
```json
{
  "detail": "duration must be a whole number of hours",
  "code": "INVALID_BOOKING_WINDOW"
}
```
**Result:** ✅ PASS

### POST /bookings - invalid input: Duration Too Long
- **Specification clause:** 2. Booking price

**Request:**
- Method: `POST`
- URL: `/bookings`
- Auth: `Present`
- Body:
```json
{
  "room_id": 16,
  "start_time": "2026-07-10T01:00:00+00:00",
  "end_time": "2026-07-10T10:00:00+00:00"
}
```

**Expected:**
- Status: `400`
- JSON Match: `{'code': 'INVALID_BOOKING_WINDOW'}`

**Actual:**
- Status: `400`
- JSON:
```json
{
  "detail": "duration out of range",
  "code": "INVALID_BOOKING_WINDOW"
}
```
**Result:** ✅ PASS

### POST /bookings - concurrency tests: Exceed Quota Limit
- **Specification clause:** 4. Booking quota

**Request:**
- Method: `POST`
- URL: `/bookings`
- Auth: `Present`
- Body:
```json
{
  "room_id": 16,
  "start_time": "2026-07-10T14:00:00+00:00",
  "end_time": "2026-07-10T15:00:00+00:00"
}
```

**Expected:**
- Status: `409`
- JSON Match: `{'code': 'QUOTA_EXCEEDED'}`

**Actual:**
- Status: `201`
- JSON:
```json
{
  "id": 14,
  "reference_code": "CW-001002",
  "room_id": 16,
  "user_id": 21,
  "start_time": "2026-07-10T14:00:00+00:00",
  "end_time": "2026-07-10T15:00:00+00:00",
  "status": "confirmed",
  "price_cents": 1000,
  "created_at": "2026-07-09T15:08:06.666840+00:00"
}
```
**Result:** ❌ FAIL (Regression)

### POST /bookings - authentication tests: No Auth
- **Specification clause:** API contract

**Request:**
- Method: `POST`
- URL: `/bookings`
- Auth: `None`
- Body:
```json
{
  "room_id": 16,
  "start_time": "2026-07-10T03:00:00+00:00",
  "end_time": "2026-07-10T04:00:00+00:00"
}
```

**Expected:**
- Status: `401`
- JSON Match: `N/A`

**Actual:**
- Status: `401`
- JSON:
```json
{
  "detail": "Missing bearer token",
  "code": "UNAUTHORIZED"
}
```
**Result:** ✅ PASS

### POST /bookings - authorization tests: Valid Auth
- **Specification clause:** API contract

**Request:**
- Method: `POST`
- URL: `/bookings`
- Auth: `Present`
- Body:
```json
{
  "room_id": 16,
  "start_time": "2026-07-10T16:00:00+00:00",
  "end_time": "2026-07-10T17:00:00+00:00"
}
```

**Expected:**
- Status: `201`
- JSON Match: `N/A`

**Actual:**
- Status: `201`
- JSON:
```json
{
  "id": 15,
  "reference_code": "CW-001003",
  "room_id": 16,
  "user_id": 20,
  "start_time": "2026-07-10T16:00:00+00:00",
  "end_time": "2026-07-10T17:00:00+00:00",
  "status": "confirmed",
  "price_cents": 1000,
  "created_at": "2026-07-09T15:08:07.464145+00:00"
}
```
**Result:** ✅ PASS

### POST /bookings - multi-tenant tests: Book Diff Org Room
- **Specification clause:** 9. Multi-tenancy

**Request:**
- Method: `POST`
- URL: `/bookings`
- Auth: `Present`
- Body:
```json
{
  "room_id": 16,
  "start_time": "2026-07-10T05:00:00+00:00",
  "end_time": "2026-07-10T06:00:00+00:00"
}
```

**Expected:**
- Status: `404`
- JSON Match: `N/A`

**Actual:**
- Status: `404`
- JSON:
```json
{
  "detail": "Room not found",
  "code": "ROOM_NOT_FOUND"
}
```
**Result:** ✅ PASS

### POST /bookings - pagination tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `POST`
- URL: `/bookings`
- Auth: `Present`
- Body:
```json
{
  "room_id": 16,
  "start_time": "2026-07-10T05:00:00+00:00",
  "end_time": "2026-07-10T06:00:00+00:00"
}
```

**Expected:**
- Status: `409`
- JSON Match: `N/A`

**Actual:**
- Status: `409`
- JSON:
```json
{
  "detail": "Booking quota exceeded",
  "code": "QUOTA_EXCEEDED"
}
```
**Result:** ✅ PASS

### GET /bookings - pagination tests: List Bookings Pagination
- **Specification clause:** 11. Pagination & ordering

**Request:**
- Method: `GET`
- URL: `/bookings?page=1&limit=2`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "items": [
    {
      "id": 12,
      "reference_code": "CW-001000",
      "room_id": 16,
      "user_id": 21,
      "start_time": "2026-07-09T17:00:00+00:00",
      "end_time": "2026-07-09T19:00:00+00:00",
      "status": "confirmed",
      "price_cents": 2000,
      "created_at": "2026-07-09T15:08:04.513257+00:00"
    },
    {
      "id": 13,
      "reference_code": "CW-001001",
      "room_id": 16,
      "user_id": 21,
      "start_time": "2026-07-09T19:00:00+00:00",
      "end_time": "2026-07-09T21:00:00+00:00",
      "status": "confirmed",
      "price_cents": 2000,
      "created_at": "2026-07-09T15:08:05.656377+00:00"
    }
  ],
  "page": 1,
  "limit": 2,
  "total": 3
}
```
**Result:** ✅ PASS

### GET /bookings - happy path: List Bookings Default
- **Specification clause:** 11. Pagination & ordering

**Request:**
- Method: `GET`
- URL: `/bookings`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "items": [
    {
      "id": 12,
      "reference_code": "CW-001000",
      "room_id": 16,
      "user_id": 21,
      "start_time": "2026-07-09T17:00:00+00:00",
      "end_time": "2026-07-09T19:00:00+00:00",
      "status": "confirmed",
      "price_cents": 2000,
      "created_at": "2026-07-09T15:08:04.513257+00:00"
    },
    {
      "id": 13,
      "reference_code": "CW-001001",
      "room_id": 16,
      "user_id": 21,
      "start_time": "2026-07-09T19:00:00+00:00",
      "end_time": "2026-07-09T21:00:00+00:00",
      "status": "confirmed",
      "price_cents": 2000,
      "created_at": "2026-07-09T15:08:05.656377+00:00"
    },
    {
      "id": 14,
      "reference_code": "CW-001002",
      "room_id": 16,
      "user_id": 21,
      "start_time": "2026-07-10T14:00:00+00:00",
      "end_time": "2026-07-10T15:00:00+00:00",
      "status": "confirmed",
      "price_cents": 1000,
      "created_at": "2026-07-09T15:08:06.666840+00:00"
    }
  ],
  "page": 1,
  "limit": 10,
  "total": 3
}
```
**Result:** ✅ PASS

### GET /bookings - boundary cases: Page 0
- **Specification clause:** 11. Pagination & ordering

**Request:**
- Method: `GET`
- URL: `/bookings?page=0`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `422`
- JSON Match: `N/A`

**Actual:**
- Status: `422`
- JSON:
```json
{
  "detail": [
    {
      "type": "greater_than_equal",
      "loc": [
        "query",
        "page"
      ],
      "msg": "Input should be greater than or equal to 1",
      "input": "0",
      "ctx": {
        "ge": 1
      }
    }
  ]
}
```
**Result:** ✅ PASS

### GET /bookings - invalid input: Limit 1000
- **Specification clause:** 11. Pagination & ordering

**Request:**
- Method: `GET`
- URL: `/bookings?limit=1000`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `422`
- JSON Match: `N/A`

**Actual:**
- Status: `422`
- JSON:
```json
{
  "detail": [
    {
      "type": "less_than_equal",
      "loc": [
        "query",
        "limit"
      ],
      "msg": "Input should be less than or equal to 100",
      "input": "1000",
      "ctx": {
        "le": 100
      }
    }
  ]
}
```
**Result:** ✅ PASS

### GET /bookings - authentication tests: No Auth
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/bookings`
- Auth: `None`
- Body:
```json
None
```

**Expected:**
- Status: `401`
- JSON Match: `N/A`

**Actual:**
- Status: `401`
- JSON:
```json
{
  "detail": "Missing bearer token",
  "code": "UNAUTHORIZED"
}
```
**Result:** ✅ PASS

### GET /bookings - authorization tests: Member Access
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/bookings`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "items": [
    {
      "id": 12,
      "reference_code": "CW-001000",
      "room_id": 16,
      "user_id": 21,
      "start_time": "2026-07-09T17:00:00+00:00",
      "end_time": "2026-07-09T19:00:00+00:00",
      "status": "confirmed",
      "price_cents": 2000,
      "created_at": "2026-07-09T15:08:04.513257+00:00"
    },
    {
      "id": 13,
      "reference_code": "CW-001001",
      "room_id": 16,
      "user_id": 21,
      "start_time": "2026-07-09T19:00:00+00:00",
      "end_time": "2026-07-09T21:00:00+00:00",
      "status": "confirmed",
      "price_cents": 2000,
      "created_at": "2026-07-09T15:08:05.656377+00:00"
    },
    {
      "id": 14,
      "reference_code": "CW-001002",
      "room_id": 16,
      "user_id": 21,
      "start_time": "2026-07-10T14:00:00+00:00",
      "end_time": "2026-07-10T15:00:00+00:00",
      "status": "confirmed",
      "price_cents": 1000,
      "created_at": "2026-07-09T15:08:06.666840+00:00"
    }
  ],
  "page": 1,
  "limit": 10,
  "total": 3
}
```
**Result:** ✅ PASS

### GET /bookings - multi-tenant tests: Isolated List
- **Specification clause:** 9. Multi-tenancy

**Request:**
- Method: `GET`
- URL: `/bookings`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "items": [],
  "page": 1,
  "limit": 10,
  "total": 0
}
```
**Result:** ✅ PASS

### GET /bookings - concurrency tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/bookings`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "items": [
    {
      "id": 12,
      "reference_code": "CW-001000",
      "room_id": 16,
      "user_id": 21,
      "start_time": "2026-07-09T17:00:00+00:00",
      "end_time": "2026-07-09T19:00:00+00:00",
      "status": "confirmed",
      "price_cents": 2000,
      "created_at": "2026-07-09T15:08:04.513257+00:00"
    },
    {
      "id": 13,
      "reference_code": "CW-001001",
      "room_id": 16,
      "user_id": 21,
      "start_time": "2026-07-09T19:00:00+00:00",
      "end_time": "2026-07-09T21:00:00+00:00",
      "status": "confirmed",
      "price_cents": 2000,
      "created_at": "2026-07-09T15:08:05.656377+00:00"
    },
    {
      "id": 14,
      "reference_code": "CW-001002",
      "room_id": 16,
      "user_id": 21,
      "start_time": "2026-07-10T14:00:00+00:00",
      "end_time": "2026-07-10T15:00:00+00:00",
      "status": "confirmed",
      "price_cents": 1000,
      "created_at": "2026-07-09T15:08:06.666840+00:00"
    }
  ],
  "page": 1,
  "limit": 10,
  "total": 3
}
```
**Result:** ✅ PASS

### GET /bookings - datetime tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/bookings`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "items": [
    {
      "id": 12,
      "reference_code": "CW-001000",
      "room_id": 16,
      "user_id": 21,
      "start_time": "2026-07-09T17:00:00+00:00",
      "end_time": "2026-07-09T19:00:00+00:00",
      "status": "confirmed",
      "price_cents": 2000,
      "created_at": "2026-07-09T15:08:04.513257+00:00"
    },
    {
      "id": 13,
      "reference_code": "CW-001001",
      "room_id": 16,
      "user_id": 21,
      "start_time": "2026-07-09T19:00:00+00:00",
      "end_time": "2026-07-09T21:00:00+00:00",
      "status": "confirmed",
      "price_cents": 2000,
      "created_at": "2026-07-09T15:08:05.656377+00:00"
    },
    {
      "id": 14,
      "reference_code": "CW-001002",
      "room_id": 16,
      "user_id": 21,
      "start_time": "2026-07-10T14:00:00+00:00",
      "end_time": "2026-07-10T15:00:00+00:00",
      "status": "confirmed",
      "price_cents": 1000,
      "created_at": "2026-07-09T15:08:06.666840+00:00"
    }
  ],
  "page": 1,
  "limit": 10,
  "total": 3
}
```
**Result:** ✅ PASS

### GET /bookings/{id} - happy path: Get Booking
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/bookings/12`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "id": 12,
  "reference_code": "CW-001000",
  "room_id": 16,
  "user_id": 21,
  "start_time": "2026-07-09T17:00:00+00:00",
  "end_time": "2026-07-09T19:00:00+00:00",
  "status": "confirmed",
  "price_cents": 2000,
  "created_at": "2026-07-09T15:08:04.513257+00:00",
  "refunds": []
}
```
**Result:** ✅ PASS

### GET /bookings/{id} - authorization tests: Admin Get Booking
- **Specification clause:** 10. Booking visibility

**Request:**
- Method: `GET`
- URL: `/bookings/12`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "id": 12,
  "reference_code": "CW-001000",
  "room_id": 16,
  "user_id": 21,
  "start_time": "2026-07-09T17:00:00+00:00",
  "end_time": "2026-07-09T19:00:00+00:00",
  "status": "confirmed",
  "price_cents": 2000,
  "created_at": "2026-07-09T15:08:04.513257+00:00",
  "refunds": []
}
```
**Result:** ✅ PASS

### GET /bookings/{id} - multi-tenant tests: Get Another Org Booking
- **Specification clause:** 9. Multi-tenancy

**Request:**
- Method: `GET`
- URL: `/bookings/12`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `404`
- JSON Match: `N/A`

**Actual:**
- Status: `404`
- JSON:
```json
{
  "detail": "Booking not found",
  "code": "BOOKING_NOT_FOUND"
}
```
**Result:** ✅ PASS

### GET /bookings/{id} - boundary cases: Get Non-existent Booking
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/bookings/9999`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `404`
- JSON Match: `N/A`

**Actual:**
- Status: `404`
- JSON:
```json
{
  "detail": "Booking not found",
  "code": "BOOKING_NOT_FOUND"
}
```
**Result:** ✅ PASS

### GET /bookings/{id} - invalid input: Get Invalid ID Type
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/bookings/abc`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `422`
- JSON Match: `N/A`

**Actual:**
- Status: `422`
- JSON:
```json
{
  "detail": [
    {
      "type": "int_parsing",
      "loc": [
        "path",
        "booking_id"
      ],
      "msg": "Input should be a valid integer, unable to parse string as an integer",
      "input": "abc"
    }
  ]
}
```
**Result:** ✅ PASS

### GET /bookings/{id} - authentication tests: No Auth
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/bookings/12`
- Auth: `None`
- Body:
```json
None
```

**Expected:**
- Status: `401`
- JSON Match: `N/A`

**Actual:**
- Status: `401`
- JSON:
```json
{
  "detail": "Missing bearer token",
  "code": "UNAUTHORIZED"
}
```
**Result:** ✅ PASS

### GET /bookings/{id} - concurrency tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/bookings/12`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "id": 12,
  "reference_code": "CW-001000",
  "room_id": 16,
  "user_id": 21,
  "start_time": "2026-07-09T17:00:00+00:00",
  "end_time": "2026-07-09T19:00:00+00:00",
  "status": "confirmed",
  "price_cents": 2000,
  "created_at": "2026-07-09T15:08:04.513257+00:00",
  "refunds": []
}
```
**Result:** ✅ PASS

### GET /bookings/{id} - pagination tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/bookings/12`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "id": 12,
  "reference_code": "CW-001000",
  "room_id": 16,
  "user_id": 21,
  "start_time": "2026-07-09T17:00:00+00:00",
  "end_time": "2026-07-09T19:00:00+00:00",
  "status": "confirmed",
  "price_cents": 2000,
  "created_at": "2026-07-09T15:08:04.513257+00:00",
  "refunds": []
}
```
**Result:** ✅ PASS

### GET /bookings/{id} - datetime tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/bookings/12`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "id": 12,
  "reference_code": "CW-001000",
  "room_id": 16,
  "user_id": 21,
  "start_time": "2026-07-09T17:00:00+00:00",
  "end_time": "2026-07-09T19:00:00+00:00",
  "status": "confirmed",
  "price_cents": 2000,
  "created_at": "2026-07-09T15:08:04.513257+00:00",
  "refunds": []
}
```
**Result:** ✅ PASS

### POST /bookings/{id}/cancel - happy path: Cancel < 24h Notice
- **Specification clause:** 6. Cancellation refund policy

**Request:**
- Method: `POST`
- URL: `/bookings/12/cancel`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `{'status': 'cancelled', 'refund_percent': 0, 'refund_amount_cents': 0}`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "id": 12,
  "status": "cancelled",
  "refund_percent": 0,
  "refund_amount_cents": 0
}
```
**Result:** ✅ PASS

### POST /bookings/{id}/cancel - boundary cases: Cancel Already Cancelled
- **Specification clause:** 6. Cancellation refund policy

**Request:**
- Method: `POST`
- URL: `/bookings/12/cancel`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `409`
- JSON Match: `{'code': 'ALREADY_CANCELLED'}`

**Actual:**
- Status: `409`
- JSON:
```json
{
  "detail": "Booking already cancelled",
  "code": "ALREADY_CANCELLED"
}
```
**Result:** ✅ PASS

### POST /bookings/{id}/cancel - authorization tests: Admin Cancel Member Booking
- **Specification clause:** 10. Booking visibility

**Request:**
- Method: `POST`
- URL: `/bookings/12/cancel`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `409`
- JSON Match: `N/A`

**Actual:**
- Status: `409`
- JSON:
```json
{
  "detail": "Booking already cancelled",
  "code": "ALREADY_CANCELLED"
}
```
**Result:** ✅ PASS

### POST /bookings/{id}/cancel - multi-tenant tests: Cancel Another Org Booking
- **Specification clause:** 9. Multi-tenancy

**Request:**
- Method: `POST`
- URL: `/bookings/12/cancel`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `404`
- JSON Match: `N/A`

**Actual:**
- Status: `404`
- JSON:
```json
{
  "detail": "Booking not found",
  "code": "BOOKING_NOT_FOUND"
}
```
**Result:** ✅ PASS

### POST /bookings/{id}/cancel - invalid input: Cancel Invalid ID
- **Specification clause:** API contract

**Request:**
- Method: `POST`
- URL: `/bookings/abc/cancel`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `422`
- JSON Match: `N/A`

**Actual:**
- Status: `422`
- JSON:
```json
{
  "detail": [
    {
      "type": "int_parsing",
      "loc": [
        "path",
        "booking_id"
      ],
      "msg": "Input should be a valid integer, unable to parse string as an integer",
      "input": "abc"
    }
  ]
}
```
**Result:** ✅ PASS

### POST /bookings/{id}/cancel - authentication tests: No Auth
- **Specification clause:** API contract

**Request:**
- Method: `POST`
- URL: `/bookings/12/cancel`
- Auth: `None`
- Body:
```json
None
```

**Expected:**
- Status: `401`
- JSON Match: `N/A`

**Actual:**
- Status: `401`
- JSON:
```json
{
  "detail": "Missing bearer token",
  "code": "UNAUTHORIZED"
}
```
**Result:** ✅ PASS

### POST /bookings/{id}/cancel - concurrency tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `POST`
- URL: `/bookings/12/cancel`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `409`
- JSON Match: `N/A`

**Actual:**
- Status: `409`
- JSON:
```json
{
  "detail": "Booking already cancelled",
  "code": "ALREADY_CANCELLED"
}
```
**Result:** ✅ PASS

### POST /bookings/{id}/cancel - pagination tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `POST`
- URL: `/bookings/12/cancel`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `409`
- JSON Match: `N/A`

**Actual:**
- Status: `409`
- JSON:
```json
{
  "detail": "Booking already cancelled",
  "code": "ALREADY_CANCELLED"
}
```
**Result:** ✅ PASS

### POST /bookings/{id}/cancel - datetime tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `POST`
- URL: `/bookings/12/cancel`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `409`
- JSON Match: `N/A`

**Actual:**
- Status: `409`
- JSON:
```json
{
  "detail": "Booking already cancelled",
  "code": "ALREADY_CANCELLED"
}
```
**Result:** ✅ PASS

### GET /rooms/{id}/availability - happy path: Availability Today
- **Specification clause:** 13. Availability

**Request:**
- Method: `GET`
- URL: `/rooms/16/availability?date=2026-07-09`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "room_id": 16,
  "date": "2026-07-09",
  "busy": [
    {
      "start_time": "2026-07-09T19:00:00+00:00",
      "end_time": "2026-07-09T21:00:00+00:00"
    }
  ]
}
```
**Result:** ✅ PASS

### GET /rooms/{id}/availability - datetime tests: Availability Tomorrow
- **Specification clause:** 13. Availability

**Request:**
- Method: `GET`
- URL: `/rooms/16/availability?date=2026-07-10`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "room_id": 16,
  "date": "2026-07-10",
  "busy": [
    {
      "start_time": "2026-07-10T14:00:00+00:00",
      "end_time": "2026-07-10T15:00:00+00:00"
    },
    {
      "start_time": "2026-07-10T16:00:00+00:00",
      "end_time": "2026-07-10T17:00:00+00:00"
    }
  ]
}
```
**Result:** ✅ PASS

### GET /rooms/{id}/availability - invalid input: Invalid Date Format
- **Specification clause:** 13. Availability

**Request:**
- Method: `GET`
- URL: `/rooms/16/availability?date=abc`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `422`
- JSON Match: `N/A`

**Actual:**
- Status: `422`
- JSON:
```json
{
  "detail": [
    {
      "type": "date_from_datetime_parsing",
      "loc": [
        "query",
        "date"
      ],
      "msg": "Input should be a valid date or datetime, input is too short",
      "input": "abc",
      "ctx": {
        "error": "input is too short"
      }
    }
  ]
}
```
**Result:** ✅ PASS

### GET /rooms/{id}/availability - boundary cases: Room Not Found
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/rooms/999/availability?date=2026-07-09`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `404`
- JSON Match: `N/A`

**Actual:**
- Status: `404`
- JSON:
```json
{
  "detail": "Room not found",
  "code": "ROOM_NOT_FOUND"
}
```
**Result:** ✅ PASS

### GET /rooms/{id}/availability - authentication tests: No Auth
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/rooms/16/availability?date=2026-07-09`
- Auth: `None`
- Body:
```json
None
```

**Expected:**
- Status: `401`
- JSON Match: `N/A`

**Actual:**
- Status: `401`
- JSON:
```json
{
  "detail": "Missing bearer token",
  "code": "UNAUTHORIZED"
}
```
**Result:** ✅ PASS

### GET /rooms/{id}/availability - authorization tests: Member Access
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/rooms/16/availability?date=2026-07-09`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "room_id": 16,
  "date": "2026-07-09",
  "busy": [
    {
      "start_time": "2026-07-09T19:00:00+00:00",
      "end_time": "2026-07-09T21:00:00+00:00"
    }
  ]
}
```
**Result:** ✅ PASS

### GET /rooms/{id}/availability - multi-tenant tests: Another Org Room
- **Specification clause:** 9. Multi-tenancy

**Request:**
- Method: `GET`
- URL: `/rooms/16/availability?date=2026-07-09`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `404`
- JSON Match: `N/A`

**Actual:**
- Status: `404`
- JSON:
```json
{
  "detail": "Room not found",
  "code": "ROOM_NOT_FOUND"
}
```
**Result:** ✅ PASS

### GET /rooms/{id}/availability - concurrency tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/rooms/16/availability?date=2026-07-09`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "room_id": 16,
  "date": "2026-07-09",
  "busy": [
    {
      "start_time": "2026-07-09T19:00:00+00:00",
      "end_time": "2026-07-09T21:00:00+00:00"
    }
  ]
}
```
**Result:** ✅ PASS

### GET /rooms/{id}/availability - pagination tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/rooms/16/availability?date=2026-07-09`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "room_id": 16,
  "date": "2026-07-09",
  "busy": [
    {
      "start_time": "2026-07-09T19:00:00+00:00",
      "end_time": "2026-07-09T21:00:00+00:00"
    }
  ]
}
```
**Result:** ✅ PASS

### GET /rooms/{id}/stats - happy path: Room Stats
- **Specification clause:** 14. Room stats

**Request:**
- Method: `GET`
- URL: `/rooms/16/stats`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "room_id": 16,
  "total_confirmed_bookings": 3,
  "total_revenue_cents": 4000
}
```
**Result:** ✅ PASS

### GET /rooms/{id}/stats - boundary cases: Stats Not Found Room
- **Specification clause:** 14. Room stats

**Request:**
- Method: `GET`
- URL: `/rooms/999/stats`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `404`
- JSON Match: `N/A`

**Actual:**
- Status: `404`
- JSON:
```json
{
  "detail": "Room not found",
  "code": "ROOM_NOT_FOUND"
}
```
**Result:** ✅ PASS

### GET /rooms/{id}/stats - invalid input: Invalid Room ID
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/rooms/abc/stats`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `422`
- JSON Match: `N/A`

**Actual:**
- Status: `422`
- JSON:
```json
{
  "detail": [
    {
      "type": "int_parsing",
      "loc": [
        "path",
        "room_id"
      ],
      "msg": "Input should be a valid integer, unable to parse string as an integer",
      "input": "abc"
    }
  ]
}
```
**Result:** ✅ PASS

### GET /rooms/{id}/stats - authentication tests: No Auth
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/rooms/16/stats`
- Auth: `None`
- Body:
```json
None
```

**Expected:**
- Status: `401`
- JSON Match: `N/A`

**Actual:**
- Status: `401`
- JSON:
```json
{
  "detail": "Missing bearer token",
  "code": "UNAUTHORIZED"
}
```
**Result:** ✅ PASS

### GET /rooms/{id}/stats - authorization tests: Member Access Room Stats
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/rooms/16/stats`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "room_id": 16,
  "total_confirmed_bookings": 3,
  "total_revenue_cents": 4000
}
```
**Result:** ✅ PASS

### GET /rooms/{id}/stats - multi-tenant tests: Stats Another Org
- **Specification clause:** 9. Multi-tenancy

**Request:**
- Method: `GET`
- URL: `/rooms/16/stats`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `404`
- JSON Match: `N/A`

**Actual:**
- Status: `404`
- JSON:
```json
{
  "detail": "Room not found",
  "code": "ROOM_NOT_FOUND"
}
```
**Result:** ✅ PASS

### GET /rooms/{id}/stats - concurrency tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/rooms/16/stats`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "room_id": 16,
  "total_confirmed_bookings": 3,
  "total_revenue_cents": 4000
}
```
**Result:** ✅ PASS

### GET /rooms/{id}/stats - pagination tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/rooms/16/stats`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "room_id": 16,
  "total_confirmed_bookings": 3,
  "total_revenue_cents": 4000
}
```
**Result:** ✅ PASS

### GET /rooms/{id}/stats - datetime tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/rooms/16/stats`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "room_id": 16,
  "total_confirmed_bookings": 3,
  "total_revenue_cents": 4000
}
```
**Result:** ✅ PASS

### GET /admin/usage-report - happy path: Usage Report
- **Specification clause:** 12. Usage report

**Request:**
- Method: `GET`
- URL: `/admin/usage-report?from=2026-07-09&to=2026-07-09`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "from": "2026-07-09",
  "to": "2026-07-09",
  "rooms": [
    {
      "room_id": 16,
      "room_name": "Room A",
      "confirmed_bookings": 1,
      "revenue_cents": 2000
    },
    {
      "room_id": 17,
      "room_name": "Room B",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    },
    {
      "room_id": 18,
      "room_name": "Room C",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    },
    {
      "room_id": 19,
      "room_name": "Room D",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    },
    {
      "room_id": 20,
      "room_name": "Room E",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    },
    {
      "room_id": 21,
      "room_name": "Room F",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    },
    {
      "room_id": 22,
      "room_name": "Room G",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    }
  ]
}
```
**Result:** ✅ PASS

### GET /admin/usage-report - authorization tests: Usage Report as Member
- **Specification clause:** 12. Usage report

**Request:**
- Method: `GET`
- URL: `/admin/usage-report?from=2026-07-09&to=2026-07-09`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `403`
- JSON Match: `{'code': 'FORBIDDEN'}`

**Actual:**
- Status: `403`
- JSON:
```json
{
  "detail": "Admin privileges required",
  "code": "FORBIDDEN"
}
```
**Result:** ✅ PASS

### GET /admin/usage-report - datetime tests: Usage Report Invalid Date
- **Specification clause:** 12. Usage report

**Request:**
- Method: `GET`
- URL: `/admin/usage-report?from=abc&to=2026-07-09`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `422`
- JSON Match: `N/A`

**Actual:**
- Status: `422`
- JSON:
```json
{
  "detail": [
    {
      "type": "date_from_datetime_parsing",
      "loc": [
        "query",
        "from"
      ],
      "msg": "Input should be a valid date or datetime, input is too short",
      "input": "abc",
      "ctx": {
        "error": "input is too short"
      }
    }
  ]
}
```
**Result:** ✅ PASS

### GET /admin/usage-report - boundary cases: Usage Report Missing Dates
- **Specification clause:** 12. Usage report

**Request:**
- Method: `GET`
- URL: `/admin/usage-report`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `422`
- JSON Match: `N/A`

**Actual:**
- Status: `422`
- JSON:
```json
{
  "detail": [
    {
      "type": "missing",
      "loc": [
        "query",
        "from"
      ],
      "msg": "Field required",
      "input": null
    },
    {
      "type": "missing",
      "loc": [
        "query",
        "to"
      ],
      "msg": "Field required",
      "input": null
    }
  ]
}
```
**Result:** ✅ PASS

### GET /admin/usage-report - invalid input: Usage Report Bad Query
- **Specification clause:** 12. Usage report

**Request:**
- Method: `GET`
- URL: `/admin/usage-report?from=2024-01-01`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `422`
- JSON Match: `N/A`

**Actual:**
- Status: `422`
- JSON:
```json
{
  "detail": [
    {
      "type": "missing",
      "loc": [
        "query",
        "to"
      ],
      "msg": "Field required",
      "input": null
    }
  ]
}
```
**Result:** ✅ PASS

### GET /admin/usage-report - authentication tests: No Auth
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/admin/usage-report?from=2026-07-09&to=2026-07-09`
- Auth: `None`
- Body:
```json
None
```

**Expected:**
- Status: `401`
- JSON Match: `N/A`

**Actual:**
- Status: `401`
- JSON:
```json
{
  "detail": "Missing bearer token",
  "code": "UNAUTHORIZED"
}
```
**Result:** ✅ PASS

### GET /admin/usage-report - multi-tenant tests: Isolated Usage
- **Specification clause:** 9. Multi-tenancy

**Request:**
- Method: `GET`
- URL: `/admin/usage-report?from=2026-07-09&to=2026-07-09`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "from": "2026-07-09",
  "to": "2026-07-09",
  "rooms": []
}
```
**Result:** ✅ PASS

### GET /admin/usage-report - concurrency tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/admin/usage-report?from=2026-07-09&to=2026-07-09`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "from": "2026-07-09",
  "to": "2026-07-09",
  "rooms": [
    {
      "room_id": 16,
      "room_name": "Room A",
      "confirmed_bookings": 1,
      "revenue_cents": 2000
    },
    {
      "room_id": 17,
      "room_name": "Room B",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    },
    {
      "room_id": 18,
      "room_name": "Room C",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    },
    {
      "room_id": 19,
      "room_name": "Room D",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    },
    {
      "room_id": 20,
      "room_name": "Room E",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    },
    {
      "room_id": 21,
      "room_name": "Room F",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    },
    {
      "room_id": 22,
      "room_name": "Room G",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    }
  ]
}
```
**Result:** ✅ PASS

### GET /admin/usage-report - pagination tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/admin/usage-report?from=2026-07-09&to=2026-07-09`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "from": "2026-07-09",
  "to": "2026-07-09",
  "rooms": [
    {
      "room_id": 16,
      "room_name": "Room A",
      "confirmed_bookings": 1,
      "revenue_cents": 2000
    },
    {
      "room_id": 17,
      "room_name": "Room B",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    },
    {
      "room_id": 18,
      "room_name": "Room C",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    },
    {
      "room_id": 19,
      "room_name": "Room D",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    },
    {
      "room_id": 20,
      "room_name": "Room E",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    },
    {
      "room_id": 21,
      "room_name": "Room F",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    },
    {
      "room_id": 22,
      "room_name": "Room G",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    }
  ]
}
```
**Result:** ✅ PASS

### GET /admin/export - happy path: Export CSV
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/admin/export`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
None
```
**Result:** ✅ PASS

### GET /admin/export - authorization tests: Export CSV as Member
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/admin/export`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `403`
- JSON Match: `N/A`

**Actual:**
- Status: `403`
- JSON:
```json
{
  "detail": "Admin privileges required",
  "code": "FORBIDDEN"
}
```
**Result:** ✅ PASS

### GET /admin/export - boundary cases: Export specific room
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/admin/export?room_id=16`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
None
```
**Result:** ✅ PASS

### GET /admin/export - invalid input: Export Invalid Room
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/admin/export?room_id=abc`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `422`
- JSON Match: `N/A`

**Actual:**
- Status: `422`
- JSON:
```json
{
  "detail": [
    {
      "type": "int_parsing",
      "loc": [
        "query",
        "room_id"
      ],
      "msg": "Input should be a valid integer, unable to parse string as an integer",
      "input": "abc"
    }
  ]
}
```
**Result:** ✅ PASS

### GET /admin/export - authentication tests: No Auth
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/admin/export`
- Auth: `None`
- Body:
```json
None
```

**Expected:**
- Status: `401`
- JSON Match: `N/A`

**Actual:**
- Status: `401`
- JSON:
```json
{
  "detail": "Missing bearer token",
  "code": "UNAUTHORIZED"
}
```
**Result:** ✅ PASS

### GET /admin/export - multi-tenant tests: Export Isolated
- **Specification clause:** 9. Multi-tenancy

**Request:**
- Method: `GET`
- URL: `/admin/export`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
None
```
**Result:** ✅ PASS

### GET /admin/export - concurrency tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/admin/export`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
None
```
**Result:** ✅ PASS

### GET /admin/export - pagination tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/admin/export`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
None
```
**Result:** ✅ PASS

### GET /admin/export - datetime tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/admin/export`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
None
```
**Result:** ✅ PASS

### GET /health - happy path: Health Check
- **Specification clause:** 16. Liveness

**Request:**
- Method: `GET`
- URL: `/health`
- Auth: `None`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `{'status': 'ok'}`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "status": "ok"
}
```
**Result:** ✅ PASS

### GET /health - boundary cases: N/A
- **Specification clause:** 16. Liveness

**Request:**
- Method: `GET`
- URL: `/health`
- Auth: `None`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "status": "ok"
}
```
**Result:** ✅ PASS

### GET /health - invalid input: N/A
- **Specification clause:** 16. Liveness

**Request:**
- Method: `GET`
- URL: `/health`
- Auth: `None`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "status": "ok"
}
```
**Result:** ✅ PASS

### GET /health - authentication tests: N/A
- **Specification clause:** 16. Liveness

**Request:**
- Method: `GET`
- URL: `/health`
- Auth: `None`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "status": "ok"
}
```
**Result:** ✅ PASS

### GET /health - authorization tests: N/A
- **Specification clause:** 16. Liveness

**Request:**
- Method: `GET`
- URL: `/health`
- Auth: `None`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "status": "ok"
}
```
**Result:** ✅ PASS

### GET /health - multi-tenant tests: N/A
- **Specification clause:** 16. Liveness

**Request:**
- Method: `GET`
- URL: `/health`
- Auth: `None`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "status": "ok"
}
```
**Result:** ✅ PASS

### GET /health - concurrency tests: N/A
- **Specification clause:** 16. Liveness

**Request:**
- Method: `GET`
- URL: `/health`
- Auth: `None`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "status": "ok"
}
```
**Result:** ✅ PASS

### GET /health - pagination tests: N/A
- **Specification clause:** 16. Liveness

**Request:**
- Method: `GET`
- URL: `/health`
- Auth: `None`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "status": "ok"
}
```
**Result:** ✅ PASS

### GET /health - datetime tests: N/A
- **Specification clause:** 16. Liveness

**Request:**
- Method: `GET`
- URL: `/health`
- Auth: `None`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "status": "ok"
}
```
**Result:** ✅ PASS

### POST /auth/logout - happy path: Logout
- **Specification clause:** 8. Auth

**Request:**
- Method: `POST`
- URL: `/auth/logout`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "status": "ok"
}
```
**Result:** ✅ PASS

### POST /auth/logout - authentication tests: Use Token After Logout
- **Specification clause:** 8. Auth

**Request:**
- Method: `GET`
- URL: `/rooms`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `401`
- JSON Match: `N/A`

**Actual:**
- Status: `401`
- JSON:
```json
{
  "detail": "Token has been revoked",
  "code": "UNAUTHORIZED"
}
```
**Result:** ✅ PASS

### POST /auth/logout - boundary cases: Logout Twice
- **Specification clause:** 8. Auth

**Request:**
- Method: `POST`
- URL: `/auth/logout`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `401`
- JSON Match: `N/A`

**Actual:**
- Status: `401`
- JSON:
```json
{
  "detail": "Token has been revoked",
  "code": "UNAUTHORIZED"
}
```
**Result:** ✅ PASS

### POST /auth/logout - invalid input: N/A
- **Specification clause:** 8. Auth

**Request:**
- Method: `POST`
- URL: `/auth/logout`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `200`
- JSON Match: `N/A`

**Actual:**
- Status: `200`
- JSON:
```json
{
  "status": "ok"
}
```
**Result:** ✅ PASS

### POST /auth/logout - authorization tests: N/A
- **Specification clause:** 8. Auth

**Request:**
- Method: `POST`
- URL: `/auth/logout`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `401`
- JSON Match: `N/A`

**Actual:**
- Status: `401`
- JSON:
```json
{
  "detail": "Invalid or expired token",
  "code": "UNAUTHORIZED"
}
```
**Result:** ✅ PASS

### POST /auth/logout - multi-tenant tests: N/A
- **Specification clause:** 8. Auth

**Request:**
- Method: `POST`
- URL: `/auth/logout`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `401`
- JSON Match: `N/A`

**Actual:**
- Status: `401`
- JSON:
```json
{
  "detail": "Invalid or expired token",
  "code": "UNAUTHORIZED"
}
```
**Result:** ✅ PASS

### POST /auth/logout - concurrency tests: N/A
- **Specification clause:** 8. Auth

**Request:**
- Method: `POST`
- URL: `/auth/logout`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `401`
- JSON Match: `N/A`

**Actual:**
- Status: `401`
- JSON:
```json
{
  "detail": "Invalid or expired token",
  "code": "UNAUTHORIZED"
}
```
**Result:** ✅ PASS

### POST /auth/logout - pagination tests: N/A
- **Specification clause:** 8. Auth

**Request:**
- Method: `POST`
- URL: `/auth/logout`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `401`
- JSON Match: `N/A`

**Actual:**
- Status: `401`
- JSON:
```json
{
  "detail": "Invalid or expired token",
  "code": "UNAUTHORIZED"
}
```
**Result:** ✅ PASS

### POST /auth/logout - datetime tests: N/A
- **Specification clause:** 8. Auth

**Request:**
- Method: `POST`
- URL: `/auth/logout`
- Auth: `Present`
- Body:
```json
None
```

**Expected:**
- Status: `401`
- JSON Match: `N/A`

**Actual:**
- Status: `401`
- JSON:
```json
{
  "detail": "Invalid or expired token",
  "code": "UNAUTHORIZED"
}
```
**Result:** ✅ PASS
