import pyttsx3 ##speech asst.
import PyPDF2  ##pdf reader

##rate setting 
engine = pyttsx3.init()
engine.setProperty("rate", 180)
engine.say("text reader speed can be changed here!!")


#voice settings
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
engine.say("hey buddy! what you like to read today!!")

engine.say("upload the pdf file of the book you want to read!")
book = open('ilets book.pdf', 'rb')#rb to read as binary book

pdfReader = PyPDF2.PdfFileReader(book)
engine.say("let's see total number of pages are")
pages = pdfReader.numPages
print(pages)

'''
engine.say("do u want to continue?")
ui = input("enter the input: ")

if ui=='yes':
    engine.say("from start or any specific page?")
'''

   ## if ui == 'specific page':

selectedpg = pdfReader.getPage(2)# input page = page -1
text = selectedpg.extractText()
engine.say(text)
 
#else
engine.say("okay! Then see you next time bye!")

engine.runAndWait()


