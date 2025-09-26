# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import fitz  # PyMuPDF
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)
CORS(app) # This will allow the React frontend to make requests to this server

# Dummy skill set for a 'Software Engineer' role
# In a real app, you'd have different lists for different roles
ROLE_SKILLS = {
    "software engineer": ["python", "java", "sql", "git", "react", "aws", "docker", "javascript"],
    "data scientist": ["python", "r", "sql", "pandas", "numpy", "tensorflow", "scikit-learn", "machine learning"],
    "frontend developer": ["html", "css", "javascript", "react", "angular", "vue", "typescript"],
    "backend developer": ["python", "java", "nodejs", "sql", "mongodb", "docker", "kubernetes"],
    "devops engineer": ["aws", "azure", "gcp", "docker", "kubernetes", "terraform", "ansible", "ci/cd"]
}

@app.route('/analyze', methods=['POST'])
def analyze_resume():
    # Check if a file was uploaded
    if 'resume' not in request.files:
        return jsonify({"error": "No resume file provided"}), 400

    file = request.files['resume']
    role = request.form.get('role', 'software engineer').lower() # Default to software engineer

    # 1. EXTRACT TEXT FROM PDF
    try:
        doc = fitz.open(stream=file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
    except Exception as e:
        return jsonify({"error": f"Error reading PDF: {e}"}), 500

    # 2. ANALYZE TEXT WITH SPACY
    resume_text = text.lower()
    required_skills = ROLE_SKILLS.get(role, [])

    found_skills = [skill for skill in required_skills if skill in resume_text]
    missing_skills = [skill for skill in required_skills if skill not in resume_text]

    # 3. CREATE A SCORE
    match_percentage = (len(found_skills) / len(required_skills)) * 100 if required_skills else 0

    # 4. RETURN RESULTS AS JSON
    result = {
        "role": role,
        "match_percentage": round(match_percentage, 2),
        "found_skills": found_skills,
        "missing_skills": missing_skills
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)