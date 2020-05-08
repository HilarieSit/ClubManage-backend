# API Specification

## FRAME 1
### Create User (user makes account during sign-in) \
**POST /api/users/** \
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

## FRAME 2
### Get Specific User by ID (login) \
**GET /api/users/{id}** \
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

## FRAME 3
### Get user's clubs (launch page) \
**GET /api/users/{id}/clubs/** \
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

## FRAME 4
### Return all clubs from DB (when user searches for clubs to add) \
**GET /api/clubs/** \
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

### Add new club to DB (Admin) \
**POST /api/clubs/** \
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

## FRAME 5
### Get club by id
**GET /api/clubs/{id}**

### Delete club from DB (Admin only) \
**DELETE /api/clubs/{id}** \
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

## FRAME 6
### User request to join club \
**POST /api/addclubrequest/** \
Request
```
{
  "user_id": <USER ID>,
  "club_id": <USER INPUT>,
  "accepted": null
}
```
Response
```
{

}
```

## FRAME 7
### Accept/decline user's request to join club (Admin) \
**POST /api/addclubrequest/{id}/** \
Request
```
{
  "accepted": true or false
}
```
Response
```
{
}
```

## FRAME 8
### Get club's group chat \


## FRAME 9
### Get user's active events in that club \
**GET /api/users/{id}/clubs/{id}/events/** \
```
{

}
```

## FRAME 10
### Get all events (can be collab with multiple clubs) \
**GET /api/events/** \

### Add event (Admin) \
**POST /api/events/** \
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

### Delete event (Admin) \
**DELETE /api/events/** \

## FRAME 11
### Get user's tasks \
**GET /api/users/{id}/events/{id}/tasks** \

## FRAME 12
### Get all tasks in event \
**GET /api/events/{id}/tasks** \

## FRAME 13
**POST /api/events/{id}/tasks** \



### User send message \
**POST /api/messages/** \
