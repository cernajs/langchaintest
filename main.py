from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema import BaseOutputParser

from dotenv import load_dotenv
import os

load_dotenv()

# class ChatOpenAI(ChatOpenAI):
#     def __init__(self, openai_api_key, **kwargs):
#         super().__init__(openai_api_key=openai_api_key, **kwargs)

#     def get_prompt(self, context):
#         return f"""{context["system"]}: {context["user"]}"""
    
# class JSONoutputParser(BaseOutputParser):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

#     def parse(self, output):
#         return output

openai_api_key = os.getenv("OPENAI_API_KEY")

chat = ChatOpenAI(openai_api_key=openai_api_key)

#input = "I am verry ussure what about now to do."

task = """You are a helpful assistan that check the next input for any errors whether it is a spelling or grammar error.
            You also check weather some parts of the input can be rephrased to make it more clear and concise. 
            Resonse should be json format with what to improve given task described before, index where it should be changed
            and the new input with the changes."""

prompt = ChatPromptTemplate.from_messages([
    ("system", task),
    ("user", "{input}"),
])

output_parser = StrOutputParser()

chain = prompt | chat | output_parser

response = chain.invoke({"input": "I am verry ussure what about now to do."})

print(response)

#print(chain.get_output())