from flask import Flask, render_template, request
from resume_parser import parse_resume
import os
from PyPDF2 import PdfReader

app = Flask(__name__)

UPLOAD_FOLDER = "resumes"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["resume"]

        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            reader = PdfReader(filepath)
            text = ""

            for page in reader.pages:
                text += page.extract_text() or ""

            data = parse_resume(text)

            return render_template("result.html", data=data)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)