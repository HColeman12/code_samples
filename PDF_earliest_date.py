import tkinter, PyPDF2
from tkinter import filedialog
from datetime import datetime
import re
import sys

'''
User is prompted to select a PDF file and the earliest date in the selectd PDF
is returned as a string which has been converted to mm-dd-yyyy format.

Author: Hunter Coleman

'''


def find_earliest_date():
    filename = filedialog.askopenfilename(title="Open PDF file", 
                                                  filetypes=[('PDF files', '*.pdf')])
    
    
    reader = PyPDF2.PdfReader(filename)
    for i in range (reader.numPages):
        current_text = reader.getPage(i).extractText()
        a_date = re.compile("\d{1,2}[\\\-]{1}\d{1,2}[\\\-]{1}\d{4}")
        b_date = re.compile("(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|June?|July?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s*\d{1,2},?\s*\d{2,4}")

        
        
        x = re.findall(a_date, current_text)
        y = re.findall(b_date, current_text)
        z = x + y
        z.sort()

        if len(z) == 0:
            print("No date found in document")
            sys.exit()
        

        date_convert_regex_abb = r"^[A-Z][a-z]{2}\s"
        date_convert_regex_full = r"^(January|February|March|April|May|Jun|July|August|September|October|November|December)\s"
        date_convert_regex_add_zero = r"^([1-9][\\\-]\d{1,2})"

        my_date_list = []
        earliest_date_list = []
        earliest_month_list = []
        earliest_day_list = []

        for i in z:
            if re.match(date_convert_regex_abb, i):
                d = datetime.strptime(i, '%b %d, %Y')
                my_date_list.append(d.strftime('%m-%d-%Y'))
            elif re.match(date_convert_regex_full, i):
                d = datetime.strptime(i, '%B %d, %Y')
                my_date_list.append(d.strftime('%m-%d-%Y'))
            elif re.match(date_convert_regex_add_zero, i):
                my_date_list.append("0" + i)
            else:
                my_date_list.append(i)
                
                
        my_date_list.sort(key=lambda x:x[-4:-1])
        earliest_year = my_date_list[0][-4:]

        for j in my_date_list:
            if j[-4:] == earliest_year:
                earliest_date_list.append(j)

        

        if len(earliest_date_list) == 1:
            print(earliest_date_list[0])
        else:
            earliest_date_list.sort(key=lambda x:x[0:2])
            earliest_month = earliest_date_list[0][0:2]
            for k in earliest_date_list:
                if k[0:2] == earliest_month:
                    earliest_month_list.append(k)
            if len(earliest_month_list) == 1:
                print(earliest_month_list[0])
            else:
                earliest_month_list.sort(key=lambda x:x[3:5])
                earliest_day = earliest_month_list[0][3:5]
                for m in earliest_month_list:
                    if m[3:5] == earliest_day:
                        earliest_day_list.append(m)
                if len(earliest_day_list) == 1:
                    print(earliest_day_list[0])
                else:
                    print(earliest_day_list[0])
                    


if __name__ == "__main__":
    find_earliest_date()




