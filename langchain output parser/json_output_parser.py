from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()

llm = HuggingFacePipeline.from_model_id(
     model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        task="text-generation",
        pipeline_kwargs=dict(
                temperature=0.5,
                max_new_tokens=100
            )
)

model = ChatHuggingFace(llm = llm)

# response = model.invoke("heicha, hechollackdic na machi lokoloko")
# print(response)

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me the name ,age and city of a fictional person \n {format_instraction}',
    input_variables=[],
    partial_variables={"format_instraction":parser.get_format_instructions() }

)

# prompt = template.format()
# result = model.invoke(prompt)

# final_result = parser.model_validate(result.content) # not work

# using chain
chian = template | model | parser

result = chian.invoke({})

print(result)



