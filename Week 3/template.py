"""
RECORD CHECK  -  my version
===========================

Name  :  Rutendo Mandizvidza
Lane  :  Cyber
Date  :  08/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""




def status_of(percent):#defining function status_of that takes 'percent' and an optional parameter 'warning_at' with a default value of 90. It returns a status based on value of 'percent'
   """returns the status based on the value of percent"""
   if percent >= 100:
        return "OVER LIMIT" 
   elif percent >= 90:
        return "WARNING"
   else:
        return "OK"

def check_record(value,limit):
    """returns the difference and percentage of failed logins"""
    difference = value - limit
    percent = ((value/limit)* 100)
    return difference, percent#returning both difference and percent in the same line as a tuple as return cannot be written twice in the same function definition

def print_report(source_ip, failed_logins, total_attempts, difference, percent, status):
    """Prints the report"""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {source_ip}")
    print("=" * 34)
    
    print(f"  Failed Logins : {failed_logins}")
    print(f"  Total Attempts : {total_attempts}")
    print(f"  Difference : {difference:>+10.2f}")
    print(f"  Percentage : {percent:>10.2f}%")
    print(f"  Status : {status}")
        
    
    print("=" * 34)
    
    

    return 

def report_summary(over_limits):
    """Prints number of records over the limit"""
    print(f"Total records Over Limit: {over_limits}")#displays only after desired records have been checked
    print("=" * 34)
    return 

over_limit = 0
source_ip = input("Enter source IP: ") 
while source_ip != "quit":      #loops until user enters 'quit' to exit the loop
    failed_logins = float(input("Enter failed logins: "))     #prompting user to enter failed logins and converting it to float
    total_attempts = float(input("Enter total attempts: "))     # prompting user to enter total attempts and converting it to float
    

    status =status_of((failed_logins / total_attempts) * 100)
    if status == "OVER LIMIT":
        over_limit+=1
    difference, percent = check_record(failed_logins, total_attempts)
    print_report(source_ip, failed_logins, total_attempts, difference, percent, status)
    source_ip = input("Enter source IP: ") #prompting user to enter new ip adress before quitting
report_summary(over_limit)



