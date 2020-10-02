import os
import csv

pybank_csv = os.path.join("Resources","budget_data.csv")

#lists to store the data I aquire

#Delcare variables to store values 

month_counter = 0
sum_profit = []
value_change = []
month_change = []
change_begin = 0
profit_data = []


#Read the file and move onto next line since there is no data on the first row

with open(pybank_csv , "r" ) as csvfile :
    csv_reader = csv.reader(csvfile, delimiter = "," )
    csv_header = next(csvfile)

    #For loop which will produce all of my values

    for row in csv_reader:
        # Count for the total number of months
        if row[0] > "": 

            month_counter = month_counter +1
        #Sum of profits
        profit_data.append(row[1])
    #average of changes in
    averange_change = int(profit_data[-1]) - int(profit_data[0])/ month_counter

#Store change in between months, since python can only read one row at a time
    change_end = int(row[1])
    value_difference = change_end - change_begin
    value_change.append(value_difference)
    change_begin = int(row[1])
    month_change.append(row[0])
    
profit_data= list(map(int, profit_data))
sum_profit = sum(profit_data)
#Max Change

max_change = max(value_change)
max_change_index = value_change.index(max_change)
max_month = month_change[max_change_index]        

#Min Change

 
min_change = min(value_change)
min_change_index = value_change.index(min_change)
min_month = month_change[min_change_index]     

#Printing to Terminal

print("Financial Analysis")  
print("-------------------")  
print("Total Months: "+ str(month_counter))  
print("Total : $" + str(sum_profit))  
print("Average Change: $" + str(averange_change))  
print("Greatest Change in Profits: " + str(max_month) + " " + "$" + str(max_change) + ")")  
print("Greatest Decrease in Profits: " + str(min_month) + " " + "$" + str(min_change) + ")")   
 # Printing to a text file
pybank_analysis = os.path.join ("Analysis", "PyBankAnalysis.txt")

with open(pybank_analysis, "w") as text_file:

    text_file.write("Financial Analysis \n")  
    text_file.write("------------------- \n")  
    text_file.write("Total Months: "+ str(month_counter) + "\n")  
    text_file.write("Total : $" + str(sum_profit)+ "\n")  
    text_file.write("Average Change: $" + str(averange_change) + "\n")  
    text_file.write("Greatest Change in Profits: " + str(max_month) + " " + "$" + str(max_change) + ")" + "\n")  
    text_file.write("Greatest Decrease in Profits: " + str(min_month) + " " + "$" + str(min_change) + ")" + "\n")      

