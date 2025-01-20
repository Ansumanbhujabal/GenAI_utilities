from langchain_openai import AzureChatOpenAI
import getpass
import os

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

messages = [
    (
        "system",
        "You are a helpful Senior SEO content writer. Format and rewrite this ",
    ),
    ("human", "Applicants must have&nbsp;passed a high schoolThe following curricular requirements are&nbsp;strongly recommended:Four years of EnglishThree years of mathematics (minimum course work equivalent to Algebra I, Geometry, Algebra II)Three years of science (two of which must be lab science)Two years of social scienceTwo years of language study other than English"),
]
ai_msg = llm.invoke(messages)
ai_msg

print(ai_msg.content)