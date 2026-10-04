from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="model name",
    max_completion_tokens=12
)

res = model.invoke("user message ")

print(res.content)
