from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate.from_template("tell me a jock about {topic}")
model = ChatGroq(model="openai/gpt-oss-120b")
parser = StrOutputParser()


chain = prompt | model | parser

response = chain.invoke({"topic": "python"})
print(response)
