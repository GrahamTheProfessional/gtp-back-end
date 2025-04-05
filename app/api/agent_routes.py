from fastapi import APIRouter
from app.agent.agent import ChatAgent
from pydantic import BaseModel

# Initialize the agent
agent = ChatAgent()

# Initialize APIRouter instance
router = APIRouter()


# Define the message schema
class Message(BaseModel):
    message: str


@router.post("/chat/deepseek/")
async def deepseek_v3_chat(message: Message):
    user_message = message.message
    response = agent.get_deepseek_response(user_message)
    return {"response": response}


@router.post("/chat/llama/")
async def groq_chat(message: Message):
    user_message = message.message
    response = agent.get_llama_response(user_message)
    return {"response": response}
