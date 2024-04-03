
import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import os
import linecache






def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def generate_prompt():
  counter = 1
  idea = linecache.getline('ideas.txt', counter)
  global prompt
  prompt = f"Write a blog post about {idea}. Write the blog post in markdown format. Make all subtitles H2 and the title H1. "


  
  
  


def get_response():
  GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
  genai.configure(api_key=GOOGLE_API_KEY)
  model = genai.GenerativeModel('gemini-pro')
  response = model.generate_content(prompt)
  to_markdown(response.text)
  print("Response generated succesfully")

