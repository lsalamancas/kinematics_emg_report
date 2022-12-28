import os
import PyPDF2

def find_events(folder):
    pdf_path = os.sep.join([path, folder,fr'{file_name}.pdf'])
    with open(pdf_path, mode='rb') as f:
        pdfdoc = PyPDF2.PdfFileReader(f)
        page_one = pdfdoc.getPage(0)
        text = page_one.extractText()
        print(text)
        text = text.split()
        c = False
        indexes = []
        print(text)
        for index, word in enumerate(text):
            print(word)
            if (word == "APOYO") & (c):
                indexes.append(index)
            if (word == "DE") | (word == "DURACIÓN"):
                c = True
            else: 
                c = False

        return text[indexes[0] + 2], text[indexes[0] + 4] , text[indexes[1] + 2], text[indexes[1] + 4] 
