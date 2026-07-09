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
  "org_name": "org_75f5e1ea",
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
  "user_id": 2,
  "org_id": 2,
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
  "org_name": "org_75f5e1ea",
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
  "user_id": 3,
  "org_id": 2,
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
  "org_name": "org_75f5e1ea",
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
        "org_name": "org_75f5e1ea",
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
  "org_name": "org_75f5e1ea",
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
  "org_name": "org_b06e17d0",
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
  "user_id": 4,
  "org_id": 3,
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
  "org_name": "org_effb2641",
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
  "user_id": 5,
  "org_id": 4,
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
  "org_name": "org_c2a0eb71",
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
  "user_id": 6,
  "org_id": 5,
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
  "org_name": "org_7fb32fbd",
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
  "user_id": 7,
  "org_id": 6,
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
  "org_name": "org_d16f5703",
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
  "user_id": 8,
  "org_id": 7,
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
  "org_name": "org_a681c2be",
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
  "user_id": 9,
  "org_id": 8,
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
  "org_name": "org_75f5e1ea",
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
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyIiwib3JnIjoyLCJyb2xlIjoiYWRtaW4iLCJqdGkiOiI4Zjc0NjVhMDBmMDc0ZjQyYTJiODYyNmJkNDNjNjg1YyIsImlhdCI6MTc4MzYwNzg0OSwiZXhwIjoxNzgzNjA4NzQ5LCJ0eXBlIjoiYWNjZXNzIn0.oIZbCnxvKj6OSz1U9oOVW1AaRNlNYjEx7o8DfaX2Jbk",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyIiwib3JnIjoyLCJyb2xlIjoiYWRtaW4iLCJqdGkiOiIyZTI3NjMyMmNjYzg0Mzc0YjliZDNjNTVkMjU4ZTRjMiIsImlhdCI6MTc4MzYwNzg0OSwiZXhwIjoxNzg0MjEyNjQ5LCJ0eXBlIjoicmVmcmVzaCJ9.nGhrgSzK3zZyQwnPcjMVBXw4UI6YOriDN6rYlCp4kWA",
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
  "org_name": "org_75f5e1ea",
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
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzIiwib3JnIjoyLCJyb2xlIjoibWVtYmVyIiwianRpIjoiZWRkNGE3YTdjMTNlNGEwY2FjNjJkMmIzMWFiM2MzYzEiLCJpYXQiOjE3ODM2MDc4NDksImV4cCI6MTc4MzYwODc0OSwidHlwZSI6ImFjY2VzcyJ9.9Fgs51o2G0Lj2ciXmD6veXpwT8FbuXLmEJ0-yUciQG4",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzIiwib3JnIjoyLCJyb2xlIjoibWVtYmVyIiwianRpIjoiM2I5YTQ1Zjc0NjJjNGRlMmE2YTRhNzg2MzJlYTA0ZDIiLCJpYXQiOjE3ODM2MDc4NDksImV4cCI6MTc4NDIxMjY0OSwidHlwZSI6InJlZnJlc2gifQ.jxfRcF2eS3hLxqBc8Momq0qgiEqrv5b2-B6KVIN_a3U",
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
  "org_name": "org_75f5e1ea",
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
  "org_name": "org_75f5e1ea",
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
  "org_name": "org_b06e17d0",
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
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0Iiwib3JnIjozLCJyb2xlIjoiYWRtaW4iLCJqdGkiOiIyZWRhMGNmYWQyN2Q0ZWRlYTA3ZDA1YzVjM2Y2NWRjMyIsImlhdCI6MTc4MzYwNzg0OSwiZXhwIjoxNzgzNjA4NzQ5LCJ0eXBlIjoiYWNjZXNzIn0.JQIEHD0ZmgEE3Y-uhbN-7UDKd9hPx7HK2Y01MY69vmQ",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0Iiwib3JnIjozLCJyb2xlIjoiYWRtaW4iLCJqdGkiOiIxNTQ4NWRhZmUwYzE0ZTY5ODllYjE2M2VmZmZjNzAwYSIsImlhdCI6MTc4MzYwNzg0OSwiZXhwIjoxNzg0MjEyNjQ5LCJ0eXBlIjoicmVmcmVzaCJ9.SS504li2ID6xCJW5OabV3Mn_0ULfhPHSxHBD-BLe7vA",
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
  "org_name": "org_b06e17d0",
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
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0Iiwib3JnIjozLCJyb2xlIjoiYWRtaW4iLCJqdGkiOiIyMTNkZGE2NjUxMTI0NjhmODRlNDY1YTUyNmNjN2ZmNCIsImlhdCI6MTc4MzYwNzg0OSwiZXhwIjoxNzgzNjA4NzQ5LCJ0eXBlIjoiYWNjZXNzIn0.yX81K_32umurE3bxzd5XteQAHAEjMnUcEKO6EiGs0H0",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0Iiwib3JnIjozLCJyb2xlIjoiYWRtaW4iLCJqdGkiOiJlYjczZDEzMTQxNjU0ZjE4OTc2NjJlYWU4MjZhNWJlNiIsImlhdCI6MTc4MzYwNzg0OSwiZXhwIjoxNzg0MjEyNjQ5LCJ0eXBlIjoicmVmcmVzaCJ9.tOpP2wWTOocRhuSv8b-bOpk0Iep4GAAkDOTMZb0XgDQ",
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
  "org_name": "org_75f5e1ea",
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
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyIiwib3JnIjoyLCJyb2xlIjoiYWRtaW4iLCJqdGkiOiIzYjUwMGIwYmRlMWQ0NjRjYmFjNTVkMDMwMDMwNGUxZiIsImlhdCI6MTc4MzYwNzg1MCwiZXhwIjoxNzgzNjA4NzUwLCJ0eXBlIjoiYWNjZXNzIn0.LlLRGIkp6AFn39LT6cKWJs3Bqjbt_YLdKv6itbDD7yM",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyIiwib3JnIjoyLCJyb2xlIjoiYWRtaW4iLCJqdGkiOiJiMTE3YWY4MGY2NDM0NzUyODJmMDM4ZjYwZjA0MWMzNSIsImlhdCI6MTc4MzYwNzg1MCwiZXhwIjoxNzg0MjEyNjUwLCJ0eXBlIjoicmVmcmVzaCJ9.Csxsi0Awow9vaK5qu1U1m12PZ9wfBd-eKQ7M4oAD9qU",
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
  "org_name": "org_75f5e1ea",
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
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyIiwib3JnIjoyLCJyb2xlIjoiYWRtaW4iLCJqdGkiOiIzZTYyMWVjZTliZDE0NmEyOWYxZTNmZDJhZjI2MTNjMyIsImlhdCI6MTc4MzYwNzg1MCwiZXhwIjoxNzgzNjA4NzUwLCJ0eXBlIjoiYWNjZXNzIn0.Q8anDIzJ-nEusMoCtuWIz1C27pQl-hj_Us8YSUQk3SM",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyIiwib3JnIjoyLCJyb2xlIjoiYWRtaW4iLCJqdGkiOiJhYzM5ZTFhYTg0ZDU0ZTZkYWQ3NjgwZTAyM2JlYmIzYyIsImlhdCI6MTc4MzYwNzg1MCwiZXhwIjoxNzg0MjEyNjUwLCJ0eXBlIjoicmVmcmVzaCJ9.Md_GEE9xH_eaYw4CJwnLY1MGlQhXgQMTfhTR2aLuz5w",
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
  "org_name": "org_75f5e1ea",
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
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyIiwib3JnIjoyLCJyb2xlIjoiYWRtaW4iLCJqdGkiOiJlNTMwNzkwNDJlYWU0MWQ1OWM0MjQ5NDAwNzcwYzQ4NiIsImlhdCI6MTc4MzYwNzg1MCwiZXhwIjoxNzgzNjA4NzUwLCJ0eXBlIjoiYWNjZXNzIn0.Z5-ReGv1dirh1V8nsgdsZeAMBh2KNLBgYfrxls3u288",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyIiwib3JnIjoyLCJyb2xlIjoiYWRtaW4iLCJqdGkiOiIyZDkzYzM2ZDIxOGU0YjcxOTM1MWZjOGIyOTEyYjRmMyIsImlhdCI6MTc4MzYwNzg1MCwiZXhwIjoxNzg0MjEyNjUwLCJ0eXBlIjoicmVmcmVzaCJ9.TbZqSU8upjrlwZLkqsE7P5zl1tNLIRwD5BvyOzF1aW8",
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
  "org_name": "org_75f5e1ea",
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
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyIiwib3JnIjoyLCJyb2xlIjoiYWRtaW4iLCJqdGkiOiI2NjFkYTM1M2NjNzQ0MmQ3Yjc1ZDcwNGEyNDg2MjU2OSIsImlhdCI6MTc4MzYwNzg1MCwiZXhwIjoxNzgzNjA4NzUwLCJ0eXBlIjoiYWNjZXNzIn0.osP2JxKi6qkV7qUGhOfAPLcQO6duo3_8rVzJgB5_pQI",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyIiwib3JnIjoyLCJyb2xlIjoiYWRtaW4iLCJqdGkiOiI3OGM0YzFmMmMzNDA0ZDQ3OTljYjkyYTczOWY2MDk5YiIsImlhdCI6MTc4MzYwNzg1MCwiZXhwIjoxNzg0MjEyNjUwLCJ0eXBlIjoicmVmcmVzaCJ9.7QAP0hrA9mg82lZYVdAzUabyb8bWl_hJhiBUihKK9No",
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
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzIiwib3JnIjoyLCJyb2xlIjoibWVtYmVyIiwianRpIjoiM2I5YTQ1Zjc0NjJjNGRlMmE2YTRhNzg2MzJlYTA0ZDIiLCJpYXQiOjE3ODM2MDc4NDksImV4cCI6MTc4NDIxMjY0OSwidHlwZSI6InJlZnJlc2gifQ.jxfRcF2eS3hLxqBc8Momq0qgiEqrv5b2-B6KVIN_a3U"
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
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzIiwib3JnIjoyLCJyb2xlIjoibWVtYmVyIiwianRpIjoiMThmNTg1YWUxMDEwNDliZGI0NTgwNmNmMjY2ZjA1MjUiLCJpYXQiOjE3ODM2MDc4NTAsImV4cCI6MTc4MzYwODc1MCwidHlwZSI6ImFjY2VzcyJ9.YrHpv5tpLEoP1BNBIx8miH-TDkqLWG0MbijFBpUmGGo",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzIiwib3JnIjoyLCJyb2xlIjoibWVtYmVyIiwianRpIjoiM2RjNjg5ZDViNGMwNDY1YmI5MDRkODE5YzU1OTM2MzIiLCJpYXQiOjE3ODM2MDc4NTAsImV4cCI6MTc4NDIxMjY1MCwidHlwZSI6InJlZnJlc2gifQ.vF3Z7fRN3koouR4nJZKED25aagvOs8dHx3SQRGbZUh4",
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
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzIiwib3JnIjoyLCJyb2xlIjoibWVtYmVyIiwianRpIjoiM2I5YTQ1Zjc0NjJjNGRlMmE2YTRhNzg2MzJlYTA0ZDIiLCJpYXQiOjE3ODM2MDc4NDksImV4cCI6MTc4NDIxMjY0OSwidHlwZSI6InJlZnJlc2gifQ.jxfRcF2eS3hLxqBc8Momq0qgiEqrv5b2-B6KVIN_a3U"
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
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzIiwib3JnIjoyLCJyb2xlIjoibWVtYmVyIiwianRpIjoiM2RjNjg5ZDViNGMwNDY1YmI5MDRkODE5YzU1OTM2MzIiLCJpYXQiOjE3ODM2MDc4NTAsImV4cCI6MTc4NDIxMjY1MCwidHlwZSI6InJlZnJlc2gifQ.vF3Z7fRN3koouR4nJZKED25aagvOs8dHx3SQRGbZUh4"
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
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzIiwib3JnIjoyLCJyb2xlIjoibWVtYmVyIiwianRpIjoiOWQ4MWNmMWIxODM4NDdjZDljMGM2YzVlNDYxOWYwNjUiLCJpYXQiOjE3ODM2MDc4NTAsImV4cCI6MTc4MzYwODc1MCwidHlwZSI6ImFjY2VzcyJ9.2FpnBxgi0MEoVqKoz_fYV-1VExMWL5nqSHzvuC9GV-Y",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzIiwib3JnIjoyLCJyb2xlIjoibWVtYmVyIiwianRpIjoiMjJiOTM2Zjk4MTM2NGJmZTk5NmMzOWQxZmNhYzMwMDMiLCJpYXQiOjE3ODM2MDc4NTAsImV4cCI6MTc4NDIxMjY1MCwidHlwZSI6InJlZnJlc2gifQ.1RdKkELOfv3ohJ9_UWi1ujQ1MBL9l3JUyzjLDgRrT44",
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
  "id": 1,
  "org_id": 2,
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
  "id": 2,
  "org_id": 2,
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
  "id": 3,
  "org_id": 2,
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
  "id": 4,
  "org_id": 2,
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
  "id": 5,
  "org_id": 2,
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
  "id": 6,
  "org_id": 2,
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
  "id": 7,
  "org_id": 2,
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
    "id": 1,
    "org_id": 2,
    "name": "Room A",
    "capacity": 10,
    "hourly_rate_cents": 1000
  },
  {
    "id": 2,
    "org_id": 2,
    "name": "Room B",
    "capacity": 5,
    "hourly_rate_cents": -100
  },
  {
    "id": 3,
    "org_id": 2,
    "name": "Room C",
    "capacity": 0,
    "hourly_rate_cents": 500
  },
  {
    "id": 4,
    "org_id": 2,
    "name": "Room D",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 5,
    "org_id": 2,
    "name": "Room E",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 6,
    "org_id": 2,
    "name": "Room F",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 7,
    "org_id": 2,
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
    "id": 1,
    "org_id": 2,
    "name": "Room A",
    "capacity": 10,
    "hourly_rate_cents": 1000
  },
  {
    "id": 2,
    "org_id": 2,
    "name": "Room B",
    "capacity": 5,
    "hourly_rate_cents": -100
  },
  {
    "id": 3,
    "org_id": 2,
    "name": "Room C",
    "capacity": 0,
    "hourly_rate_cents": 500
  },
  {
    "id": 4,
    "org_id": 2,
    "name": "Room D",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 5,
    "org_id": 2,
    "name": "Room E",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 6,
    "org_id": 2,
    "name": "Room F",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 7,
    "org_id": 2,
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
    "id": 1,
    "org_id": 2,
    "name": "Room A",
    "capacity": 10,
    "hourly_rate_cents": 1000
  },
  {
    "id": 2,
    "org_id": 2,
    "name": "Room B",
    "capacity": 5,
    "hourly_rate_cents": -100
  },
  {
    "id": 3,
    "org_id": 2,
    "name": "Room C",
    "capacity": 0,
    "hourly_rate_cents": 500
  },
  {
    "id": 4,
    "org_id": 2,
    "name": "Room D",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 5,
    "org_id": 2,
    "name": "Room E",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 6,
    "org_id": 2,
    "name": "Room F",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 7,
    "org_id": 2,
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
    "id": 1,
    "org_id": 2,
    "name": "Room A",
    "capacity": 10,
    "hourly_rate_cents": 1000
  },
  {
    "id": 2,
    "org_id": 2,
    "name": "Room B",
    "capacity": 5,
    "hourly_rate_cents": -100
  },
  {
    "id": 3,
    "org_id": 2,
    "name": "Room C",
    "capacity": 0,
    "hourly_rate_cents": 500
  },
  {
    "id": 4,
    "org_id": 2,
    "name": "Room D",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 5,
    "org_id": 2,
    "name": "Room E",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 6,
    "org_id": 2,
    "name": "Room F",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 7,
    "org_id": 2,
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
    "id": 1,
    "org_id": 2,
    "name": "Room A",
    "capacity": 10,
    "hourly_rate_cents": 1000
  },
  {
    "id": 2,
    "org_id": 2,
    "name": "Room B",
    "capacity": 5,
    "hourly_rate_cents": -100
  },
  {
    "id": 3,
    "org_id": 2,
    "name": "Room C",
    "capacity": 0,
    "hourly_rate_cents": 500
  },
  {
    "id": 4,
    "org_id": 2,
    "name": "Room D",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 5,
    "org_id": 2,
    "name": "Room E",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 6,
    "org_id": 2,
    "name": "Room F",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 7,
    "org_id": 2,
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
    "id": 1,
    "org_id": 2,
    "name": "Room A",
    "capacity": 10,
    "hourly_rate_cents": 1000
  },
  {
    "id": 2,
    "org_id": 2,
    "name": "Room B",
    "capacity": 5,
    "hourly_rate_cents": -100
  },
  {
    "id": 3,
    "org_id": 2,
    "name": "Room C",
    "capacity": 0,
    "hourly_rate_cents": 500
  },
  {
    "id": 4,
    "org_id": 2,
    "name": "Room D",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 5,
    "org_id": 2,
    "name": "Room E",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 6,
    "org_id": 2,
    "name": "Room F",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 7,
    "org_id": 2,
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
    "id": 1,
    "org_id": 2,
    "name": "Room A",
    "capacity": 10,
    "hourly_rate_cents": 1000
  },
  {
    "id": 2,
    "org_id": 2,
    "name": "Room B",
    "capacity": 5,
    "hourly_rate_cents": -100
  },
  {
    "id": 3,
    "org_id": 2,
    "name": "Room C",
    "capacity": 0,
    "hourly_rate_cents": 500
  },
  {
    "id": 4,
    "org_id": 2,
    "name": "Room D",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 5,
    "org_id": 2,
    "name": "Room E",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 6,
    "org_id": 2,
    "name": "Room F",
    "capacity": 5,
    "hourly_rate_cents": 500
  },
  {
    "id": 7,
    "org_id": 2,
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
  "room_id": 1,
  "start_time": "2026-07-09T16:00:00+00:00",
  "end_time": "2026-07-09T18:00:00+00:00"
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
  "id": 1,
  "reference_code": "CW-001000",
  "room_id": 1,
  "user_id": 3,
  "start_time": "2026-07-09T16:00:00+00:00",
  "end_time": "2026-07-09T18:00:00+00:00",
  "status": "confirmed",
  "price_cents": 2000,
  "created_at": "2026-07-09T14:37:31.288604+00:00"
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
  "room_id": 1,
  "start_time": "2026-07-09T12:00:00+00:00",
  "end_time": "2026-07-09T15:00:00+00:00"
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
  "room_id": 1,
  "start_time": "2026-07-09T17:00:00+00:00",
  "end_time": "2026-07-09T19:00:00+00:00"
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
  "room_id": 1,
  "start_time": "2026-07-09T18:00:00+00:00",
  "end_time": "2026-07-09T20:00:00+00:00"
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
  "id": 2,
  "reference_code": "CW-001001",
  "room_id": 1,
  "user_id": 3,
  "start_time": "2026-07-09T18:00:00+00:00",
  "end_time": "2026-07-09T20:00:00+00:00",
  "status": "confirmed",
  "price_cents": 2000,
  "created_at": "2026-07-09T14:37:32.457819+00:00"
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
  "room_id": 1,
  "start_time": "2026-07-10T00:00:00+00:00",
  "end_time": "2026-07-10T01:07:33.137365+00:00"
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
  "room_id": 1,
  "start_time": "2026-07-10T00:00:00+00:00",
  "end_time": "2026-07-10T09:00:00+00:00"
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
  "room_id": 1,
  "start_time": "2026-07-10T13:00:00+00:00",
  "end_time": "2026-07-10T14:00:00+00:00"
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
  "id": 3,
  "reference_code": "CW-001002",
  "room_id": 1,
  "user_id": 3,
  "start_time": "2026-07-10T13:00:00+00:00",
  "end_time": "2026-07-10T14:00:00+00:00",
  "status": "confirmed",
  "price_cents": 1000,
  "created_at": "2026-07-09T14:37:33.465757+00:00"
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
  "room_id": 1,
  "start_time": "2026-07-10T02:00:00+00:00",
  "end_time": "2026-07-10T03:00:00+00:00"
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
  "room_id": 1,
  "start_time": "2026-07-10T15:00:00+00:00",
  "end_time": "2026-07-10T16:00:00+00:00"
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
  "id": 4,
  "reference_code": "CW-001003",
  "room_id": 1,
  "user_id": 2,
  "start_time": "2026-07-10T15:00:00+00:00",
  "end_time": "2026-07-10T16:00:00+00:00",
  "status": "confirmed",
  "price_cents": 1000,
  "created_at": "2026-07-09T14:37:34.273174+00:00"
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
  "room_id": 1,
  "start_time": "2026-07-10T04:00:00+00:00",
  "end_time": "2026-07-10T05:00:00+00:00"
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
  "room_id": 1,
  "start_time": "2026-07-10T04:00:00+00:00",
  "end_time": "2026-07-10T05:00:00+00:00"
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
      "id": 1,
      "reference_code": "CW-001000",
      "room_id": 1,
      "user_id": 3,
      "start_time": "2026-07-09T16:00:00+00:00",
      "end_time": "2026-07-09T18:00:00+00:00",
      "status": "confirmed",
      "price_cents": 2000,
      "created_at": "2026-07-09T14:37:31.288604+00:00"
    },
    {
      "id": 2,
      "reference_code": "CW-001001",
      "room_id": 1,
      "user_id": 3,
      "start_time": "2026-07-09T18:00:00+00:00",
      "end_time": "2026-07-09T20:00:00+00:00",
      "status": "confirmed",
      "price_cents": 2000,
      "created_at": "2026-07-09T14:37:32.457819+00:00"
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
      "id": 1,
      "reference_code": "CW-001000",
      "room_id": 1,
      "user_id": 3,
      "start_time": "2026-07-09T16:00:00+00:00",
      "end_time": "2026-07-09T18:00:00+00:00",
      "status": "confirmed",
      "price_cents": 2000,
      "created_at": "2026-07-09T14:37:31.288604+00:00"
    },
    {
      "id": 2,
      "reference_code": "CW-001001",
      "room_id": 1,
      "user_id": 3,
      "start_time": "2026-07-09T18:00:00+00:00",
      "end_time": "2026-07-09T20:00:00+00:00",
      "status": "confirmed",
      "price_cents": 2000,
      "created_at": "2026-07-09T14:37:32.457819+00:00"
    },
    {
      "id": 3,
      "reference_code": "CW-001002",
      "room_id": 1,
      "user_id": 3,
      "start_time": "2026-07-10T13:00:00+00:00",
      "end_time": "2026-07-10T14:00:00+00:00",
      "status": "confirmed",
      "price_cents": 1000,
      "created_at": "2026-07-09T14:37:33.465757+00:00"
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
      "id": 1,
      "reference_code": "CW-001000",
      "room_id": 1,
      "user_id": 3,
      "start_time": "2026-07-09T16:00:00+00:00",
      "end_time": "2026-07-09T18:00:00+00:00",
      "status": "confirmed",
      "price_cents": 2000,
      "created_at": "2026-07-09T14:37:31.288604+00:00"
    },
    {
      "id": 2,
      "reference_code": "CW-001001",
      "room_id": 1,
      "user_id": 3,
      "start_time": "2026-07-09T18:00:00+00:00",
      "end_time": "2026-07-09T20:00:00+00:00",
      "status": "confirmed",
      "price_cents": 2000,
      "created_at": "2026-07-09T14:37:32.457819+00:00"
    },
    {
      "id": 3,
      "reference_code": "CW-001002",
      "room_id": 1,
      "user_id": 3,
      "start_time": "2026-07-10T13:00:00+00:00",
      "end_time": "2026-07-10T14:00:00+00:00",
      "status": "confirmed",
      "price_cents": 1000,
      "created_at": "2026-07-09T14:37:33.465757+00:00"
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
      "id": 1,
      "reference_code": "CW-001000",
      "room_id": 1,
      "user_id": 3,
      "start_time": "2026-07-09T16:00:00+00:00",
      "end_time": "2026-07-09T18:00:00+00:00",
      "status": "confirmed",
      "price_cents": 2000,
      "created_at": "2026-07-09T14:37:31.288604+00:00"
    },
    {
      "id": 2,
      "reference_code": "CW-001001",
      "room_id": 1,
      "user_id": 3,
      "start_time": "2026-07-09T18:00:00+00:00",
      "end_time": "2026-07-09T20:00:00+00:00",
      "status": "confirmed",
      "price_cents": 2000,
      "created_at": "2026-07-09T14:37:32.457819+00:00"
    },
    {
      "id": 3,
      "reference_code": "CW-001002",
      "room_id": 1,
      "user_id": 3,
      "start_time": "2026-07-10T13:00:00+00:00",
      "end_time": "2026-07-10T14:00:00+00:00",
      "status": "confirmed",
      "price_cents": 1000,
      "created_at": "2026-07-09T14:37:33.465757+00:00"
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
      "id": 1,
      "reference_code": "CW-001000",
      "room_id": 1,
      "user_id": 3,
      "start_time": "2026-07-09T16:00:00+00:00",
      "end_time": "2026-07-09T18:00:00+00:00",
      "status": "confirmed",
      "price_cents": 2000,
      "created_at": "2026-07-09T14:37:31.288604+00:00"
    },
    {
      "id": 2,
      "reference_code": "CW-001001",
      "room_id": 1,
      "user_id": 3,
      "start_time": "2026-07-09T18:00:00+00:00",
      "end_time": "2026-07-09T20:00:00+00:00",
      "status": "confirmed",
      "price_cents": 2000,
      "created_at": "2026-07-09T14:37:32.457819+00:00"
    },
    {
      "id": 3,
      "reference_code": "CW-001002",
      "room_id": 1,
      "user_id": 3,
      "start_time": "2026-07-10T13:00:00+00:00",
      "end_time": "2026-07-10T14:00:00+00:00",
      "status": "confirmed",
      "price_cents": 1000,
      "created_at": "2026-07-09T14:37:33.465757+00:00"
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
- URL: `/bookings/1`
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
  "id": 1,
  "reference_code": "CW-001000",
  "room_id": 1,
  "user_id": 3,
  "start_time": "2026-07-09T16:00:00+00:00",
  "end_time": "2026-07-09T18:00:00+00:00",
  "status": "confirmed",
  "price_cents": 2000,
  "created_at": "2026-07-09T14:37:31.288604+00:00",
  "refunds": []
}
```
**Result:** ✅ PASS

### GET /bookings/{id} - authorization tests: Admin Get Booking
- **Specification clause:** 10. Booking visibility

**Request:**
- Method: `GET`
- URL: `/bookings/1`
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
  "id": 1,
  "reference_code": "CW-001000",
  "room_id": 1,
  "user_id": 3,
  "start_time": "2026-07-09T16:00:00+00:00",
  "end_time": "2026-07-09T18:00:00+00:00",
  "status": "confirmed",
  "price_cents": 2000,
  "created_at": "2026-07-09T14:37:31.288604+00:00",
  "refunds": []
}
```
**Result:** ✅ PASS

### GET /bookings/{id} - multi-tenant tests: Get Another Org Booking
- **Specification clause:** 9. Multi-tenancy

**Request:**
- Method: `GET`
- URL: `/bookings/1`
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
- URL: `/bookings/1`
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
- URL: `/bookings/1`
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
  "id": 1,
  "reference_code": "CW-001000",
  "room_id": 1,
  "user_id": 3,
  "start_time": "2026-07-09T16:00:00+00:00",
  "end_time": "2026-07-09T18:00:00+00:00",
  "status": "confirmed",
  "price_cents": 2000,
  "created_at": "2026-07-09T14:37:31.288604+00:00",
  "refunds": []
}
```
**Result:** ✅ PASS

### GET /bookings/{id} - pagination tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/bookings/1`
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
  "id": 1,
  "reference_code": "CW-001000",
  "room_id": 1,
  "user_id": 3,
  "start_time": "2026-07-09T16:00:00+00:00",
  "end_time": "2026-07-09T18:00:00+00:00",
  "status": "confirmed",
  "price_cents": 2000,
  "created_at": "2026-07-09T14:37:31.288604+00:00",
  "refunds": []
}
```
**Result:** ✅ PASS

### GET /bookings/{id} - datetime tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/bookings/1`
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
  "id": 1,
  "reference_code": "CW-001000",
  "room_id": 1,
  "user_id": 3,
  "start_time": "2026-07-09T16:00:00+00:00",
  "end_time": "2026-07-09T18:00:00+00:00",
  "status": "confirmed",
  "price_cents": 2000,
  "created_at": "2026-07-09T14:37:31.288604+00:00",
  "refunds": []
}
```
**Result:** ✅ PASS

### POST /bookings/{id}/cancel - happy path: Cancel < 24h Notice
- **Specification clause:** 6. Cancellation refund policy

**Request:**
- Method: `POST`
- URL: `/bookings/1/cancel`
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
  "id": 1,
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
- URL: `/bookings/1/cancel`
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
- URL: `/bookings/1/cancel`
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
- URL: `/bookings/1/cancel`
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
- URL: `/bookings/1/cancel`
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
- URL: `/bookings/1/cancel`
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
- URL: `/bookings/1/cancel`
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
- URL: `/bookings/1/cancel`
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
- URL: `/rooms/1/availability?date=2026-07-09`
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
  "room_id": 1,
  "date": "2026-07-09",
  "busy": [
    {
      "start_time": "2026-07-09T18:00:00+00:00",
      "end_time": "2026-07-09T20:00:00+00:00"
    }
  ]
}
```
**Result:** ✅ PASS

### GET /rooms/{id}/availability - datetime tests: Availability Tomorrow
- **Specification clause:** 13. Availability

**Request:**
- Method: `GET`
- URL: `/rooms/1/availability?date=2026-07-10`
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
  "room_id": 1,
  "date": "2026-07-10",
  "busy": [
    {
      "start_time": "2026-07-10T13:00:00+00:00",
      "end_time": "2026-07-10T14:00:00+00:00"
    },
    {
      "start_time": "2026-07-10T15:00:00+00:00",
      "end_time": "2026-07-10T16:00:00+00:00"
    }
  ]
}
```
**Result:** ✅ PASS

### GET /rooms/{id}/availability - invalid input: Invalid Date Format
- **Specification clause:** 13. Availability

**Request:**
- Method: `GET`
- URL: `/rooms/1/availability?date=abc`
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
- URL: `/rooms/1/availability?date=2026-07-09`
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
- URL: `/rooms/1/availability?date=2026-07-09`
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
  "room_id": 1,
  "date": "2026-07-09",
  "busy": [
    {
      "start_time": "2026-07-09T18:00:00+00:00",
      "end_time": "2026-07-09T20:00:00+00:00"
    }
  ]
}
```
**Result:** ✅ PASS

### GET /rooms/{id}/availability - multi-tenant tests: Another Org Room
- **Specification clause:** 9. Multi-tenancy

**Request:**
- Method: `GET`
- URL: `/rooms/1/availability?date=2026-07-09`
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
- URL: `/rooms/1/availability?date=2026-07-09`
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
  "room_id": 1,
  "date": "2026-07-09",
  "busy": [
    {
      "start_time": "2026-07-09T18:00:00+00:00",
      "end_time": "2026-07-09T20:00:00+00:00"
    }
  ]
}
```
**Result:** ✅ PASS

### GET /rooms/{id}/availability - pagination tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/rooms/1/availability?date=2026-07-09`
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
  "room_id": 1,
  "date": "2026-07-09",
  "busy": [
    {
      "start_time": "2026-07-09T18:00:00+00:00",
      "end_time": "2026-07-09T20:00:00+00:00"
    }
  ]
}
```
**Result:** ✅ PASS

### GET /rooms/{id}/stats - happy path: Room Stats
- **Specification clause:** 14. Room stats

**Request:**
- Method: `GET`
- URL: `/rooms/1/stats`
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
  "room_id": 1,
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
- URL: `/rooms/1/stats`
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
- URL: `/rooms/1/stats`
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
  "room_id": 1,
  "total_confirmed_bookings": 3,
  "total_revenue_cents": 4000
}
```
**Result:** ✅ PASS

### GET /rooms/{id}/stats - multi-tenant tests: Stats Another Org
- **Specification clause:** 9. Multi-tenancy

**Request:**
- Method: `GET`
- URL: `/rooms/1/stats`
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
- URL: `/rooms/1/stats`
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
  "room_id": 1,
  "total_confirmed_bookings": 3,
  "total_revenue_cents": 4000
}
```
**Result:** ✅ PASS

### GET /rooms/{id}/stats - pagination tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/rooms/1/stats`
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
  "room_id": 1,
  "total_confirmed_bookings": 3,
  "total_revenue_cents": 4000
}
```
**Result:** ✅ PASS

### GET /rooms/{id}/stats - datetime tests: N/A
- **Specification clause:** API contract

**Request:**
- Method: `GET`
- URL: `/rooms/1/stats`
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
  "room_id": 1,
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
      "room_id": 1,
      "room_name": "Room A",
      "confirmed_bookings": 1,
      "revenue_cents": 2000
    },
    {
      "room_id": 2,
      "room_name": "Room B",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    },
    {
      "room_id": 3,
      "room_name": "Room C",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    },
    {
      "room_id": 4,
      "room_name": "Room D",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    },
    {
      "room_id": 5,
      "room_name": "Room E",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    },
    {
      "room_id": 6,
      "room_name": "Room F",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    },
    {
      "room_id": 7,
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
      "room_id": 1,
      "room_name": "Room A",
      "confirmed_bookings": 1,
      "revenue_cents": 2000
    },
    {
      "room_id": 2,
      "room_name": "Room B",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    },
    {
      "room_id": 3,
      "room_name": "Room C",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    },
    {
      "room_id": 4,
      "room_name": "Room D",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    },
    {
      "room_id": 5,
      "room_name": "Room E",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    },
    {
      "room_id": 6,
      "room_name": "Room F",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    },
    {
      "room_id": 7,
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
      "room_id": 1,
      "room_name": "Room A",
      "confirmed_bookings": 1,
      "revenue_cents": 2000
    },
    {
      "room_id": 2,
      "room_name": "Room B",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    },
    {
      "room_id": 3,
      "room_name": "Room C",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    },
    {
      "room_id": 4,
      "room_name": "Room D",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    },
    {
      "room_id": 5,
      "room_name": "Room E",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    },
    {
      "room_id": 6,
      "room_name": "Room F",
      "confirmed_bookings": 0,
      "revenue_cents": 0
    },
    {
      "room_id": 7,
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
- URL: `/admin/export?room_id=1`
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
