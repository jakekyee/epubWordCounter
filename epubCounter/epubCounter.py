import os
import ebooklib
import bs4
import tabulate
from tabulate import tabulate
from ebooklib import epub
from bs4 import BeautifulSoup


testfile = "C:\\Users\\jgkye\\Desktop\\Books\\Dune by Herbert Frank (z-lib.org).epub"
book = epub.read_epub(testfile)
items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
table = [] #Title,words

directory = input("directory:")
allorone = input("Everything?(Y/N)")
if allorone == "N":
    bookname = input("name:")
    book = epub.read_epub(directory + "\\" + bookname)
    items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
    number = -1
    total = 0
    for i in items:
       number = number+1
       chapter = items[number].get_body_content()
       soup = BeautifulSoup(chapter, 'html.parser')
       parsed = soup.get_text()
       wordchapter = 0
       for i in parsed:
           if i == " ":
              wordchapter = wordchapter + 1
       total = total + wordchapter
    table.append([bookname, total])
else:
    for file in os.listdir(directory):
        book = epub.read_epub(directory + "\\" + file)
        items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
        number = -1
        total = 0
        for i in items:
            number = number+1
            chapter = items[number].get_body_content()
            soup = BeautifulSoup(chapter, 'html.parser')
            parsed = soup.get_text()
            wordchapter = 0
            for i in parsed:
                if i == " ":
                    wordchapter = wordchapter + 1
            total = total + wordchapter
        table.append([file,total])

print(table)
print(tabulate(table))


#print(items[6].get_body_content())
#test = beautifulsoup(items[6].get_body_content(), 'html.parser')
#def countWordsinTotal(items):
#    totalwords = 0
#    for z in items:
#         totalwords = totalwords + countWordsinSection(z)
#         test = BeautifulSoup(items[z], 'html.parser')
#         text = test.getText()
#         print(z)
#         print(test)
#         print(text)
#    return totalwords


#def countWordsinSection(section):
#    words = 0
#    selected = BeautifulSoup(section.get_body_content(), 'html.parser')
#    text = [para.get_text() for para in selected.find_all('p')]
#    for i in text:
#        if i == " ":
#            words = words + 1
#    return words
#directory = input("Directory:")
#allornot = input("Everything? (Y or N)")
#books = [[],[]]

#if allornot == "Y":
#    for file in os.listdir(directory):
#        book = epub.read_epub(directory + file)
#        items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
#        print(countWordsInTotal(items))
#else:
#    filename = input("Filename: ")
#    book = epub.read_epub(directory + "\\" + filename)
#    items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
#    finaltotal = countWordsinTotal(items)
#    print(finaltotal)




