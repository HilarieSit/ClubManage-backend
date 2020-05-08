##API Specification

Create User (user makes account during sign-in)
**POST /api/users/**
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
      "email": <USER INPUT>,
      "password": <USER INPUT>
      "clubs": [],
      "events": [],
      "tasks": [],
      "messages": []
    },
}
```

Get Specific User by ID (login)
**GET /api/users/{id}**
Response
```
{
  "success": true,
  "data": [
    {
      "id": <ID>,
      "email": <USER INPUT>,
      "password": <USER INPUT>
      "clubs": [],
      "events": [],
      "tasks": [],
      "messages": []
    },
}
```

Get user's clubs (launch page)
**GET /api/users/{id}/clubs/{id}/**
Response
```
{  
  "success": true,
  "data": [
    {
      "id": 1,
      "name": "Intramural Volleyball",
      "description": "Intramural volleyball team",
      "events": [ <SERIALIZED EVENTS WITHOUT CLUB FIELD>, ... ],
      "admins": [ <SERIALIZED USER WITHOUT CLUB FIELD>, ... ],
      "members": [ <SERIALIZED USER WITHOUT CLUB FIELD>, ... ],
      "messages": [ <SERIALIZED USER WITHOUT CLUB FIELD>, ... ]
    },
    {
      "id": 2,
      "name": "APO",
      "description": "National service fraternity",
      "events": [ <SERIALIZED EVENTS WITHOUT CLUB FIELD>, ... ],
      "admins": [ <SERIALIZED USER WITHOUT CLUB FIELD>, ... ],
      "members": [ <SERIALIZED USER WITHOUT CLUB FIELD>, ... ]
      "messages": [ <SERIALIZED USER WITHOUT CLUB FIELD>, ... ]
    }
    ...
  ]
}
```

Return all clubs from DB (when user searches for clubs to add)
**GET /api/clubs/{id}**
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
    },
}
```

Add new club to DB (Admin)
**POST /api/clubs/**
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

Delete club from DB (Admin)
**DELETE /api/clubs/{id}**
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
    },
}
```

User request to join club
**POST /api/users/{id}/clubs/{id}/add**

Add user to club (Admin)
**POST /api/??**

Get all events in club
**GET /api/clubs/{id}/events/**

Get specific event (can be collab with multiple clubs)
**GET /api/events/{id}**

Add event (Admin)
**GET /api/events/**

Delete event (Admin)
**GET /api/events/**

Get all tasks in event
**POST /api/events/{id}/task**

Get all tasks in event
**POST /api/events/{id}/task**
