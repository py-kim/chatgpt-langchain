from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv
import os
import openai


load_dotenv()
openai.api_key = os.environ.get("openai_api_key")

chat = ChatOpenAI(temperature=0)
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Who won the world series in 2020?"),
    AIMessage(content="The Los Angeles Dodgers won the World Series in 2020."),
    HumanMessage(content="Where was it played?"),
]

print(chat(messages))
