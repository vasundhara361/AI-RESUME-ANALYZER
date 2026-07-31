from flask import Flask, render_template, request, send_file
from gemini_analyzer import analyze_with_gemini
from report_generator import generate_report
import os
import fitz

app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = os.path.join(app.root_path, "static", "uploads")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Report file
REPORT_FILE = os.path.join(app.root_path, "resume_report.pdf")

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    # Check resume
    if "resume" not in request.files:
        return "No File Selected"

    file = request.files["resume"]
    job_description = request.form["job_description"]

    if file.filename == "":
        return "No File Selected"

    # Save uploaded file
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # Extract text from PDF
    text = ""

    try:
        doc = fitz.open(filepath)

        for page in doc:
            text += page.get_text()

        doc.close()

    except Exception as e:
        return f"<h2>Error Reading PDF</h2><p>{e}</p>"

    try:
        # Analyze with Gemini
        analysis = analyze_with_gemini(text, job_description)

        # Generate PDF Report
        generate_report(REPORT_FILE, analysis)

        # Show Result Page
        return render_template(
            "result.html",
            score=analysis["ats_score"],
            job_match=analysis["job_match"],
            technical_skills=analysis["technical_skills"],
            soft_skills=analysis["soft_skills"],
            matched_skills=analysis["matched_skills"],
            missing_skills=analysis["missing_skills"],
            suggestions=analysis["suggestions"],
            summary=analysis["summary"]
        )

    except Exception as e:
        return f"""
        <h2>❌ AI Analysis Failed</h2>
        <p>{e}</p>
        <br>
        <a href="/">Go Back</a>
        """


@app.route("/download")
def download():
    return send_file(REPORT_FILE, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)