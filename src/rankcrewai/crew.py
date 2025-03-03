from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Rankcrewai():
        """Rankcrewai crew"""

        # Learn more about YAML configuration files here:
        # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
        # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
        agents_config = 'config/agents.yaml'
        tasks_config = 'config/tasks.yaml'

        # If you would like to add tools to your agents, you can learn more about it here:
        # https://docs.crewai.com/concepts/agents#agent-tools
        @agent
        def researcher_agent(self) -> Agent:
                return Agent(
                        config=self.agents_config['researcher_agent'],
                        tools=[already_exist]
                        verbose=True
                )

        @agent
        def keyword_agent(self) -> Agent:
                return Agent(
                        config=self.agents_config['keyword_agent'],
                        verbose=True
                )

        @agent
        def seo_writter(self) -> Agent:
                return Agent(
                        config=self.agents_config['seo_writter'],
                        verbose=True
                )

        @agent
        def seo_manager(self) -> Agent:
                return Agent(
                        config=self.agents_config['seo_manager'],
                        verbose=True
                )

        # To learn more about structured task outputs, 
        # task dependencies, and task callbacks, check out the documentation:
        # https://docs.crewai.com/concepts/tasks#overview-of-a-task
        @task
        def research_task(self) -> Task:
                return Task(
                        config=self.tasks_config['research_task'],
                )

        @task
        def keyword_task(self) -> Task:
                return Task(
                        config=self.tasks_config['keyword_task'],
                )

        @task
        def writter_task(self) -> Task:
                return Task(
                        config=self.tasks_config['writter_task'],
                        output_file='blog.html'
                )

        @crew
        def crew(self) -> Crew:
                """Creates the Rankcrewai crew"""
                # To learn how to add knowledge sources to your crew, check out the documentation:
                # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

                return Crew(
                        agents=[researcher_agent, keyword_task, seo_writter],
                        tasks=self.tasks, # Automatically created by the @task decorator
                        manager_agent=seo_manager,
                        process=Process.sequential,
                        verbose=True,
                        # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
                )
