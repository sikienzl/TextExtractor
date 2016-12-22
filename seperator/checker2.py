#!/usr/bin/python3

import difflib

MAX_PROCENT = 90
MAX_LINE_COUNT = 200
INPUT_FILE = open("test.txt", "r")
OUTPUT_FILE = open('example3.txt', 'wt')

def checking():
        liste_wiederholungen = []
        liste_zwischen = []
        count_empty_list = 0
        count_liste_zwischen = 0
        list_without_empty_lines = delete_empty_lines(INPUT_FILE)
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
        output_liste = extract_repeted_lines(list_without_empty_lines, liste_wiederholungen)
        for i in output_liste:
            OUTPUT_FILE.write(i+'\n')
        INPUT_FILE.close()
        OUTPUT_FILE.close()





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



checking()
