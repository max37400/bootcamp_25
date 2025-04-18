from agents import Agent
from app.agents.tools.lie_answer import lie_answer
from app.agents.tools.context_usage import get_5_last_context_messages

def create_hr_validation_agent(system_prompt: str) -> Agent:
    return Agent(
        name="Агент HR эксперт в процессе рекрутмента.",
        handoff_description="Ты HR эксперт в процессах найма. Ты оцениваешь и помогаешь другим рекрутерам проводить интервью.",
        instructions=system_prompt,
        tools=[get_5_last_context_messages],
    )