import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import AzureChatOpenAI

llm = AzureChatOpenAI(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),   # nama deployment, BUKAN endpoint
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),        # URL resource Azure Anda
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    temperature=0,
)

response = llm.stream("Write a poem about AI")

for chunk in response:
    print(chunk.content, end="", flush=True)