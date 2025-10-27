# 🚀 Django REST Framework API

A RESTful API built with **Django** and **Django REST Framework (DRF)**.  
This project provides a scalable backend for applications, including authentication, CRUD operations, and role-based permissions.

---

## 📁 Project Structure

```
myapp/
│
├── api/                     # Main app containing model folder, view folder, serializer folder
│   ├── models/
│   ├── serializers/
│   ├── views/
│   ├── urls.py
│   ├── permissions.py
│   └── helpers.py
│
├── project_name/            # Project configuration folder
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── db.sqlite3
└── README.md
```

---

## ⚙️ Requirements

- Python 3.10+
- Django 5.2.7
- Django REST Framework
- `djangorestframework-simplejwt` for JWT authentication
- SQLite database

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🛠️ Setup & Installation

1. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate       # macOS/Linux
   venv\Scripts\activate        # Windows
   ```

2. **Configure environment variables**

   Create a `.env` file in the root directory and copy the contents from `.env.example` then paste it on the `.env` file

3. **Run migrations**

   ```bash
   python manage.py migrate
   ```

4. **Create a superuser**

   ```bash
   python manage.py createsuperuser
   ```

5. **Run the server**

   ```bash
   python manage.py runserver
   ```

Then visit: 👉 **http://127.0.0.1:8000/**

---

## 🔐 Authentication (JWT)

If you’re using JWT (via `djangorestframework-simplejwt`):

---

## 📦 API Endpoints

More can be found on the postman collection I will be sharing on the email.

### Users and Login

- `{{baseURL}}/api/login/`
- `{{baseUrl}}/api/users/`

### Rides

- `{{baseUrl}}/api/rides/`
- `{{baseUrl}}/api/rides/?sort=distance&lat=14.58769703183692&lon=121.11383554304926`
- `{{baseUrl}}/api/rides/?sort=rider-email&email=dutch@gmail.com`
- `{{baseUrl}}/api/rides/?sort=ride-status&status=dropoff`

### Ride Events

- `{{baseUrl}}/api/ride_events/`

### Bonus

- `{{baseUrl}}/api/rides/count_trip_more_than_hour`

---

## Postman

- Admin user created for testing and credentials are displayed below..
  ```
    {
       "email": "test@gmail.com",
       "password": "test123"
    }
  ```
- Apply these values to environment when using postman
  - _baseUrl_: `[http://127.0.0.1:8000)](http://127.0.0.1:8000)`
  - _accessToken_: Get token after logging in with admin user

## 🧩 Useful Management Commands

| Command                            | Description                    |
| ---------------------------------- | ------------------------------ |
| `python manage.py makemigrations`  | Create migration files         |
| `python manage.py migrate`         | Apply migrations               |
| `python manage.py createsuperuser` | Create admin account           |
| `python manage.py runserver`       | Start local development server |
| `python manage.py shell`           | Open Django shell              |

---

## 🧰 Development Tools

| Tool                      | Purpose                         |
| ------------------------- | ------------------------------- |
| **Django REST Framework** | API framework                   |
| **SimpleJWT**             | Token-based authentication      |
| **django-environ**        | Environment variable management |
| **SQLite**                | Database                        |
| **DBeaver**               | Database Management Tool        |

---

## Bonus

- The query is in SQLite.
- I wasn't able to default to creating a ride event and set the description for picking up a rider upon the creation of ride data.
- Raw SQL Query:
  ```SELECT
  STRFTIME('%Y-%m', ar.pickup*time) AS Month,
  au.first_name || ' ' || SUBSTR(au.last_name,1,1) AS Driver,
  COUNT(*) AS 'Count of Trips > 1'
  FROM api*ride ar
  JOIN api_user au
  ON ar.id_driver_id = au.id_user
  JOIN api_rideevent rev
  ON ar.id_ride = rev.id_ride_id
  WHERE ar.status = "dropoff"
  AND (julianday(rev.created_at) - julianday(ar.pickup_time)) * 24 \* 60 > 60
  AND (
  rev.description LIKE '%%dropoff%%'
  )
  GROUP BY Month, Driver
  ORDER BY Month, Driver;
  ```

---

## Note(s)

- I've also added the sqlite db file on the email, in case if you want to have populated data already for testing

---

## 🌐 Links

- [Django REST Framework Docs](https://www.django-rest-framework.org/)
- [Django Official Docs](https://docs.djangoproject.com/)
- [SimpleJWT Docs](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
