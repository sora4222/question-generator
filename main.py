from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate


def main():
    """Entry."""
    template = "Generate a question and it's answer that can be used to test a student's knowledge of the following topic: {topic}"
    prompt = ChatPromptTemplate.from_template(template)
    llm = init_chat_model("llama3.2:3b", model_provider="ollama", temperature=0.2)
    chain = prompt | llm
    response = chain.invoke({"topic": "Python programming"})
    print(response)


if __name__ == "__main__":
    main()
