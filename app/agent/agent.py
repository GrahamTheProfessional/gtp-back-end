from openai import OpenAI
from dotenv import load_dotenv
from groq import Groq
import os


class ChatAgent:
    def __init__(self):
        load_dotenv()
        openrouter_api_key = os.getenv("OPENROUTER_DS_V3_API_KEY")
        groq_api_key = os.getenv("GROQ_API_KEY")

        self.deepseek_v3_client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=openrouter_api_key,
        )

        self.groq_client = Groq(
            api_key=groq_api_key,
        )

    def get_deepseek_response(self, user_message: str) -> str:
        response = self.deepseek_v3_client.chat.completions.create(
            model="deepseek/deepseek-chat-v3-0324:free",
            # model="deepseek/deepseek-r1-zero:free",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": user_message},
            ],
            stream=False,
        )
        return response.choices[0].message.content

    def get_groq_response(self, user_message: str) -> str:
        response = self.groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content
