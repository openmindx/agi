# Autonomous General Intelligence (AGI) Solution Generator

This project leverages the OpenAI API to create a script that interacts with a model named `gpt-4o` to generate an openmind solutions for user-provided prompts. The script runs interactively, continuously accepting user inputs, processing them through the AI model, and returning the solution until a solution is found or the user decides to exit.

## Objective

To showcase a recursivce prompt solutions generator as openmind infinite response openai gpt-4o api call

## prompt

prompt = f"Autonomous general intelligence return solution: {agi_prompt}."


## Script Overview

This Python script allows users to input problem statements, processes these inputs using OpenAI's `gpt-4o` model, and continues to returns the solutions generated by the AI.

### Key Components

**Importing Required Libraries**

```python
import openai
```

This line imports the OpenAI library, which is essential for interacting with OpenAI's API to utilize their AI models

# ADD YOUR API KEY

```python
openai.api_key = ''
```

<a href="https://openai.com/index/openai-api/">openai-api signup</a><br />


### Defining the Function to Get Solutions from the AGI

```python
def get_solution_from_agi(agi_prompt):
    prompt = f"Autonomous general intelligence return solution: {agi_prompt}."

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are openmind the easy action event AGI solution creator."},
            {"role": "user", "content": prompt}
        ]
    )
    solution = response.choices[0].message.content
    return solution
```
    Function Name: get_solution_from_agi

    Parameters:
        agi_prompt: A string that contains the problem statement or question provided by the user.

    Process:
        Prompt Construction:
            The prompt for the AI model is constructed by embedding the user's input into a pre-defined template: "Autonomous general intelligence return solution: {agi_prompt}.".
        API Call:
            openai.chat.completions.create method is used to interact with the OpenAI API. The model parameter specifies the AI model (gpt-4o), and the messages parameter provides the conversation context.
            A system message sets the context for the AI, indicating it is an AGI solution creator. A user message includes the prompt constructed earlier.
        Extracting the Solution:
            The response from the API call is parsed to extract the solution content, which is then returned by the function.

### Main Function for User Interaction

```python
def main():
    while True:
        agi_prompt = input("Enter the problem to solve (or type 'exit' to quit): ")
        if (agi_prompt.lower() == 'exit'):
            break
        solution = get_solution_from_agi(agi_prompt)
        print(f"\nSolution:\n{solution}\n")
```
Function Name: main

Process:

    Infinite Loop:
        The script enters an infinite loop to continually accept user inputs.
    User Prompt:
        The user is prompted to enter a problem statement or question. The input is stored in the variable agi_prompt.
    Exit Condition:
        If the user types 'exit' (case insensitive), the loop breaks, terminating the program.
    Solution Generation and Display:
        The input agi_prompt is passed to the get_solution_from_agi function to generate a solution.
        The returned solution is then printed to the console.

### Script Entry Point

```python
if __name__ == "__main__":
    main()
```
    Purpose:
        This conditional statement ensures that the main function is executed only when the script is run directly, not when imported as a module.

### Usage

    Setup:
        Ensure you have the openai library installed.
        Set your OpenAI API key in the openai.api_key variable.

    Execution:
        Run the script
        
        # bash
        git clone https://github.com/openmindx/agi
        cd agi
        python3 -m venv agi
        source agi/bin/activate
        pip install openai
        python3 agi.py
        
        
        Enter a problem statement or question at the prompt.
        The AI will return an infinite solution iterating over itself which is printed on the console.
        Type 'exit' to terminate the program.


*** This recusive version of openmind AGI is an example of connection to openai API using python. This script will continue indefinately recursively improving upon your problem as a solution response. agi.py is published for further research and expansion into building openmind intoan autonomous general intelligence multi-model integration environment. Use at your own risk and know your API limits. agi.py will not stop until you tell it to stop. For a deep dive into AGI research and development enter <b>agi</b> as the problem to solve.





