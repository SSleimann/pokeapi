# PokeDja

Basic API to see the pokemons and their types

## Features

- See, create and delete pokemons
- Create types of pokemon
- User authentication
- Register and verify users

## Usage

First you must make sure you have PostgreSQL installed

After that, you should:

1. First you need to have a virtual environment
2. Clone the repository from Github and switch to the new directory:

   ```bash
   git clone https://github.com/SSleimann/pokeapi.git
   cd pokeapi
   ```

3. Activate the virtualenv for your project and install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set the environment variables

    ```bash
    DJANGO_DEBUG=True
    DJANGO_SECRET_KEY=yourmegasecretpassword
    DATABASE_URL=postgres://user:password@host:port/db
   ```

5. Apply the migrations:

   ```bash
   python manage.py migrate --settings=pokeapi.settings.local
   ```

6. Now you can run the server:

   ```bash
   python manage.py runserver --settings=pokeapi.settings.local
   ```

## Methods

### GET

`GET /pokemon/{pokename}` Displays information about the pokemon

`GET /pokemon/all_types` Shows all types of pokemon

`GET /accounts/{user}/` Display user information

### POST

`POST /pokemon/create_poke/` Create a pokemon

`POST /pokemon/create_type/` Create a type of pokemon

`POST /accounts/login/` Login user and returns a token

`POST /accounts/signup/` Register a new user

`POST /accounts/verify/` Verify a new user

### PUT, PATCH and DELETE

`DELETE /pokemon/{pokename}/` Delete a pokemon

`PUT and PATCH /pokemon/{pokename}` Update or partially update the pokemon

`PUT and PATCH /accounts/{user}` Update or partially update the user

`PUT and PATCH /accounts/profile` Update or partially update the user profile
