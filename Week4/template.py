"""
RECORD CHECK  -  my version
===========================

Name  : Rutendo Mandizvidza
Lane  :   Cyber 
Date  : 16/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


def check_record(value,limit):
    """returns the difference and percentage of failed logins"""
    difference = value - limit
    percent = ((value/limit)* 100)
    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "OK"

    return difference, percent, status#returning  difference ,percent and status

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



"""opening, writing a dictionary in my_record text file"""
with open("my_record.txt", "w") as f:#opening file to be able to write in file
    f.write("10.08.07,60,100\n")
    f.write("10.07.06,80,70\n")
    f.write("10.05.04,60,50\n")

"""reading records_sample.txt line by line and spliting the line"""
def load_records(path):
    """reads `label,value,limit` lines from a file and returns a list of dicts"""
    records = []
    try:
        with open(path) as f:
            for line in f:
                line = line.strip()
                source_ip, failed_logins, total_attempts = line.split(",")#spliting the line to store separate values in variables
                failed_logins = float(failed_logins)
                total_attempts = float(total_attempts)
                records.append({"source_ip": source_ip, "failed_logins": failed_logins, "total_attempts": total_attempts})
    except FileNotFoundError:
        print(f"File {path} not found.")
        return []
    return records




records = load_records("my_record.txt")
over_limit = 0

with open("my_results.txt", "w") as f:
    for rec in records:
        difference, percent, status = check_record(rec["failed_logins"], rec["total_attempts"])
        print_report(rec["source_ip"], rec["failed_logins"], rec["total_attempts"], difference, percent, status)
        f.write(f"{rec['source_ip']} : {status}\n")

        if status == "OVER LIMIT":
            over_limit += 1

   
       
              
print(f"Total OVER LIMIT: {over_limit}")



        
file1 = load_records("my_record.txt")
file2 = load_records("nah.txt")#testing code
print(f"{file1}\n {file2}")
       


