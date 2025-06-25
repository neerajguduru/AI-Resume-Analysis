import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def analyze_resume_with_gemini(resume_text, job_description=None):
    if not resume_text:
        return {"error": "Resume text is required for analysis."}

    job_context = job_description if job_description else "General Professional Role"
    
    prompt = f"""
You are an expert ATS and career consultant. Analyze this resume against the job requirements and provide concise, actionable feedback.

JOB REQUIREMENTS:
{job_context}

Provide analysis in this exact format:

🎯 ATS MATCH SCORE: X.X/10 (XX%)
Brief reason for score

📊 OVERALL ASSESSMENT:
2-3 sentences on resume strengths and main weaknesses

🔍 KEYWORD ANALYSIS:
Found: [5 relevant keywords present]
Missing: [5 critical keywords needed]

💼 EXPERIENCE EVALUATION:
Relevant experience percentage and 1-2 key gaps

🛠️ SKILLS ASSESSMENT:
Present: [relevant skills found]
Missing: [4-5 critical missing skills]
Priority: [top 3 skills to learn immediately]

🎓 LEARNING RECOMMENDATIONS:
For each priority skill:
- Skill: Course platform suggestions (Coursera, Udemy, etc.)

📝 IMPROVEMENT PRIORITIES:
1. Most critical fix needed
2. Second priority improvement  
3. Third priority improvement

🎨 FORMATTING SUGGESTIONS:
- 2-3 specific ATS-friendly formatting tips

✅ STRONG SECTIONS: [well-developed areas]
⚠️ NEEDS WORK: [sections requiring improvement]
❌ MISSING: [essential sections not present]

🚀 NEXT STEPS:
Top 3 immediate actions to take this week

Keep response concise, professional, and actionable. Avoid markdown formatting, asterisks, and unnecessary explanations.

RESUME:
{resume_text}
"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Gemini API Error: {str(e)}"

def answer_resume_question(question, resume_text, job_description=None):
    """Answer specific questions about the resume"""
    if not question or not resume_text:
        return {"error": "Question and resume text are required."}

    job_context = job_description if job_description else "General Professional Role"
    
    prompt = f"""
You are a senior career consultant and professional resume advisor with 15+ years of experience in talent acquisition and career development. Provide expert guidance on the user's specific resume question.

PROFESSIONAL CONTEXT:
Target Role: {job_context}

CLIENT INQUIRY:
{question}

RESUME ANALYSIS CONTENT:
{resume_text}

RESPONSE GUIDELINES:
- Maintain a formal, professional consulting tone throughout
- Avoid using asterisks, markdown formatting, or special characters around words
- Provide direct, evidence-based recommendations
- Include specific, actionable steps the candidate can implement immediately
- Reference industry standards and best practices where applicable
- If discussing improvements, provide concrete examples and measurable outcomes
- When addressing skills, clearly distinguish between existing competencies and development areas
- Structure your response with clear, logical flow
- Limit response to 150-200 words for conciseness while maintaining thoroughness
- Use professional terminology appropriate for executive-level communication
- Conclude with prioritized next steps when relevant

Deliver your professional consultation response:
"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Gemini API Error: {str(e)}"
