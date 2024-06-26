# Autonomous General Intelligence (AGI) Solution Generator

This project leverages the OpenAI API to create a script that interacts with a model named `gpt-4o` to generate an openmind solution for user-provided prompts. The script runs interactively, continuously accepting user inputs, processing them through the AI model, and returning the solution until a solution is found or the user decides to exit.

## Objective

To showcase a recursive prompt solution generator as openmind openai gpt-4o api call using minimal python code.

## prompt

```bash
prompt = f"Autonomous general intelligence return solution: {agi_prompt}."
agi_prompt = input("Enter the problem to solve (or type 'exit' to quit): ")
```


## Script Overview

This Python script allows input <b>problem</b> as statement to openmind processed response using OpenAI's `gpt-4o` model to return <b>solution</a> generated from agi_prompt using the gpt-4o API.

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


### Defining the Function to Get Solutions from openmind Autonomous General Intelligence

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


*** This recursive version of openmind agi_prompt is an example of connection to openai API using python. This script will continue indefinately recursively generating solution from problem. agi.py is published for further research building openmind autonomous general intelligence multi-model integration environment. Use at your own risk and know your API limits. agi.py will not stop until you exit to quit. For a deep dive into <a href="https://github.com/Professor-Codephreak"><b>AGI</b></a> research and development enter <b>agi</b> as the problem to solve.





