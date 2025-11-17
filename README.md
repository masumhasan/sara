# sara

A simple agent implementation.

## Overview

Sara is a basic agent that can process inputs and maintain memory of interactions.

## Usage

```python
from agent import Agent

# Create an agent instance
agent = Agent("Sara")

# Process inputs
response = agent.process("Hello")
print(response)  # Output: Sara: Processed 'Hello'

# Check memory
memory = agent.get_memory()
print(memory)  # Output: ['Hello']
```

## Running the Example

```bash
python agent.py
```

## Features

- Simple input processing
- Memory management
- Easy to extend and customize
