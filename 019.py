from datetime import date

start = date(1901,1,1)
end = date(2000, 12, 31)

sundays = []

for year in range(1901, 2001):
	for month in range(1,13):
		day = date(year, month, 1)
		if day.weekday() == 6: #Sunday
			sundays.append(day)


print len(sundays)
