from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():

    job_description = request.form["job_description"]

    with open("resume.txt", "r", encoding="utf-8") as file:
        resume = file.read()

    prompt = f"""
You are an expert ATS resume optimizer.

Your task:

1. Analyze the resume against the job description.
2. Give a realistic ATS score.
3. List missing skills.
4. Rewrite and optimize the resume professionally.
5. Improve wording and ATS keywords.
6. DO NOT invent fake skills or fake experience.

Return in this format:

ATS MATCH SCORE:
(score)

WHY THIS SCORE:
(short explanation)

MISSING SKILLS:
(list)

OPTIMIZED RESUME:
Rewrite the resume professionally and make it ATS optimized.

Resume:
{resume}

Job Description:
{job_description}
"""
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    result = response.choices[0].message.content

    return result

if __name__ == "__main__":
    app.run(debug=True)