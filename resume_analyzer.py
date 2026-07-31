skills_db = [
    "Python",
    "Java",
    "C",
    "C++",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "Flask",
    "Django",
    "SQL",
    "MySQL",
    "Machine Learning",
    "Artificial Intelligence",
    "Data Science",
    "Git",
    "GitHub",
    "AWS",
    "Docker",
    "Linux"
]


def analyze_resume(text):

    found_skills = []

    lower_text = text.lower()

    for skill in skills_db:
        if skill.lower() in lower_text:
            found_skills.append(skill)

    ats_score = min(len(found_skills) * 5, 100)

    suggestions = []

    if ats_score < 40:
        suggestions.append("Add more technical skills.")
        suggestions.append("Include academic or personal projects.")
        suggestions.append("Mention certifications.")

    elif ats_score < 70:
        suggestions.append("Add GitHub profile.")
        suggestions.append("Add achievements.")
        suggestions.append("Improve project descriptions.")

    else:
        suggestions.append("Excellent Resume!")
        suggestions.append("Keep it updated.")

    return {
        "skills": found_skills,
        "score": ats_score,
        "suggestions": suggestions
    }