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

## CI/CD Deployment

This project uses **GitHub Actions** for continuous deployment.

### **1. Setup (First Time Only)**
To enable automated deployment, you must add your AWS credentials to the GitHub Repository Secrets:

1.  Go to your GitHub Repository -> **Settings** -> **Secrets and variables** -> **Actions**.
2.  Add the following secrets:
    *   `AWS_ACCESS_KEY_ID`: Your AWS Access Key.
    *   `AWS_SECRET_ACCESS_KEY`: Your AWS Secret Key.

### **2. How to Deploy**
Simply push any changes to the `main` branch. The deployment will happen automatically.

```bash
git add .
git commit -m "Your update message"
git push origin main
```

*   **View Logs:** Go to the "Actions" tab on GitHub to see the deployment progress.
*   **App URL:** The URL of your deployed application will be printed in the logs at the end of the "Get Application URL" step.

---

## Manual Deployment (Fallback)
If you need to deploy manually from your local machine:


2.  **Create Environment:**
    ```bash
    eb create django-scraper-env-mumbai
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
