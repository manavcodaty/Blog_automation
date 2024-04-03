import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import os
import linecache

prompt = ''

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def get_response():
  GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
  genai.configure(api_key=GOOGLE_API_KEY)
  model = genai.GenerativeModel('gemini-pro')
  response = model.generate_content(prompt)
  to_markdown(response.text)
  print("Response generated succesfully")