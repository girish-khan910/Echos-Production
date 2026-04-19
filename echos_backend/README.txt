# Echos Production — Django Backend

## Local Setup

1. Install dependencies:
   pip install -r requirements.txt

2. Set environment variables (create a .env file or set manually):
   EMAIL_HOST_USER=echosproduction@gmail.com
   EMAIL_HOST_PASSWORD=your_gmail_app_password
   SECRET_KEY=any_random_long_string
   DEBUG=True

3. Run the server:
   python manage.py migrate
   python manage.py runserver

4. Test it:
   Open browser → http://127.0.0.1:8000/api/contact/send/

---

## Deploy to Render (Free)

1. Push this folder to GitHub

2. Go to https://render.com → New → Web Service

3. Connect your GitHub repo

4. Use these settings:
   - Environment: Python
   - Build Command: ./build.sh
   - Start Command: gunicorn echos_backend.wsgi:application

5. Add Environment Variables on Render dashboard:
   - SECRET_KEY        → any long random string
   - EMAIL_HOST_USER   → echosproduction@gmail.com
   - EMAIL_HOST_PASSWORD → your Gmail App Password (16 chars)

6. After deploy, your API URL will be:
   https://your-app-name.onrender.com/api/contact/send/

---

## Gmail App Password (required)

1. Go to Google Account → Security
2. Enable 2-Step Verification
3. Search "App Passwords"
4. Create one → select Mail → Other → name it "Echos Django"
5. Copy the 16-character password → use as EMAIL_HOST_PASSWORD

---

## Update your HTML file

In echos_production.html, find this line:
   const API_URL = 'http://127.0.0.1:8000/api/contact/send/';

Change it to your Render URL after deploying:
   const API_URL = 'https://your-app-name.onrender.com/api/contact/send/';

---

## API Endpoint

POST /api/contact/send/

Request body (JSON):
{
  "name": "John",
  "email": "john@example.com",
  "message": "Hello Echos!"
}

Success response:
{
  "success": true,
  "message": "Email sent successfully!"
}
