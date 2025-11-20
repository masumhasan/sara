from dotenv import load_dotenv
from mem0 import MemoryClient
import logging
import json


load_dotenv()
user_name = 'Masum'
mem0 = MemoryClient()

def add_memory():
    
    # Memory for Masum
    masum_messages = [
        {
            "role": "user",
            "content": "My favorite movie is Interstellar."
        },
        {
            "role": "assistant",
            "content": "That's a great choice, a modern sci-fi classic."
        }
    ]
    mem0.add(masum_messages, user_id="Masum")
    print("Added memory for Masum.")

    # Memory for Liza
    liza_messages = [
        {
            "role": "user",
            "content": "I enjoy painting in my free time."
        },
        {
            "role": "assistant",
            "content": "That's a wonderful hobby! What do you like to paint?"
        }
    ]
    mem0.add(liza_messages, user_id="Liza")
    print("Added memory for Liza.")


def get_memory_by_query(user_name: str):
    mem0 = MemoryClient()
    query = f"What are {user_name}'s preferences and hobbies?"
    results = mem0.search(query, user_id=user_name)

    if not results:
        print(f"No memories found for {user_name} with query: {query}")
        return "[]"

    memories = [
            {
                "memory": result["memory"],
                "updated_at": result["updated_at"]
            }
            for result in results
        ]
    memories_str = json.dumps(memories, indent=2)
    print(f"Memories for {user_name}: {memories_str}")
    return memories_str


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    add_memory()
    print("\n--- Getting memories for Masum ---")
    get_memory_by_query(user_name="Masum")
    print("\n--- Getting memories for Liza ---")
    get_memory_by_query(user_name="Liza")
