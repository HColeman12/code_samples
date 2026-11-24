#include <ctype.h>
#include <stdio.h>
#include <string.h>

int
check_user_date_format (char *the_date)
{
  if (strlen (the_date) != 10)
    {
      printf ("Date format SHOULD be YYYY-MM-DD\n");
      return 0;
    }
  return isdigit ((unsigned char)the_date[0])
         && isdigit ((unsigned char)the_date[1])
         && isdigit ((unsigned char)the_date[2])
         && isdigit ((unsigned char)the_date[3]) && the_date[4] == '-'
         && isdigit ((unsigned char)the_date[5])
         && isdigit ((unsigned char)the_date[6]) && the_date[7] == '-'
         && isdigit ((unsigned char)the_date[8])
         && isdigit ((unsigned char)the_date[9]);
  //	return 0;
}

// check that a valid date was entered
int
is_valid_date (int day, int month, int year)
{
  if (year < 1800 || month < 1 || month > 12 || day < 1)
    return 0;

  int days_in_month[] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

  // Leap year check
  if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0))
    days_in_month[1] = 29;

  return day <= days_in_month[month - 1];
}

// returns the name of the
// month for the given month Number
// January - 0, February - 1
char *
getMonthName (int monthNumber)
{
  char *month;

  switch (monthNumber)
    {
    case 0:
      month = "January";
      break;
    case 1:
      month = "February";
      break;
    case 2:
      month = "March";
      break;
    case 3:
      month = "April";
      break;
    case 4:
      month = "May";
      break;
    case 5:
      month = "June";
      break;
    case 6:
      month = "July";
      break;
    case 7:
      month = "August";
      break;
    case 8:
      month = "September";
      break;
    case 9:
      month = "October";
      break;
    case 10:
      month = "November";
      break;
    case 11:
      month = "December";
      break;
    default:
      month = "Invalid"; // HC Do I need this?
      break;
    }
  return month;
}
