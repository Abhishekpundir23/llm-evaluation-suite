import json
from collections import defaultdict
import matplotlib.pyplot as plt

# Load results
with open("results/report.json", "r") as file:
    results = json.load(file)

# Prepare data structures
score_summary = defaultdict(lambda: defaultdict(int))

for item in results:
    model = item["model_type"]
    score = item["score"]
    score_summary[model][score] += 1

# Prepare data for plotting
models = list(score_summary.keys())
scores = [0, 1, 2]

data = {
    model: [score_summary[model].get(score, 0) for score in scores]
    for model in models
}

# Plot
x = range(len(scores))
width = 0.35

plt.figure()
for i, model in enumerate(models):
    plt.bar(
        [pos + i * width for pos in x],
        data[model],
        width=width,
        label=model
    )

plt.xlabel("Score (0 = Incorrect, 1 = Partial, 2 = Correct)")
plt.ylabel("Number of Responses")
plt.title("LLM Evaluation Score Distribution by Model")
plt.xticks([pos + width / 2 for pos in x], scores)
plt.legend()

plt.tight_layout()
plt.show()
