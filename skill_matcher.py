import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_skills():
    with open("data/skills_db.json", "r") as f:
        return json.load(f)

def match_skills(resume_text, jd_text):
    skills = load_skills()

    jd_skills = []
    matched = []
    missing = []

    # Find skills mentioned in JD
    for skill in skills:
        if skill in jd_text:
            jd_skills.append(skill)

    # Compare with resume
    for skill in jd_skills:
        if skill in resume_text:
            matched.append(skill)
        else:
            missing.append(skill)

    # New score logic
    if len(jd_skills) == 0:
        score = 0
    else:
        score = (len(matched) / len(jd_skills)) * 100

    return matched, missing, round(score, 2)

    from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(resume_text, jd_text):
    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform([resume_text, jd_text])

    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]

    return round(similarity * 100, 2)