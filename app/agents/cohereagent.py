from app.interfaces.agent import AIAgentI

from langchain_cohere import ChatCohere
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.schema import StrOutputParser
from langchain_core.runnables import RunnableSequence

class CohereAgent(AIAgentI):

    def query_agent(self, question: str, context: list[str]) -> str:
        model = ChatCohere(model="command-r-plus")
        
        system_message_prompt = (
            SystemMessagePromptTemplate.from_template(self.template)
        )
        human_message_prompt = (
            HumanMessagePromptTemplate.from_template(template=f"{question}")

        )
        chat_prompt_template = (
            ChatPromptTemplate.from_template([system_message_prompt, human_message_prompt])
        )
        chain: RunnableSequence = chat_prompt_template | model | StrOutputParser()

        answer: str = chain.invoke({
            "question": question,
            "context": context
        })

        return answer