from flask import Flask, redirect, render_template, send_from_directory, url_for
import os

app = Flask(__name__, template_folder='template', static_folder='src', static_url_path='/src')

# Routes
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/resources')
def resource():
    return render_template("resource.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/app')
def app_route():
    template_path = os.path.join(app.template_folder, 'app.html')
    if os.path.exists(template_path):
        return render_template('app.html')
    else:
        return redirect(url_for('page_not_found'))

@app.route('/404')
def page_not_found():
    return render_template('404.html'), 404

@app.route('/script.js')
def serve_script():
    return send_from_directory('src', 'script.js')

# Error handlers
@app.errorhandler(404)
def handle_404(error):
    return render_template('404.html'), 404

# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)