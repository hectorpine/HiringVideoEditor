# main.py
from crewai import Crew, Process
from tasks import tasks as setup_tasks  # Import the dictionary directly
from agents import get_agents

def main():
    # Retrieve the agents and tasks from the setup modules
    agents = get_agents()
    tasks = setup_tasks  # No need to call it, it's already a dictionary

    # Initialize the Crew with agents and their respective tasks
    crew = Crew(
        agents=list(agents.values()),  # Convert agent dict values to a list
        tasks=list(tasks.values()),    # Convert tasks dict values to a list
        process=Process.sequential     # Define the process as sequential
    )

    # Define the inputs for your crew; these could be dynamic based on your requirements
    inputs = {'problem': 'Excessive time spent on video editing'}

    # Start the crew with the defined inputs
    result = crew.kickoff(inputs=inputs)

    # Print the results of the crew's work
    print("Crew execution result:", result)

if __name__ == "__main__":
    main()
