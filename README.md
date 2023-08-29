# Airport Service API
- An API service for airport management, written in Django REST Framework

## Features
- Management of buying tickets
- Supports JWT authentication.
- Swagger documentation.


## Technologies Used

- Django
- Django REST framework
- SQLite (or your preferred database)
- JSON Web Tokens (JWT) for authentication

## There are such endpoints:

### User:

- [POST] /users/register/   (register your user)
- [GET] /users/me   (info about yourself)
- [PUT] /users/me   (update all info about yourself)
- [PATCH] /users/me  (partial update of info about yourself)
- [POST] /users/token (get your JWT token for access)
- [POST] /users/token/refresh (update your access token)

### Airport:

- [POST] /api/airport/airports   (create nem airport)
- [GET] /api/airport/airports   (list of all airports)
- [GET] /api/airport/airports/{id}   (detail info about airport)
- [PUT] /api/airport/airports/{id}   (update all airport instance)
- [PATCH] /api/airport/airports/{id}   (partial update of airport instance)
- [DELETE] /api/airport/airports/{id}   (delete airport with chosen id)

### Route:

- [POST] /api/airport/routes   (create nem route)
- [GET] /api/airport/routes   (list of all routes)
- [GET] /api/airport/routes/{id}   (detail info about route)
- [PUT] /api/airport/routes/{id}   (update all route instance)
- [PATCH] /api/airport/routes/{id}   (partial update of route instance)
- [DELETE] /api/airport/routes/{id}   (delete route with chosen id)

### Airplane type:

- [POST] /api/airport/airplane_types   (create nem airplane type)
- [GET] /api/airport/airplane_types   (list of all airplane types)
- [GET] /api/airport/airplane_types/{id}   (detail info about airplane type)
- [PUT] /api/airport/airplane_types/{id}   (update all airplane type instance)
- [PATCH] /api/airport/airplane_types/{id}   (partial update of airplane type instance)
- [DELETE] /api/airport/airplane_types/{id}   (delete airplane type with chosen id)

### Crew:

- [POST] /api/airport/crews   (create nem crew)
- [GET] /api/airport/crews   (list of all crews)
- [GET] /api/airport/crews/{id}   (detail info about crew)
- [PUT] /api/airport/crews/{id}   (update all crew instance)
- [PATCH] /api/airport/crews/{id}   (partial update of crew instance)
- [DELETE] /api/airport/crews/{id}   (delete crew with chosen id)

### Airplane:

- [POST] /api/airport/airplanes   (create nem airplane)
- [GET] /api/airport/airplanes   (list of all airplanes)
- [GET] /api/airport/airplanes/{id}   (detail info about airplane)
- [PUT] /api/airport/airplanes/{id}   (update all airplane instance)
- [PATCH] /api/airport/airplanes/{id}   (partial update of airplane instance)
- [DELETE] /api/airport/airplanes/{id}   (delete airplane with chosen id)

### Flights:

- [POST] /api/airport/flights   (create nem flight)
- [GET] /api/airport/flights   (list of all flights)
- [GET] /api/airport/flights/{id}   (detail info about flight)
- [PUT] /api/airport/flights/{id}   (update all flight instance)
- [PATCH] /api/airport/flights/{id}   (partial update of flight instance)
- [DELETE] /api/airport/flights/{id}   (delete flight with chosen id)

## How to run

- Copy this repo from GitHub:
```git
git clone https://github.com/ochernyi/airport-api-service.git
```
- Create venv and activate it through terminal:
```git
python -m venv venv

#Windows activaition:
myvenv\Scripts\activate

#Unix or Linux activation:
source myvenv/bin/activate
pip install -r requirements.txt
```
1. Configure your database settings in `settings.py`.
2. Apply database migrations: `python manage.py migrate`
3. Create a superuser for admin access: `python manage.py createsuperuser`
4. Run the development server: `python manage.py runserver`

- Create admin user & Create schedule for running sync in DB

## Pre-installed test users:
You can test this service by using pre-installed test users.

Admin:
```git
email: admin@admin.com
password: qwe123
```


## How to register:
- Create user at /api/user/register/ endpoint
- Get user token at /api/user/token/ endpoint
- Authorize with it on /api/doc/swagger/ or use ModHeader wtih Request header:
```
Header: Authorization
Value: Bearer <Your access token> 
```
