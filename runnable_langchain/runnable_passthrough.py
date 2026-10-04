from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableSequence, RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")
prompt1 = PromptTemplate.from_template("write a jock about {topic}")
prompt2 = PromptTemplate.from_template("Explain the followig jock {topic}")
parser = StrOutputParser()

jock_generator_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    "jock":RunnablePassthrough(),
    "explanation":RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(jock_generator_chain, parallel_chain)

res = final_chain.invoke({"topic":"Machine Larning"})

print(res)

