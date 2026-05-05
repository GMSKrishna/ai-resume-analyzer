from fastapi import FastAPI, UploadFile, File, Form
import shutil

from resume_parser import extract_resume_text
from skill_matcher import match_skills, compute_similarity
from database import init_db, save_result

app = FastAPI()
init_db()

@app.get("/")
def home():
    return {"message": "AI Resume Analyzer Running"}

@app.post("/analyze_resume")
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    file_path = f"temp_{file.filename}"

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract resume text
    resume_text = extract_resume_text(file_path)

    # Skill matching
    matched, missing, score = match_skills(
        resume_text.lower(),
        job_description.lower()
    )

    # 🔥 Filtered similarity
    filtered_resume = " ".join(matched)

    similarity_score = compute_similarity(
        filtered_resume,
        job_description.lower()
    )

    # Save result in DB
    save_result(file.filename, score, similarity_score)

    return {
        "score": score,
        "similarity_score": similarity_score,
        "matched_skills": matched,
        "missing_skills": missing
    }