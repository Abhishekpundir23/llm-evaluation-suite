def has_uncertainty(text):
    flags = ["not sure", "cannot determine", "unknown"]
    text = text.lower()
    return any(flag in text for flag in flags)
