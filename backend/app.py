from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from utils.preprocess import extract_text_from_file
from utils.gemini_api import analyze_resume_with_gemini, answer_resume_question

app = Flask(__name__)
CORS(app)
# CORS means cross origin resourse sharing
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/api/analyze_with_gemini", methods=["POST"])
def gemini_analysis():
    try:
        resume = request.files["resume"]
        jd_text = request.form["job_description"]
        
        # Extract text from resume
        resume_text = extract_text_from_file(resume)
        
        if resume_text.startswith("❌"):
            return jsonify({"error": resume_text}), 400
        
        # Analyze with Gemini
        analysis = analyze_resume_with_gemini(resume_text, jd_text)
        
        return jsonify({
            "gemini_analysis": analysis,
            "resume_text": resume_text  # Include for Q&A feature
        })
        
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

@app.route("/api/ask_question", methods=["POST"])
def ask_question():
    try:
        data = request.get_json()
        question = data.get('question', '')
        resume_text = data.get('resume_text', '')
        job_description = data.get('job_description', '')
        
        if not question or not resume_text:
            return jsonify({"error": "Question and resume text are required"}), 400
            
        # Get answer from Gemini
        answer = answer_resume_question(question, resume_text, job_description)
        
        return jsonify({"answer": answer})
        
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
