import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

llm = OpenAI(
    temperature=0.7,
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]
)

main_prompt = PromptTemplate(
    template="You are an emotion detection AI. Analyze the following user message and determine the main emotion.\n\nUser Text: {text}",
    input_variables=["text"]
)

detailed_prompt = PromptTemplate(
    template="List the user's exact emotions (no explanations). User message: {text}",
    input_variables=["text"]
)

final_prompt = PromptTemplate(
    template="""
You've identified that the user is mainly feeling: {main_emotion}.
The detailed emotional layers include: {detailed_emotions}.

Now, respond directly to the user. Offer a clear and empathetic explanation of what they're feeling, why that might be happening, and give advice or motivation based on that emotional state.

Your tone should be professional, motivational, and supportive.
""",
    input_variables=["main_emotion", "detailed_emotions"]
)

main_chain = main_prompt | llm
detailed_chain = detailed_prompt | llm
final_chain = final_prompt | llm

def get_the_emotions(text: str):
    print(f"\n🔍 Analyzing Text: {text}\n")

    main_emotion = main_chain.invoke({"text": text})
    print("\n📌 Main Emotion:")
    print(main_emotion.strip())

    detailed_emotions = detailed_chain.invoke({"text": text})
    print("\n📋 Detailed Emotions:")
    print(detailed_emotions.strip())

    print("\n💬 Final Feedback:")
    final_output = final_chain.invoke({
        "main_emotion": main_emotion,
        "detailed_emotions": detailed_emotions
    })
    print(final_output.strip())

if __name__ == "__main__":
    user_input = """
I studied all night hoping to finally pass this time, but when I saw my results, my heart sank. Another failure. I feel like no matter how hard I try, I just can’t get it right. Everyone around me seems to be moving forward, and I’m stuck — exhausted, angry, and questioning if I’m even capable anymore.
"""
    get_the_emotions(user_input)
