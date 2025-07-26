from app.interfaces.agent import AIAgentI


class FakeAgent(AIAgentI):
    def query_agent(self, question: str, context: list[str]) -> str:
        answer = f"""
        Hello, you asked me the following question:
        {question} based on the following context:
        {context}.
        However I am only a fake agent, I don't have any answer
        """
        return answer
