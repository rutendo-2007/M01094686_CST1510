"""
RECORD CHECK  -  my version
===========================

Name  :Rutendo Mandizvidza
Lane  :  Cyber 
Date  :02/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
"""using while loop to ask user for source ip, failed logins and total attempts; calculating difference and percentage before finally printing the report and number of reports over the limit outside the loop"""

over_limit = 0
source_ip = input("Enter source IP: ") 
while source_ip != "quit":      #loops until user enters 'quit' to exit the loop
    failed_logins = float(input("Enter failed logins: "))     #prompting user to enter failed logins and converting it to float
    total_attempts = float(input("Enter total attempts: "))     # prompting user to enter total attempts and converting it to float




    difference = total_attempts - failed_logins   # calculating difference between total attempts and failed logins
    percent = ((failed_logins / total_attempts) * 100)   # calculating failed logins as a perecentage   of total attempts
# Deciding a status and store it in a variable called status.
    if percent >= 100:
        status = "OVER LIMIT"
        over_limit += 1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {source_ip}")
    print("=" * 34)

    print(f"  Failed Logins : {failed_logins:>10}")
    print(f"  Total Attempts : {total_attempts:>10}")
    print(f"  Difference : {difference:>+10.2f}")
    print(f"  Percentage : {percent:>10.2f}%")
    print(f"  Status : {status:>10}")
    

    print("=" * 34)
    source_ip = input("Enter source IP: ") #prompting user to enter new ip adress before quitting

print(f"Total records Over Limit: {over_limit}")#displays only after desired records have been checked
print("=" * 34)



