# VoiceChatBot

# LangChain Voice Bot

A voice-enabled chatbot using LangChain, OpenAI, and pyttsx3 for text-to-speech output. The bot answers questions and speaks responses aloud using the OpenAI API.

## Features
- Ask the bot any question, and it will respond using OpenAI's GPT model.
- Responses are spoken aloud using the pyttsx3 text-to-speech engine.
- The bot can be interacted with through text input and outputs via both console and speech.



 ## File Structure

 langchain_voice_bot/
 
   .env # Environment variables (store your OpenAI API key here)
   
   voice_bot.py # Main script to run the voice bot
   
   requirements.txt # List of dependencies to install via pip




1. Install Dependencies

    pip install -r requirements.txt

 pyttsx3
 langchain
 openai
 python-dotenv

2. Set Up Environment Variables

   OPENAI_API_KEY=your_openai_api_key_here

3. Run the Bot

   python voice_bot.py

Example Usage!!

Voice Bot is ready! Type 'exit' to quit.

Ask me something: What is LangChain?

Bot: LangChain is a framework for developing applications powered by large language models, enabling easy integration with external tools and data sources.

Troubleshooting:

1. ModuleNotFoundError: No module named 'pyttsx3'

    pip install pyttsx3

2. No Sound or Issues with TTS (Text-to-Speech)
  Ensure your microphone and speakers are set up properly. You can also try adjusting the pyttsx3 settings by setting a different voice 
  engine or rate.

3. OpenAI API Key Issues
  If you get an error like Invalid API Key, check that your .env file contains the correct API key and that it's being loaded correctly.



Acknowledgments
LangChain: A powerful framework for large language model-based applications.
OpenAI: Provides the GPT-3 API for intelligent chatbot responses.
pyttsx3: A Python library for text-to-speech synthesis.








