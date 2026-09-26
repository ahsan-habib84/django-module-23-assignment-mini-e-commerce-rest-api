# Mini E-commerce REST API

A Django REST Framework project based on the Mini E-commerce REST API assignment.

## Features

- Category CRUD
- Product CRUD
- Product search by name
- Product filtering by category and price
- Product ordering by price
- Pagination
- Token authentication
- User registration
- Login and token generation
- Protected Order API
- Users can create and view their own orders
- Automatic total price calculation
- Django Admin
- Postman-ready endpoints

## Setup

```bash
python -m venv venv
```

Windows:

```powershell
venv\Scripts\activate
```

Install packages:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Create admin user:

```bash
python manage.py createsuperuser
```

Run server:

```bash
python manage.py runserver
```

## API Endpoints

### Authentication

Register:

`POST /api/auth/register/`

```json
{
  "username": "ahsan",
  "email": "ahsan@example.com",
  "password": "12345678",
  "password2": "12345678"
}
```

Login / get token:

`POST /api/auth/login/`

```json
{
  "username": "ahsan",
  "password": "12345678"
}
```

Use returned token:

```text
Authorization: Token YOUR_TOKEN
```

### Categories

- `GET /api/categories/`
- `POST /api/categories/`
- `GET /api/categories/<id>/`
- `PUT /api/categories/<id>/`
- `PATCH /api/categories/<id>/`
- `DELETE /api/categories/<id>/`

### Products

- `GET /api/products/`
- `POST /api/products/`
- `GET /api/products/<id>/`
- `PUT /api/products/<id>/`
- `PATCH /api/products/<id>/`
- `DELETE /api/products/<id>/`

Example product:

```json
{
  "name": "iPhone 17",
  "description": "Apple smartphone",
  "price": "999.00",
  "stock": 10,
  "category": 1
}
```

Filtering/search/ordering:

- `/api/products/?search=phone`
- `/api/products/?category=1`
- `/api/products/?min_price=100&max_price=1000`
- `/api/products/?ordering=price`
- `/api/products/?ordering=-price`
- `/api/products/?page=2`

### Orders

Authentication required.

Create order:

`POST /api/orders/`

```json
{
  "product": 1,
  "quantity": 2
}
```

The server calculates total price automatically.

View logged-in user's orders:

`GET /api/orders/`

View one order:

`GET /api/orders/<id>/`

## Postman

1. Register a user.
2. Login and copy the returned token.
3. In Postman, set header:
   `Authorization: Token YOUR_TOKEN`
4. Create categories and products.
5. Create an order using a logged-in user.
6. Test search, filtering, ordering and pagination.

## Project Structure

```text
MiniEcommerceAPI/
├── manage.py
├── requirements.txt
├── README.md
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── store/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── urls.py
    ├── views.py
    ├── pagination.py
    ├── filters.py
    ├── tests.py
    └── migrations/
        └── __init__.py
```
