# Real Estate Django Application

A Django-based real estate web application with Docker and Jenkins CI/CD pipeline integration.

## Project Overview

This is a Django web application for real estate management with the following features:
- Agent profiles management
- Team profiles management
- Category and subcategory management
- Containerized deployment using Docker and Docker Compose
- CI/CD pipeline using Jenkins

## Tech Stack

- **Backend**: Django 4.2
- **Database**: SQLite (default)
- **Frontend**: Django Templates
- **Containerization**: Docker
- **CI/CD**: Jenkins
- **Dependencies**:
  - Django
  - Pillow (for image processing)

## Project Structure

```
realstate/
├── core/                   # Django project settings
├── estate/                 # App for agent and team profiles
├── master/                 # App for categories and subcategories
├── media/                  # Uploaded media files
├── static/                 # Static files (CSS, JS, images)
├── template/               # HTML templates
├── docker-compose.yaml     # Docker Compose configuration
├── dockerfile              # Docker container configuration
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Models

### Estate App
- **AgentProfile**: Real estate agents information
- **TeamProfile**: Team members information

### Master App
- **BaseContent**: Abstract base model with common fields
- **Category**: Property categories
- **SubCategory**: Property subcategories

## Docker Setup

The application is containerized using Docker:

```dockerfile
# Use the official Python image as a base
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Expose the port Django runs on
EXPOSE 8000

# Run migrations and start the Django server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
```

## Docker Compose Configuration

```yaml
services:
  web:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
```

## Jenkins Pipeline Setup

To set up a Jenkins pipeline for this project, create a `Jenkinsfile` in the root directory with the following content:

```groovy
pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker-compose build'
            }
        }
        
        stage('Run Tests') {
            steps {
                sh 'docker-compose run --rm web python manage.py test'
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'docker-compose down || true'
                sh 'docker-compose up -d'
            }
        }
    }
    
    post {
        always {
            sh 'docker-compose logs'
        }
        failure {
            echo 'Pipeline failed!'
        }
        success {
            echo 'Pipeline succeeded!'
        }
    }
}
```

## Local Development Setup

1. Clone the repository:
   ```
   git clone https://github.com/JayLikhare316/realstate.git
   cd realstate
   ```

2. Create and activate a virtual environment (optional):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

## Docker Deployment

1. Build and start the containers:
   ```
   docker-compose up -d
   ```

2. Access the application at http://localhost:8000

3. Stop the containers:
   ```
   docker-compose down
   ```

## Jenkins CI/CD Integration

1. Install Jenkins and required plugins:
   - Docker Pipeline
   - Git Integration

2. Create a new Jenkins Pipeline job
   - Configure it to use the Jenkinsfile from SCM
   - Set the repository URL to your Git repository
   - Configure credentials if needed

3. Set up webhooks in GitHub to trigger the pipeline on code changes

4. Run the pipeline manually for the first time to ensure everything works

## Security Notes

- The Django SECRET_KEY is exposed in settings.py and should be moved to environment variables for production
- DEBUG is set to True and should be set to False in production
- ALLOWED_HOSTS is set to ['*'] which should be restricted in production

## License

This project is open-source and available under the MIT License.
