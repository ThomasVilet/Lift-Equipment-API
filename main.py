from flask import Flask, request, jsonify, render_template
from app.routes import api as main_routes

app = Flask(__name__, template_folder='app/templates')
app.register_blueprint(main_routes)

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/docs')
def docs():
    return render_template('docs.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == "__main__":
    app.run(debug=True)