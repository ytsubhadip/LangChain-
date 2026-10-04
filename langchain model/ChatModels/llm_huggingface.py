from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(

    model="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    max_new_tokens=100,
    temperature=0.7

)

model = ChatHuggingFace(llm = llm)

response = model.invoke("what is AI and how use it in python? ")
print(response.text)