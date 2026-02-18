Once update the .env file --> go to langchain1.py and modularize the code to ocnsume in other python programs.



langchain1.py:

"""
Modular LangChain + Gemini integration.
Import and use get_model(), chat(), chat_with_system(), stream() from other modules,
or run this file to demo (optionally pass a prompt as argument).
"""
"""
Modular LangChain + Gemini integration.
Import and use get_model(), chat(), chat_with_system(), stream() from other modules,
or run this file to demo (optionally pass a prompt as argument).
"""
import os
import sys
from dotenv import load_dotenv

load_dotenv()


def get_model(model_name="gemini-2.5-flash"):
    """Return a Gemini chat model (uses GOOGLE_API_KEY from .env)."""
    from langchain_google_genai import ChatGoogleGenerativeAI
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not set in .env")
    return ChatGoogleGenerativeAI(model=model_name, google_api_key=api_key)


def chat(prompt, model=None):
    """Send a prompt and return the full response text."""
    if model is None:
        model = get_model()
    return model.invoke(prompt).content


def chat_with_system(system_prompt, user_prompt, model=None):
    """Chat with a system message (role/behavior) plus one user message."""
    from langchain_core.messages import SystemMessage, HumanMessage
    if model is None:
        model = get_model()
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt),
    ]
    return model.invoke(messages).content


def stream(prompt, model=None):
    """Yield response chunks as they arrive (streaming)."""
    if model is None:
        model = get_model()
    for chunk in model.stream(prompt):
        if chunk.content:
            yield chunk.content


if __name__ == "__main__":
    print("Gemini (LangChain) demo\n")
    prompt = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Say hello in one short sentence."
    try:
        response = chat(prompt)
        print("Response:", response)
    except Exception as e:
        print("Error:", e)


