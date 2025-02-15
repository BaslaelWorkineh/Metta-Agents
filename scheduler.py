import concurrent.futures
import time
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from agents.agent_base import AgentObject


from agents.agent_base import AgentObject

class ParallelScheduler:
    def __init__(self):
        self.agents = {}

    def register_agent(self, agent_id, agent_creator):
        """ Register agents for execution """
        self.agents[agent_id] = agent_creator
        print(f"Registered agent: {agent_id}")

    def create_agent(self, agent_id: str) -> AgentObject:
        """ Create and return an agent """
        if agent_id in self.agents:
            print(f"Creating instance of {agent_id}...")
            agent = self.agents[agent_id]()  # This should return an AgentObject
            if agent:
                print(f"Successfully created {agent_id}.")
            else:
                print(f"Failed to create {agent_id}.")
            return agent
        else:
            print(f"Agent {agent_id} not found.")
            return None

    def execute_agent(self, agent_id: str):
        """ Execute a single agent """
        print(f"Creating agent: {agent_id}...")
        agent = self.create_agent(agent_id)
        
        if agent:
            print(f"Executing {agent_id}...")
            try:
                # Ensure the type of agent is known
                if isinstance(agent, AgentObject):
                    agent.run()
                print(f"Finished executing {agent_id}")
            except Exception as e:
                print(f"Error executing {agent_id}: {e}")
        else:
            print(f"Failed to create agent: {agent_id}")

    def run_all_agents_parallel(self):
        """ Run all registered agents in parallel """
        if not self.agents:
            print("No agents registered! Exiting...")
            return

        print("Starting parallel execution...")
        
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for agent_id in self.agents:
                print(f"Submitting agent {agent_id} to executor...")
                futures.append(executor.submit(self.execute_agent, agent_id))
            
            concurrent.futures.wait(futures)  # Wait for all agents to complete execution
        
        print("All agents finished execution.")

# Example usage
scheduler = ParallelScheduler()

# Register agents
scheduler.register_agent("AFImportanceDiffusionAgent", lambda: AgentObject(path="./mettaAgents/AFImportanceDiffusionAgent.metta"))
scheduler.register_agent("WAImportanceDiffusionAgent", lambda: AgentObject(path="./mettaAgents/WAImportanceDiffusionAgent.metta"))
scheduler.register_agent("AFRentCollectionAgent", lambda: AgentObject(path="./mettaAgents/AFRentCollectionAgent.metta"))
scheduler.register_agent("WARentCollectionAgent", lambda: AgentObject(path="./mettaAgents/WARentCollectionAgent.metta"))
scheduler.register_agent("ForgettingAgent", lambda: AgentObject(path="./mettaAgents/ForgettingAgent.metta"))
scheduler.register_agent("HebbianCreationAgent", lambda: AgentObject(path="./mettaAgents/HebbianCreationAgent.metta"))
scheduler.register_agent("HebbianUpdatingAgent", lambda: AgentObject(path="./mettaAgents/HebbianUpdatingAgent.metta"))

# Run all agents in parallel
scheduler.run_all_agents_parallel()


# agent = AgentObject(path="./mettaAgents/AFImportanceDiffusionAgent.metta")
# print("Executing agent manually...")
# agent.run()
# print("Execution finished!")
