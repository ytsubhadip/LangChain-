from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
load_dotenv()

LLM = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
            temperature=0.5,
            max_new_tokens=100
        )
)

model = ChatHuggingFace(llm=LLM)
# 1st prompt
template1 = PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=["topic"]
)

# 2nd prompt 
template2 = PromptTemplate(
    template='write a 5 line summery on the following text./n{text}',
    input_variables=["text"]
)

parser = StrOutputParser()
chain = (
    template1
    | model
    | parser
    | (lambda text: {"text": text})
    | template2
    | model
    | parser
)
result = chain.invoke({'topic':'black hole'})
print(result)













