from bs4 import BeautifulSoup
from googletrans import Translator
from time import sleep

# Code to translate an HTML file
# Class of the googletrans module to translate the text
translator =  Translator(service_urls=['translate.google.com'])
translator.raise_Exception = True

# Reading the HTML file, the path to the file is placed in the quotation marks.
with open("path_HTML", "r", encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
# Filtering of labels containing text
tags = soup.body.find_all(lambda tag: tag.name != 'script' and tag.string)

# Translation of content
try:
    for i in range(len(tags)):
                    print(i)
                    print(tags[i].string)
                    sleep(1.5)
                    texto_translate = translator.translate(str(tags[i].string.strip().replace(".","")), dest='hi').text
                    print(texto_translate)
                    tags[i].string.replace_with(texto_translate) 
except Exception as e: 
    print("Log", e)

# Writing the translated text to the HTML file
with open("path_file", "w", encoding="utf-8") as f:
    f.write(str(soup))
