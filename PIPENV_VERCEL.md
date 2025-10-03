# 🐍 Pipenv Configuration for Vercel

## ✅ Changes Made

Your project now uses **pipenv** for dependency management on Vercel!

### Updated Files:

1. **`build.sh`** - Now uses pipenv commands:

   ```bash
   pip install pipenv
   pipenv install --deploy --ignore-pipfile
   pipenv run python manage.py collectstatic --noinput --clear
   ```

2. **`vercel.json`** - Added pipenv configuration:
   ```json
   {
     "env": {
       "PIPENV_VENV_IN_PROJECT": "1"
     },
     "installCommand": "pip install pipenv && pipenv install --deploy --ignore-pipfile"
   }
   ```

## 📦 How It Works

### During Deployment:

1. Vercel installs `pipenv`
2. Runs `pipenv install --deploy --ignore-pipfile`
   - `--deploy`: Ensures Pipfile.lock is used (production-ready)
   - `--ignore-pipfile`: Uses locked versions only
3. Collects static files using `pipenv run`
4. All Django commands run through pipenv

### Dependency Files:

- **`Pipfile`** - Package declarations
- **`Pipfile.lock`** - Locked versions (production)
- **`requirements.txt`** - Backup/fallback

## 🔄 Adding New Dependencies

When you add new packages locally:

```bash
# Install package
pipenv install package-name

# For dev dependencies
pipenv install --dev package-name

# Update requirements.txt (for reference)
pipenv requirements > requirements.txt

# Commit changes
git add Pipfile Pipfile.lock requirements.txt
git commit -m "Add new dependency"
git push
```

## 🚀 Vercel Deployment

The configuration is already set! Just:

1. **Push to GitHub:**

   ```bash
   git add .
   git commit -m "Use pipenv for Vercel deployment"
   git push origin main
   ```

2. **Import to Vercel:**
   - Vercel will automatically use pipenv
   - No manual configuration needed

## 🔧 Local Development

Continue using pipenv as usual:

```bash
# Activate virtual environment
pipenv shell

# Run development server
pipenv run python manage.py runserver

# Run any Django command
pipenv run python manage.py <command>
```

## 📊 Benefits

✅ **Deterministic Builds** - Same versions everywhere
✅ **Security** - Pipfile.lock prevents dependency confusion
✅ **Performance** - Faster installs with locked dependencies
✅ **Compatibility** - Works seamlessly with Vercel

## 🎯 Commands Reference

### Build Commands (Vercel):

```bash
pip install pipenv
pipenv install --deploy --ignore-pipfile
pipenv run python manage.py collectstatic --noinput --clear
```

### Local Commands:

```bash
pipenv install              # Install dependencies
pipenv shell               # Activate environment
pipenv run python manage.py # Run Django commands
pipenv lock                # Update lock file
pipenv requirements        # Generate requirements.txt
```

---

**Your project is now fully configured to use pipenv on Vercel!** 🎉
