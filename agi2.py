# openmind (c) Gregory L. Magnusson 2024 MIT license
import openai
import os
import argparse # Added for command-line arguments
from dotenv import load_dotenv
from openai import OpenAIError # Import specific OpenAI errors

# --- Configuration ---
# load environment variables # improve this logic consider config files or explicit args
load_dotenv()
# Get the API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

# api key validation # improve this logic guide user on how to set env var
if not api_key:
    raise ValueError(
        "OpenAI API key not found. "
        "Set the OPENAI_API_KEY environment variable (e.g., in a .env file)."
        )
openai.api_key = api_key

# model selection # improve this logic make configurable via args
MODEL_NAME = "gpt-4o"
# system persona # improve this logic make configurable via args
SYSTEM_PROMPT = "You are openmind the easy action event AGI solution creator."


def get_solution_from_agi(agi_prompt: str) -> str:
    """
    Sends a problem prompt to the OpenAI API and returns the solution.

    Args:
        agi_prompt (str): The problem description provided by the user.

    Returns:
        str: The solution text from the AI, or an error message.
    """
    # prompt construction # improve this logic add options for different prompt templates
    prompt = f"Autonomous general intelligence return solution: {agi_prompt}."

    try:
        # api interaction # improve this logic add configurable timeout retry mechanism
        response = openai.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ]
            # consider adding parameters like temperature max_tokens etc # config options
        )
        # solution extraction # improve this logic add check for content field existence
        if response.choices and response.choices[0].message.content:
            solution = response.choices[0].message.content
            return solution.strip() # Remove leading/trailing whitespace
        else:
            # handle empty response case # improve this logic log the full response object
            return "Error: Received no valid response content from the API."

    # error handling block # improve this logic provide more user friendly error messages log details
    except OpenAIError as e:
        error_message = f"\nAn API error occurred: {e}"
        print(error_message)
        # Consider specific handling for authentication vs rate limit vs server errors
        return f"Error: Could not get solution due to API error ({type(e).__name__}). Check connection, key, limits."
    except Exception as e:
        error_message = f"\nAn unexpected error occurred: {e}"
        print(error_message)
        return f"Error: Could not get solution due to an unexpected error ({type(e).__name__})."

def run_interaction(counter: Optional[int] = None):
    """Handles a single prompt-solution interaction cycle."""
    prefix = f"[{counter}] " if counter is not None else ""
    try:
        # user input logic # improve this logic add support for multi line input?
        agi_prompt = input(f"\n{prefix}Enter the problem to solve (or type 'exit' to quit): ")
        if agi_prompt.lower() == 'exit':
            return False # Signal to exit loop
        if not agi_prompt.strip(): # handle empty input gracefully
            print("Please enter a problem description.")
            return True # Continue loop

        print("\nThinking...") # user feedback
        solution = get_solution_from_agi(agi_prompt)
        # output formatting # improve this logic allow different output formats e g json
        print(f"\nSolution:\n{'-'*20}\n{solution}\n{'-'*20}")

    except EOFError: # handle end of input if piped
        print("\nInput stream ended.")
        return False # Signal to exit loop
    return True # Continue loop

def main():
    """
    Main loop to get user input and display solutions from the AI,
    optionally running for a fixed number of loops.
    """
    # command line argument parsing # improve this logic add args for model system prompt etc
    parser = argparse.ArgumentParser(description="OpenMind AGI Solution Interface")
    parser.add_argument(
        "-n", "--num_loops", type=int, default=0,
        help="Number of interaction loops to run. Default 0 runs indefinitely."
    )
    args = parser.parse_args()

    print("--- OpenMind AGI Solution Interface ---")
    print(f"(Using Model: {MODEL_NAME})")

    try:
        if args.num_loops > 0:
            # fixed number of loops execution path
            print(f"Running for {args.num_loops} interaction(s).")
            for i in range(1, args.num_loops + 1):
                if not run_interaction(counter=i): # Pass counter
                    break # Exit if run_interaction signals exit
            print(f"\nFinished {args.num_loops} interaction(s).")
        else:
            # indefinite loop execution path
            print("Running indefinitely. Type 'exit' or press Ctrl+C to quit.")
            while True:
                 if not run_interaction():
                     break # Exit if run_interaction signals exit

    except KeyboardInterrupt: # handle Ctrl C gracefully
         print("\nExiting OpenMind due to user interruption.")
    finally:
        # cleanup tasks if any needed # placeholder for potential cleanup
        print("OpenMind session ended.")


if __name__ == "__main__":
    main()
