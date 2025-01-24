from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv, find_dotenv
import os
import time
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

api_key=os.getenv("AZURE_OPENAI_API_KEY"), 
azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
llm = AzureChatOpenAI(
    azure_deployment="gpt-4",
    api_version="2024-08-01-preview", 
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)



# create the prompt
# prompt_template: str = """/
# You are a professional senior SEO and Content Paraphrase specialist./
# For the given input make it formatted and SEO oriented and Paraphrase it./
# For number of years use digits. Example : Make "five" to "5"./ 
# question: {question}./
# only give the content in output in a human readable format. /

# ##Here is an example 
# question:Applicants must have&nbsp;passed a high schoolSubjects required :Four years of EnglishThree years of mathematics (minimum course work equivalent to Algebra I, Geometry, Algebra II)Three years of science (two of which must be lab science)Two years of social scienceTwo years of language study other than English

# Answer: 
# Criteria: 
#  Education - High School Graduation
# Coursework:
#  English: 4 years
#  Mathematics: 3 years (Algebra I, Geometry, Algebra II required)
#  Science: 3 years (2 years must include lab-based courses)
#  Social Science: 2 years
#  Language Study: 2 years (non-English language)

# make sure folowing the format as the example   
# """



prompt_template: str = """/
You are a professional senior Content and Data extraction and gatherer  specialist
For the input {question}./
Find the coordinates 
The months in which they start taking new admissions
University Official Link
Eligibility description segregated with 10th,12th, Graduation as applicable for the course/
##Example
question:Vidyasagar College
Answer:
Coordinates:Latitude: 20.3553° N
            Longitude: 85.8182° E
Intake Month: Early Januray 
Link:https://www.vidyasagarcollege.edu.in/   
Eligibility:
10th:Mandatory
12th:Mandatory(with Science and Maths)
Graduation:BTech (Computer Science And Related Branch)        
"""

prompt = PromptTemplate.from_template(template=prompt_template)



f1="Applicants must have&nbsp;passed a high schoolThe following curricular requirements are&nbsp;strongly recommended:Four years of EnglishThree years of mathematics (minimum course work equivalent to Algebra I, Geometry, Algebra II)Three years of science (two of which must be lab science)Two years of social scienceTwo years of language study other than English"

f2="Applicants must have passed a high school.The following curricular requirements are&nbsp;strongly recommended:Four years of EnglishThree years of mathematics (minimum course work equivalent to Algebra I, Geometry, Algebra II)Three years of science (two of which must be lab science)Two years of social scienceTwo years of language study other than English."

f3="Applicants must have&nbsp;passed a high schoolSubjects required :Four years of EnglishThree years of mathematics (minimum course work equivalent to Algebra I, Geometry, Algebra II)Three years of science (two of which must be lab science)Two years of social scienceTwo years of language study other than English"

f4={
    "College name":"DePaul University",
    "Course name":"Bachelor of Science Network Engineering and Security"
}
f5={
    "College name":"DePaul University",
    "Course name":"Bachelor of Arts in Political Science"
}
f6={
    "College name":"DePaul University",
    "Course name":"Bachelor of Science in Neuroscience"
}
# Questions 
questions =[
    f4,f5,f6
]
# Iterate through the questions
for question in questions:
    prompt_formatted_str = prompt.format(question=question)
    # time.sleep(15)
    prediction = llm.invoke(prompt_formatted_str)

    print("Question:", question)
    print("Answer:", prediction.content)
    print("-----------------")  # separator between results




#     format1=
#     """
#     Answer:
# Requirements for applicants include the following:
# - Graduation from high school
# - Completion of 4 years of English
# - Completion of 3 years of mathematics, with a minimum coursework equivalent to Algebra I, Geometry, and Algebra II
# - Completion of 3 years of science, with at least 2 years of lab science
# - Completion of 2  years of social science
# - Completion of 2  years of language study other than English


#     """

# format2="""
# Applicant Requirements
# To be eligible, applicants must meet the following criteria:
# Education
#  -Graduation from high school
# Coursework
#   The following academic requirements:
# -   4 Years Completion of 
#     - English  
# -   3 Years Completion of  
#     - Mathematics  : Must include coursework equivalent to Algebra I, Geometry, and Algebra II.
#     - Science  : At least 2 years must include lab-based science courses  .
# -   2 Years Completion of
#     - Social Science  
#     - Language Study (other than English) 
# """


# format3="""
# Applicants must have successfully completed high school. 
# The required subjects include 4 years of English, 3 years of mathematics (with coursework equivalent to Algebra I, Geometry, and Algebra II), 
# 3 years of science (at least 2 of which must be lab-based), 
# 2 years of social science, 
# and 2 years of language study other than English."""


# jsonformat="""
# {
#   "ApplicantRequirements": [
#     {
#       "Criteria": "Education",
#       "Details": "High school graduation"
#     },
#     {
#       "Criteria": "Coursework",
#       "Details": [
#         {
#           "Subject": "English",
#           "Requirement": "4 years"
#         },
#         {
#           "Subject": "Mathematics",
#           "Requirement": "3 years",
#           "Notes": "Must include coursework equivalent to Algebra I, Geometry, and Algebra II"
#         },
#         {
#           "Subject": "Science",
#           "Requirement": "3 years",
#           "Notes": "At least 2 years must include lab-based science courses"
#         },
#         {
#           "Subject": "Social Science",
#           "Requirement": "2 years"
#         },
#         {
#           "Subject": "Language Study",
#           "Requirement": "2 years",
#           "Notes": "Must be in a language other than English"
#         }
#       ]
#     }
#   ]
# }

# """