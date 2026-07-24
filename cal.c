#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

void display_usage(void) {
  const char *usage = "Usage: [Program Name] [Options]\n\n";
  const char *header = "Options:\n";
  /* width of left column (option names) */
  const int optw = 20;
  const char *fmt = "%-20s-%s\n"; /* left-align option column */

  printf("\n ------------------------------------\n");
  printf("%s%s", usage, header);
  printf("%-20s-%s", "-h, --help", "Displays this menu\n");
  printf(fmt, "None", "Displays calendar for current year");

  printf(fmt, "[-y] year",
         "Displays calendar for specified year (between 1900 and 3000)");
  printf(fmt, "month name [year]", "Displays calendar for specified month");
  printf(fmt, "-dow [YYYY-MM-DD]",
         "Displays day name of the specified date, or current day if no date "
         "is specified.");
  printf(fmt, "--until YYYY-MM-DD",
         "Displays number of days until specified date ");

  printf("\nValid years are 1900 through 3000.\n");

  printf(" ------------------------------------\n");
}

int get_dow(int year, int month, int day) {
  if (month < 3) {
    month += 12;
    year -= 1;
  }
  int k = year % 100;  // Year within the century
  int j = year / 100;  // Century
  int dayOfWeek =
      (day + (13 * (month + 1)) / 5 + k + (k / 4) + (j / 4) - (2 * j)) % 7;
  return (dayOfWeek + 7) % 7;  // Ensure non-negative result
}

int check_user_date_format(char *the_date) {
  if (strlen(the_date) != 10) {
    printf("Date format SHOULD be YYYY-MM-DD\n");
    return 0;
  }
  return isdigit((unsigned char)the_date[0]) &&
         isdigit((unsigned char)the_date[1]) &&
         isdigit((unsigned char)the_date[2]) &&
         isdigit((unsigned char)the_date[3]) && the_date[4] == '-' &&
         isdigit((unsigned char)the_date[5]) &&
         isdigit((unsigned char)the_date[6]) && the_date[7] == '-' &&
         isdigit((unsigned char)the_date[8]) &&
         isdigit((unsigned char)the_date[9]);
  //	return 0;
}

// check that a valid date was entered
int is_valid_date(int day, int month, int year) {
  if (year < 1800 || month < 1 || month > 12 || day < 1) return 0;

  int days_in_month[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

  // Leap year check
  if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0))
    days_in_month[1] = 29;

  return day <= days_in_month[month - 1];
}

// Tomohiko Sakamoto's algorithm
// returns the index of the
// day for date DD/MM/YYYY
int dayNumber(int day, int month, int year) {
  static int t[] = {0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4};
  year -= month < 3;
  return (year + year / 4 - year / 100 + year / 400 + t[month - 1] + day) % 7;
}

// returns the name of the
// month for the given month Number
// January - 0, February - 1
char *getMonthName(int monthNumber) {
  char *month;

  switch (monthNumber) {
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
      month = "Invalid";  // HC Do I need this?
      break;
  }
  return month;
}

// return the number of days in a given month
int numberOfDays(int monthNumber, int year) {
  // January
  if (monthNumber == 0) return (31);

  // February
  if (monthNumber == 1) {
    // If the year is leap then Feb
    // has 29 days
    if (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0))
      return (29);
    else
      return (28);
  }

  // March
  if (monthNumber == 2) return (31);

  // April
  if (monthNumber == 3) return (30);

  // May
  if (monthNumber == 4) return (31);

  // June
  if (monthNumber == 5) return (30);

  // July
  if (monthNumber == 6) return (31);

  // August
  if (monthNumber == 7) return (31);

  // September
  if (monthNumber == 8) return (30);

  // October
  if (monthNumber == 9) return (31);

  // November
  if (monthNumber == 10) return (30);

  // December
  if (monthNumber == 11) return (31);

}  // end of numberOfDays

// print the calendar of the given year
void printCalendar(int year, int month_start, int month_stop) {
  printf("     Calendar - %d\n\n", year);
  int days;

  // Index of the day from 0 to 6
  // current determines when the first day of the month is. If it's zero, the
  // first of the month falls on Sunday below the second parameter was 1,
  // changing to 2 makes february calendar correct, when viewing just feb.
  // maybe try chaning to month_stop
  //  doing that works when selecting a single month, but when viewing entire
  //  year, the calendar days are one month behind
  // printf("month_stop is %d\n",month_stop);
  // printf("month_start is %d\n",month_start);
  int current;
  if (month_stop == 12 && month_start == 0) {
    current = dayNumber(1, 1, year);
  } else {
    current = dayNumber(1, month_stop, year);
  }

  // i is iterate through months
  // j is iterate through days
  // of the month - i
  for (int i = month_start; i < month_stop; i++) {  // HCtst
    days = numberOfDays(i, year);

    // Print the current month name
    //	if (i == 1){
    printf("\n ------------%s-------------\n", getMonthName(i));
    //	}

    const char *print_cal_days[] = {"Sun", "Mon", "Tue", "Wed",
                                    "Thu", "Fri", "Sat"};
    printf("   ");
    for (size_t i = 0; i < sizeof(print_cal_days) / sizeof(print_cal_days[0]);
         ++i) {
      printf("%-5s",
             print_cal_days[i]); /* %-5s = left-aligned in a 5-char field */
    }
    putchar('\n');

    // Print appropriate spaces
    // ie How far to the right day the first of the month is printed
    int k;
    for (k = 0; k < current; k++)
      printf("     ");  // HC added one more space here

    for (int j = 1; j <= days; j++) {
      printf("%5d", j);

      if (++k > 6) {
        k = 0;
        printf("\n");
      }
    }

    if (k) printf("\n");

    current = k;
  }

  return;
}  // End of printCalendar function

int main(int argc, char *argv[]) {
  // Getting the current year month and day
  time_t current_time = time(NULL);
  // convert to local time
  struct tm *local_time = localtime(&current_time);
  int year = local_time->tm_year + 1900;
  int month = local_time->tm_mon + 1;
  int day = local_time->tm_mday;

  // Check if user entered a month name as arg1 and an optional year
  int month_start = 0;
  int month_stop = 12;

  const char *month_names[] = {"January",   "February", "March",    "April",
                               "May",       "June",     "July",     "August",
                               "September", "October",  "November", "December"};
  int num_month_names = sizeof(month_names) / sizeof(month_names[0]);

  const char *holiday_names[] = {"Christmas", "Memorial Day", "Easter",
                                 "Labor Day", "Chanuka"};

  if (argc == 1) {
    // no args provided
    printCalendar(year, month_start, month_stop);
    return 0;
  }

  if (argc == 2 && strcmp(argv[1], "-h") == 0 ||
      strcmp(argv[1], "--help") == 0) {
    display_usage();
    return 0;
  }

  // If user enters -dow and a date
  // If user enters -dow but no other agrument, default to the current day
  if (argc == 2 || argc == 3) {
    const char *days[] = {"Saturday",  "Sunday",   "Monday", "Tuesday",
                          "Wednesday", "Thursday", "Friday"};
    if ((strcasecmp(argv[1], "-dow") == 0) && (argc == 2)) {
      // using dow without other arguments, default to current day
      int day_of_week = get_dow(
          year, month, day);  // these are the current day variables, set above
      printf("%s\n", days[day_of_week]);
      return 0;
    }

    if (argc == 3) {

      // Check that argv[2] is a properly formatted date
      if (check_user_date_format(argv[2])) {
        char *the_date_input = argv[2];
        int yy = (the_date_input[0] - '0') * 1000 +
                 (the_date_input[1] - '0') * 100 +
                 (the_date_input[2] - '0') * 10 + (the_date_input[3] - '0');
        int mm = (the_date_input[5] - '0') * 10 + (the_date_input[6] - '0');
        int dd = (the_date_input[8] - '0') * 10 + (the_date_input[9] - '0');

        if (!is_valid_date(dd, mm, yy)) {
          printf("Invalid date entered.\n");
          return 1;
        }

        if (strcasecmp(argv[1], "-dow") == 0) {
          int day_of_week = get_dow(yy, mm, dd);
          printf("%s\n", days[day_of_week]);
          return 0;
        }

        if (strcasecmp(argv[1], "--until") == 0 ||
            strcasecmp(argv[1], "-u") == 0) {
          int day, month, year;
          time_t now;
          struct tm future_date = {0}, today_tm = {0};

          // Get today's date
          time(&now);
          today_tm = *localtime(&now);
          today_tm.tm_hour = 0;
          today_tm.tm_min = 0;
          today_tm.tm_sec = 0;

          // Set future date struct
          future_date.tm_mday = dd;
          future_date.tm_mon = mm - 1;      // tm_mon is 0-based
          future_date.tm_year = yy - 1900;  // tm_year is years since 1900

          // Convert to time_t
          time_t future_time = mktime(&future_date);
          time_t today_time = mktime(&today_tm);

          if (future_time == (time_t)-1) {
            printf("Error converting date.\n");
            return 1;
          }

          // Check if date is in the future
          if (future_time <= today_time) {
            printf("When using --until, the date must be in the future.\n");
            return 1;
          }

          // Calculate difference in days
          double diff_seconds = difftime(future_time, today_time);
          int diff_days = (int)(diff_seconds / (60 * 60 * 24));

          printf("Number of days until %04d-%02d-%02d: %d days\n", yy, mm, dd,
                 diff_days);

          return 0;

        }  // end if argv1 is --until
        else {
          printf(
              "user done entered --until or -u and NOT valid formatted date "
              "yo\n");
        }
      }
    }
  }

  if (argc > 1) {
    for (int i = 0; i < num_month_names; i++) {
      if (strcasecmp(argv[1], month_names[i]) == 0) {
        month_start = i;
        month_stop = i + 1;
        // In addition to a month name, did they also enter a year
        if (argc == 3 && atoi(argv[2]) >= 1900 && atoi(argv[2]) <= 3000) {
          year = atoi(argv[2]);
        } else {
          printf("Valid years are 1900 through 3000\n");
          return 1;
        }

        printCalendar(year, month_start, month_stop);
        return 0;
      }
    }
    for (int i = 1; i < argc; i++) {
      if ((strcmp(argv[i], "-y") == 0 && i + 1 < argc) &&
          (atoi(argv[i + 1]) >= 1900 && atoi(argv[i + 1]) <= 3000)) {
        year = atoi(argv[++i]);
      } else if (atoi(argv[1]) >= 1900 && atoi(argv[1]) <= 3000) {
        year = atoi(argv[1]);
      } else {
        display_usage();
        return 1;
      }
    }
  } else {
    printCalendar(year, month_start, month_stop);
  }

  printCalendar(year, month_start, month_stop);
  return 0;
}
