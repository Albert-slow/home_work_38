from flask import Blueprint, render_template, redirect
from flask import request
questions = {}

question_bp = Blueprint('question', __name__, url_prefix="/question")

@question_bp.route("/", methods=["POST", "GET"])
def question_add():

    questions = {'question': request.form.get("question")}
    print(questions)

    return render_template("question.html", questions=questions)


