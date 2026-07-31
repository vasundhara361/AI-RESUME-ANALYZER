from gemini_analyzer import analyze_with_gemini

resume = """
Name: S. Vasundhara

Skills:
Python
Java
HTML
CSS
Flask

Projects:
AI Resume Analyzer
Credit Card Approval Prediction
"""

result = analyze_with_gemini(resume)

print(result)