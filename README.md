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

`GET /pokemon/{pokename}/` Displays information about the pokemon

`GET /pokemon/` Shows all types of pokemon. You can also paginate: `/pokemon/?limit=100&offset=400`

`GET /pokemon/all_pokemon/` Shows all pokemon

`GET /accounts/{user}/` Display user information

### POST

`POST /pokemon/create_poke/` Create a pokemon. Expected fields:

- name, description, type name, height, weight and picture

`POST /pokemon/create_type/` Create a type of pokemon. Expected fields:

- name and description
  
`POST /accounts/login/` Login user and returns a token. Expected fields:

- email and password

`POST /accounts/signup/` Register a new user. Expected fields:

- username, email, first_name, last_name, password and password_confirmation

`POST /accounts/verify/` Verify a new user. Expected fields:

- token

### PUT, PATCH and DELETE

`DELETE /pokemon/{pokename}/` Delete a pokemon

`PUT and PATCH /pokemon/{pokename}/` Update or partially update the pokemon. Expected fields:

- name, description, type name, height, weight and picture

`PUT and PATCH /accounts/{user}/` Update or partially update the user. Expected fields:

- username, email, first_name and last_name

`PUT and PATCH /accounts/{user}/profile/` Update or partially update the user profile. Expected fields:

- picture

## Example

### Login

In this example, a POST request is made to the `POST /accounts/login/` route with the email and the password. Then the content of the request is decoded, the json is obtained and then the token is obtained.

![example-1](/.github/images/example1.png)

### Display pokemon types

A GET request is made to the `GET /pokemon/all_types` route, the authorization header is set with a token, and the data is returned.

![example-2](/.github/images/example2.png)