#!/usr/bin/python3

"""
main.py:
separates the senteces in a file.
"""

__author__ = "Mark Unger, Siegfried Kienzle"


import sys
import getopt
import loggingModule
import subprocess
import os
import configparser

config = configparser.ConfigParser()
config.read('path.cfg')

def main():
    argv = sys.argv[1:]
    string = None
    if(len(sys.argv) == 1):
        loggingModule.logger9.info("Please put a correct parameter!\n")
        loggingModule.logger9.info(help())

    try:
        opts, args = getopt.getopt(
            argv, "hi:p:d", ['help', 'input=', 'path=', 'delete'])
    except getopt.GetoptError as e:
        loggingModule.logger9.info("Please put a correct parameter!\n")

    for o, a in opts:
        if o in ("-h", "--help"):
            loggingModule.logger9.info(help())
        elif o in ("-i", "--input"):
            input_file = a
            work(input_file)
        elif o in ("-p", "--path"):
            path = a
            path_with_files(path)
        else:
            loggingModule.logger9.info(help())


def path_with_files(path):
    endings = ['pdf', 'rtf', 'doc', 'docx', 'odt']
    listr = []
    encoding = 'utf-8'
    clean_list = []

    try:
        proc3 = subprocess.Popen(["ls", path], stdout=subprocess.PIPE)
        list_with_filenames = proc3.stdout.readlines()
    except Exception as e:
        loggingModule.logger9.error("Cannot get files: " + str(e))

    for filename1 in list_with_filenames:
        filename2 = str(filename1)
        get_info_about_file = filename2.split('.')
        get_info_about_file2 = get_info_about_file[-1].rstrip(' \\n \'')

        if(get_info_about_file2 in endings):
            clean_list.append(filename1)

    for filename in clean_list:
        filename_encoded = str(filename, encoding)
        clean_filename = filename_encoded.strip(' \n\r\t')

        input_path = path + clean_filename

        loggingModule.logger9.info(input_path + " goes in process")

        work(input_path)

    loggingModule.logger9.info("----------READY----------")
'''
work():
calls the moduls to converts, remove duplications and seperates sentences.
The tree files _converted, _removed_lines and _final stay where the input_file is.
'''


def work(input_file):
    converter_path=config['PFAD']['converter'] 
    checker_path=config['PFAD']['checker'] 
    seperator_path=config['PFAD']['seperator'] 

    file_name_process = input_file.split('.')
    file_name = file_name_process[0]

    file_name_converted = file_name + '_converted.txt'
    try:
        proc = subprocess.Popen(
            ["python3",
             converter_path,
             '-i',
             input_file,
             '-o',
             file_name_converted],
            stdout=subprocess.PIPE)
        proc.wait()
    except Exception as e:
        loggingModule.logger9.error("Cannot convert file: " + str(e))

    file_name_removedLines = file_name + '_removed_lines.txt'
    try:
        proc1 = subprocess.Popen(
            ["python3",
             checker_path,
             '-i',
             file_name_converted,
             '-o',
             file_name_removedLines],
            stdout=subprocess.PIPE)
        proc1.wait()
        os.remove(file_name_converted)
    except Exception as e:
        loggingModule.logger9.error("Cannot check file: " + str(e))

    file_name_seperator = file_name + '_final.txt'
    try:
        proc2 = subprocess.Popen(
            ["python3",
             seperator_path,
             '-i',
             file_name_removedLines,
             '-o',
             file_name_seperator],
            stdout=subprocess.PIPE)
        proc2.wait()
        os.remove(file_name_removedLines)
    except Exception as e:
        loggingModule.logger9.error("Cannot seperate sentence: " + str(e))


def help():
    return("arguments\n" +
           "-h,                      --help                          " +
           "show help message and exit\n" +
           "-i [path to file]        --input  [path to file]         " +
           "to run the program\n" +
           "-p [path to folder]  --path [path to folder]   " +
           "process all file in a folder\n")

if __name__ == '__main__':
    main()
