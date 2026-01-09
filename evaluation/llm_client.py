from transformers import pipeline

# Load models once (important)
baseline_model = pipeline(
    "text-generation",
    model="distilgpt2",
    max_new_tokens=100
)

instruction_model = pipeline(
    "text2text-generation",
    model="google/flan-t5-small",
    max_new_tokens=100
)


def query_llm(prompt, model_type="baseline"):
    if model_type == "baseline":
        output = baseline_model(prompt)
        return output[0]["generated_text"]

    if model_type == "instruction":
        output = instruction_model(prompt)
        return output[0]["generated_text"]

    return "ERROR: Unknown model type"
