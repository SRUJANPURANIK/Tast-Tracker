<<<<<<< HEAD
# Task Tracker

A simple Flask web app for tracking to-do tasks. Built as a learning
project to walk through the full process: code → run locally → GitHub → live deployment.

---

## 1. Run it locally in VS Code

**Prerequisite:** Python 3.9+ installed. Check with:
```bash
python3 --version
```

**Steps:**

1. Open this `task-tracker` folder in VS Code (`File > Open Folder...`).
2. Open the built-in terminal: `` Terminal > New Terminal `` (or `` Ctrl+` ``).
3. Create a virtual environment (keeps this project's packages separate from the rest of your system):
   ```bash
   python3 -m venv venv
   ```
4. Activate it:
   - **Mac/Linux:** `source venv/bin/activate`
   - **Windows:** `venv\Scripts\activate`

   You'll see `(venv)` appear in your terminal prompt once it's active.
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Run the app:
   ```bash
   python app.py
   ```
7. You'll see output like `Running on http://127.0.0.1:5000`. Open that URL in your browser.

Try adding a task, checking it off, and deleting it. Edit `app.py` or
`templates/index.html`, save, and refresh the browser — Flask's debug
mode reloads automatically.

---

## 2. Push the code to GitHub

1. Create a new repo on [github.com](https://github.com) (click **New**), name it e.g. `task-tracker`. Don't initialize it with a README (you already have one).
2. Back in your VS Code terminal, initialize git and push:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: task tracker app"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/task-tracker.git
   git push -u origin main
   ```
3. Refresh your GitHub repo page — your code is now version-controlled and public (or private, your choice).

---

## 3. Deploy it live (so anyone can use it online)

**Note:** GitHub Pages can't run Python — it only serves static HTML/CSS/JS.
Since this is a Flask (Python) app, we deploy it on **Render**, a free host
that connects directly to your GitHub repo and auto-deploys on every push.

1. Go to [render.com](https://render.com) and sign up (you can sign in with your GitHub account).
2. Click **New > Web Service**.
3. Connect your GitHub account and select your `task-tracker` repo.
4. Fill in the settings:
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Click **Create Web Service**. Render will install dependencies and start your app.
6. After a minute or two, you'll get a live URL like `https://task-tracker-xxxx.onrender.com` — that's your app, live on the internet.

From now on, every time you `git push` to `main`, Render automatically redeploys the latest version.

---

## How it works

- `app.py` — the Flask server: defines routes (`/`, `/add`, `/complete`, `/delete`) and handles reading/writing tasks.
- `templates/index.html` — the page shown to users, using Jinja2 templating to loop through tasks.
- `static/style.css` — page styling.
- `tasks.json` — created automatically to store your tasks (ignored by git, so it stays local/per-deployment).

## Ideas to extend it (good next learning steps)

- Add due dates or priority levels to tasks
- Switch from JSON file storage to a real database (SQLite)
- Add user accounts so each person has their own task list
- Add categories/tags and filtering
=======
# Tast-Tracker
>>>>>>> 2e9fdfaceebc9f05358f4d08c231106f5720e167
