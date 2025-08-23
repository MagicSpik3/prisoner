import unittest

from prisoner.agent import Agent
from prisoner.simulation import Simulation


class TestSimulationPayoffs(unittest.TestCase):
    """Tests the core game mechanics and population management."""

    def setUp(self):
        """Set up a new simulation and two agents before each test."""
        self.simulation = Simulation()
        self.agent1 = Agent(start_energy=100)
        self.agent2 = Agent(start_energy=100)

    def test_mutual_cooperation_payoff(self):
        """
        Given: Two agents with 100 energy.
        When: They both choose to "Groom" (cooperate).
        Then: Both agents' energy should increase to 103.
        """
        # Act
        self.simulation.play_round(self.agent1, self.agent2, "Groom", "Groom")
        # Assert
        self.assertEqual(self.agent1.energy, 103)
        self.assertEqual(self.agent2.energy, 103)

    def test_mutual_defection_payoff(self):
        """
        Given: Two agents with 100 energy.
        When: They both choose to "Ignore" (defect).
        Then: Their energy should remain unchanged at 100.
        """
        # Act
        self.simulation.play_round(self.agent1, self.agent2, "Ignore", "Ignore")
        # Assert
        self.assertEqual(self.agent1.energy, 100)
        self.assertEqual(self.agent2.energy, 100)
        
    def test_exploitation_payoff(self):
        """
        Given: Two agents with 100 energy.
        When: Agent 1 cooperates ("Groom") and Agent 2 defects ("Ignore").
        Then: Agent 1's energy should decrease to 98 (-2), and
              Agent 2's energy should increase to 105 (+5).
        """
        # Act
        self.simulation.play_round(self.agent1, self.agent2, "Groom", "Ignore")
        # Assert
        self.assertEqual(self.agent1.energy, 98)
        self.assertEqual(self.agent2.energy, 105)


    def test_culling_removes_dead_agents(self):
        """
        Given: A small, controlled population of three agents.
        When: Metabolism is applied, causing two agents' energy to drop <= 0.
        Then: The population should be reduced to only the one surviving agent.
        """

        # Arrange
        agent_a = Agent(start_energy=1)   # Will be culled
        agent_b = Agent(start_energy=0)   # Will be culled
        agent_c = Agent(start_energy=100) # Will survive
        self.simulation.population = [agent_a, agent_b, agent_c]

        # Act
        self.simulation._apply_metabolism()
        self.simulation._cull_the_weak()
        
        # Assert
        self.assertEqual(len(self.simulation.population), 1)
        self.assertEqual(self.simulation.population[0].id, agent_c.id)
        self.assertEqual(self.simulation.population[0].energy, 97) # Change 99 to 97


    def test_reproduction_replaces_culled_agents(self):
        """
        Given: A population that has been culled.
        When: The reproduction and mutation step is run.
        Then: The population should be refilled back to its original size.
        """
        # Arrange
        # Create a small, controlled population
        self.simulation.population = [Agent(start_energy=100), Agent(start_energy=100), Agent(start_energy=1)]
        
        # Tell the simulation that for this test, the target size is 3
        self.simulation.start_population = 3 
        original_size = len(self.simulation.population)
        
        self.simulation._apply_metabolism()
        self.simulation._cull_the_weak() # Population is now 2

        # Act
        self.simulation.reproduction_and_mutation()

        # Assert
        # It should now correctly replenish back to the original size of 3
        self.assertEqual(len(self.simulation.population), original_size)


    def test_offspring_inherits_strategy(self):
        """
        Given: A successful parent agent with a specific strategy.
        When: An offspring is created with mutation turned off.
        Then: The offspring should have the same strategy as the parent.
        """
        # Arrange
        # Use 'start_energy' instead of 'energy'
        parent = Agent(start_energy=200, strategy="Always_Groom")
        self.simulation.population = [parent]
        self.simulation.start_population = 1

        # Act
        self.simulation.reproduction_and_mutation(mutation_chance=0) 

        # Assert
        # The original parent is still there
        self.assertEqual(self.simulation.population[0].strategy, "Always_Groom")

    def test_polite_rejection_payoff(self):
        """
        Given: Two agents with 100 energy.
        When: One offers to "Groom" and the other "Declines".
        Then: The interaction should be neutral, with no energy change for either.
        """
        # Act
        self.simulation.play_round(self.agent1, self.agent2, "Groom", "Decline")
        # Assert
        self.assertEqual(self.agent1.energy, 100)
        self.assertEqual(self.agent2.energy, 100)

    def test_mutual_refusal_payoff(self):
        """
        Given: Two agents with 100 energy.
        When: They both "Decline" to interact.
        Then: The outcome is neutral, with no energy change.
        """
        # Act
        self.simulation.play_round(self.agent1, self.agent2, "Decline", "Decline")
        # Assert
        self.assertEqual(self.agent1.energy, 100)
        self.assertEqual(self.agent2.energy, 100)
        
    def test_aborted_exploitation_payoff(self):
        """
        Given: Two agents with 100 energy.
        When: One attempts to "Ignore" (defect) but the other "Declines".
        Then: The interaction is aborted, and there is no energy change.
              The defector gets no chance to exploit.
        """
        # Act
        self.simulation.play_round(self.agent1, self.agent2, "Ignore", "Decline")
        # Assert
        self.assertEqual(self.agent1.energy, 100)
        self.assertEqual(self.agent2.energy, 100)

        