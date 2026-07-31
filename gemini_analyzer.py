import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-3.6-flash")


def analyze_with_gemini(resume_text, job_description):

    prompt = f"""
You are an expert ATS Resume Analyzer.

Compare the following resume with the given job description.

Resume:
{resume_text}

Job Description:
{job_description}

Return ONLY valid JSON.

Format:

{{
    "ats_score": 85,
    "job_match": 82,
    "technical_skills": [],
    "soft_skills": [],
    "matched_skills": [],
    "missing_skills": [],
    "suggestions": [],
    "summary": ""
}}
"""

    response = model.generate_content(prompt)

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()

    elif text.startswith("```"):
        text = text.replace("```", "").strip()

    return json.loads(text)