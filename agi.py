import openai

openai.api_key = ''

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

def main():
    while True:
        agi_prompt = input("Enter the problem to solve (or type 'exit' to quit): ")
        if agi_prompt.lower() == 'exit':
            break
        solution = get_solution_from_agi(agi_prompt)
        print(f"\nSolution:\n{solution}\n")

if __name__ == "__main__":
    main()
