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

## Setup

Create and activate a virtual environment:

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Linux/Mac:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
```

## Running the Example

```bash
python agent.py
```

## Running Tests

```bash
python -m unittest test_agent.py -v
```

## Features

- Simple input processing
- Memory management
- Easy to extend and customize
