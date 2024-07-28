
# Django Project

This project is a Django application with REST API documentation using `drf-spectacular`. Follow the steps below to set up, test, migrate, and launch the app locally.

## Prerequisites

- Python 3.x
- pip
- Docker (optional, if you prefer using Docker)
- Virtualenv (optional, recommended for isolating dependencies)

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Create and activate a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Create a `.env` file:**

   Copy the `.env.example` to `.env` and configure your environment variables.

   ```bash
   cp .env.example .env
   ```

2. **Update `settings.py`:**

   Make sure your `settings.py` file is configured correctly. This includes database settings, installed apps, middleware, etc.

## Database Migration

1. **Run migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Create a superuser (optional, for admin access):**

   ```bash
   python manage.py createsuperuser
   ```

## Running the Application

1. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

2. **Access the application:**

   Open your browser and navigate to `http://localhost:8000/`.

3. **Access API documentation:**

   - Swagger UI: `http://localhost:8000/api/docs/`
   - ReDoc UI: `http://localhost:8000/api/redoc/`

## Running Tests

1. **Run tests using the Django test framework:**

   ```bash
   python manage.py test
   ```

## Docker (Optional)

1. **Build and run the application using Docker:**

   ```bash
   docker-compose up --build
   ```

2. **Stop the Docker containers:**

   ```bash
   docker-compose down
   ```

## Troubleshooting

If you encounter any issues, please refer to the Django documentation or the documentation for any additional packages you are using. You can also create an issue on the project's GitHub page for further assistance.

