import datetime

var = datetime.datetime.today()

comparisonDate = datetime.timedelta(1)

date2 = var - comparisonDate
print(date2)

date2 = datetime.datetime.strftime(date2, "%d/%m/%Y")
print(date2)
