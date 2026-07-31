# 🤖 AI Resume Analyzer

An AI-powered Resume Analyzer built with **Flask** and **Google Gemini AI** that evaluates resumes, calculates ATS scores, matches resumes against job descriptions, and generates downloadable PDF reports.

---

## 📌 Features

- 📄 Upload resumes in PDF format
- 🤖 AI-powered resume analysis using Google Gemini AI
- 📊 ATS (Applicant Tracking System) Score calculation
- 🎯 Job Description Matching Score
- ⭐ Resume Rating
- 📝 AI-generated Resume Summary
- 🟢 Detect Technical Skills
- 🤝 Detect Soft Skills
- ✅ Show Matched Skills
- ❌ Identify Missing Skills
- 💡 Personalized AI Suggestions
- 📥 Download Analysis Report as PDF
- 🎨 Clean and responsive user interface

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3

### Backend
- Python
- Flask

### AI
- Google Gemini AI API

### Libraries
- PyMuPDF (fitz)
- ReportLab
- python-dotenv
- Google Generative AI SDK

---

## 📂 Project Structure

```
AI-RESUME-ANALYZER/
│
├── static/
│   ├── css/
│   ├── js/
│   ├── uploads/
│   └── images/
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── app.py
├── gemini_analyzer.py
├── report_generator.py
├── resume_analyzer.py
├── requirements.txt
├── runtime.txt
├── .gitignore
├── .env
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/vasundhara361/AI-RESUME-ANALYZER.git
```

### 2. Open the Project

```bash
cd AI-RESUME-ANALYZER
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

Windows

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Create a `.env` File

```text
GEMINI_API_KEY=YOUR_API_KEY
```

### 7. Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🚀 How It Works

1. Upload your resume (PDF).
2. Paste the Job Description.
3. AI analyzes the resume.
4. ATS Score is calculated.
5. Job Match Score is generated.
6. Skills are extracted.
7. Missing skills are identified.
8. AI provides personalized suggestions.
9. Download the PDF report.

---

## 📸 Screenshots

### Home Page

_Add a screenshot here_

### Analysis Result

_Add a screenshot here_

### PDF Report

_Add a screenshot here_

---

## 🎯 Future Improvements

- Support DOCX resumes
- Resume keyword highlighting
- Resume grammar checker
- Resume comparison
- Multiple resume analysis
- Authentication and user accounts
- Resume history dashboard
- Dark Mode
- Cloud deployment

---

## 👩‍💻 Author

**S. Vasundhara**

- GitHub: https://github.com/vasundhara361
- LinkedIn: *(Add your LinkedIn profile URL here)*

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub!

---

## 📄 License

This project is created for educational and portfolio purposes.