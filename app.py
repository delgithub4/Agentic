from agent import Agent

agent = Agent()

print("=" * 40)
print("      AGENTIC AI")
print("=" * 40)

while True:

    task = input("\nTask: ")

    if task.lower() in ["exit", "quit"]:
        break

    result = agent.run(task)

    print("\nResult:")
    print(result)
