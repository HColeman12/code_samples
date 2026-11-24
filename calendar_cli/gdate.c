
int
get_dow (int year, int month, int day)
{
  if (month < 3)
    {
      month += 12;
      year -= 1;
    }
  int k = year % 100; // Year within the century
  int j = year / 100; // Century
  int dayOfWeek
      = (day + (13 * (month + 1)) / 5 + k + (k / 4) + (j / 4) - (2 * j)) % 7;
  return (dayOfWeek + 7) % 7; // Ensure non-negative result
}

// Tomohiko Sakamoto's algorithm
// returns the index of the
// day for date DD/MM/YYYY
int
dayNumber (int day, int month, int year)
{
  static int t[] = { 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 };
  year -= month < 3;
  return (year + year / 4 - year / 100 + year / 400 + t[month - 1] + day) % 7;
}

// return the number of days in a given month
int
numberOfDays (int monthNumber, int year)
{
  // January
  if (monthNumber == 0)
    return (31);

  // February
  if (monthNumber == 1)
    {
      // If the year is leap then Feb
      // has 29 days
      if (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0))
        return (29);
      else
        return (28);
    }

  // March
  if (monthNumber == 2)
    return (31);

  // April
  if (monthNumber == 3)
    return (30);

  // May
  if (monthNumber == 4)
    return (31);

  // June
  if (monthNumber == 5)
    return (30);

  // July
  if (monthNumber == 6)
    return (31);

  // August
  if (monthNumber == 7)
    return (31);

  // September
  if (monthNumber == 8)
    return (30);

  // October
  if (monthNumber == 9)
    return (31);

  // November
  if (monthNumber == 10)
    return (30);

  // December
  if (monthNumber == 11)
    return (31);

} // end of numberOfDays
