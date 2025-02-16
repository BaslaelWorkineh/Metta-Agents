import concurrent.futures
import time
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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
            agent = self.agents[agent_id]()
            return agent
        else:
            print(f"Agent {agent_id} not found.")
            return None

    def stimulate(self):
        """ Run all agents once in parallel """
        if not self.agents:
            print("No agents registered!")
            return

        print("\nStarting agent execution cycle...")
        
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for agent_id in self.agents:
                agent = self.create_agent(agent_id)
                if agent:
                    futures.append(executor.submit(agent.run))
            
            # Wait for all agents to complete
            concurrent.futures.wait(futures)
        
        print("Agent execution cycle completed.")
