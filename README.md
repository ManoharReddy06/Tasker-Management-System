# Team Task Manager

A professional, full-stack collaborative project management application built with Django and Bootstrap 5.

## 🚀 Features

- **Authentication System**: Secure signup, login, and logout.
- **Role-Based Access Control (RBAC)**:
    - **Admin**: Full control over projects, tasks, and users.
    - **Member**: Access to assigned projects and tasks; ability to update task status.
- **Dashboard**: Interactive analytics with Chart.js showing task distribution and project progress.
- **Project Management**: CRUD operations for projects with deadlines and status tracking.
- **Task Management**: Task assignment, priority levels, overdue detection, and real-time filtering.
- **REST API**: Fully functional API built with Django REST Framework.
- **Responsive Design**: Mobile-friendly, modern UI with a premium sidebar layout.

## 🛠 Tech Stack

- **Backend**: Python 3.12, Django, Django REST Framework
- **Frontend**: HTML5, CSS3 (Custom), Bootstrap 5, JavaScript, Chart.js
- **Database**: SQLite (Dev) / PostgreSQL (Prod)
- **Deployment**: Railway (Gunicorn + WhiteNoise)

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd team-task-manager
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup environment variables**:
   Create a `.env` file in the root directory:
   ```env
   DEBUG=True
   SECRET_KEY=your-secret-key
   ALLOWED_HOSTS=*,localhost,127.0.0.1
   DATABASE_URL=sqlite:///db.sqlite3
   ```

4. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the server**:
   ```bash
   python manage.py runserver
   ```

## 🚀 Railway Deployment

1. Login to **Railway** and create a new project.
2. Link your GitHub repository.
3. Add a **PostgreSQL** database plugin.
4. Set the following Environment Variables in Railway:
   - `DEBUG=False`
   - `SECRET_KEY=your-production-secret-key`
   - `DATABASE_URL` (Automatically populated by Railway)
   - `ALLOWED_HOSTS=your-app-url.railway.app`
5. Railway will automatically detect the `Procfile` and deploy.

## 📡 API Endpoints

- `GET /api/projects/`: List projects
- `GET /api/tasks/`: List tasks
- `GET /api/users/`: List users

## 👥 Demo Credentials

- **Admin**: `admin` / `admin123` (suggested)
- **Member**: `member1` / `member123` (suggested)

---
*Built with ❤️ by Antigravity*
