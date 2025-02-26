import os

from langchain_openai import AzureChatOpenAI

from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def get_llm_model():
    """Initializes and returns the Azure OpenAI Chat model."""
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    print(os.environ['DEBUG'])
    return AzureChatOpenAI(
        azure_deployment="gpt-4o-mini",
        temperature=0,
        max_tokens=600,
        timeout=None,
        max_retries=2,
    )

