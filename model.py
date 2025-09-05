from transformers import pipeline

fill_mask = pipeline("fill-mask", model="bert-base-uncased")
print(fill_mask("your name is [MASK].")[0]['sequence'])
