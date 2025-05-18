from typing import Optional
import sys
import os

# Add src to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.app.expense import Expenses
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_mistralai import ChatMistralAI
from langchain_core.utils.function_calling import convert_to_openai_tool
from dotenv import load_dotenv, dotenv_values

class LLMService:
    def __init__(self):
        load_dotenv()
        self.prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an expert extraction algorithm. "
                "Only extract relevant information from the text. "
                "If you do not know the value of an attribute asked to extract, "
                "return null for the attribute's value.",
            ),
            ("human", "{text}")
        ]
        )
        self.apiKey = os.getenv('OPENAI_API_KEY')
        self.llm = ChatMistralAI(api_key=self.apiKey, model="mistral-large-latest", temperature=0)
        self.runnable = self.prompt | self.llm.with_structured_output(schema=Expenses)

    def runLLM(self, message):
        return self.runnable.invoke({"text":message})