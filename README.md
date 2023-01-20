# Pokemon API

This project represents a Pokemon API which is used for publish and share Pokemons


# Requirements
- Docker
- Docker-compose

# Instructions
- Build the docker image using the command `docker-compose build`
- Run the docker image using the command `docker-compose up -d`
  - To run the tests use the command `docker exec -it pokemos_api_sophi_web_1 python manage.py test core`


## Endpoints

### Register and Authentication
- POST `/api/register/` - Create User
- GET `/api/v1/me/` - User Info
- POST`/api/auth/token/` - Get Token
- POST `/api/auth/token/refresh/` - Refresh Token

### Pokemon CRUD
- GET `/api/v1/pokemon/` - Read only pokemon types
- ALL Verbs`/api/v1/pokemon_type/` - CRUD operation on pokemons


### Get random number from external API
- POST `/api/random_number/` - Get random number (public)

## Rules
- The public Pokemons can't update/deleted unless the owner send the request
- A private pokemon should have associated always a user
- Only the owners can update their pokemons

## Note: Be sure you add the Authorization header as follows:
```
Authorization: "Bearer token..."
```

### Example:
- Payload Registration:
<img width="655" alt="image" src="https://user-images.githubusercontent.com/51680387/213747682-2c42f510-8acc-45eb-ab05-47a76b1e971b.png">

- Payload Get Token:
<img width="1086" alt="image" src="https://user-images.githubusercontent.com/51680387/213747878-f05c88de-2fd9-4f61-bacd-9ddef0e06168.png">

- Payload Example Pokemon Creation:
Notice the user could be optional, but the pokemon type is a must, so you have to get the pokemon_type_id from pokemon type endpoint
<img align="center" src="https://i.imgur.com/4d8stlA.png" height="50%" width="50%"/>

- Get random Number:

