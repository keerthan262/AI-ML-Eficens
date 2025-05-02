import openai
import os
from dotenv import load_dotenv

load_dotenv() 
OpenAI_Key = os.getenv("OPENAI_API_KEY")

# Set your API key
client = openai.OpenAI(api_key=OpenAI_Key)

def resumeValidation(value,user_input):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content":value },
                {"role": "user", "content": user_input}
            ],
            temperature=0 
        )
        return response.choices[0].message.content.strip();

#resume used below
'''
Sarah Johnson
sarah.johnson@email.com | (555) 987-6543
📍 Seattle, WA

Professional Summary
Detail-oriented software engineer with 4+ years of experience in backend development and cloud infrastructure. Passionate about building scalable systems and improving development workflows.

Professional Experience
Software Engineer
BlueSky Technologies, Seattle, WA | June 2021 – Present

Designed and maintained RESTful APIs using Python (Flask) and PostgreSQL

Migrated monolithic services to microservices architecture on AWS

Implemented CI/CD pipelines using Jenkins, reducing deployment time by 40%

Junior Developer
InnovateX Solutions, Bellevue, WA | Jan 2019 – May 2021

Collaborated with frontend team to integrate APIs into React applications

Wrote unit and integration tests using pytest

Participated in Agile ceremonies and sprint planning

Education
B.S. in Computer Science
University of Washington – 2018

Skills
Python, AWS, Docker, Kubernetes, SQL, Git, REST APIs, Jenkins, Agile/Scrum
'''
print(" ");
user_input = input("Please enter the resume : ");
print(" ");
print("Your hiring manager is reviewing your resume please wait....");
    
response_prompt = "You are a hiring manager reviewing a resume for a software engineering position. Evaluate thoughts for the following resume with hiring recuriter : {user_input}";
feedback_prompt = "Evaluate the resume and give feedback on this candidate resume : {user_input} ";

res_prompt = resumeValidation(response_prompt, user_input);
feed_prompt = resumeValidation(feedback_prompt,user_input);

print(" ");
print(" ");
print("******* Evaluation Response Prompot from hiring manager with recrutier ***********");
print(res_prompt);
print(" ");
print(" ");
print("******* Feedback Prompot from hiring manager ***********");
print(feed_prompt);
