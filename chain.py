import os
from dotenv import load_dotenv
from langchain_openai import OpenAI  # ✅ Correct import now

from langchain.prompts import PromptTemplate  # ✅ Correct import now





from langchain.chains import LLMChain

load_dotenv()

llm = OpenAI(temperature=0.7)




template = "Give me a {number} of tips for coders (short ones)"

prompt = PromptTemplate( template = template, input_variables = ["number"])


llm_chain = prompt | llm  # Create an LLMChain with the prompt and the LLM


response = llm_chain.invoke({"number": 3})

print(response)






