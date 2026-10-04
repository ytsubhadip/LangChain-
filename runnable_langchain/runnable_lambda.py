from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnablePassthrough, RunnableParallel, RunnableLambda
from dotenv import load_dotenv

load_dotenv()

def word_count(text):
    return len(text.split())

prompt1 = PromptTemplate.from_template("Gneerate a jock given {topic}")
model = ChatGroq(model="openai/gpt-oss-120b")
parser = StrOutputParser()

# create a jock generator
jock_generate_chain = RunnableSequence(prompt1, model, parser)

# create a parrale jock lenght count chain
parallel_chain = RunnableParallel({
    "jock": RunnablePassthrough(),
    "work_count":RunnableLambda(word_count)
})

final_chain = RunnableSequence(jock_generate_chain, parallel_chain)

res = final_chain.invoke({"topic": "ML"})

print(res)