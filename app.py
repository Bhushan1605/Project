from flask import Flask, render_template, request
from report_generator import generate_report
import os

app = Flask(__name__)

REPORT_FOLDER = "reports"
os.makedirs(REPORT_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    skills = request.form["skills"]
    experience = request.form["experience"]

    file_path = os.path.join(REPORT_FOLDER, f"{name}_report.pdf")
    generate_report(file_path, name, email, skills, experience)

    return f"Report Generated Successfully at {file_path}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)