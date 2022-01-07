import re

def clean_text(text):
    
    # remove header
    pattern = "(From)(.|\n)*(: )(\d)*(\n)"
    replace = ""
    new = re.sub(pattern, replace, text)

    text = re.sub(r'\W+', ' ', text)  # remove non-alphanumeric characters
    # replace numbers with the word 'number'
    text = re.sub(r"\d+", "number", text)
    # don't consider sentenced with less than 3 words (i.e. assumed noise)
    if len(text.strip().split()) < 3:
        return None

    text = text.lower()  # lower case everything
    
    return text.strip() # remove redundant spaces

