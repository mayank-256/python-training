# import string
# text = """
# Python is great.
# Python is powerful.
# Python is easy to learn.
# """

# def clean_text(text):
#     """clean the punctuation from the text."""
#     translator = str.maketrans('', '', string.punctuation)
#     cleaned_text = text.translate(translator)

#     return cleaned_text


# def clean_text(text):
#     """clean the punctuation from the text."""
#     cleaned_text = ""
#     for char in text:
#         if char not in string.punctuation:
#             cleaned_text += char

#     return cleaned_text