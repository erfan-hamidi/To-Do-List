# Todo App with Django Rest Framework

This is a simple Todo app built with Django Rest Framework (DRF) that allows users to create, view, update, and delete tasks.

## Features

- User registration
- User login
- User logout
- Create, read, update, and delete tasks (CRUD operations)
- JWT authentication for API endpoints

## Technologies Used

- Django
- Django Rest Framework (DRF)
- Django Rest Framework Simple JWT
- PostgreSQL (optional, based on your database setup)

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/todo-app.git
   cd todo-app
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```

## API Endpoints
- User registration: POST /api/register/
- User login: POST /api/login/
- User logout: POST /api/logout/
- Todo tasks list and create: GET/POST /api/tasks/
- Todo task detail, update, and delete: GET/PUT/DELETE /api/tasks/<task_id>/
## Authentication
- Use JWT tokens for authentication.
- Obtain tokens by sending a POST request to /api/login/.
- Include the access token in the Authorization header for protected endpoints.
- Refresh tokens can be obtained from the /api/token/refresh/ endpoint.
## Contribution
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.



