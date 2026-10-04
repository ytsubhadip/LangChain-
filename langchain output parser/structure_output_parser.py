import os
from langchain_mistralai import ChatMistralAI
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers.structured import (
    StructuredOutputParser,
    ResponseSchema)

from dotenv import load_dotenv

load_dotenv()

# llm = HuggingFacePipeline.from_model_id(
#     model_id="google/gemma-2-2b-it",
#     task="text-generation",
#     pipeline_kwargs=dict(
#                     temperature=0.5,
#                     max_new_tokens=100
#                 )


# )
# model = ChatHuggingFace(llm=llm)
model = ChatMistralAI(
    model="mistral-small-latest",
    api_key=os.getenv("MISTRAL_API")
)
result = model.invoke("what is google ? ")

print(result.content)