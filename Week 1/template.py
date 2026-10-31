"""
RECORD CHECK  -  my version
===========================

Name  :Rutendo Mandizvidza
Lane  :  Cyber
Date  : 26/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

"""asking user for source ip, failed logins and total attempts; calculating difference and percentage before finally printing the report"""

source_IP = input("Enter Source IP: ")#prompting user to enter label
failed_logins = float(input("Enter failed logins: "))#prompting user to enter num of failed logins
total_attempts = float(input("Enter total attempts"))#prompting user to enter num of total attempts



difference = total_attempts - failed_logins # difference between total attempts and failed logins
percent = ((failed_logins/total_attempts) * 100)     #the failed logins as a percentage of the total attempts




print()
print("=" * 34)
print(f"  RECORD CHECK  -  {source_IP}")
print("=" * 34)
print(f"{'Failed logins :':>10} {failed_logins:>11} \n{'Total attempts :':>10} {total_attempts:>10} \n{'Difference :':>10} {difference:>+15.2f} \n{'Percent :':>10} {percent:>17.2f}% ") #displays line by line the 2 other inputs plus difference and failed logins as a percentage of total attempts




print("=" * 34)#border line

