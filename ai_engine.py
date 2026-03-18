# import json
# import os
# import requests
# from dotenv import load_dotenv

# load_dotenv()

# HF_API_KEY = os.getenv("HF_API_KEY")

# if not HF_API_KEY:
#     raise ValueError("HF_API_KEY not found in .env")

# HEADERS = {
#     "Authorization": f"Bearer {HF_API_KEY}"
# }

# # A stable instruction-following model
# MODEL_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"


# def query_hf(prompt):
#     response = requests.post(
#         MODEL_URL,
#         headers=HEADERS,
#         json={"inputs": prompt},
#         timeout=60
#     )
#     response.raise_for_status()
#     return response.json()[0]["generated_text"]


# def generate_student_profile(responses):
#     prompt = f"""
# You are an expert career counselor in Kerala.

# Analyze the student responses below and return ONLY valid JSON with:
# - academic_strength
# - interest_areas
# - personality
# - constraints
# - career_goals

# Student responses:
# {json.dumps(responses, indent=2)}
# """

#     text = query_hf(prompt)

#     return json.loads(extract_json(text))


# def recommend_courses(student_profile):
#     prompt = f"""
# You are a career guidance expert in Kerala.

# Based on the student profile below, return ONLY JSON in this format:
# {{
#   "top_recommendations": [
#     {{ "course": "", "reason": "" }}
#   ],
#   "alternative_paths": [
#     {{ "path": "", "reason": "" }}
#   ]
# }}

# Student profile:
# {json.dumps(student_profile, indent=2)}
# """

#     text = query_hf(prompt)
#     return json.loads(extract_json(text))


# def extract_json(text):
#     import re
#     match = re.search(r"\{.*\}", text, re.DOTALL)
#     if not match:
#         raise ValueError("No JSON found in model output")
#     return match.group()


# MOCK_MODE = True


# def generate_student_profile(responses):
#     """
#     Generate a structured student profile.
#     Mock mode returns deterministic output.
#     """

#     if MOCK_MODE:
#         return {
#             "academic_strength": "average",
#             "interest_areas": ["technology", "problem-solving"],
#             "personality": "introverted",
#             "constraints": ["low budget", "prefer Kerala"],
#             "career_goals": ["early employment"]
#         }

#     # Real LLM logic intentionally disabled
#     raise NotImplementedError("Live LLM integration disabled")


# def recommend_courses(student_profile):
#     """
#     Recommend courses based on student profile.
#     """

#     if MOCK_MODE:
#         return {
#             "top_recommendations": [
#                 {
#                     "course": "B.Sc Computer Science",
#                     "reason": "Matches interest in technology and analytical thinking, with good job opportunities in Kerala."
#                 },
#                 {
#                     "course": "BCA",
#                     "reason": "Practical IT-focused degree suitable for early employment."
#                 },
#                 {
#                     "course": "Diploma in Computer Engineering",
#                     "reason": "Affordable, hands-on course with industry relevance."
#                 }
#             ],
#             "alternative_paths": [
#                 {
#                     "path": "ITI Computer Operator",
#                     "reason": "Short-term program for quick entry into the workforce."
#                 },
#                 {
#                     "path": "Online Skill Certifications",
#                     "reason": "Flexible, low-cost way to gain job-ready skills."
#                 }
#             ]
#         }

#     raise NotImplementedError("Live LLM integration disabled")

import joblib

model = joblib.load("career_model.pkl")

def recommend_courses(profile):
    features = [[
        profile["class_12"],
        profile["science_stream"],
        profile["interest_tech"],
        profile["interest_creative"],
        profile["practical_learning"],
        profile["introvert"],
        profile["budget_low"],
        profile["stay_kerala"],
        profile["early_job"]
    ]]

    prediction = model.predict(features)[0]

    reasons = []
    if profile["interest_tech"]:
        reasons.append("interest in technology")
    if profile["interest_creative"]:
        reasons.append("creative skills")
    if profile["budget_low"]:
        reasons.append("budget-friendly preference")
    if profile["early_job"]:
        reasons.append("goal of early employment")
    if profile["stay_kerala"]:
        reasons.append("preference to study in Kerala")

    explanation = "Recommended based on your " + ", ".join(reasons) + "."

    return {
        "recommended_course": prediction,
        "reason": explanation
    }