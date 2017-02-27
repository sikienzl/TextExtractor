#!/usr/bin/python3

"""
checker.py: 
Checks the files for repetitions and writes to a 
file without the repetitions
"""

__author__      = "Mark Unger, Siegfried Kienzle"

import sys
import getopt
import difflib
import loggingModule

MAX_PROCENT = 90
MAX_LINE_COUNT = 400
MAX_COUNT_REPETITION = 5


def main():
    argv = sys.argv[1:]
    liste = []
    liste_wiederholungen = []
    output_liste = []
    if(len(sys.argv) == 1):
        loggingModule.logger2.info("Please put a correct parameter!\n")
        loggingModule.logger2.info(help())
    try:
        opts, args = getopt.getopt(
            argv, "rhvi:o:", ['help', 'input=', 'output='])
    except getopt.GetoptError as e:
        loggingModule.logger2.info("Please put a correct parameter!\n")
    verbose = False
    repetitions = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o == "-r":
            repetitions = True
        elif o in ("-h", "--help"):
            loggingModule.logger2.info(help())
        elif o in ("-i", "--input"):
            liste = getListWithoutEmptyLines(a)
            if liste:
                liste_wiederholungen = get_wiederholung_list(liste)
                output_liste = extract_repeated_lines(liste, liste_wiederholungen)
            if(repetitions):
                output_liste.append("\n\nWiederholungen:")
                for a in liste_wiederholungen:
                    output_liste.append(a)
        elif o in ("-o", "--output"):
            write_into_file(a, output_liste)
    if verbose:
        if liste is not None:
            for zeile in output_liste:
                loggingModule.logger2.info(zeile)
        else:
            loggingModule.logger2.info(help())

'''
Deletes empty line in the string
'''
def getListWithoutEmptyLines(file):
    try:
        INPUT_FILE = open(file, "r")
        list_without_empty_lines = []
        list_without_empty_lines = delete_empty_lines(INPUT_FILE)
        INPUT_FILE.close()
        return list_without_empty_lines
    except Exception as e:
        loggingModule.logger2.error("Error: " + str(e))

'''
shows and compares with the repetitions, and if its a repetitions it is deleted
'''
def extract_repeated_lines(list_without_empty_lines, liste_wiederholungen):
    liste_final = []
    for i in list_without_empty_lines:
        is_repetition = False
        for ii in liste_wiederholungen:
            prozent = difference(i, ii) #call difference function
            if(prozent > MAX_PROCENT):
                is_repetition = True
        if(is_repetition is False):
            liste_final.append(i)
    return liste_final


'''
deletes empty lines in the string
'''
def delete_empty_lines(input_file):
    list_without_empty_lines = []
    for line in input_file:
        one_line = line.rstrip()
        one_line = one_line.strip('\n\r\t')
        if(one_line != ''):
            list_without_empty_lines.append(one_line)
    return list_without_empty_lines


'''
returns all repetitions
'''
def get_wiederholung_list(list_without_empty_lines):
    #only run wenn list is not empty
    if list_without_empty_lines:
        
        liste_zwischen = []
        liste_wiederholungen = []
        dictionary_wiederholungen = {}
        count_liste_zwischen = 0
        count_empty_list = 0

        for one_line in list_without_empty_lines:
            count_empty_list += 1

            for a in reversed(liste_zwischen):
                count_liste_zwischen += 1
                prozent = difference(one_line, a)#call difference function

                if(prozent > MAX_PROCENT):
                # if the line on the whole document and the line in liste_zwischen
                # are similar
                    is_repetition_inside_wiederholungen = False
                    # check if the line or a similar line is already inside
                    # dictionary_wiederholungen
                    for key, value in dictionary_wiederholungen.items():
                        prozent = difference(key, a) #call difference function
                        if(prozent > MAX_PROCENT):
                            dictionary_wiederholungen[
                                key] += 1  # key exist and
                                           # is similar than increment
                            if(dictionary_wiederholungen[key] ==
                               MAX_COUNT_REPETITION):
                                liste_wiederholungen.append(a)
                            is_repetition_inside_wiederholungen = True
                            break

                    if(is_repetition_inside_wiederholungen is False):
                        dictionary_wiederholungen[a] = 0

                if(count_liste_zwischen > MAX_LINE_COUNT):
                    count_liste_zwischen = 0
                    break
            liste_zwischen.append(one_line)

            if(count_empty_list > MAX_LINE_COUNT):
                break

        return liste_wiederholungen

def difference(string1, string2):
    difference = difflib.SequenceMatcher(None, string1, string2)
    prozent = difference.ratio() * 100
    return prozent
'''
writes the builded string into a file 
'''
def write_into_file(out_file, liste):
    if liste:
        try:
            OUTPUT_FILE = open(out_file, "w+")
            for i in liste:
                OUTPUT_FILE.write(i)
            OUTPUT_FILE.close()
        except:
            loggingModule.logger2.error("Error: when trying to write to file")

'''
returns the help text
'''
def help():
    return("arguments\n" +
           "-h,                     --help                        " +
           "show help message and exit\n" +
           "-i [path to file]       --input [path to file]        " +
           "to run the program\n" +
           "-o [path to outputfile] --output [path to outputfile] " +
           "to extract text into file\n" +
           "-r                                                    " +
           "add repetitions at the end\n" +
           "-v                                                    " +
           "verbose-Mode")

if __name__ == "__main__":
    main()
