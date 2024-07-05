import uuid
from langchain_openai import AzureChatOpenAI
from config import AZURE_CHATBOT_API_KEY, AZURE_CHATBOT_ENDPOINT, AZURE_CHATBOT_OPENAI_VERSION


def get_llm():
    llm_instance = AzureChatOpenAI(
        api_key=AZURE_CHATBOT_API_KEY,
        azure_endpoint=AZURE_CHATBOT_ENDPOINT,
        openai_api_version=AZURE_CHATBOT_OPENAI_VERSION,
    )

    return llm_instance


def generate_uuid_str():
    return str(uuid.uuid4())
