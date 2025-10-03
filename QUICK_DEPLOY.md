# ⚡ Quick Deploy to Vercel

## 🚀 Fast Deployment Steps

### 1. Push to GitHub

```bash
git add .
git commit -m "Ready for Vercel deployment"
git push origin main
```

### 2. Import to Vercel

1. Go to [vercel.com](https://vercel.com)
2. Click **"Add New Project"**
3. Import your repository
4. Framework Preset: **Other**

### 3. Add Environment Variables

In Vercel Dashboard → Settings → Environment Variables:

```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=.vercel.app
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-password
EMAIL_USE_TLS=True
```

### 4. Deploy!

Click **"Deploy"** and wait ~2-3 minutes

---

## 📝 Files Created

✅ `vercel.json` - Vercel configuration
✅ `build.sh` - Build script
✅ `requirements.txt` - Python dependencies
✅ `.vercelignore` - Exclude files
✅ `api/index.py` - Serverless entry point

---

## ⚠️ Important Notes

- **Database:** SQLite is ephemeral on Vercel. Use PostgreSQL for production.
- **Media Files:** Vercel filesystem is read-only. Use external storage (S3, Cloudinary).
- **Static Files:** Handled by WhiteNoise ✅

---

## 🔗 After Deployment

Your site will be at: `https://your-project.vercel.app`

Admin panel: `https://your-project.vercel.app/admin/`

---

## 🐛 If Something Goes Wrong

1. Check build logs in Vercel dashboard
2. Verify environment variables are set
3. Set `DEBUG=True` temporarily to see errors
4. Check function logs in Vercel

---

For detailed instructions, see **VERCEL_DEPLOYMENT.md**
