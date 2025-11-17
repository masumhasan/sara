"""
Tests for the Sara agent
"""
import unittest
from agent import Agent


class TestAgent(unittest.TestCase):
    """Test cases for the Agent class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.agent = Agent("TestAgent")
    
    def test_agent_initialization(self):
        """Test that agent initializes correctly"""
        self.assertEqual(self.agent.name, "TestAgent")
        self.assertEqual(self.agent.memory, [])
    
    def test_agent_default_name(self):
        """Test agent with default name"""
        agent = Agent()
        self.assertEqual(agent.name, "Sara")
    
    def test_process_input(self):
        """Test processing input"""
        response = self.agent.process("Hello")
        self.assertEqual(response, "TestAgent: Processed 'Hello'")
    
    def test_memory_storage(self):
        """Test that inputs are stored in memory"""
        self.agent.process("First input")
        self.agent.process("Second input")
        memory = self.agent.get_memory()
        self.assertEqual(len(memory), 2)
        self.assertEqual(memory[0], "First input")
        self.assertEqual(memory[1], "Second input")
    
    def test_clear_memory(self):
        """Test clearing memory"""
        self.agent.process("Test input")
        self.agent.clear_memory()
        self.assertEqual(self.agent.get_memory(), [])
    
    def test_memory_copy(self):
        """Test that get_memory returns a copy"""
        self.agent.process("Test")
        memory = self.agent.get_memory()
        memory.append("Modified")
        agent_memory = self.agent.get_memory()
        self.assertEqual(len(agent_memory), 1)


if __name__ == "__main__":
    unittest.main()
