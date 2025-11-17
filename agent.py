"""
Sara - A simple agent implementation
"""


class Agent:
    """A basic agent class"""
    
    def __init__(self, name="Sara"):
        """
        Initialize the agent
        
        Args:
            name (str): The name of the agent
        """
        self.name = name
        self.memory = []
    
    def process(self, input_text):
        """
        Process input and generate a response
        
        Args:
            input_text (str): The input to process
            
        Returns:
            str: The agent's response
        """
        self.memory.append(input_text)
        return f"{self.name}: Processed '{input_text}'"
    
    def get_memory(self):
        """
        Get the agent's memory
        
        Returns:
            list: List of processed inputs
        """
        return self.memory.copy()
    
    def clear_memory(self):
        """Clear the agent's memory"""
        self.memory.clear()


def main():
    """Example usage of the agent"""
    agent = Agent("Sara")
    print(f"Agent '{agent.name}' initialized")
    
    # Process some inputs
    response1 = agent.process("Hello")
    print(response1)
    
    response2 = agent.process("How are you?")
    print(response2)
    
    # Show memory
    print(f"\nMemory: {agent.get_memory()}")


if __name__ == "__main__":
    main()
