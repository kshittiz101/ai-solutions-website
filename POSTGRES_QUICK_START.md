# 🚀 PostgreSQL Quick Start Guide

## ✅ Already Configured!

Your project now supports PostgreSQL! Here's everything you need to know:

---

## 📦 What's Installed

```bash
✅ psycopg2-binary==2.9.10  # PostgreSQL adapter
✅ dj-database-url==3.0.1   # Database URL parser
```

---

## 🔧 How to Use

### Local Development (SQLite - Default)

```bash
# Just run as normal - no setup needed!
pipenv run python manage.py runserver
```

### Production (PostgreSQL)

```bash
# Set DATABASE_URL environment variable
export DATABASE_URL="postgresql://user:pass@host:5432/dbname"

# Run migrations
pipenv run python manage.py migrate

# Create superuser
pipenv run python manage.py createsuperuser
```

---

## 🌐 Get PostgreSQL Database

### **Option 1: Vercel Postgres** (Easiest)

1. Go to [vercel.com/dashboard](https://vercel.com/dashboard)
2. Select your project
3. Click **Storage** → **Create Database** → **Postgres**
4. DATABASE_URL is automatically added ✨

### **Option 2: Supabase** (Free)

1. Go to [supabase.com](https://supabase.com)
2. Create project
3. Get connection string from **Project Settings** → **Database**
4. Add to Vercel: `DATABASE_URL=postgresql://...`

### **Option 3: Neon** (Serverless)

1. Go to [neon.tech](https://neon.tech)
2. Create project
3. Copy connection string
4. Add to Vercel: `DATABASE_URL=postgresql://...`

---

## 🔄 Test Database Connection

```bash
# Test your database connection
pipenv run python test_db_connection.py
```

**Expected Output:**

```
✅ Successfully connected to [SQLite/PostgreSQL]!
📦 Database Version: ...
📋 Database Tables: XX
🔄 Applied Migrations: XX
```

---

## 🚀 Deploy to Vercel

### Step 1: Push to GitHub

```bash
git add .
git commit -m "Add PostgreSQL support"
git push origin main
```

### Step 2: Add DATABASE_URL to Vercel

1. Vercel Dashboard → Your Project
2. **Settings** → **Environment Variables**
3. Add:
   ```
   Name: DATABASE_URL
   Value: postgresql://user:pass@host:5432/dbname
   ```

### Step 3: Deploy

Vercel will automatically deploy with PostgreSQL! 🎉

### Step 4: Run Migrations (First Time Only)

```bash
# Install Vercel CLI
npm i -g vercel

# Pull environment
vercel env pull .env.local

# Run migrations
export $(cat .env.local | xargs)
pipenv run python manage.py migrate
pipenv run python manage.py createsuperuser
pipenv run python manage.py loaddata demo_data.json
```

---

## 📋 Common Commands

```bash
# Run migrations
pipenv run python manage.py migrate

# Create new migration
pipenv run python manage.py makemigrations

# Create superuser
pipenv run python manage.py createsuperuser

# Load demo data
pipenv run python manage.py loaddata demo_data.json

# Test database
pipenv run python test_db_connection.py

# Database shell
pipenv run python manage.py dbshell
```

---

## 🔍 Database URL Format

```
postgresql://[user]:[password]@[host]:[port]/[database]
```

**Example:**

```
postgresql://myuser:mypass123@db.example.com:5432/mydb
```

---

## ⚙️ Configuration Files

### `config/settings.py`

```python
import dj_database_url

# Default: SQLite (local)
DATABASES = {'default': {...}}

# Production: PostgreSQL (if DATABASE_URL set)
if os.getenv('DATABASE_URL'):
    DATABASES['default'] = dj_database_url.parse(
        os.getenv('DATABASE_URL'),
        conn_max_age=600,
        conn_health_checks=True,
    )
```

### `.env` (for local PostgreSQL)

```env
DATABASE_URL=postgresql://user:pass@localhost:5432/dbname
```

---

## 🎯 Next Steps

1. **Choose Provider:** Pick a PostgreSQL provider (Vercel/Supabase/Neon)
2. **Get DATABASE_URL:** Copy connection string
3. **Add to Vercel:** Set environment variable
4. **Deploy:** Push and deploy
5. **Migrate:** Run migrations on production

---

## 📚 More Information

See **`POSTGRESQL_SETUP.md`** for:

- Detailed provider comparisons
- Local PostgreSQL setup
- Troubleshooting guide
- Security best practices

---

## ✅ Status Check

```bash
# Check installed packages
pipenv graph | grep -E "(psycopg2|dj-database)"

# Test connection
pipenv run python test_db_connection.py

# Check Django settings
pipenv run python manage.py diffsettings | grep DATABASE
```

---

**Your Django project is PostgreSQL-ready!** 🐘✨
