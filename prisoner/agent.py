# prisoner/agent.py
import uuid


class Agent:
    """Represents an individual agent in the Prisoner's Dilemma simulation.

    Each agent has a unique identifier, an energy level that acts as its
    fitness score, and a memory of past interactions.

    Attributes:
        id (UUID): A universally unique identifier for the agent.
        energy (int): The agent's current life force or score.
        memory (dict): A dictionary to store history of interactions with
                       other agents, mapping their ID to a list of outcomes.
    """
    def __init__(self, start_energy: int = 100, strategy: str = "Random"):
        """Initializes an Agent with a starting energy level and a strategy."""
        self.id = uuid.uuid4()
        self.energy = start_energy # Keep this line
        self.memory = {}
        self.strategy = strategy