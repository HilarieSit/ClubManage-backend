# API Specification

### 1 Create User
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
      "tasks": [],
      "messages": []
    }
  ]
}
```

### 2 Get Specific User by ID
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
      "tasks": [<SERIALIZED TASKS>, ... ],
      "messages": [<SERIALIZED MESSAGES>, ... ]
    }
  ]
}
```

### 3 Return All Clubs
User searches for clubs to add, Return all clubs from DB
(Only return name, description, events)
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
      "description": <USER INPUT FOR DESCRIPTION>,
      "events": [ <SERIALIZED EVENTS WITHOUT TASKS/ADMINS/MEMBERS FIELDS>, ... ]
    }
    ...
  ]
}
```

### 4 Add New Club to DB (Admin)
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
      "members": [],
      "messages": []
    },
}
```

### 5 Delete Club From DB (Admin)
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
      "messages": [ <SERIALIZED MESSAGES WITHOUT CLUB FIELD>, ... ]
    }
  ]
}
```

### 6 Get Club by Id
User clicks on club from search for more info, Returns club info
(Only return name, description, events)
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
      "events": [ <SERIALIZED EVENTS WITHOUT TASKS/ADMINS/MEMBERS FIELDS>, ... ]
    }
  ]
}
```

### 7 User Request to Join Club
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

### 8 Accept/Decline Requests to Join Club (Admin)
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

### 9 Get All Events
User searches for events in club, Returns events
```
GET /api/clubs/{id}/events/
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
      "date": <USER INPUT FOR DATE>,
      "budget": <USER INPUT FOR BUDGET>,
      "active": <USER INPUT FOR ACTIVE>,
      "clubs": [<SERIALIZED CLUBS>, ... ],
      "users": [<SERIALIZED USERS>, ... ],
      "tasks": [<SERIALIZED TASKS>, ... ]
    }
    ...
  ]
}
```

### 10 Add Event (Admin)
Club Admin adds new event
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
    "active": true
  }
}
```

### 11 Add Club to Event (Admin)
Admin adds another club (collaboration)
```
POST /api/events/addclub
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
    "active": true
  }
}
```

### 12 Delete event (Admin)
``` DELETE /api/events/
```

### 13 Get all tasks in event
``` GET /api/events/{id}/tasks
```

``` POST /api/events/{id}/tasks
```

``` DELETE /api/events/{id}/tasks
```
