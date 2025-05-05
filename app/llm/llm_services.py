from langchain_openai import ChatOpenAI
from app.config import get_settings
settings = get_settings()

OPENAI_API_KEY = settings.OPENAI_API_KEY

llm= ChatOpenAI(model='gpt-4o', temperature= 0.2)