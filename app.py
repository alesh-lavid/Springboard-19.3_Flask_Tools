from flask import Flask, request, render_template, redirect, flash, session
from surveys import satisfaction_survey as survey

app = Flask(__name__)

responses = []

@app.route("/")
def handle_home():
    return render_template("home.html", survey=survey)

@app.route("/start", methods=["POST"])
def handle_start():
    return redirect("/questions/0")

@app.route("/questions/<int:ques_num>")
def handle_questions(ques_num):
    question = survey.questions[ques_num]

    if (len(responses ) == len(survey.questions)):
        return redirect("/finish")

    if ques_num != len(responses):
        flash(f"Invalid question order: {ques_num}.")
        return redirect(f"/questions/{len(responses)}")

    return render_template("questions.html", question_num = ques_num, question = question)

@app.route("/answer", methods=["POST"])
def handle_answer():
    answer = request.form["answer"]

    responses.append(answer)
    
    if (len(responses ) == len(survey.questions)):
        return redirect("/finish")

    return redirect(f"/questions/{len(responses)}")

@app.route("/finish")
def handle_finish():
    return render_template("finish.html")