import os
from dotenv import load_dotenv
from langchain_openai import OpenAI 

load_dotenv()





llm = OpenAI(temperature=0.7)

#
response = llm.invoke("Write a motivational quote for a student about discipline.")
print(response)
