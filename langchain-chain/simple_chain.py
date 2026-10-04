import os

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser   

from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate(
    template="generate 5 interesting fact about this {topic}",
    input_variables=["topic"]
)

model = ChatMistralAI(
    api_key=os.getenv("MISTRAL_API")
    # model = "mistral-small-latest"
    )

parser = StrOutputParser()
chain = prompt | model | parser

result = chain.invoke({'topic':'cricket'})  

print(result)
chain.get_graph().print_ascii()