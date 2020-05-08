# API Specification

### Create User
User makes account during sign-in, returns user info \
```
**POST /api/users/**
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
      "password": <USER INPUT>
      "clubs": [],
      "events": [],
      "tasks": [],
      "messages": []
    }
  ]
}
```

### Get Specific User by ID
Homepage, return user's clubs, events, & tasks \
```
**GET /api/users/{id}/**
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
      "password": <USER INPUT>,
      "clubs": [<SERIALIZED CLUBS>, ... ],
      "events": [<SERIALIZED EVENTS>, ... ],
      "tasks": [<SERIALIZED TASKS>, ... ],
      "messages": [<SERIALIZED MESSAGES>, ... ]
    }
  ]
}
```

### Return all clubs
Return all clubs from DB (when user searches for clubs to add) \
```
**GET /api/clubs/**
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
      "messages": [ <SERIALIZED USER WITHOUT CLUB FIELD>, ... ]
    }
    ...
  ]
}
```

### Add new club to DB (Admin)
```
**POST /api/clubs/**
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

### Get club by id
```
**GET /api/clubs/{id}/**
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
      "events": [<SERIALIZED CLUBS WITHOUT CLUB FIELD>, ... ],
      "admins": [<SERIALIZED USERS WITHOUT CLUB FIELD>, ... ],
      "members": [<SERIALIZED USERS WITHOUT CLUB FIELD>, ... ],
      "messages": [<SERIALIZED MESSAGES WITHOUT CLUB FIELD>, ... ]
    }
    ...
  ]
}
```

### Delete club from DB (Admin only)
```
**DELETE /api/clubs/{id}/**
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

### User request to join club
```
**POST /api/addrequest/**
```
Request
```
{
  "user_id": <USER INPUT>,
  "club_id": <USER INPUT>,
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
      "name": <USER INPUT FOR NAME>,
      "description": <USER INPUT FOR DESCRIPTION>,
      "events": [<SERIALIZED CLUBS WITHOUT CLUB FIELD>, ... ],
      "admins": [<SERIALIZED USERS WITHOUT CLUB FIELD>, ... ],
      "members": [<SERIALIZED USERS WITHOUT CLUB FIELD>, ... ],
      "messages": [<SERIALIZED MESSAGES WITHOUT CLUB FIELD>, ... ]
    }
  ]
}
```

### Accept/decline user's request to join club (Admin)
```
**POST /api/addrequest/{id}/**
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
      "name": <USER INPUT FOR NAME>,
      "description": <USER INPUT FOR DESCRIPTION>,
      "events": [<SERIALIZED EVENTS>, ... ],
      "admins": [<SERIALIZED USERS>, ... ],
      "members": [<SERIALIZED USERS>, ... ],
      "messages": [<SERIALIZED MESSAGES>, ... ]
    }
  ]
}
```

### Get all events
```
**GET /api/clubs/{id}/events/**
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

### Add event (Admin)
```
**POST /api/events/**
```
Response
```
{
  "success": true,
  "data": {
    "id": <ID>,
    "name": <USER INPUT FOR NAME>,
    "budget": <USER INPUT FOR BUDGET>
  }
}
```

### Add club to event (Admin)
```
**POST /api/events/addclub**
```
Response
```
{
  "success": true,
  "data": {
    "id": <ID>,
    "name": <USER INPUT FOR NAME>,
    "budget": <USER INPUT FOR BUDGET>
  }
}
```

### Delete event (Admin)
``` **DELETE /api/events/**
```

### Get all tasks in event
``` **GET /api/events/{id}/tasks**
```

``` **POST /api/events/{id}/tasks**
```

``` **DELETE /api/events/{id}/tasks**
```
