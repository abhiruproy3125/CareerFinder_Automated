import os
import pandas as pd
from openai import OpenAI
from jobspy import scrape_jobs
from datetime import datetime

# --- CONFIGURATION ---
API_KEY = os.getenv("DEEPSEEK_API_KEY", "sk-0d8de3fecd65465991f3c0d335739a36")

client = OpenAI(
    base_url='https://api.groq.com/openai/v1',
    api_key='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', # Put your gsk_ key here
)

# Use their DeepSeek Distill model (much smarter than the 1.5B version!)
MODEL_NAME = "llama-3.3-70b-versatile"

with open("resume.txt", "r", encoding="utf-8") as file:
    MY_RESUME = file.read()

EXCEL_FILE = "Job_Hunt_Tracker.xlsx"

def analyze_job_with_ai(job_title, job_description):
    """Asks DeepSeek to the score the job match and find gaps."""

    # SAFETY CHECK: If description is missing, use a placeholder
    if pd.isna(job_description) or not job_description:
        job_description = "No description provided."
    job_description = str(job_description)

    prompt = f"""
    You are a career advisor. Given the following job title and description, analyze how well it matches the provided resume. 
    Provide a match score from 0 to 100 and identify any skill gaps.

    Job Title: {job_title}
    Job Description:{job_title} - {job_description[:2000]} # Limit for tokens


    Resume: {MY_RESUME}

    Provide a response in exactly this format:
    MATCH_SCORE: [X/10]
    GAPS: [Top 3 missing skills]
    ADVICE: [One sentence on how to tailor the application]
    """
    print(prompt)
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return response.choices[0].message.content    
    except Exception as e:
        return f"Error during AI analysis: {str(e)}"
    
    # ---EXECUTION---

print("Searching for SLAM/Robotics roles in Germany...")

jobs = scrape_jobs(
    site_name=["linkedin","indeed"],
    search_term='("SLAM" OR "Simultaneous Localization and Mapping" OR "Robotics") AND "C++"',
    location="Germany",
    results_wanted=10,
    hours_old=24,
    linkedin_fetch_description=True
)

# 2. Process and Save
if not jobs.empty:
    results = []
    for _, row in jobs.iterrows():
        print(f"Analyzing job: {row['title']} at {row['company']}...")
        analysis = analyze_job_with_ai(row['title'], row['description'])
        
        results.append({
            "Date": datetime.now().strftime("%Y-%m-%d"),
            "Company": row['company'],
            "Title": row['title'],
            "AI Analysis": analysis,
            "Link": row['job_url']
        })


    #3. Save to Excel
    new_df = pd.DataFrame(results)
    if os.path.exists(EXCEL_FILE):
        old_df = pd.read_excel(EXCEL_FILE)
        final_df = pd.concat([old_df, new_df]).drop_duplicates(subset=['Link'])
    else:
        final_df = new_df

    final_df.to_excel(EXCEL_FILE, index=False)
    print(f"✅ Success! Check {EXCEL_FILE} for results.")
else:
    print("No new jobs for your search criteria found.")
