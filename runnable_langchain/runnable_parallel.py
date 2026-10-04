from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence
from dotenv import load_dotenv

load_dotenv()

# create prompt template

prompt1 = PromptTemplate.from_template("Generate a tweet about {topic}")

prompt2 = PromptTemplate.from_template("Generate a Linkedin post about {topic}")

model = ChatGroq(model="openai/gpt-oss-120b")

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkden': RunnableSequence(prompt2, model, parser)
})

result = parallel_chain.invoke({"topic": "ai"})

print(result)

