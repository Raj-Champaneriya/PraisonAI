from praisonaiagents import Agent, Task, PraisonAIAgents
from pydantic import BaseModel
from typing import List, Dict

class CVAnalysisReport(BaseModel):
    overall_score: int
    key_strengths: List[str]
    areas_for_improvement: List[str]
    market_fit: str
    recommendations: List[str]
    technical_skills: List[str]
    soft_skills: List[str]
    skill_gaps: List[str]
    key_achievements: List[str]
    impact_metrics: List[Dict[str, str]]
    areas_of_expertise: List[str]

# Create single CV analysis agent
cv_analyzer = Agent(
    role="CV Analysis Expert",
    goal="Provide comprehensive CV evaluation and recommendations",
    backstory="""You are an expert CV analyst with deep knowledge of industry requirements, 
    market trends, and talent assessment. You excel at evaluating skills, experience, 
    and providing actionable recommendations.""",
    verbose=True
)

# Single comprehensive analysis task
cv_analysis_task = Task(
    description="""Analyze the CV comprehensively including:
    1. Technical and soft skills assessment
    2. Experience and achievements evaluation
    3. Overall CV evaluation with recommendations
    Provide detailed insights and actionable recommendations.""",
    expected_output="Complete CV analysis report",
    agent=cv_analyzer,
    output_pydantic=CVAnalysisReport
)

# Create and run the agent
agents = PraisonAIAgents(
    agents=[cv_analyzer],
    tasks=[cv_analysis_task]
)

# Read and pass CV content through start()
with open('cv.txt', 'r') as file:
    cv_content = file.read()

# Start the analysis by passing CV content
result = agents.start(cv_content)

print(result)