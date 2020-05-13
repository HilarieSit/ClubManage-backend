# API Specification

### 1) Create User
User makes account during sign-in, returns user info

<code>POST</code> /api/users/

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
Homepage, Return user's clubs, events, tasks

<code>GET</code> /api/users/{id}/

Response
```
{
  "success": true,
  "data": [
    {
      "id": <ID>,
      "name": <USER INPUT>,
      "email": <USER INPUT>,
      "clubs": [<SERIALIZED CLUB INFO>, ... ],
      "events": [<SERIALIZED EVENT INFO>, ... ],
      "tasks": [<SERIALIZED TASK INFO>, ... ]
    }
  ]
}
```

### 3) Return All Clubs
User searches for clubs to add, Return all clubs from DB
(return name, description)

<code>GET</code> /api/clubs/

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

<code>POST</code> /api/clubs/

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

<code>DELETE</code> /api/clubs/{id}/

Response
```
{
  "success": true,
  "data": [
    {
      "id": <ID>,
      "name": <USER INPUT FOR NAME>,
      "description": <USER INPUT FOR DESCRIPTION>,
      "events": [ <SERIALIZED EVENT INFO>, ... ],
      "admins": [ <SERIALIZED USER INFO>, ... ],
      "members": [ <SERIALIZED USER INFO>, ... ]
    }
  ]
}
```

### 6) User Request to Join Club
Return request info (for joining club)

<code>POST</code> /api/addrequest/

Request
```
{
  "user_id": <USER INPUT>,
  "club_id": <USER INPUT>,
  "message": <USER INPUT> or null,
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
      "user_id": <USER INPUT FOR NAME>,
      "club_id": <USER INPUT FOR CLUB ID>,
      "message": <USER INPUT FOR MESSAGE>
      "accepted": <USER INPUT FOR ACCEPTED>
    }
  ]
}
```

### 7) Accept/Decline Requests to Join Club (Admin)
Admin accepts or declines request & set user type

<code>POST</code> /api/addrequest/{id}/

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

### 8) Add User to Club (Admin)
Add user to club

<code>POST</code> /api/clubs/{id}/adduser/

Request
```
{
  "user_id": <USER INPUT>,
  "type": "admin" or "member"
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
      "events": [<SERIALIZED EVENT INFO>, ... ],
      "admins": [<SERIALIZED USER INFO>, ... ],
      "members": [<SERIALIZED USER INFO>, ... ]
    }
  ]
}
```


### 9) Get Club by Id
Returns club info by id

<code>GET</code> /api/clubs/{id}/

Response
```
{
  "success": true,
  "data": [
    {
      "id": <ID>,
      "name": <USER INPUT FOR NAME>,
      "description": <USER INPUT FOR DESCRIPTION>,
      "events": [<SERIALIZED EVENT INFO>, ... ],
      "admins": [<SERIALIZED USER INFO>, ... ],
      "members": [<SERIALIZED USER INFO>, ... ]
    }
  ]
}
```

### 10) Create New Event
Adds new event

<code>POST</code> /api/events/

Request
```
{
  "name": <USER INPUT>,
  "date": <USER INPUT>,
  "description": <USER INPUT>,
  "budget": <USER INPUT>,
  "location": <USER INPUT> 
  "time": <USER INPUT>
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
    "location": <USER INPUT FOR LOCATION>
    "time": <USER INPUT FOR TIME> 
    "budget": <USER INPUT FOR BUDGET>,
    "tasks": [],
    "clubs": [],
    "users": []
  }
}
```

### 11) Add Another Club to Event (Admin)
Club Admin adds another club (collaboration)

<code>POST</code> /api/events/{id}/addclub/

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

### 12) Delete Event
Delete event

<code>DELETE</code> /api/events/{id}/

Response
```
{
  "success": true,
  "data": {
    "id": <ID>,
    "name": <USER INPUT FOR NAME>,
    "date": <USER INPUT FOR DATE>,
    "description": <USER INPUT FOR DESCRIPTION>,
    "location": <USER INPUT FOR LOCATION>
    "time": <USER INPUT FOR TIME> //in Unix String
    "budget": <USER INPUT FOR BUDGET>,
    "tasks": [<SERIALIZED TASK INFO>, ... ],
    "clubs": [<SERIALIZED CLUB INFO>, ... ],
    "users": [<SERIALIZED USER INFO>, ... ]
  }
}
```

### 13) Get Event by Id
Returns event info by id

<code>GET</code> /api/events/{id}/

Response
```
{
  "success": true,
  "data": {
    "id": <ID>,
    "name": <USER INPUT FOR NAME>,
    "date": <USER INPUT FOR DATE>,
    "description": <USER INPUT FOR DESCRIPTION>,
    "location": <USER INPUT FOR LOCATION>
    "time": <USER INPUT FOR TIME> //in Unix String
    "budget": <USER INPUT FOR BUDGET>,
    "tasks": [<SERIALIZED TASK INFO>, ... ],
    "clubs": [<SERIALIZED CLUB INFO>, ... ],
    "users": [<SERIALIZED USER INFO>, ... ]
  }
}
```

### 14) Add User to Event
Add a user to a event

<code>POST</code> /api/events/<int:event_id>/adduser/

Request
```
{
  "user_id": <USER INPUT>
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
    "location": <USER INPUT FOR LOCATION>
    "time": <USER INPUT FOR TIME> //in Unix String
    "budget": <USER INPUT FOR BUDGET>,
    "tasks": [<SERIALIZED TASK INFO>, ... ],
    "clubs": [<SERIALIZED CLUB INFO>, ... ],
    "users": [<SERIALIZED USER INFO>, ... ]
  }
}
```

### 15) Create Task
Create task

<code>POST</code> /api/events/{id}/tasks/

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
    "clubs": [],
    "users": []
  }
}
```

### 16) Delete Task
Delete task

<code>DELETE</code> /api/events/{id}/tasks/

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
    "clubs": [<SERIALIZED CLUB>, ... ],
    "users": [<SERIALIZED USERS>, ... ]
  }
}
```

### 17) Add User to Task
Add a user to a task

<code>POST</code> /api/tasks/<int:task_id>/adduser/

Request
```
{
  "user_id": <USER INPUT>
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
    "clubs": [<SERIALIZED CLUB>, ... ],
    "users": [<SERIALIZED USERS>, ... ]
  }
}
```

### 18) Edit an Event

Update an event 

<code>POST</code> /api/events/{id}/

Request
```
{
  "name": <USER INPUT FOR NAME OPTIONAL>,
  "date": <USER INPUT FOR DATE OPTIONAL>,
  "description": <USER INPUT FOR DESCRIPTION OPTIONAL>,
  "budget": <USER INPUT FOR BUDGET OPTIONAL>,
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
    "location": <USER INPUT FOR LOCATION>
    "time": <USER INPUT FOR TIME> //in Unix String
    "budget": <USER INPUT FOR BUDGET>,
    "tasks": [<SERIALIZED TASK INFO>, ... ],
    "clubs": [<SERIALIZED CLUB INFO>, ... ],
    "users": [<SERIALIZED USER INFO>, ... ]
  }
}
```

### 19) Edit a Club

Update a club

<code>POST</code> /api/clubs/{id}/

Request
```
{
  "name": <USER INPUT OPTIONAL>,
  "description": <USER INPUT OPTIONAL>
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

### 20) Remove a Club from User
<code>POST</code> /api/clubs/{cid}/{uid}

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
