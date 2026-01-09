import json
from evaluation.metrics import exact_match
from evaluation.reasoning_checks import has_reasoning
from evaluation.hallucination_checks import has_uncertainty


def load_jsonl(path):
    with open(path, "r") as file:
        return [json.loads(line) for line in file]


prompts = load_jsonl("data/prompts.jsonl")
answers = {item["id"]: item["answer"] for item in load_jsonl("data/ground_truth.jsonl")}

results = []

for item in prompts:
    # TEMPORARY model output (we'll replace later)
    model_output = "40 km/h"

    result = {
        "id": item["id"],
        "exact_match": exact_match(model_output, answers[item["id"]]),
        "has_reasoning": has_reasoning(model_output),
        "uncertainty_flag": has_uncertainty(model_output)
    }

    results.append(result)

with open("results/report.json", "w") as file:
    json.dump(results, file, indent=2)

print("Evaluation completed.")
