import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


def generate_suggestions(resume: str, jd: str) -> str:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return "⚠️ GROQ_API_KEY is not set. Please add it to your .env file."

    prompt = f"""
You are an expert ATS (Applicant Tracking System) and career coach.

Carefully compare the resume below with the job description and provide a structured analysis.

Resume:
{resume}

Job Description:
{jd}

Provide your response in the following format:

## 1. AI ATS Match Score
Give a score out of 100 with a brief justification.

## 2. Missing Keywords & Skills
List the important keywords or skills from the JD that are absent in the resume.

## 3. Improvement Suggestions
Give 5–7 specific, actionable suggestions to improve the resume for this role.

## 4. Strengths
List 3–5 things the resume does well relative to the JD.
"""

    try:
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"⚠️ Error generating suggestions: {str(e)}"