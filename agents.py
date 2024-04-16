# agents.py
import os
import crewai_tools 
from crewai import Agent
from crewai.memory.contextual import contextual_memory
from crewai_tools import SerperDevTool

# Set your environment variables for any API keys required
os.environ["OPENAI_API_KEY"] = "API_KEY_HERE" # Replace with your actual key
os.environ["SERPER_API_KEY"] = "API_KEY_HERE"

# Define your agents with roles, goals, and backstory here
business_analyst = Agent(
    role='Business Solutions Analyst',
    goal='Define the problem of spending too much time editing videos',
    backstory='Experienced in identifying inefficiencies and optimizing business processes.',
    memory=contextual_memory,
    tools=[SerperDevTool()],
    verbose=True,
    allow_delegation=True
)

video_editor_consultant = Agent(
    role='Professional Video Editor',
    goal='Outline the necessary skills and software for video editing tasks',
    backstory='A seasoned editor with a wealth of experience in various editing tools and techniques.',
    memory=contextual_memory,
    tools=[SerperDevTool()],
    verbose=True,
    allow_delegation=True
)

talent_recruiter = Agent(
    role='Hiring Manager',
    goal='Develop a comprehensive job posting and candidate evaluation criteria',
    backstory='Specializes in talent acquisition with an extensive network in the creative industry.',
    memory=contextual_memory,
    tools=[SerperDevTool()],
    verbose=True,
    allow_delegation=True
)

project_manager = Agent(
    role='Project Manager',
    goal='Create a 14-day plan to hire a video editor',
    backstory='Expert in project planning and execution, ensuring deliverables are met on time.',
    memory=contextual_memory,
    tools=[SerperDevTool()],
    verbose=True,
    allow_delegation=True
)

# Assuming you have a manager role that oversees the project
# manager_agent = ...

# Collect all agents into a dictionary for easy access
agents = {
    'business_analyst': business_analyst,
    'video_editor_consultant': video_editor_consultant,
    'talent_recruiter': talent_recruiter,
    'project_manager': project_manager,
    # 'manager_agent': manager_agent,
}

def get_agents():
    return agents
