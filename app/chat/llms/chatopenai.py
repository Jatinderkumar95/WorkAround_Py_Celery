from langchain.chat_models import ChatopenAI


def build_llm(chat_args, model_name):
    return ChatopenAI(streaming=chat_args.streaming, model_name=model_name)