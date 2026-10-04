import os

from langchain_core.prompts import PromptTemplate
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

from dotenv import load_dotenv

load_dotenv()

model = ChatMistralAI(
    model="mistral-small-latest",
    api_key=os.getenv("MISTRAL_API"),
    temperature=0.7
)

chat_history = []
chat_history.append(SystemMessage(content="you are a helpfull ai assistant"))

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    result = model.invoke(chat_history)

    if user_input == 'exit':
        print("AI: ", result.content)
        break;
    
    else:
        chat_history.append(AIMessage(content=result.content))
        print("AI: ", result.content)

print(chat_history)