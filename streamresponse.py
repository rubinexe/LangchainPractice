import os
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import OpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import PromptTemplate

def main():
    # Define your prompt template — no inputs here, just a fixed string
    prompt_template = PromptTemplate(
        ##template="Write a motivational quote about discipline in {number} lines!.",
        ##input_variables=["number"]

         template="Write a motivational quote about discipline!.",
         input_variables=[]  # No inputs needed since prompt is fixed
    )

    # Setup streaming callback to print tokens as they come in
    streaming_callback = StreamingStdOutCallbackHandler()

    # Initialize OpenAI LLM with streaming and callback
    llm = OpenAI(
        streaming=True,
        callbacks=[streaming_callback],
        temperature=0.7
    )

    # Use new pipe syntax: prompt_template | llm
    # This creates a RunnableSequence (chain) under the hood
    chain = prompt_template | llm

    # Run chain — streaming output prints live
    chain.invoke({})  # No inputs needed since prompt is fixed thats why its empty bruh
   ## chain.invoke({"number" : 10}) 
if __name__ == "__main__":
    main()
