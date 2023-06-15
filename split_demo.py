#[2, 6, 8, 9]
date = "6/15/2023"

#gety the month, day, year values from the date
#use the .split() string method
date_parts = date.split("/")
print(date_parts)

#to just access a certain part (in this case year)
#in this case the year would be at index 2

#print day, month, year
print(f"Day: {date_parts[1]}")
print(f"Month: {date_parts[0]}")
print(f"Year: {date_parts[2]}")

print("\n\n")
"or this would be more effiecent in some cases"
month_number = int(date_parts[0])
#month_number = date_parts[0]
day = date_parts[1]
year = date_parts[2] 

#print(f"Day: {day}")
#print(f"Month: {month_number}")
#print(f"Year: {year}")

print("\n\n")
months= ["January, Febuary, March, April, May, June, July, August, September, October, November, December"]
print(f"Day: {day}")
print(f"Month: {months[month_number -1]}")
print(f"Year: {year}")
