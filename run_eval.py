import json

from evaluation.metrics import exact_match, score_response
from evaluation.reasoning_checks import has_reasoning
from evaluation.hallucination_checks import has_uncertainty
from evaluation.llm_client import query_llm


def load_jsonl(path):
    with open(path, "r") as file:
        return [json.loads(line) for line in file]


# Load data
prompts = load_jsonl("data/prompts.jsonl")
answers = {
    item["id"]: item["answer"]
    for item in load_jsonl("data/ground_truth.jsonl")
}

results = []

# Run evaluation
for item in prompts:
    for model_type in ["baseline", "instruction"]:
        model_output = query_llm(item["prompt"], model_type)

        score, category = score_response(
            model_output,
            answers[item["id"]],
            has_reasoning(model_output),
            has_uncertainty(model_output)
        )

        result = {
            "id": item["id"],
            "task": item["task"],
            "model_type": model_type,
            "prompt": item["prompt"],
            "model_output": model_output,
            "score": score,
            "category": category
        }

        results.append(result)

# Save results
with open("results/report.json", "w") as file:
    json.dump(results, file, indent=2)

print("Evaluation completed.")
