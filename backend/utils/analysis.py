import re

def find_missing_skills(resume_text, jd_text, keyword_list):
    resume_words = set(re.findall(r'\b\w+\b', resume_text.lower()))
    jd_words = set(re.findall(r'\b\w+\b', jd_text.lower()))
    return list(jd_words & keyword_list - resume_words)

def analyze_format(text):
    issues = []
    if 'education' not in text.lower():
        issues.append("Missing 'Education' section.")
    if 'experience' not in text.lower():
        issues.append("Missing 'Experience' section.")
    if len(text.split()) > 1000:
        issues.append("Resume is too long.")
    return {
        "structure_rating": 100 - len(issues) * 15,
        "suggestions": issues
    }