def has_reasoning(text):
    keywords = ["because", "therefore", "so", "thus"]
    text = text.lower()
    return any(word in text for word in keywords)
