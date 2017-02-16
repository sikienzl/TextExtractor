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


def main():
    argv = sys.argv[1:]
    string = None
    if(len(sys.argv) == 1):
        loggingModule.logger9.info("Please put a correct parameter!\n")
        loggingModule.logger9.info(help())

    try:
        opts, args = getopt.getopt(
            argv, "hvi:o:", ['help', 'input=', 'output='])
    except getopt.GetoptError as e:
        loggingModule.logger9.info("Please put a correct parameter!\n")

    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            loggingModule.logger9.info(help())
        elif o in ("-i", "--input"):
            input_file = a
            string = work()
        elif o in ("-o", "--output"):
            writeIntoFile(a, string)
        else:
            loggingModule.logger9.info(help())
    if verbose:
        if string is not None:
            loggingModule.logger9.info(string)
        else:
            loggingModule.logger9.info(help())


def work():
    converter_path = 'converter/current/convertToTxt.py'
    checker_path = 'seperator/checker.py'
    seperator_path = 'seperator/seperator.py'

    listr = []
    try:
        proc = subprocess.Popen(["ls", "testdata"], stdout=subprocess.PIPE)
        listr = proc.stdout.readlines()
    except Exception as e:
        loggingModule.logger9.error("Cannot get files: " + str(e))
    encoding = 'utf-8'

    for l in listr:
        words = str(l, encoding)
        input_file = words.strip(' \n\r\t')

        input_path = "testdata/" + input_file

        try:
            file_name_process = input_file.split('.')
            file_name = file_name_process[0]

        except Exception as e:
            loggingModule.logger9.error("Cannot split file name: " + str(e))

        file_name_converted = file_name + '_converted.txt'
        try:
            proc = subprocess.Popen(
                ["python3",
                 converter_path,
                 '-i',
                 input_path,
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
        except Exception as e:
            loggingModule.logger9.error("Cannot seperate sentence: " + str(e))

    loggingModule.logger9.info("----------READY----------")


def help():
    return("arguments\n" +
           "-h,                      --help                          " +
           "show help message and exit\n" +
           "-i [path to file]        --input  [path to file]         " +
           "to run the program\n" +
           "-o [path to outputfile]  --output [path to outputfile]   " +
           "to extract text into file\n" +
           "-v                                                       " +
           "verbose-Mode")

if __name__ == '__main__':
    main()
