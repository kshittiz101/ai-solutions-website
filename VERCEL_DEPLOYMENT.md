# 🚀 Vercel Deployment Guide for AI Solutions Django Project

## 📋 Prerequisites

- Vercel account (sign up at [vercel.com](https://vercel.com))
- Vercel CLI installed (optional): `npm i -g vercel`
- Git repository (GitHub, GitLab, or Bitbucket)

## 📁 Configuration Files Created

This project includes the following Vercel deployment files:

1. **`vercel.json`** - Main Vercel configuration
2. **`build.sh`** - Build script for static files
3. **`requirements.txt`** - Python dependencies
4. **`.vercelignore`** - Files to exclude from deployment
5. **`api/index.py`** - Serverless function entry point

## 🔧 Environment Variables

### Required Environment Variables in Vercel

You need to set these in your Vercel project dashboard:

```bash
# Django Settings
SECRET_KEY=your-super-secret-key-here-change-this
DEBUG=False
ALLOWED_HOSTS=.vercel.app,your-custom-domain.com

# Email Configuration (if using email features)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
EMAIL_USE_TLS=True

# Optional: Database URL for PostgreSQL
# DATABASE_URL=postgresql://user:password@host:port/dbname
```

### How to Add Environment Variables:

1. Go to your Vercel project dashboard
2. Navigate to **Settings** → **Environment Variables**
3. Add each variable with its value
4. Choose appropriate environment (Production, Preview, Development)

## 📦 Deployment Methods

### Method 1: Deploy via Vercel Dashboard (Recommended)

1. **Push to GitHub:**

   ```bash
   git add .
   git commit -m "Configure for Vercel deployment"
   git push origin main
   ```

2. **Import Project to Vercel:**

   - Go to [vercel.com](https://vercel.com)
   - Click **"Add New Project"**
   - Import your GitHub repository
   - Vercel will auto-detect it as a Python project

3. **Configure Build Settings:**

   - Framework Preset: **Other**
   - Build Command: `bash build.sh`
   - Output Directory: `staticfiles`
   - Install Command: `pip install pipenv && pipenv install --deploy --ignore-pipfile`

   **Note:** The project uses **pipenv** for dependency management

4. **Add Environment Variables** (see above section)

5. **Deploy!** Click "Deploy" and wait for the build to complete

### Method 2: Deploy via Vercel CLI

1. **Install Vercel CLI:**

   ```bash
   npm i -g vercel
   ```

2. **Login to Vercel:**

   ```bash
   vercel login
   ```

3. **Deploy to Preview:**

   ```bash
   vercel
   ```

4. **Deploy to Production:**
   ```bash
   vercel --prod
   ```

## 🗄️ Database Configuration

### Option 1: SQLite (Simple, Not Recommended for Production)

- SQLite works on Vercel but data is **ephemeral** (resets on each deployment)
- Good for testing but not for production

### Option 2: PostgreSQL (Recommended for Production)

1. **Choose a Database Provider:**

   - [Vercel Postgres](https://vercel.com/storage/postgres)
   - [Supabase](https://supabase.com) (Free tier available)
   - [Neon](https://neon.tech) (Serverless Postgres)
   - [Railway](https://railway.app)

2. **Get Database URL:**

   ```
   postgresql://username:password@host:port/database
   ```

3. **Add to Vercel Environment Variables:**

   ```
   DATABASE_URL=postgresql://...
   ```

4. **Update dependencies:**

   ```bash
   pipenv install psycopg2-binary dj-database-url
   pipenv lock
   pipenv requirements > requirements.txt  # Update requirements.txt
   ```

5. **Uncomment database configuration in `config/settings.py`:**
   ```python
   import dj_database_url
   if os.getenv('DATABASE_URL'):
       DATABASES['default'] = dj_database_url.parse(os.getenv('DATABASE_URL'))
   ```

## 🔄 Running Migrations & Loading Data

### Initial Setup (Run Once)

After deploying, you need to run migrations and load data:

1. **Install Vercel CLI** (if not already installed)

2. **Run migrations:**

   ```bash
   vercel env pull .env.local
   python manage.py migrate
   ```

3. **Create superuser:**

   ```bash
   python manage.py createsuperuser
   ```

4. **Load demo data:**
   ```bash
   python manage.py loaddata demo_data.json
   ```

## 📂 Static Files & Media

### Static Files (CSS, JS, Images)

- Already configured with **WhiteNoise**
- Static files are collected during build: `python manage.py collectstatic`
- Served from `/staticfiles/` directory

### Media Files (User Uploads)

**⚠️ Important:** Vercel's filesystem is **read-only** in production!

For media files, you need external storage:

#### Option 1: Vercel Blob Storage

```bash
pip install vercel-storage
```

#### Option 2: AWS S3 (Recommended)

```bash
pip install django-storages boto3
```

#### Option 3: Cloudinary

```bash
pip install django-cloudinary-storage
```

## 🔍 Troubleshooting

### Common Issues:

1. **Build Fails:**

   - Check `requirements.txt` is up to date
   - Verify Python version compatibility (3.12.6)
   - Check build logs in Vercel dashboard

2. **Static Files Not Loading:**

   - Ensure `python manage.py collectstatic` runs successfully
   - Check `STATIC_ROOT` and `STATIC_URL` in settings.py
   - Verify WhiteNoise is installed

3. **Database Errors:**

   - Check `DATABASE_URL` environment variable
   - Run migrations after deployment
   - Consider using PostgreSQL for production

4. **500 Internal Server Error:**
   - Set `DEBUG=True` temporarily to see error details
   - Check Vercel function logs
   - Verify all environment variables are set

## 📊 Vercel Dashboard Features

After deployment, use Vercel dashboard to:

- **Monitor:** View deployment logs and analytics
- **Logs:** Check function logs for debugging
- **Domains:** Add custom domains
- **Environment Variables:** Manage secrets and configs
- **Deployments:** Roll back to previous versions

## 🔐 Security Checklist

Before going live:

- [ ] Change `SECRET_KEY` to a strong random value
- [ ] Set `DEBUG=False` in production
- [ ] Configure proper `ALLOWED_HOSTS`
- [ ] Use PostgreSQL instead of SQLite
- [ ] Set up external media storage
- [ ] Enable HTTPS (automatic on Vercel)
- [ ] Configure CORS if using API
- [ ] Set up monitoring and error tracking

## 🌐 Custom Domain

To add a custom domain:

1. Go to **Vercel Dashboard** → **Project Settings** → **Domains**
2. Add your domain (e.g., `ai-solutions.com`)
3. Update DNS records as instructed
4. Update `ALLOWED_HOSTS` in environment variables

## 📚 Useful Commands

```bash
# Check deployment status
vercel ls

# View deployment logs
vercel logs

# View environment variables
vercel env ls

# Add environment variable
vercel env add SECRET_KEY

# Pull environment variables locally
vercel env pull .env.local

# Redeploy
vercel --prod
```

## 🎉 Success!

Your Django application should now be live on Vercel!

**Production URL:** `https://your-project.vercel.app`

**Admin Panel:** `https://your-project.vercel.app/admin/`

---

## 📞 Need Help?

- [Vercel Documentation](https://vercel.com/docs)
- [Django Deployment Guide](https://docs.djangoproject.com/en/stable/howto/deployment/)
- [Vercel Community](https://github.com/vercel/vercel/discussions)

---

**Last Updated:** October 3, 2025
