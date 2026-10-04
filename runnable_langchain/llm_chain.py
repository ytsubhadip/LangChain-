from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-120b",temperature=0.7)
prompt = PromptTemplate.from_template(
   "suggest a catchy blog title about {topic}"
)

chain = prompt | llm | StrOutputParser()

topic = input("Enter the topic: ")

response = chain.invoke({"topic": topic})

print(response)