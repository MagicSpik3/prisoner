import unittest

from prisoner.agent import Agent  # Import the class we want to test


class TestAgentInitialization(unittest.TestCase):
    """Tests the creation and default state of the Agent class."""

    def test_agent_is_created_with_correct_defaults(self):
        """
        Given: No specific inputs are required.
        When: A new Agent is initialized with a starting energy.
        Then: The agent should have the correct energy, an empty memory,
              and a non-null unique ID.
        """
        # Arrange
        start_energy = 100

        # Act
        agent = Agent(start_energy=start_energy)

        # Assert
        self.assertEqual(agent.energy, start_energy)
        self.assertEqual(agent.memory, {})
        self.assertIsNotNone(agent.id)