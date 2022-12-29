#!/bin/bash

# Author: Kris Armstrong
# Description: 
"""
This script is used to generate a mp3 file from a pdf file.
input file PDF Document
output file mp3 file
"""

import PyPDF2
import pyttsx3
from gtts import gTTS


def google_text_to_speach(g_clean_text, outputfile):
    """
    This function is used to convert text to speach.
    """
    print('\n','Creating MP3 file')
    
    # Set the language to English
    # tts.setLanguage('en')
    tts = gTTS(g_clean_text, lang='en')
    print('Writing file: ', outputfile, '\n')
    tts.save(outputfile)
    
    '''
    # Set the language to German
    tts.setLanguage('de')

    # Set the language to Spanish
    tts.setLanguage('es')

    # Set the language to Portuguese
    tts.setLanguage('pt')

    # Set the language to Italian
    tts.setLanguage('it')
    '''   
    
def pyttsx2_text_to_speach(p_clean_text, outputfile):
    """
    This function is used to convert text to speach.
    """
    print('PyTtsx2')
    engine = pyttsx3.init()
              
    engine.save_to_file(p_clean_text, outputfile)
    engine.runAndWait()
    engine.stop()


def main():
    # Main function

    while True:
        filename = input("Enter the pdf file you want to convert to MP3: ")
        inputfile = open(filename, 'rb')
        outfile = filename.strip('.pdf' or 'PDF') + '.mp3'
        
        try:            
            print('\n','Please wait while reading PDF', filename, '\n')
            pdfreader = PyPDF2.PdfReader(inputfile)
 
            for i in range(len(pdfreader.pages)):
                text = pdfreader.pages[i].extract_text()
                clean_text = text.replace('\n', '')  
            break        
        except Exception as e:
            print(e)
            continue
        break
    
    while True:
        optionkey = input('Press (G) for Google or Press (P) for for pyttsx2: ')
        if optionkey == 'G' or 'g':
            print('\n',"You choose Google be sure you have a internet connection")
            google_text_to_speach(clean_text, outfile)
        elif optionkey == 'P' or 'p':
            print('\n',"You choose pyttsx2 internet is not required")
            pyttsx2_text_to_speach(clean_text, outfile)
        else:
            print('\n',"Invalid option")
            continue
        break
    
if __name__ == '__main__':
    main()
