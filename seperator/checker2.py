#!/usr/bin/python3

import difflib

MAXLINES = 55

def checking():
        file1 = open("test.txt", "r")
        file2 = open("tmp_test.txt", "r")
        liste = []
        tmp_liste = []
        listeFinal = []
        unterschied = 0
        count = 0
        for line1 in file1:
                str1 = line1.rstrip()
                liste.append(str1)
                #for i in liste:
                    #print('i: \n'+i+'\n')
                    #print('str1: \n'+str1+'\n')
                    #unterschied = LD(str1, i)
                    #print('unterschied: \n'+str(unterschied)+'\n')
                #liste.append(str1)
               # print(unterschied+'\n')
        tmp_liste = liste
        for i in liste:
            #print(i)
            for j in tmp_liste:
                unterschied = LD(i, j)
                if unterschied > 5 and count < len(tmp_liste):
                   print(unterschied)
                   print(j) 
                   listeFinal.append(j) 
                   count = count + 1
                   continue


        file1.close()
        print(listeFinal) 
                #for line2 in file2:
		#	str2 = line2.rstrip()
	#		if(str1 == str2):
	#			print(str1 + " " + str2)
	#			print("alles gut")

	


def LD(s,t):
    s = ' ' + s
    t = ' ' + t
    d = {}
    S = len(s)
    T = len(t)
    for i in range(S):
        d[i, 0] = i
    for j in range (T):
        d[0, j] = j
    for j in range(1,T):
        for i in range(1,S):
            if s[i] == t[j]:
                d[i, j] = d[i-1, j-1]
            else:
                d[i, j] = min(d[i-1, j], d[i, j-1], d[i-1, j-1]) + 1
    return d[S-1, T-1]

checking()
