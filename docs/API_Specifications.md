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

### 6) User Request to Join Club
Return request info
```
POST /api/addrequest/
```
Request
```
{
  "user_id": <USER INPUT>,
  "club_id": <USER INPUT>,
  "message": <USER INPUT>,
  "accepted": null
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
      "message": <USER INPUT FOR MESSAGE>
      "accepted": <USER INPUT FOR ACCEPTED>
    }
  ]
}
```

### 7) Accept/Decline Requests to Join Club (Admin)
```
POST /api/addrequest/{id}/
```
Request
```
{
  "accepted": true or false
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
      "message": <USER INPUT FOR MESSAGE>
      "accepted": <USER INPUT FOR ACCEPTED>
    }
  ]
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
      "events": [<SERIALIZED EVENTS>, ... ],
      "admins": [<SERIALIZED USERS>, ... ],
      "members": [<SERIALIZED USERS>, ... ]
    }
  ]
}
```

### 9) Add Event
Adds new event
```
POST /api/events/
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
    "active": true,
    "tasks": [],
    "clubs": [],
    "users": []
  }
}
```

### 10) Add Another Club to Event (Admin)
Club Admin adds another club (collaboration)
```
POST /api/events/addclub/
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
    "active": true,
    "tasks": [<SERIALIZED TASK>, ... ],
    "clubs": [<SERIALIZED CLUB>, ... ],
    "users": [<SERIALIZED USERS>, ... ]
  }
}
```

### 11) Delete event (Admin)
```
DELETE /api/events/{id}/
```
Delete event
```
{
  "success": true,
  "data": {
    "id": <ID>,
    "name": <USER INPUT FOR NAME>,
    "date": <USER INPUT FOR DATE>,
    "description": <USER INPUT FOR DESCRIPTION>,
    "budget": <USER INPUT FOR BUDGET>,
    "active": true,
    "tasks": [<SERIALIZED TASK>, ... ],
    "clubs": [<SERIALIZED CLUB>, ... ],
    "users": [<SERIALIZED USERS>, ... ]
  }
}
```

### 12) Add User to Event
```
POST /api/events/{id}/add/
```
User add event
```
{
  "success": true,
  "data": <SERIALIZED EVENT>
  }
}
```

### 12) Create Task
```
POST /api/events/{id}/tasks/
```
```
{
  "success": true,
  "data": {
    "id": <ID>,
    "name": <USER INPUT FOR NAME>,
    "date": <USER INPUT FOR DATE>,
    "description": <USER INPUT FOR DESCRIPTION>,
    "budget": <USER INPUT FOR BUDGET>,
    "active": true,
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
```
{
  "success": true,
  "data": {
    "id": <ID>,
    "name": <USER INPUT FOR NAME>,
    "date": <USER INPUT FOR DATE>,
    "description": <USER INPUT FOR DESCRIPTION>,
    "budget": <USER INPUT FOR BUDGET>,
    "active": true,
    "tasks": [<SERIALIZED TASK>, ... ],
    "clubs": [<SERIALIZED CLUB>, ... ],
    "users": [<SERIALIZED USERS>, ... ]
  }
}
```

### 14) Add Task to User
```
POST /api/events/{id}/tasks/add/
```
```
{
  "success": true,
  "data": <SERIALIZED TASK>
}
```
