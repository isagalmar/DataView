import os
import openai
from langchain_community.chat_models import ChatOpenAI
import litellm

class IAClientMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    

class IAClient(metaclass=IAClientMeta):
    chat = None

    def __init__(self):
        self.chat = self.create_chat()

    def create_chat(self):
        if(self.chat != None):
            print("Chat IA ya inicializado!")
            return None
        
        
        return ChatOpenAI(api_key="sk-XBSp_9YujYTb8ZKUFxleNQ", base_url="https://litellm.dccp.pbu.dedalus.com", model="bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0")
        
