from dotenv import load_dotenv
from mem0 import MemoryClient
import logging
import json
import uuid

load_dotenv()

def test_single_insertion(user_id: str, content: str):
    """
    Tests adding a single piece of memory and verifies it was inserted.
    """
    print(f"\n--- Testing memory insertion for user: {user_id} ---")
    mem0 = MemoryClient()
    
    # 1. Add a unique memory
    messages = [{"role": "user", "content": content}]
    print(f"Attempting to add memory: '{content}'")
    try:
        mem0.add(messages, user_id=user_id)
        print("Memory added successfully via API.")
    except Exception as e:
        print(f"Error adding memory: {e}")
        return

    # 2. Verify the memory was inserted
    print("Verifying insertion...")
    try:
        all_memories = mem0.get_all(user_id=user_id)
        if not all_memories:
            print("Verification failed: No memories found for user.")
            return

        # Check if a memory containing the unique content exists
        found = any(content in mem.get("memory", "") for mem in all_memories)

        if found:
            print("Verification successful: The new memory was found.")
        else:
            print("Verification failed: The new memory was not found in the user's history.")
        
        print("Current memories for user:")
        print(json.dumps(all_memories, indent=2))

    except Exception as e:
        print(f"Error retrieving memories for verification: {e}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    # Generate unique content for this test run
    masum_unique_fact = f"Masum's secret code is {uuid.uuid4()}."
    liza_unique_fact = f"Liza's favorite flower is the sunflower."

    test_single_insertion(user_id="Masum", content=masum_unique_fact)
    test_single_insertion(user_id="Liza", content=liza_unique_fact)
