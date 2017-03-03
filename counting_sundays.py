#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)
import datetime
count = 0
for y in range(1901,2001):
 for m in range(1,13):
  if datetime.datetime.weekday(datetime.datetime(y,m,1))==6: 
   print y, m
   count+=1
print count
