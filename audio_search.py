'''
After trancribing an audio file using the OpenAI Whisper module, this program allows you to search the
audio for spoken words and returns all the timestamps where the audio is located.
'''

import re
from bisect import bisect
from tkinter import Tk     
from tkinter.filedialog import askopenfilename


the_text = []
lookup_a = []
lookup_b = []
runner = []

Tk().withdraw() # Don't need the full tkinter GUI
filename = askopenfilename() 
print(f"Selected file: {filename}")


def format_timestamp(ts):
    if len(ts) <= 5:
        fts = ts[0:2] + " seconds"
    elif len(ts) == 6:
        fts = ts[0:1] + " minutes:" + ts[1:3] + " seconds"
    elif len(ts) == 7:
        fts = ts[0:2] + " minutes:" + ts[2:4] + " seconds"
    elif len(ts) == 8:
        fts = ts[0:1] + " hours:" + ts[1:3] + " minutes:" + ts[3:5] + " seconds"
    elif len(ts) == 9:
        fts = ts[0:2] + " hours:" + ts[2:4] + " minutes:" + ts[4:6] + " seconds"
    return fts


query = input("Enter your search query: ")


correct_file_format = False

with open(filename, "r") as f:
    regex_pattern = '(^\d+)\s+(\d+)\s+(.+)$'
    for line in f:
        if line[0].isalpha():
            continue
        else:
            result = re.match(regex_pattern,line)
            if result:
                correct_file_format = True
                k = len(result.group(3))
                runner.append(k)
                lookup_a.append(result.group(1))
                lookup_b.append(str(sum(runner)))
                for word in result.group(3).split(" "):
                    the_text.append(word)
                    
if not correct_file_format:
    print("Incorrect file format.\nSelected file should be an output file from the OpenAI Whisper api or similar. (.tsv file extension)")


mod_lookup_b = [eval(i) for i in lookup_b]

# Convert list of the words to a string
the_string = ' '.join(the_text)

if query not in the_string:
    print(f"No matches for {query} were found.")
    
else:
    result = the_string.index(query)

    which_line = bisect(mod_lookup_b,result)
    found_timestamps = []
    # Get a list of all the starting indices (the query could appear more than once)
    all_found = [m.start() for m in re.finditer(query, the_string)]
    qnty_found = len(all_found)
    print(f"\nYour query was: {query}")
    for i in all_found:
        which_line = bisect(mod_lookup_b,i)
        found_timestamps.append(format_timestamp(lookup_a[which_line]))
        

    if qnty_found > 0:
        print(f"Found a total of {qnty_found} matches.")
        print("Your query can be found at the following timestamps:\n")
        for i,j in enumerate(found_timestamps,1):
            print(f"\t{i}: {j}")
    

