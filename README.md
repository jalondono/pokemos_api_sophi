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
- `/api/register/` - Create User
- `/api/v1/me/` - User Info
- `/api/auth/token/` - Get Token
- `/api/auth/token/refresh/` - Refresh Token

### Pokemon CRUD
- `/api/v1/pokemon/` - Read only pokemon types
- `/api/v1/pokemon_type/` - CRUD operation on pokemons


### Get random number from external API
- `/api/random_number/` - Get random number (public)

## Rules
- The public Pokemons can't update/deleted unless the owner send the request
- A private pokemon should have associated always a user
- Only the owners can update their pokemons

## Note: Be sure you add the Authorization header as follows:
```
Authorization: "Bearer token..."
```

### Example:
- Payload Example:
Notice the user could be optional, but the pokemon type is a must, so you have to get the pokemon_type_id from pokemon type endpoint
<img align="center" src="https://i.imgur.com/4d8stlA.png" height="50%" width="50%"/>


