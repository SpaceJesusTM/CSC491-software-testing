# from tokenizer import tokenize
# from sentiment import score

# def analyze(text: str) -> dict:
#     """
#     Integrates tokenizer + sentiment scorer.
#     Returns {'words': [...], 'score': int, 'label': 'pos'|'neg'|'neu'}
#     """
    
#     words = tokenize(text)
#     s = score(words)
#     if s > 0: label = "pos"
#     elif s < 0: label = "neg"
#     else: label = "neu"
#     return {"words": words, "score": s, "label": label}

from tokenizer import tokenize
from sentiment import score

def analyze(text: str) -> dict:
    """
    Integrates tokenizer + sentiment scorer.
    Returns {'words': [...], 'score': int, 'label': 'pos'|'neg'|'neu'}
    """
    if not isinstance(text, str):
        raise TypeError("analyze() requires a string input")

    words = tokenize(text)
    normalized_words = [w.lower() for w in words]
    s = score(normalized_words)
    if s > 0: label = "pos"
    elif s < 0: label = "neg"
    else: label = "neu"
    return {"words": words, "score": s, "label": label}
