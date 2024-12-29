from flask import Flask, render_template, request, abort
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

# Home Page
@app.route('/')
def home():
    return render_template('index.html', title="Home")

# About Page
@app.route('/about')
def about():
    return render_template('about.html', title="About Us")

# Projects Page
@app.route('/projects')
def projects():
    project_list = [
        {"id": 1, "name": "AI Chatbot", "description": "An AI-based chatbot for customer service."},
        {"id": 2, "name": "Portfolio Website", "description": "A personal portfolio website."},
        {"id": 3, "name": "E-commerce App", "description": "A small e-commerce platform demo."}
    ]
    return render_template('projects.html', projects=project_list, title="Projects")

# Dynamic Project Detail Page
@app.route('/projects/<int:project_id>')
def project_detail(project_id):
    project_list = {
        1: {"name": "AI Chatbot", "description": "Detailed info about AI Chatbot."},
        2: {"name": "Portfolio Website", "description": "Detailed info about Portfolio Website."},
        3: {"name": "E-commerce App", "description": "Detailed info about E-commerce App."}
    }
    project = project_list.get(project_id)
    if project:
        return render_template('project_detail.html', project=project, title=project['name'])
    else:
        abort(404)

# Custom 404 Error Page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="Page Not Found"), 404

# Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', title="Server Error"), 500

# Flask App Runner
def run_flask():
    debug_mode = os.getenv("FLASK_DEBUG", "False") == "True"
    app.run(host="0.0.0.0", port=5000, debug=debug_mode)
