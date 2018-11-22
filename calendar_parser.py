#!/usr/bin/env python

import PyPDF2 

#variables globales


file_name='/home/daniki/Documents/devs/python_calendar/python_calendar/resources/demo.pdf'
w_text=""


# funciones auxiliares
def extraer_texto():
	# creating a pdf file object 
	pdfFileObj = open(file_name, 'rb') 
	  
	# creating a pdf reader object 
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
	  
	# printing number of pages in pdf file 
	print(pdfReader.numPages) 
	  
	# creating a page object 
	pageObj = pdfReader.getPage(0) 
	  
	# extracting text from page 
	w_text = pageObj.extractText()
	print(w_text) 
	  
	# closing the pdf file object 
	pdfFileObj.close()

# funciones programa principal

def do_job():
	print("do_job")

	
def do_post_job():
	print("do_post_job")
	
def do_pre_job():
	print("do_pre_job")
	
	# descargar_pdf
	extraer_texto()





# programa principal

def main():

	do_pre_job()
	
	do_job()
	
	do_post_job()
	


# llamada a la funcion principal

main() 