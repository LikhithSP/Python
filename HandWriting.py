
import pywhatkit
text = """
THE KASHMIR FILES

It is a great movie. We should watch
it. It shows the real pain, suffering,
struggle and trauma of Kashmiri.
"""

pywhatkit.text_to_handwriting(text, "sample.jpg")
print('Done')
