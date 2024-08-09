# Django Project with PostgreSQL and Docker

## Description

This is a Django project configured to use PostgreSQL as the database and Docker for containerization. It provides a clean and isolated environment for development and deployment.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Setup

1. **Clone the repository:**

   git clone https://github.com/Yolke/Library_Manager.git
   cd Library_Manager


2. **Build and start the containers:**

   docker-compose up --build

3. **Run database migrations:**

   Open a new terminal and run:

   docker-compose exec web python manage.py migrate

4. **Create a superuser (optional):**

   docker-compose exec web python manage.py createsuperuser

5. **Access the application:**

   Open your browser and navigate to `http://localhost:8000` to view the application.

### Project Structure

- `Dockerfile` - Defines the Docker image for the Django application.
- `docker-compose.yml` - Configures the services for the project, including Django and PostgreSQL.
- `django/` - Contains the Django project code and configurations.
- `.env` - Environment variables for configuration.

## Configuration

- **Database**: PostgreSQL
  - Database host: `db`
  - Database name, user, and password are defined in the `.env` file.

## Development

To make changes to the code, you can modify files in the `django/` directory. The application will automatically reload with changes due to the Docker configuration.
