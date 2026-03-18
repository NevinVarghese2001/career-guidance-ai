import streamlit as st
from questions import questions
from storage import save_response
from ai_engine import recommend_courses

st.set_page_config(page_title="AI Career Guidance", layout="centered")

st.title("🎓 AI Career Guidance for Students in Kerala")
st.write(
    "Answer the following questions honestly. "
    "Based on your responses, the system will suggest suitable career paths."
)

responses = {}

# with st.form("career_guidance_form"):
#     for section, qs in questions.items():
#         st.subheader(section.replace("_", " ").title())
#         for q in qs:
#             responses[q] = st.text_input(q)

#     submitted = st.form_submit_button("Get Career Guidance")

# if submitted:
#     save_response(responses)

# with st.spinner("Analyzing your profile..."):
#     profile = generate_student_profile(responses)

# st.success("Profile generated successfully!")
# st.write("### Student Profile")
# st.json(profile)

# with st.spinner("Finding the best career options for you..."):
#     recommendations = recommend_courses(profile)

# st.subheader("🎯 Recommended Career Paths")

# for idx, rec in enumerate(recommendations["top_recommendations"], start=1):
#     st.markdown(f"**{idx}. {rec['course']}**")
#     st.write(rec["reason"])

# st.subheader("🔄 Alternative Options")
# for alt in recommendations["alternative_paths"]:
#     st.markdown(f"- **{alt['path']}**: {alt['reason']}")


#     student_profile = {
#     "maths": maths_marks,
#     "science": science_marks,
#     "interest_tech": 1 if interest == "Technology" else 0,
#     "interest_creative": 1 if interest == "Creative" else 0,
#     "budget_low": 1 if budget == "Low" else 0,
#     "job_fast": 1 if goal == "Early Job" else 0
# }


# result = recommend_courses(student_profile)
# st.success(result["recommended_course"])


with st.form("career_form"):
    class_completed = st.selectbox("Which class have you completed?", ["10th", "12th"])
    stream = st.selectbox("Which stream did you study?", ["Science", "Commerce", "Humanities"])
    interest = st.selectbox("Which activities do you enjoy the most?", ["Technology", "Creativity", "Other"])
    learning = st.selectbox("Preferred learning style?", ["Practical", "Theoretical"])
    personality = st.selectbox("Personality type?", ["Introvert", "Extrovert"])
    budget = st.selectbox("Education budget?", ["Low", "Medium", "High"])
    location = st.selectbox("Preferred study location?", ["Kerala", "Outside Kerala"])
    goal = st.selectbox("Career goal?", ["Early Employment", "Higher Studies"])

    submitted = st.form_submit_button("Get Career Guidance")

if submitted:
    student_profile = {
        "class_12": 1 if class_completed == "12th" else 0,
        "science_stream": 1 if stream == "Science" else 0,
        "interest_tech": 1 if interest == "Technology" else 0,
        "interest_creative": 1 if interest == "Creativity" else 0,
        "practical_learning": 1 if learning == "Practical" else 0,
        "introvert": 1 if personality == "Introvert" else 0,
        "budget_low": 1 if budget == "Low" else 0,
        "stay_kerala": 1 if location == "Kerala" else 0,
        "early_job": 1 if goal == "Early Employment" else 0
    }

    result = recommend_courses(student_profile)

    st.success(f"🎓 Recommended Course: {result['recommended_course']}")
    st.info(result["reason"])