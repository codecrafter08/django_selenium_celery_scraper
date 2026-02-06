# Django Selenium Scraper with Celery

This is a Django application that uses Selenium for scraping and Celery for background task processing. It is configured for deployment on AWS Elastic Beanstalk.

## Prerequisites

*   Python 3.11+
*   Git
*   AWS EB CLI (`pip install awsebcli`)
*   Redis (for Celery broker)

## Local Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd django_selenium_celery_scraper
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Run the server:**
    ```bash
    python manage.py runserver
    ```

6.  **Run Celery worker:**
    ```bash
    celery -A myproject worker --loglevel=info
    ```

## Deployment to AWS Elastic Beanstalk

1.  **Initialize EB Application:**
    ```bash
    eb init -p python-3.11 django-scraper-app --profile <your-aws-profile>
    ```

2.  **Create Environment:**
    ```bash
    eb create django-scraper-env
    ```

3.  **Set Environment Variables:**
    ```bash
    eb setenv DEBUG=False SECRET_KEY=<your-secret-key> REDIS_URL=<your-redis-url>
    ```

4.  **Deploy Updates:**
    ```bash
    git add .
    git commit -m "Your commit message"
    eb deploy
    ```

## Configuration Details

*   **Selenium**: Configured to run in headless mode (required for server environments).
*   **Celery**: Runs on the same instance as the web server via `Procfile`. For high load, consider a separate worker environment.
*   **Database**: Uses SQLite by default. For production, configure `DATABASES` in `settings.py` to use RDS (PostgreSQL/MySQL).
