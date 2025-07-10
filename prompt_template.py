import os
from dotenv import load_dotenv
from langchain_openai import OpenAI  

from langchain.prompts import PromptTemplate


load_dotenv()




llm = OpenAI(temperature=0.7)


template = "Give me a {number} of tips for coders (short ones)"

prompt = PromptTemplate.from_template(template)

final_prompt = prompt.format(number = 3)

reply = llm.invoke(final_prompt)

print(reply)
