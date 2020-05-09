# API Specification

### 1) Create User
User makes account during sign-in, returns user info
```
POST /api/users/
```
Request
```
{
  "name": <USER INPUT>,
  "email": <USER INPUT>,
  "password": <USER INPUT>
}
```
Response
```
{
  "success": true,
  "data": [
    {
      "id": <ID>,
      "name": <NAME>,
      "email": <USER INPUT>,
      "clubs": [],
      "events": [],
      "tasks": []
    }
  ]
}
```

### 2) Get Specific User by ID
Login/homepage, return user's clubs, events, tasks & messages (if receiver)
```
GET /api/users/{id}/
```
Response
```
{
  "success": true,
  "data": [
    {
      "id": <ID>,
      "name": <USER INPUT>,
      "email": <USER INPUT>,
      "clubs": [<SERIALIZED CLUBS>, ... ],
      "events": [<SERIALIZED EVENTS>, ... ],
      "tasks": [<SERIALIZED TASKS>, ... ]
    }
  ]
}
```

### 3) Return All Clubs
User searches for clubs to add, Return all clubs from DB
(return name, description)
```
GET /api/clubs/
```
Response
```
{
  "success": true,
  "data": [
    {
      "id": <ID>,
      "name": <USER INPUT FOR NAME>,
      "description": <USER INPUT FOR DESCRIPTION>
    }
    ...
  ]
}
```

### 4) Add New Club to DB (Admin)
Admin adds new club, Returns club info
```
POST /api/clubs/
```
Request
```
{
  "name": <USER INPUT>,
  "description": <USER INPUT>
}
```
Response
```
{
  "success": true,
  "data": [
    {
      "id": <ID>,
      "name": <USER INPUT FOR NAME>,
      "description": <USER INPUT FOR DESCRIPTION>,
      "events": [],
      "admins": [],
      "members": []
    },
}
```

### 5) Delete Club From DB (Admin)
Admin deletes club, Returns club info
```
DELETE /api/clubs/{id}/
```
Response
```
{
  "success": true,
  "data": [
    {
      "id": <ID>,
      "name": <USER INPUT FOR NAME>,
      "description": <USER INPUT FOR DESCRIPTION>,
      "events": [ <SERIALIZED EVENTS WITHOUT CLUB FIELD>, ... ],
      "admins": [ <SERIALIZED USER WITHOUT CLUB FIELD>, ... ],
      "members": [ <SERIALIZED USER WITHOUT CLUB FIELD>, ... ]
    }
  ]
}
```

### 6) User Request to Join Club/Event/Task
Return request info (for joining club, set accepted = null (require admin approval))
```
POST /api/addrequest/
```
Request
```
{
  "user_id": <USER INPUT>,
  "club_id": <USER INPUT>,
  "event_id": <USER INPUT> or null,
  "task_id": <USER INPUT> or null,
  "message": <USER INPUT> or null,
  "accepted": true or null
}
```
Response
```
{
  "success": true,
  "data": [
    {
      "id": <ID>,
      "time": <NOW>,
      "user_id": <USER INPUT FOR NAME>,
      "club_id": <USER INPUT FOR CLUB ID>,
      "event_id": <USER INPUT FOR EVENT ID>,
      "task_id": <USER INPUT FOR TASK ID>,
      "message": <USER INPUT FOR MESSAGE>
      "accepted": <USER INPUT FOR ACCEPTED>
    }
  ]
}
```

### 7) Accept/Decline Requests to Join Club (Admin)
Admin accepts or declines request & set user type
```
POST /api/addrequest/{id}/
```
Request
```
{
  "accepted": true or false,
  "type": "admin" or "member"
}
```
Response
```
{
  "success": true,
  "data": <SERIALIZED CLUB>
}
```

### 8) Get Club by Id
Returns club info by id
```
GET /api/clubs/{id}/
```
Response
```
{
  "success": true,
  "data": [
    {
      "id": <ID>,
      "name": <USER INPUT FOR NAME>,
      "description": <USER INPUT FOR DESCRIPTION>,
      "events": [<SERIALIZED EVENTS WITHOUT CLUB INFO>, ... ],
      "admins": [<SERIALIZED USERS WITHOUT CLUB INFO>, ... ],
      "members": [<SERIALIZED USERS WITHOUT CLUB INFO>, ... ]
    }
  ]
}
```

### 9) Add Event
Adds new event
```
POST /api/events/
```
Request
```
{
  "name": <USER INPUT>,
  "date": <USER INPUT>,
  "description": <USER INPUT>,
  "budget": <USER INPUT>
}
```
Response
```
{
  "success": true,
  "data": {
    "id": <ID>,
    "name": <USER INPUT FOR NAME>,
    "date": <USER INPUT FOR DATE>,
    "description": <USER INPUT FOR DESCRIPTION>,
    "budget": <USER INPUT FOR BUDGET>,
    "tasks": [],
    "clubs": [],
    "users": []
  }
}
```

### 10) Add Another Club to Event (Admin)
Club Admin adds another club (collaboration)
```
POST /api/events/{id}/addclub/
```
Request
```
{
  "club_id": <USER INPUT>
}
```
Response
```
{
  "success": true,
  "data": <SERIALIZED EVENT>
}
```

### 11) Delete event
Delete event
```
DELETE /api/events/{id}/
```
Response
```
{
  "success": true,
  "data": {
    "id": <ID>,
    "name": <USER INPUT FOR NAME>,
    "date": <USER INPUT FOR DATE>,
    "description": <USER INPUT FOR DESCRIPTION>,
    "budget": <USER INPUT FOR BUDGET>,
    "tasks": [<SERIALIZED TASK WITHOUT EVENT INFO>, ... ],
    "clubs": [<SERIALIZED CLUB WITHOUT EVENT INFO>, ... ],
    "users": [<SERIALIZED USERS WITHOUT EVENT INFO>, ... ]
  }
}
```

### 12) Create Task
Create task
```
POST /api/events/{id}/tasks/
```
Request
```
{
  "name": <USER INPUT>,
  "date": <USER INPUT>,
  "description": <USER INPUT>,
  "budget": <USER INPUT>
}
```
Response
```
{
  "success": true,
  "data": {
    "id": <ID>,
    "name": <USER INPUT FOR NAME>,
    "date": <USER INPUT FOR DATE>,
    "description": <USER INPUT FOR DESCRIPTION>,
    "budget": <USER INPUT FOR BUDGET>,
    "tasks": [],
    "clubs": [],
    "users": []
  }
}
```

### 13) Delete Task

```
DELETE /api/events/{id}/tasks/
```
Response
```
{
  "success": true,
  "data": {
    "id": <ID>,
    "name": <USER INPUT FOR NAME>,
    "date": <USER INPUT FOR DATE>,
    "description": <USER INPUT FOR DESCRIPTION>,
    "budget": <USER INPUT FOR BUDGET>,
    "tasks": [<SERIALIZED TASK>, ... ],
    "clubs": [<SERIALIZED CLUB>, ... ],
    "users": [<SERIALIZED USERS>, ... ]
  }
}
```