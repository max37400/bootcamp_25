from fastapi import APIRouter, Request

from app.agents.evaluation_agent import create_evaluation_agent

from agents import Runner

from app.agents.prompts.utils import load_prompts

router = APIRouter()

prompts = load_prompts("evaluation_system_prompt.yaml")
system_prompt = prompts["evaluation_system_prompt"]

# Хранилище для последних результатов оценки
last_evaluation_result:dict = {}

@router.post("/api/evaluation")
async def evaluate_endpoint(request: Request):
    global last_evaluation_result
    
    last_evaluation_result = {}
    data = await request.json()
    messages = data.get("messages", [])
    messages = [{k: v for k, v in m.items() if k in ['role', 'content']} for m in messages]
    skills = data['skill'].split(',')
    
    for sk in skills:
        system_prompt = prompts["evaluation_system_prompt"].format(skill=sk)
        agent = create_evaluation_agent(system_prompt)  
        response = await Runner.run(agent, messages)
        last_evaluation_result[sk] = response.final_output_as(cls=dict)
    print(last_evaluation_result)
    return last_evaluation_result

@router.get("/api/evaluation")
async def get_evaluation_result():
    """Эндпоинт для получения последних результатов оценки."""
    return last_evaluation_result