from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from documentazione_flow.tools.rag_tool import search_rag
from documentazione_flow.tools.user_input_tool import request_user_input, collect_missing_information

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class RagCrew():
    """RagCrew crew for generating application documentation using RAG"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    @agent
    def documentation_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['documentation_researcher'], # type: ignore[index]
            tools=[search_rag],
            verbose=True
        )

    @agent
    def documentation_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['documentation_generator'], # type: ignore[index]
            tools=[request_user_input, collect_missing_information],
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def research_documentation_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_documentation_task'], # type: ignore[index]
        )

    @task
    def generate_documentation_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_documentation_task'], # type: ignore[index]
            output_file='application_documentation.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the RagCrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
