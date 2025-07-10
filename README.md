
# LangChain Practical Learning - Rubin

This repository contains my hands-on experiments and projects with LangChain, showcasing the key concepts I learned today. It includes everything from basic prompt engineering and chaining to real-time streaming and a full emotion detection pipeline built with OpenAI LLMs.

---

## What I Learned Today

1. **LangChain Basics**
   - Setting up LangChain with `langchain-openai`
   - Managing deprecated imports and keeping the code updated
   - Using `.env` files for secure API key management

2. **Prompting and Chaining**
   - Creating and using `PromptTemplate` for dynamic prompts
   - Chaining prompts and LLMs using the pipe (`|`) syntax
   - Passing inputs through `.invoke()` method with dictionaries

3. **Streaming Outputs**
   - Using `StreamingStdOutCallbackHandler` for real-time token streaming
   - Understanding how streaming improves UX by showing responses as they generate

4. **Emotion Detection Project**
   - Building a 3-step pipeline:
     - Detect main emotion from user input
     - Extract detailed emotions
     - Provide motivational and empathetic feedback based on detected emotions
   - Using multiple prompt templates chained with the LLM for modular design
   - Formatting responses clearly and professionally

---

## Emotion Detection Pipeline Breakdown

- **Main Prompt**: Analyzes user text to find the main emotion
- **Detailed Prompt**: Lists all specific emotions present in the text
- **Final Prompt**: Combines previous outputs to give a supportive, motivational response

This project demonstrates how to combine prompt engineering, chaining, and streaming to build an interactive NLP app.

---

## How to Run

1. Clone this repo

2. Add your OpenAI API key to a `.env` file:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
3. Run the emotion detection script:
   ```
   python emotion_project.py
   ```

---

## Next Steps

- Explore advanced prompt templates like `ChatPromptTemplate`
- Add memory modules for conversational context
- Experiment with LangChain agents and tool integration

---

Built by Rubin while leveling up on LangChain 🚀
