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
prompt_template: str = """/
You are a professional senior SEO and Content specialist./
For the given input make it formatted and SEO oriented and Paraphrase it./
For number of years use digits. Example : Make "five" to "5"./ 
question: {question}./
only give the content in output in a human readable format ./
##Here is an example 
question:Applicants must have&nbsp;passed a high schoolSubjects required :Four years of EnglishThree years of mathematics (minimum course work equivalent to Algebra I, Geometry, Algebra II)Three years of science (two of which must be lab science)Two years of social scienceTwo years of language study other than English

Answer:
Requirements for applicants include the following:
- Graduation from high school
- Completion of 4 years of English
- Completion of 3 years of mathematics, with a minimum coursework equivalent to Algebra I, Geometry, and Algebra II
- Completion of 3 years of science, with at least 2 years of lab science
- Completion of 2  years of social science
- Completion of 2  years of language study other than English
"""

prompt = PromptTemplate.from_template(template=prompt_template)



f1="Applicants must have&nbsp;passed a high schoolThe following curricular requirements are&nbsp;strongly recommended:Four years of EnglishThree years of mathematics (minimum course work equivalent to Algebra I, Geometry, Algebra II)Three years of science (two of which must be lab science)Two years of social scienceTwo years of language study other than English"

f2="Applicants must have passed a high school.The following curricular requirements are&nbsp;strongly recommended:Four years of EnglishThree years of mathematics (minimum course work equivalent to Algebra I, Geometry, Algebra II)Three years of science (two of which must be lab science)Two years of social scienceTwo years of language study other than English."

f3="Applicants must have&nbsp;passed a high schoolSubjects required :Four years of EnglishThree years of mathematics (minimum course work equivalent to Algebra I, Geometry, Algebra II)Three years of science (two of which must be lab science)Two years of social scienceTwo years of language study other than English"

# Questions 
questions =[
    f3
]
# Iterate through the questions
for question in questions:
    prompt_formatted_str = prompt.format(question=question)
    time.sleep(15)
    prediction = llm.invoke(prompt_formatted_str)

    print("Question:", question)
    print("Answer:", prediction.content)
    print("-----------------")  # separator between results