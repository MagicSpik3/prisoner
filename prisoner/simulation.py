# prisoner/simulation.py
import random

from .agent import Agent


class Simulation:
    """Manages the population and rules of the Prisoner's Dilemma world."""

    def __init__(self, start_population: int = 100):
        """Initializes the simulation with a starting population."""
        self.payoffs = {
            # Original outcomes
            ("Groom", "Groom"): (3, 3),
            ("Groom", "Ignore"): (-2, 5),
            ("Ignore", "Groom"): (5, -2),
            ("Ignore", "Ignore"): (0, 0),
            
            # New outcomes involving "Decline"
            ("Groom", "Decline"): (0, 0),
            ("Decline", "Groom"): (0, 0),
            ("Ignore", "Decline"): (0, 0),
            ("Decline", "Ignore"): (0, 0),
            ("Decline", "Decline"): (0, 0),
        }
        self.start_population = start_population
        # (The rest of your __init__ method stays the same)
        # Create a mixed population of strategies
        strategies = ["Always_Groom", "Always_Ignore", "Tit_for_Tat", "Random"]
        self.population = [Agent(strategy=random.choice(strategies)) for _ in range(start_population)]


    def _get_move(self, agent: Agent, opponent: Agent) -> str:
        """Determines an agent's move based on its strategy."""
        if agent.strategy == "Random":
            # --- UPDATE THIS LINE ---
            return random.choice(["Groom", "Ignore", "Decline"])
        if agent.strategy == "Always_Groom":
            return "Groom"
        if agent.strategy == "Always_Ignore":
            return "Ignore"
        if agent.strategy == "Tit_for_Tat":
            # Cooperate on the first move, then copy opponent's last move
            if opponent.id not in agent.memory:
                return "Groom"
            return agent.memory[opponent.id][-1] # Return the opponent's last move

    def play_round(self, agent1: Agent, agent2: Agent, move1: str, move2: str):
        """Updates agent energy and memory based on a single interaction."""
        # Update memory for Tit_for_Tat
        agent1.memory.setdefault(agent2.id, []).append(move2)
        agent2.memory.setdefault(agent1.id, []).append(move1)
        
        payoff1, payoff2 = self.payoffs[(move1, move2)]
        agent1.energy += payoff1
        agent2.energy += payoff2

    def run_generation(self):
        """Runs one full generation of the simulation."""
        random.shuffle(self.population)
        for i in range(0, len(self.population) - 1, 2):
            agent1 = self.population[i]
            agent2 = self.population[i+1]
            
            move1 = self._get_move(agent1, agent2)
            move2 = self._get_move(agent2, agent1)
            
            self.play_round(agent1, agent2, move1, move2)

        self._apply_metabolism()
        self._cull_the_weak()
        self.reproduction_and_mutation() # Add this step

    def _apply_metabolism(self, cost: int = 3): # Change this from 1 to 3
        """Subtracts a fixed energy cost from every agent for survival."""
        for agent in self.population:
            agent.energy -= cost

    def _cull_the_weak(self):
        """Removes agents from the population if their energy is <= 0."""
        self.population = [agent for agent in self.population if agent.energy > 0]

    def reproduction_and_mutation(self, mutation_chance: float = 0.05):
        """Selects the fittest agents and creates offspring to replenish the population."""
        num_to_reproduce = self.start_population - len(self.population)
        if num_to_reproduce <= 0:
            return

        # Select the fittest agents to be parents
        fittest_agents = sorted(self.population, key=lambda agent: agent.energy, reverse=True)
        
        new_population = []
        for _ in range(num_to_reproduce):
            parent = random.choice(fittest_agents)
            offspring_strategy = parent.strategy
            
            # Apply mutation
            if random.random() < mutation_chance:
                strategies = ["Always_Groom", "Always_Ignore", "Tit_for_Tat", "Random"]
                offspring_strategy = random.choice(strategies)

            new_population.append(Agent(strategy=offspring_strategy))
        
        self.population.extend(new_population)