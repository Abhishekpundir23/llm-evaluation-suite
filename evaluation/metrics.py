def exact_match(prediction, ground_truth):
    return prediction.strip().lower() == ground_truth.strip().lower()


def score_response(prediction, ground_truth, has_reasoning, has_uncertainty):
    if has_uncertainty:
        return 0, "uncertain_or_weak"

    if exact_match(prediction, ground_truth):
        if has_reasoning:
            return 2, "correct"
        else:
            return 1, "correct_but_no_reasoning"

    return 0, "incorrect"
