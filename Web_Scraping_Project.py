# python web scraping project for portfolio
# today is january 27 2023
# I am scraping unemployment data for different groups from the BLS

# new idea: this project gets the latest months values (whatever the last month happens to be) for unemployment rate by race and
# builds sql statements (with non-real open curator sql values in it: for example, it's a fake table name)

# NOTE: unemployment rate comes out at 8:30 AM Eastern the first Friday of every month

# crontab example for 8 45 in the mornint first friday of the month
#  45 08 * * 5 [ $(date +\%d) -le 07 ] && /path/to/python_script

# note above crontab is from https://stackoverflow.com/questions/3241086/how-to-schedule-to-run-first-sunday-of-every-month

#https://www.bls.gov/charts/employment-situation/civilian-unemployment-rate.htm

from bs4 import BeautifulSoup
import requests
import re


source = requests.get('https://www.bls.gov/charts/employment-situation/civilian-unemployment-rate.htm').text

soup = BeautifulSoup(source, 'lxml')

#print(soup.title.text)

tables = soup.findChildren('table')

my_table = tables[0]

# Get all the dates (and the last date)
rows = my_table.findChildren(['tr'])

date_count = 0

for row in rows:
    cells = row.findChildren('th')
    for cell in cells:
        #if (cell.string == 'Dec 2022'):
         #   print(cell.get("id"))
        date_count = date_count + 1
        date_value = cell.string
        #if (date_value[-4:] == '2003'):
            #print(cell.get("id"))
         #   print("The date in this cell is %s" % date_value)

last_date = date_value
#print("Last date is %s" % last_date)

# convert last_date to sql friendly version

sql_month = "0"

last_month = last_date[:4]
match last_month:
    case 'Jan ':
        sql_month = "1"
    case 'Feb ':
        sql_month = "2"
    case 'Mar ':
        sql_month = "3"
    case 'Apr ':
        sql_month = "4"
    case 'May ':
        sql_month = "5"
    case 'Aug ':
        sql_month = "8"
    case 'Oct ':
        sql_month = "10"
    case 'Nov ':
        sql_month = "11"
    case 'Dec ':
        sql_month = "12"
    

if (sql_month == "0"):
    last_month = last_date[:5]
    match last_month:
        case 'June ':
            sql_month = "6"
        case 'July ':
            sql_month = "7"
        case 'Sept ':
            sql_month = "9"
        
    


last_year = last_date[-4:]

sql_date = sql_month + last_year

for row in rows:
    cells = row.findChildren('th')
    for cell in cells:
        if (cell.string == last_date):
            super_last_id = cell.get("id")
            #print(cell.get("id"))
        

print('----------------------------')

# HUNTER, for this fake data, the sql data ids will be 112 for white, 113 for black, 115 for asian and 125 for hispanic
predefined_list = ["112;","113;","115;", "125;"]
sql_start = "INSERT INTO OC_t32 ("
sql_start2 = ") VALUES "
sql_next = "Where data_id = "
my_counter = 0

for row in rows:
    cells = row.findChildren('td')
    for cell in cells:
        the_value = cell
        x = re.search(super_last_id, str(the_value))

        if x:
          #print(the_value.string)
          #print(predefined_list[my_counter] + " is " + the_value.string)
          #print(f"{predefined_list[my_counter]} is {the_value.string} " )
          #my_counter = my_counter + 1
          if (my_counter >= 4 and my_counter < 8):
              print(f"{sql_start}{sql_date}{sql_start2}{the_value.string} {sql_next} {predefined_list[my_counter - 4]} " )
          my_counter = my_counter + 1
        
        
        






#last_date = date_value
#print("Last date is %s" % last_date)

print('----------------------------')
'''
# get last months data
for the_data in soup.find_all('th'):
    if (the_data.string == last_date):
        last_id = the_data.get('id')
        print(last_id)

        '''
'''
for team in my_table.find_all('tbody'):
    rows = team.find_all('tr')
    for row in rows:
        new_row = row.find_all('th')
        x = re.findall("Dec", new_row)
        print(x)
'''
#tb = my_table.find_all("tr")


#td2 = tb.find("td", attrs={"headers" : 'cps_rc_uemprtcat.r.4 cps_rc_uemprtcat.h.1.3'})


              





        

