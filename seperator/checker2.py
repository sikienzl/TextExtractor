#!/usr/bin/python3

import difflib

MAX_PROCENT = 90
MAX_LINE_COUNT = 200
INPUT_FILE = open("test.txt", "r")
OUTPUT_FILE = open('example3.txt', 'wt')

def checking():
        output_liste = []
        wiederholungen = {}
        liste_wiederholungen = []
        liste_zwischen = []
        unterschied = 0
        count = 0
        count2 = 0
        one_line = ''
        ueberspringen=0
        list_without_empty_lines = delete_empty_lines(INPUT_FILE)
        for one_line in list_without_empty_lines:
            count += 1
            for a in reversed(liste_zwischen):
                count2 += 1
                unterschied = difflib.SequenceMatcher(None, one_line,a)
                prozent=unterschied.ratio()*100
                if(prozent > 90):
                    test = False
                    for i in liste_wiederholungen:
                        unterschied = difflib.SequenceMatcher(None, i,a)
                        prozent=unterschied.ratio()*100
                        if(prozent > 90):
                            test = True
                            break
                    if(test == False):
                        liste_wiederholungen.append(a)
                if(count2 > 200):
                    count2 = 0
                    break
            liste_zwischen.append(one_line)
            if(count > 200):
                break
        output_liste = extract_repeted_lines(list_without_empty_lines, liste_wiederholungen)
        for i in output_liste:
            OUTPUT_FILE.write(i+'\n')
        INPUT_FILE.close()
        OUTPUT_FILE.close()





def extract_repeted_lines(list_without_empty_lines, liste_wiederholungen):
    print("test")
    liste_final = []
    for i in list_without_empty_lines:
        test = False
        for ii in liste_wiederholungen:
            unterschied = difflib.SequenceMatcher(None, i,ii)
            prozent=unterschied.ratio()*100
            if(prozent > 90):
                test = True
        if(test == False):
            liste_final.append(i)
    return liste_final


def delete_empty_lines(input_file):
    list_without_empty_lines = []
    for line in input_file:
            one_line = line.rstrip()
            if(one_line != ''):
                list_without_empty_lines.append(one_line)
    return list_without_empty_lines



checking()
