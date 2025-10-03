# 🐘 PostgreSQL Configuration Guide

## ✅ What's Been Configured

Your Django project is now configured to use PostgreSQL with `psycopg2-binary` and `dj-database-url`!

### Installed Packages:
- ✅ `psycopg2-binary` - PostgreSQL adapter for Python
- ✅ `dj-database-url` - Parse database URLs easily

### Updated Files:
- ✅ `Pipfile` & `Pipfile.lock` - Added PostgreSQL dependencies
- ✅ `requirements.txt` - Updated with new packages
- ✅ `config/settings.py` - Database configuration

---

## 🔧 How It Works

### Database Configuration in `settings.py`:

```python
import dj_database_url

# Default to SQLite for local development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Use PostgreSQL if DATABASE_URL is set (production/Vercel)
if os.getenv('DATABASE_URL'):
    DATABASES['default'] = dj_database_url.parse(
        os.getenv('DATABASE_URL'),
        conn_max_age=600,           # Connection pooling
        conn_health_checks=True,    # Health checks
    )
```

### Behavior:
- **Local Development:** Uses SQLite (no setup needed)
- **Production/Vercel:** Uses PostgreSQL (when `DATABASE_URL` is set)

---

## 🗄️ PostgreSQL Database Providers

Choose one of these providers for your production database:

### Option 1: **Vercel Postgres** (Recommended for Vercel)
- **Website:** [vercel.com/storage/postgres](https://vercel.com/storage/postgres)
- **Pricing:** Free tier available
- **Setup:**
  1. Go to your Vercel project dashboard
  2. Navigate to **Storage** tab
  3. Click **Create Database** → **Postgres**
  4. Connect to your project
  5. DATABASE_URL is automatically added to your environment variables

### Option 2: **Supabase**
- **Website:** [supabase.com](https://supabase.com)
- **Pricing:** Free tier (500MB, 2GB bandwidth)
- **Setup:**
  1. Create account at supabase.com
  2. Create a new project
  3. Go to **Project Settings** → **Database**
  4. Copy the connection string (URI format)
  5. Add to Vercel as `DATABASE_URL`

### Option 3: **Neon**
- **Website:** [neon.tech](https://neon.tech)
- **Pricing:** Free tier (3GB storage)
- **Setup:**
  1. Create account at neon.tech
  2. Create a new project
  3. Copy the connection string
  4. Add to Vercel as `DATABASE_URL`

### Option 4: **Railway**
- **Website:** [railway.app](https://railway.app)
- **Pricing:** $5 credit free monthly
- **Setup:**
  1. Create account at railway.app
  2. Create **New Project** → **Provision PostgreSQL**
  3. Copy `DATABASE_URL` from variables
  4. Add to Vercel environment variables

### Option 5: **ElephantSQL**
- **Website:** [elephantsql.com](https://elephantsql.com)
- **Pricing:** Free tier (20MB)
- **Setup:**
  1. Create account at elephantsql.com
  2. Create a new instance
  3. Copy the URL
  4. Add to Vercel as `DATABASE_URL`

---

## 🚀 Vercel Deployment Setup

### Step 1: Get Database URL

Example PostgreSQL URL format:
```
postgresql://username:password@host:port/database
```

Real example:
```
postgresql://myuser:mypassword@db.example.com:5432/mydb
```

### Step 2: Add to Vercel Environment Variables

1. Go to your Vercel project dashboard
2. Navigate to **Settings** → **Environment Variables**
3. Add new variable:
   - **Name:** `DATABASE_URL`
   - **Value:** `postgresql://username:password@host:port/database`
   - **Environment:** Production, Preview, Development (select all)

### Step 3: Run Migrations on Vercel

After deploying, you need to run migrations:

#### Method A: Using Vercel CLI
```bash
# Pull environment variables
vercel env pull .env.local

# Load env and run migrations
export $(cat .env.local | xargs)
pipenv run python manage.py migrate

# Create superuser
pipenv run python manage.py createsuperuser

# Load demo data
pipenv run python manage.py loaddata demo_data.json
```

#### Method B: Add to build.sh (One-time Setup)

Uncomment in `build.sh`:
```bash
# Run migrations
pipenv run python manage.py migrate --noinput

# Load demo data (first deployment only)
# pipenv run python manage.py loaddata demo_data.json
```

⚠️ **Note:** Running migrations in `build.sh` will execute on every deployment!

---

## 💻 Local Development with PostgreSQL

If you want to use PostgreSQL locally instead of SQLite:

### Install PostgreSQL Locally:

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

**macOS (Homebrew):**
```bash
brew install postgresql
brew services start postgresql
```

**Windows:**
Download from [postgresql.org](https://www.postgresql.org/download/windows/)

### Create Local Database:
```bash
# Access PostgreSQL
sudo -u postgres psql

# Create database and user
CREATE DATABASE ai_solutions_db;
CREATE USER ai_solutions_user WITH PASSWORD 'yourpassword';
ALTER ROLE ai_solutions_user SET client_encoding TO 'utf8';
ALTER ROLE ai_solutions_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE ai_solutions_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE ai_solutions_db TO ai_solutions_user;
\q
```

### Add to .env:
```env
DATABASE_URL=postgresql://ai_solutions_user:yourpassword@localhost:5432/ai_solutions_db
```

### Run Migrations:
```bash
pipenv run python manage.py migrate
pipenv run python manage.py createsuperuser
pipenv run python manage.py loaddata demo_data.json
```

---

## 🔄 Database Migration Commands

```bash
# Create migrations
pipenv run python manage.py makemigrations

# Apply migrations
pipenv run python manage.py migrate

# Show migrations status
pipenv run python manage.py showmigrations

# Create superuser
pipenv run python manage.py createsuperuser

# Load demo data
pipenv run python manage.py loaddata demo_data.json

# Dump data to fixture
pipenv run python manage.py dumpdata > backup.json

# Database shell
pipenv run python manage.py dbshell
```

---

## 🔍 Testing PostgreSQL Connection

Create a test script `test_db.py`:

```python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.db import connection

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print(f"✅ Connected to PostgreSQL!")
        print(f"Database version: {version[0]}")
except Exception as e:
    print(f"❌ Connection failed: {e}")
```

Run:
```bash
pipenv run python test_db.py
```

---

## 🛠️ Troubleshooting

### Error: "role does not exist"
```bash
# Create the user in PostgreSQL
sudo -u postgres createuser -s your_username
```

### Error: "database does not exist"
```bash
# Create the database
sudo -u postgres createdb your_database
```

### Error: "connection refused"
```bash
# Check if PostgreSQL is running
sudo systemctl status postgresql

# Start PostgreSQL
sudo systemctl start postgresql
```

### Error: "password authentication failed"
```bash
# Update password in PostgreSQL
sudo -u postgres psql
ALTER USER username WITH PASSWORD 'newpassword';
```

### Vercel Deployment Issues:
1. Check `DATABASE_URL` is set in environment variables
2. Verify connection string format is correct
3. Check database allows connections from Vercel IPs
4. Run migrations after first deployment

---

## 📊 Database Comparison

| Feature | SQLite | PostgreSQL |
|---------|--------|------------|
| Setup | ✅ None | ⚠️ Requires setup |
| Vercel | ⚠️ Ephemeral | ✅ Persistent |
| Performance | Good | Excellent |
| Scalability | Limited | High |
| Concurrent Users | Low | High |
| Cost | Free | Free tier available |
| Production Ready | ❌ No | ✅ Yes |

---

## 🔐 Security Best Practices

✅ **Never commit** database credentials to Git
✅ Use **environment variables** for sensitive data
✅ Use **strong passwords** (20+ characters)
✅ Enable **SSL** for database connections
✅ Restrict database access to specific IPs
✅ Regular **backups** of production data
✅ Use **different databases** for dev/staging/production

---

## 📚 Useful Resources

- [Django Database Documentation](https://docs.djangoproject.com/en/stable/ref/databases/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [psycopg2 Documentation](https://www.psycopg.org/docs/)
- [dj-database-url GitHub](https://github.com/jazzband/dj-database-url)
- [Vercel Postgres Docs](https://vercel.com/docs/storage/vercel-postgres)

---

## ✅ Configuration Complete!

Your Django project is now ready to use PostgreSQL in production! 🎉

**Next Steps:**
1. Choose a PostgreSQL provider
2. Get your `DATABASE_URL`
3. Add it to Vercel environment variables
4. Deploy and run migrations

---

**Last Updated:** October 3, 2025

