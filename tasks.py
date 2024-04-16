# tasks.py
from crewai import Task
from agents import get_agents

agents = get_agents()

# Define the tasks that correspond to each agent's role and goal
def setup_tasks():
    # Task for the Business Solutions Analyst
    business_analysis_task = Task(
        description="Analyze the current video editing workflow and time expenditure.",
        expected_output='A report defining the problem in business terms and potential solutions.',
        agent=agents['business_analyst'],
    )

    # Task for the Professional Video Editor Consultant
    video_editor_task = Task(
        description="Outline the qualifications, skills, and software requirements for a video editor.",
        expected_output='A detailed description of the video editing needs.',
        agent=agents['video_editor_consultant'],
    )

    # Task for the Talent Recruiter
    recruitment_task = Task(
        description="Create a job description and define the hiring process for a video editor.",
        expected_output='A job posting ready to be published and a guide for the recruitment process.',
        agent=agents['talent_recruiter'],
    )

    # Task for the Project Manager
    project_management_task = Task(
        description="Devise a 14-day action plan to hire a video editor.",
        expected_output='A step-by-step hiring plan with milestones and deadlines.',
        agent=agents['project_manager'],
    )

    # Organize tasks in a list or a dictionary as preferred for your workflow
    tasks = {
        'business_analysis_task': business_analysis_task,
        'video_editor_task': video_editor_task,
        'recruitment_task': recruitment_task,
        'project_management_task': project_management_task
    }

    return tasks

# Export the setup function for use in the main application
tasks = setup_tasks()
