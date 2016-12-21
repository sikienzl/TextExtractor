#!/usr/bin/python3

import difflib

def checking():
        input_file = open("test.txt", "r")
        output_file = open('example3.txt', 'wt')
        liste = []
        dictionary = {}
        listeFinal = []
        unterschied = 0
        count = 0
        one_line = ''
        ueberspringen=0
        for line in input_file:
                one_line = line.rstrip()
                if(one_line != ''):
                    for i in reversed(liste):
                        unterschied = difflib.SequenceMatcher(None, i,one_line)
                        prozent=unterschied.ratio()*100
                        if(prozent > 80):
                            ueberspringen=1
                            continue
                        count += 1
                        if(count > 100):
                            count = 0
                            break
                    if(ueberspringen == 0):
                        liste.append(one_line)
                    else:
                        ueberspringen = 0

        for i in liste:
            output_file.write(i+'\n')
        input_file.close()
        output_file.close()

checking()
