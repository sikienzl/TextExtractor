#!/usr/bin/python3

import sys
import getopt
import difflib

MAX_PROCENT = 90
MAX_LINE_COUNT = 200
#INPUT_FILE = open("test.txt", "r")
#OUTPUT_FILE = open('example3.txt', 'wt')

def main():
        argv = sys.argv[1:]
        liste = []
        liste_wiederholungen = []
        output_liste = []
        if(len(sys.argv) == 1):
            print("Please put a correct parameter!\n")
            print(help())
        try:
            opts, args = getopt.getopt(argv, "hvi:o:", ['help', 'input=', 'output='])
        except getopt.GetoptError as e:
            print("Please put a correct parameter!\n")
        verbose = False
        for o, a in opts:
            if o == "-v":
                verbose = True
            elif o in ("-h", "--help"):
                print(help())
            elif o in ("-i", "--input"):
                liste = getListWithoutEmptyLines(a)
                liste_wiederholungen = get_wiederholung_list(liste)
                output_liste = extract_repeted_lines(liste, liste_wiederholungen)
            elif o in ("-o", "--output"):
                writeIntoFile(a, output_liste)
        if verbose == True:
            if liste != None:
               for zeile in output_liste:
                   print(zeile)
            else:
               print(help())

def getListWithoutEmptyLines(file):
    INPUT_FILE = open(file, "r")
    list_without_empty_lines = []
    list_without_empty_lines = delete_empty_lines(INPUT_FILE)
    INPUT_FILE.close()
    return list_without_empty_lines

def extract_repeted_lines(list_without_empty_lines, liste_wiederholungen):
    liste_final = []
    for i in list_without_empty_lines:
        is_repetition = False
        for ii in liste_wiederholungen:
            unterschied = difflib.SequenceMatcher(None, i,ii)
            prozent=unterschied.ratio()*100
            if(prozent > MAX_PROCENT):
                is_repetition = True
        if(is_repetition == False):
            liste_final.append(i)
    return liste_final


def delete_empty_lines(input_file):
    list_without_empty_lines = []
    for line in input_file:
            one_line = line.rstrip()
            if(one_line != ''):
                list_without_empty_lines.append(one_line)
    return list_without_empty_lines

def get_wiederholung_list(list_without_empty_lines):
    liste_zwischen = []
    liste_wiederholungen = []
    count_liste_zwischen = 0
    count_empty_list = 0
    for one_line in list_without_empty_lines:
        count_empty_list += 1
        for a in reversed(liste_zwischen):
            count_liste_zwischen += 1
            unterschied = difflib.SequenceMatcher(None, one_line,a)
            prozent=unterschied.ratio()*100
            if(prozent > MAX_PROCENT):
                is_repetition = False
                for i in liste_wiederholungen:
                    unterschied = difflib.SequenceMatcher(None, i,a)
                    prozent=unterschied.ratio()*100
                    if(prozent > MAX_PROCENT):
                        is_repetition = True
                        break
                if(is_repetition == False):
                    liste_wiederholungen.append(a)
            if(count_liste_zwischen > MAX_LINE_COUNT):
                count_liste_zwischen = 0
                break
        liste_zwischen.append(one_line)
        if(count_empty_list > MAX_LINE_COUNT):
            break
    return liste_wiederholungen
	
def writeIntoFile(out_file, liste):
        OUTPUT_FILE = open(out_file, "wt")
        for i in liste:
            OUTPUT_FILE.write(i+'\n')
        OUTPUT_FILE.close()

def help():
    return("arguments\n" +
       "-h,                     --help                        show help message and exit\n" +
       "-i [path to file]       --input [path to file]        to run the program\n" +
       "-o [path to outputfile] --output [path to outputfile] to extract text into file\n" +
       "-v                                                    verbose-Mode")

if __name__ == "__main__":
    main()
