import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate


load_dotenv()



llm = OpenAI(temperature=0.7)


subtopic_prompt= PromptTemplate(template="What are the sub-subtopics of {topic}?", input_variables=["topic"])

subtopic_chain = subtopic_prompt | llm   # prompt | llm 

explanation_prompt =  PromptTemplate(template="Explain {subtopic} in simple terms.", input_variables=["subtopic"])

explanation_chain = explanation_prompt | llm  # prompt | llm



def explain_topic(topic: str):
    print(f"\n🔍 Topic: {topic}\n")

    # Step 1: Get subtopics
    subtopics_raw = subtopic_chain.invoke({"topic": topic})
    print("📚 Subtopics generated:")
    print(subtopics_raw)

    # Clean and split subtopics
    subtopics = [s.strip("-•1234567890. ").strip() for s in subtopics_raw.split("\n") if s.strip()]
    
    print("\n🧠 Explanations:\n")

    # Step 2: Explain each subtopic
    for sub in subtopics:
        print(f"👉 {sub}")
        explanation = explanation_chain.invoke({"subtopic": sub})
        print(explanation.strip(), "\n")


explain_topic("Fake Love and Betrayal in Relationships")
