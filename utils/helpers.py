def extract_digits(text):
    digits = "".join(c for c in text if c.isdigit())
    return int(digits) if digits else 0

def extract_digits_from_elements(elements):
    return [extract_digits(el.text) for el in elements]