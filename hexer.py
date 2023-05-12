'''
This module produces a hex dump for a file.

Usage:
    hexer.py [-h] [-t] [-s] [-l LENGTH] filename

Positional arguments:
  filename              The file to be dumped

User options:
   [--help | -h]      : Display help menu
   [--length n | -l n]: Limits the output of the hex dump to n bytes
   [--silent | -s]    : Supresses output of hex dump
   [--type | -t]      : Attempts to determine the type of file submitted for hex dump

'''

import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="the file to be dumped", type=str)
parser.add_argument("-t","--type", help="show file type", action="store_true")
parser.add_argument("-s","--silent", help="do not show hex dump", action="store_true")
parser.add_argument("-l","--length", help="limit hex output to LENGTH bytes", action="store")
args = parser.parse_args()

def main():
    try:
        with open(args.filename, "rb") as f:
            n = 0
            b = f.read(16)  
            filetype = ""
            line_read = 0
            lines_to_read = ""

            if args.length:
                lines_to_read = int(args.length) // 16
                if lines_to_read != 0:
                    bytes_left_to_read = int(args.length) % (16 * int(lines_to_read))
                else:
                    bytes_left_to_read = args.length
            

            while b:
                st_1 = " ".join([f"{i:02x}" for i in b]) 
                st_1 = st_1[0:23] + " " + st_1[23:] #Divide each line of hex output with a space into two equal groups for aesthetics 

                st_2 = "".join([chr(i) if 32 <= i <= 127 else "." for i in b]) #Display a dot for non-ASCII values

                if not args.silent:
                    line_read = line_read + 1
                    if (args.length and (line_read > lines_to_read)) and (lines_to_read != 0):
                        print(f"{n * 16:08x} {st_1[0:bytes_left_to_read * 3]:<48} |{st_2[0:bytes_left_to_read]:<16}|")
                        
                        if f.tell() > int(args.length):
                            break
                    else:
                        if lines_to_read != 0:
                            print(f"{n * 16:08x} {st_1:<48} |{st_2}|")
                        else:
                            print(f"{n * 16:08x} {st_1[0:int(bytes_left_to_read) * 3]:<48} |{st_2[0:int(bytes_left_to_read)]:<16}|")
                    if lines_to_read == 0:
                        break
                    

                if filetype == "":
                    filetype = st_1[0:23]

                n += 1
                b = f.read(16)

        if filetype == "":
            filetype = st_1[0:23]

        if args.type:
            print(f"This file appears to be: {get_filetype(filetype)}")
            

    except Exception as e:
        print(__file__, ": ", type(e).__name__, " - ", e, sep="", file=sys.stderr)

def get_filetype(x):
    '''Searches for a file signature within the hex dump.'''
    if x == "89 50 4e 47 0d 0a 1a 0a":
        return "PNG file"
    elif x[0:14] == "25 50 44 46 2d":
        return "PDF file"
    elif x[0:5] == "1f 8b":
        return "GZip file"
    elif x[0:8] == "ff d8 ff":
        return "JPEG file"
    elif x[0:11] == "47 49 46 38":
        return "GIF file"
    elif x[0:8] == "ef bb bf":
        return "UTF-8 text file"
    else:
        return "Undetermined"
    

if __name__ == '__main__':
    main()

            
