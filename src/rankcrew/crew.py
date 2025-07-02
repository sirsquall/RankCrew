from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from rankcrew.tools.custom_tool import DrupalPublishTool
import os

# Configure OpenAI o3 model
openai_api_key = os.getenv("OPENAI_API_KEY")
if openai_api_key:
    os.environ["OPENAI_API_KEY"] = openai_api_key

o3_llm = LLM(
    model="o3",
    drop_params=True,
    additional_drop_params=["stop"]
)

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Rankcrew():
    """Rankcrew crew"""
    
    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def idea_planner(self) -> Agent:    
        return Agent(           
            config=self.agents_config['idea_planner'],
            llm=o3_llm,
            verbose=True,
        )
    
    @agent
    def content_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['content_planner'],
            llm=o3_llm,
            verbose=True,
        )

    @agent
    def content_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['content_writer'],
            llm=o3_llm,
            verbose=True,
        )

    @agent
    def style_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['style_agent'],
            llm=o3_llm,
            verbose=True,
        )

    @agent
    def seo_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['seo_manager'],
            llm=o3_llm,
            verbose=True,
        )
    
    @agent
    def translater_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['translater_agent'],
            llm=o3_llm,
            verbose=True,
        )
    
    # To learn more about structured task outputs, 
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def idea_planner_task(self) -> Task:
        return Task(
            config=self.tasks_config['idea_planner_task'],
        )

    @task
    def planner_task(self) -> Task:
        return Task(
            config=self.tasks_config['planner_task'],
        )

    @task
    def write_task(self) -> Task:
        return Task(
            config=self.tasks_config['write_task'],
        )
    
    @task
    def style_task(self) -> Task:
        return Task(
            config=self.tasks_config['style_task'],
        )
    
    @task
    def translater_task(self) -> Task:
        return Task(
            config=self.tasks_config['translater_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Rankcrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        manager = next(
            (ag for ag in self.agents if ag.role.strip() == "SEO manager"),
            None
        )

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            manager_agent=manager,
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
