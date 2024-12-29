from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

# Home Page
@app.route('/')
def home():
    return render_template('index.html', title="Home")

# About Page
@app.route('/about')
def about():
    return render_template('about.html', title="About Us")

# Projects Page (Dynamic Example)
@app.route('/projects')
def projects():
    project_list = [
        {"name": "AI Chatbot", "description": "An AI-based chatbot for customer service."},
        {"name": "Portfolio Website", "description": "A personal portfolio website."},
        {"name": "E-commerce App", "description": "A small e-commerce platform demo."}
    ]
    return render_template('projects.html', projects=project_list, title="Projects")

# Custom 404 Error Page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="Page Not Found"), 404

# Run the App
if __name__ == '__main__': 
    app.run(debug=True)
