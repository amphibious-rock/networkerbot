import csv
from datetime import date
import matplotlib.pyplot as plt


'''
CSV Year
csv_year.csv

Month Number
Month Name
Month Total
Days In Month


CSV Month
csv_month.csv
day
daily total

'''
def print_array(array):
    for row in array:
        print(row)
        
        
def extract_csv(filename):
    data = []
    csv_file = open(filename,"r") #open the csv file
    csvreader = csv.reader(csv_file)
    
    for row in csvreader:
        if len(row) > 3:
            data.append(row)
        
    csv_file.close()
    return data


def commands_increase():
    #extract dates
    date_file = open("last_command.txt","rt")
    date_now = date.today()
    
    last_date = (date_file.read()).split("-")
    now_date = str(date_now).split("-")
    date_file.close()
    
    date_file = open("last_command.txt","wt")
    date_file.write(str(date_now))
    date_file.close()
    
    last_day, last_month, last_year = last_date[2], last_date[1], last_date[0]
    now_day, now_month, now_year = now_date[2], now_date[1], now_date[0]
    
    
    # Load Databases
    year_data = extract_csv("csv_year.csv") #Month No, Month Name, Month Tot, Days
    month_data = extract_csv("csv_month.csv") # Day No, Daily Tot

    # compare and act on changes. Year --> Month --> Day
    # If Year != old year --> drop year
    # If Month != old month --> Drop month
    
    

    if now_year != last_year: #If it is a new year, wipe all data
        for m in range(0,(len(year_data[1])-1)):
            year_data[1][m] = 0
            
        print("HAPPY NEW YEAR!!!!! - All Year Data Wiped")
        
    
    if now_month != last_month:
        for d in range(0,(len(month_data[1])-1)):
            month_data[1][d] = d
            
    
    # add 1 to correct sections
    #month --> year[month-1]
    #day --> month[1][day-1]
    
    #increment data
    #print_array(month_data)
    month_data[1][int(now_day)-1] = int(month_data[1][int(now_day)-1]) + 1
    year_data[2][int(now_month)-1] = int(year_data[2][int(now_month)-1]) + 1
    
    #WRITE DATA YOU DINGLEBERRY
    csv_file = open("csv_month.csv","w") #open the csv file to write
    csvwriter = csv.writer(csv_file)
    csvwriter.writerows(month_data)
    csv_file.close()
    
    csv_file = open("csv_year.csv","w") #open the csv file to write
    csvwriter = csv.writer(csv_file)
    csvwriter.writerows(year_data)
    csv_file.close()
    
    
    
    
def extract_stats():
    #extract dates
    date_now = date.today()
    now_date = str(date_now).split("-")
    now_day, now_month, now_year = now_date[2], now_date[1], now_date[0]

    daily_total = 0
    monthly_daily_avg = 0
    monthly_total = 0
    yearly_monthly_avg = 0
    yearly_total = 0
    
    year_data = extract_csv("csv_year.csv")
    month_data = extract_csv("csv_month.csv")
    
    #-----------------------------------------#
    
    daily_total = month_data[1][int(now_day)-1]
    
    temp_total=0
    for i in month_data[1]:
        temp_total += int(i)
    
    temp_avg = temp_total/int(now_day)
    monthly_daily_avg = temp_avg
    
    monthly_total = temp_total
    
    temp_total = 0
    for i in year_data[2]:
        temp_total += int(i)
    temp_avg = temp_total/int(now_month)
    
    yearly_monthly_avg = temp_avg
    yearly_total = temp_total
    
    stats = [daily_total, monthly_daily_avg, monthly_total, yearly_monthly_avg, yearly_total]
    
    for i in range(0,len(month_data[1])-1):
        month_data[1][i] = int(month_data[1][i])
    
    
    fig, ax = plt.subplots( nrows=1, ncols=1, figsize=(15, 6))# create figure & 1 axis
 
    x_axis = month_data[0][0:int(year_data[3][int(now_month)-1])]
    y_axis = month_data[1][0:int(year_data[3][int(now_month)-1])]
    #print(x_axis,"\n\n\n",y_axis,"\n\n",len(x_axis),len(y_axis))
    ax.plot(x_axis, y_axis)
    fig.savefig('month.png')   # save the figure to file
    plt.close(fig)

    
    fig, ax = plt.subplots( nrows=1, ncols=1, figsize=(15, 6))# create figure & 1 axis
 
    x_axis = year_data[1]
    y_axis = year_data[2]
    #print(x_axis,"\n\n\n",y_axis,"\n\n",len(x_axis),len(y_axis))
    ax.plot(x_axis, y_axis)
    fig.savefig('year.png')   # save the figure to file
    plt.close(fig)
    
    return stats


#extract_stats()


'''
Total cmds today      CSV Month         total[today]
This Month's average cmds per day         CSV Month         sum(total))/date
Total This month         CSV Month         sum(total)
Graph of commands this month         CSV Month         y=Total

This Year's Average cmds per month         CSV Year         sum(total))/month
Total This Year         CSV Year         sum(total)
Graph of Total Monthly         CSV Year         y=Total
'''
