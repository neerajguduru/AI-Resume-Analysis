# 🧠 AI-Powered Resume Analyzer

An intelligent web application that evaluates resumes against a given job role using Google Gemini API. The app provides structured feedback including match score, missing skills, suggested courses, and formatting tips — all with a simple upload interface.

---

## 🚀 Features

- 📄 **Upload Resume**: Supports PDF, DOCX, and image formats (JPG, PNG)
- 🔍 **Gemini-Powered Analysis**: Uses LLM to assess match with job descriptions
- 🎯 **Match Score**: Quantifies resume-job alignment
- 📉 **Missing Skills**: Identifies gaps compared to ideal candidate profile
- 🎓 **Course Suggestions**: Recommends relevant online resources
- 🧹 **Formatting Tips**: Suggests ATS-friendly improvements
- 💬 **Q&A Chat**: Ask questions based on your own resume content

---

## 🛠 Tech Stack

| Layer           | Tools Used                            |
|-----------------|----------------------------------------|
| Backend         | Python, Flask, Flask-CORS             |
| LLM Integration | Google Gemini API (`google-generativeai`) |
| Resume Parsing  | `pdfminer.six`, `python-docx`, `pytesseract`, `Pillow` |
| Frontend (UI)   | HTML, CSS (Flask Jinja templates)     |

---
