import json
from collections import defaultdict

# Load results
with open("results/report.json", "r") as file:
    results = json.load(file)

# Data structures
summary = defaultdict(lambda: defaultdict(list))

# Organize scores by task and model
for item in results:
    task = item["task"]
    model = item["model_type"]
    score = item["score"]

    summary[task][model].append(score)

# Print task-wise summary
print("\nTASK-WISE PERFORMANCE SUMMARY\n")

for task, models in summary.items():
    print(f"Task: {task}")

    for model, scores in models.items():
        avg_score = sum(scores) / len(scores)
        correct = scores.count(2)
        partial = scores.count(1)
        incorrect = scores.count(0)

        print(f"  Model: {model}")
        print(f"    Average score : {avg_score:.2f}")
        print(f"    Correct (2)   : {correct}")
        print(f"    Partial (1)   : {partial}")
        print(f"    Incorrect (0): {incorrect}")

    print("-" * 40)
