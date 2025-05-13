import os
import pyttsx3 
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI LLM
llm = OpenAI(openai_api_key=api_key, temperature=0.7)

# Initialize Text to Speech engine
engine = pyttsx3.init()

# Create prompt template (optional, can be simplified)
prompt_template = PromptTemplate(
    input_variables=["topic"],
    template="Tell me something interesting about {topic}."
)

# Chat loop
print("Voice Bot is ready! Type 'exit' to quit.\n")
while True:
    topic = input("Ask me something: ").strip()
    if topic.lower() == "exit":
        break

    # Format and get response
    prompt = prompt_template.format(topic=topic)
    response = llm(prompt)

    # Print and speak
    print("Bot:", response.strip())
    engine.say(response)
    engine.runAndWait()