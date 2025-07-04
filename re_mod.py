import re

def clean_text(text):
    # Remove dates
    text = re.sub(r'\b\d{2}[/-]\d{2}[/-]\d{4}\b', '', text)
    text = re.sub(r'\b\d{4}-\d{2}-\d{2}\b', '', text)
    text = re.sub(r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2}, \d{4}\b', '', text, flags=re.IGNORECASE)

    # Remove email addresses
    text = re.sub(r'\S+@\S+(?=\s|$)', '', text)

    # Remove emojis / non-ASCII
    text = re.sub(r'[^\x00-\x7F]', '', text)

    # Replace multiple spaces/newlines
    text = re.sub(r'\s+', ' ', text)

    # Replace repeated punctuation
    text = re.sub(r'([!?.,])\1+', r'\1', text)

    # Fix missing full stop after "Contact me at"
    text = re.sub(r'(Contact me at)\s*(?=[A-Z])', r'\1.', text)

    return text.strip()


# Sample input
text = """
Hey! Contact me at person@example.com.  
The event was on 04/07/2025, and another one on July 4, 2025. 
Visit for more info... 
We also met on 2025-07-04. 
Call me!!!    Or not... 😅😅   
"""

# Cleaned output
cleaned = clean_text(text)
print(cleaned)
