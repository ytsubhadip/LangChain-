from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate

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

prompt1 = template1.invoke({'topic':'car'})
result = model.invoke(prompt1)

prompt2 = template2.invoke({'text': result.content})

result1 = model.invoke(prompt2)
print(result1.content)













