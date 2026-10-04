from langchain_core.output_parsers import PydanticOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from pydantic import  BaseModel, Field

from dotenv import load_dotenv

load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id="google/gemma-2-2b-it",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
        )
)
model = ChatHuggingFace(llm = llm)

class Person(BaseModel):
    name: str=Field(description="Name of the person")
    age: int=Field(gt=18, description="Age of the person")
    city : str=Field(description="name of the city the person belong to")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate the name, age and city of the fictional {place} person\n {formate_instraction}",
    input_variables=["place"],
    partial_variables={"formate_instraction": parser.get_format_instructions()}
)   

prompt = template.invoke({'place':'pakisthan'})
result = model.invoke(prompt)

final_result = parser.parse(result.content)
print(final_result)