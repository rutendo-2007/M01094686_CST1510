"""
RECORD CHECK  -  my version
===========================

Name  : Rutendo Mandizvidza
Lane  :Cyber     
Date  : 23/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
class Record:
    over_limit_count = 0 #shared attributes amongst all objects
    """defining the attributes of Record"""
    def __init__(self, source_ip, failed_logins, total_attempts):
        self.source_ip = source_ip
        self.failed_logins = failed_logins
        self.total_attempts = total_attempts


    def percent(self):
        """Return failed_logins as a percentage of total_attempts."""
        return (self.failed_logins / self.total_attempts) * 100

    def status(self):
        """Return OVER LIMIT, WARNING or OK based on percent()."""
        percent = self.percent()
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"

    def is_over(self):
        """checks if status is over limit"""
        return self.status() == "OVER LIMIT"





with open("my_records.txt", "w") as f:#opening file to be able to write in file
    f.write("10.03.07,90,10\n")
    f.write("10.09.06,60,70\n")
    f.write("10.07.04,40,30\n")


def load_records(path):
    """Read source_ip,failed_logins,total_attempts from a file and return a list of Records."""
    records = []
    with open(path) as f:
        for line in f:
            source_ip, failed_logins, total_attempts = line.strip().split(",")
            records.append(Record(source_ip, float(failed_logins), float(total_attempts)))
    return records





        
records = load_records("my_records.txt")


for record in records:
    state = record.status()  #calling method status() then storing in a variable
    if state == "OVER LIMIT":
        Record.over_limit_count += 1



    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.source_ip}")
    print("=" * 34)
    print(f"Failed logins : {record.failed_logins:>10}\nTotal attempts: {record.total_attempts:>10}")
    print(f"Percentage: {record.percent():>10.2f}")
    print(f"Status : {state:>10}")
    print("=" * 34)
    

    print("=" * 34)


       
        

print(f"{Record.over_limit_count} of {len(records)} records are OVER LIMIT")