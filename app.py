from flask import Flask, render_template
from users import user_bp
from questions import question_bp


app = Flask(__name__)
app.config["CSRF_ENABLED"] = True
app.config["SECRET_KEY"] = "SofT-project-49-Flask-1234567890987654321"
app.register_blueprint(user_bp)
app.register_blueprint(question_bp)


@app.route('/')
def home():
    return render_template('home.html')

app.run(debug=True)