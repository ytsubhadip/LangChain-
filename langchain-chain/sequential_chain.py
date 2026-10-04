import os

from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template="generate a detailed report on {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a 5 pointer summary from the following text \n{text}",
    input_variables=["text"]
)

model = ChatMistralAI(
    api_key= os.getenv("MISTRAL_API")
)

parser = StrOutputParser()

chain = (
    prompt1
    | model
    | parser
    | RunnableLambda(lambda text: {"text": text})
    | prompt2
    | model
    | parser
)

result = chain.invoke({"topic": "Unemployment of India"})
print(result)