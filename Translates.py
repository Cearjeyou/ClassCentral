from bs4 import BeautifulSoup
from googletrans import Translator
import os

# Code to translate various HTML files
# Class of the googletrans module to translate the text
translator = Translator(service_urls=['translate.google.com'])
translator.raise_exception = True

# The path where the files are located is enclosed in quotation marks
htmls_dir = "path_files"



# Iteration over each of the HTML files
for html in os.listdir(htmls_dir):
    if html.endswith('.html') and os.path.isfile(os.path.join(htmls_dir, html)):
        # Reading the HTML file
        with open(os.path.join(htmls_dir, html), 'r', encoding='utf-8') as file:
            content = file.read()
        soup = BeautifulSoup(content, "html.parser")
        # Filter to translate tags with text
        tags = soup.body.find_all(lambda tag: tag.name != 'script' and tag.string)
        # Translation of tag content
        try:
            for i in range(len(tags)):
                        print(i, html)
                        print(tags[i].string)
                        texto_translate = translator.translate(str(tags[i].string.strip().replace(".","")), dest='hi').text
                        print(texto_translate)
                        tags[i].string.replace_with(texto_translate) 
        except Exception as e: 
            print("Log", e)
        # Writing of the translated text in HTML
        with open(os.path.join(htmls_dir, html), "w", encoding="utf-8") as file:
            file.write(str(soup))