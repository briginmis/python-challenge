import os
import csv

#state variables
list = []
profitloss = 0
changecalc = [0]
changelist = []
changesum = 0
rowignore = 1
greatestprofit = 0
greatestloss = 0

#obtain file path
filepath = os.path.join("Resources","budget_data.csv")

#read csv file
with open(filepath,"r") as data:
    csvreader = csv.reader(data, delimiter = ",")

    #ignore the first row
    header = next(csvreader)

    #loop through to obtain information
    for row in csvreader:
        #add each row to data list, to obtain data length
        list.append(row[0])
        #accumulate profit/loss, to obtain total profit/losses over the entire period
        profitloss = profitloss + int(row[1])
        #calculate change in profit between periods and add to list, then accumulate change
        changecalc.append(int(row[1]))
        change = changecalc[1] - changecalc[0]
        if rowignore == 1:
            change = 0
            rowignore = 0
        else:
            changelist.append(change)
            changesum = changesum + change       
        #if change in profit is greater than previous, then replace
        if change > greatestprofit:
            greatestprofit = change
            profitdate = row[0]
        #if change in profit/loss is less than previous, then replace
        if change < greatestloss:
            greatestloss = change
            lossdate = row[0]        
        #remove first number in list, to be replaced by the new profit/loss in the next loop
        changecalc.pop(0)

#calculate final figures
print("Financial Analysis")
print("----------------------------")
#Total months
print(f"Total Months: {len(list)}")
#Total p&l
print(f"Total: ${profitloss}")
#Average change
average = changesum / float(len(changelist))
print(f"Average Change: ${round(average,2)}")
#Greatest increase in profits, date and amount
print(f"Greatest Increase in Profits: {profitdate} (${greatestprofit})")
#Greatest decrease in losses, date and amount
print(f"Greatest Decrease in Profits: {lossdate} (${greatestloss})")

# Specify the file to write to
analysis_path = os.path.join("Analysis", "bank.txt")

#Open the file using "write" mode. Specify the variable to hold the contents
with open(analysis_path, 'w') as txtfile:

    #write in text file
    txtfile.write("Financial Analysis")
    txtfile.write('\n'"----------------------------")
    txtfile.write('\n'f"Total Months: {len(list)}")
    txtfile.write('\n'f"Total: ${profitloss}")
    txtfile.write('\n'f"Average Change: ${round(average,2)}")
    txtfile.write('\n'f"Greatest Increase in Profits: {profitdate} (${greatestprofit})")
    txtfile.write('\n'f"Greatest Decrease in Profits: {lossdate} (${greatestloss})")
