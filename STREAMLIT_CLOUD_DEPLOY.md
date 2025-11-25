# 🚀 Deploy to Streamlit Community Cloud

Your code is now on GitHub! Follow these steps to deploy to Streamlit Community Cloud:

## Step 1: Sign in to Streamlit Cloud

1. Go to **[https://streamlit.io/cloud](https://streamlit.io/cloud)**
2. Click **"Sign in"** and authorize with your GitHub account
3. Grant necessary permissions to Streamlit Cloud

## Step 2: Create New App

1. Click the **"New app"** button (usually in the top right or dashboard)
2. You'll see a deployment form

## Step 3: Configure Deployment

Fill in the deployment settings:

- **Repository**: Select `vikramsankhala/condenser-inspection-app`
- **Branch**: `main`
- **Main file path**: `app.py`
- **App URL** (optional): Choose a custom subdomain like `condenser-inspection` 
  - Your app will be at: `https://condenser-inspection.streamlit.app`

## Step 4: Deploy

1. Click **"Deploy"** button
2. Streamlit Cloud will:
   - Install dependencies from `requirements.txt`
   - Build your app
   - Deploy it (usually takes 2-5 minutes)

## Step 5: Monitor Deployment

- Watch the build logs in real-time
- Once complete, you'll see "Your app is live!"
- Click the app URL to open it

## ✅ Your App Will Be Live At:

`https://[your-chosen-name].streamlit.app`

## 🔄 Updating Your App

After making changes:

```bash
git add .
git commit -m "Your commit message"
git push
```

Streamlit Cloud will automatically redeploy your app!

## 📋 Quick Checklist

- ✅ Code pushed to GitHub
- ⏳ Sign in to Streamlit Cloud
- ⏳ Create new app
- ⏳ Configure deployment settings
- ⏳ Deploy and wait for build
- ⏳ Share your live app URL!

---

**Need help?** Check the [Streamlit Cloud documentation](https://docs.streamlit.io/streamlit-community-cloud) or the build logs in the Streamlit Cloud dashboard.

