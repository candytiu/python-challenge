from statistics import mean
import os
import csv
csvpath = os.path.join("budget_data.csv") 
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)
    csvlist = list(csvreader)

# #creating lists
    dates = []
    revenues = []
    revenuechange = []

# #loop
    for row in csvlist:
        dates.append(row[0])
        revenues.append(int(row[1]))
        revenue_change = [revenues[i+1] - revenues[i] for i in range(len(revenues) -1)]
        total_revenue = sum(revenues)
    
# #variables
    max_change = max(revenue_change)
    min_change = min(revenue_change)
    avg_change = mean(revenue_change)
    total_month = len(dates)
    max_month = None
    min_month = None
    avg_change = float(avg_change)

# #for loop to find corresponding date 
    min_initial = None
    for row in csvlist:
        if min_initial is None:
            min_initial = int(row[1])
        if int(row[1]) - min_initial == min_change:
            min_month = row[0]
        min_initial = int(row[1])

    max_initial = None
    for row in csvlist:
        if max_initial is None:
            max_initial = int(row[1])
        if abs(int(row[1])) - max_initial == max_change:
            max_month = row[0]
        max_initial = int(row[1])
    

print("Financial Analysis")
print("----------------------------------------------------------")
print(f"Total Months: {total_month}")
print(f"Total Revenues:${total_revenue}")
print(f"Average change: $%.2f" % avg_change)
print(f"Greatest Increase in Profits: {max_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_month} (${min_change})")

