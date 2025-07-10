import spacy

nlp = spacy.load("en_core_web_sm")

text = "Apple is looking at buying U.K. startup for $1 billion. The deal was finalized in September, and everyone was excited about the acquisition."

doc = nlp(text)

tokens = [token.text for token in doc]
print("Tokens:")
print(tokens)


tokens_no_stop = [token.text for token in doc if not token.is_stop]
print("\nTokens without stopwords:")
print(tokens_no_stop)


print("\nLemmatization:")
for token in doc:
    print(f"{token.text:15} ➜ {token.lemma_}")
