1. .env
2. langcha1.py
3. langchin2.py - import the langchain1.py modules

langchain2.py 
_____________

"""Consumes multiple exports from langchain1 in one statement."""
"""Consumes multiple exports from langchain1 in one statement."""
from langchain1 import get_model, chat, stream

if __name__ == "__main__":
    # Multiple models in one statement (different Gemini variants)
    flash, pro = get_model("gemini-2.5-flash"), get_model("gemini-1.5-flash")
    print("gemini-2.5-flash:", flash.invoke("Say hi in 3 words.").content)
    # print("gemini-1.5-flash:", pro.invoke("Say hi in 3 words.").content)

or

from langchain1 import get_model, chat, stream

if __name__ == "__main__":
    # Multiple models in one statement (different Gemini variants)
    flash, pro = get_model("gemini-2.0-flash"), get_model("gemini-1.5-flash")
    print("gemini-2.0-flash:", flash.invoke("Say hi in 3 words.").content)
    print("gemini-1.5-flash:", pro.invoke("Say hi in 3 words.").content)






