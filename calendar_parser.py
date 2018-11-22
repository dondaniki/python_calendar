#!/usr/bin/env python

import PyPDF2 

#variables globales


file_name='/home/daniki/Documents/devs/python_calendar/python_calendar/resources/demo.pdf'
w_text=""
script_version='b-0.0.1-r0-d0'


# funciones auxiliares
def extraer_texto():
	# creating a pdf file object 
	pdfFile = open('demo2.pdf', 'rb') 
	txtFile = open('demo2.txt', 'wb') 
	  
	# creating a pdf reader object 
	pdfReader = PyPDF2.PdfFileReader(pdfFile) 
	
	print(pdfReader.isEncrypted) 
	
	# printing number of pages in pdf file 
	print 'No. paginas ' , pdfReader.numPages 
	 
	for page in range(0, (pdfReader.numPages -1)):		  
		# creating a page object 
		pageObj = pdfReader.getPage(page) 
		  
		# extracting text from page 
		w_text = pageObj.extractText()
		txtFile.write(w_text.encode('utf-8'))
		
		#print(w_text) 
	  
	# closing the pdf file object 
	pdfFile.close()
	txtFile.close()
	
#def limpiar_texto():
#	pdfFile = open('demo2.txt', 'rb') 
#	txtFile = open('demo.txt', 'wb') 



# funciones programa principal

def do_job():
	print("do_job")

	
def do_post_job():
	print("do_post_job")
	
def do_pre_job():
	print("do_pre_job")
	
	# descargar_pdf
	extraer_texto()
	
	#limpiar_texto()





# programa principal

def main():

	do_pre_job()
	
	do_job()
	
	do_post_job()
	


# llamada a la funcion principal

main() 