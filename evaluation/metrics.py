def exact_match(prediction, ground_truth):
    prediction = prediction.strip().lower()
    ground_truth = ground_truth.strip().lower()
    return prediction == ground_truth
