"""
Task Tracker - A simple Flask web app
--------------------------------------
This is a beginner-friendly web app that lets you add, view, and
delete tasks. Tasks are stored in a JSON file so they persist
between restarts (no database needed).
"""

from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

DATA_FILE = "tasks.json"


def load_tasks():
    """Read tasks from the JSON file. Returns an empty list if none exist yet."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    """Write the current list of tasks back to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


@app.route("/")
def index():
    """Homepage: show all current tasks."""
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    """Handle the 'add task' form submission."""
    task_text = request.form.get("task", "").strip()
    if task_text:
        tasks = load_tasks()
        tasks.append({"text": task_text, "done": False})
        save_tasks(tasks)
    return redirect(url_for("index"))


@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    """Toggle a task's completed status."""
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]["done"] = not tasks[task_id]["done"]
        save_tasks(tasks)
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    """Remove a task from the list."""
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)
    return redirect(url_for("index"))


if __name__ == "__main__":
    # debug=True auto-reloads the server when you save code changes
    app.run(debug=True)
