import sys
import os
import datetime

def main():
    #Display Title and Instructions
    print("Estimated Due Date Calculator")
    print("Input the last menstrual period (LMP) to get the estimated due date (EDD)")

    #Receive Input
    lmp = input("First Day of Last Menstrual Period (LMP) (dd/mm/yyyy): ")
    lmp = convert_to_date(lmp)

    #Calculate EDD
    forty_weeks_edd_due_date = forty_weeks_edd(lmp)
    print("Forty Weeks EDD: " + forty_weeks_edd_due_date.strftime("%d/%m/%Y"))
    naegele_rule_edd_due_date = naegele_rule_edd(lmp)
    print("Naegele's Rule EDD: " + naegele_rule_edd_due_date.strftime("%d/%m/%Y"))

    #Prevent Script from Closing
    os.system("PAUSE")
    
def convert_to_date(value):
    try:
        return datetime.datetime.strptime(value, "%d/%m/%Y")
    except:
        print("Invalid Date Format. Please, input the date in the correct format.")
        sys.exit()

def forty_weeks_edd(lmp):
    forty_weeks_time = datetime.timedelta(weeks = 40)
    due_date = lmp + forty_weeks_time
    return due_date

def naegele_rule_edd(lmp):
    three_months_time = datetime.timedelta(days = 3 * 30)
    one_year_time = datetime.timedelta(weeks = 52)
    seven_days_time = datetime.timedelta(days = 7)
    due_date = lmp - three_months_time + one_year_time + seven_days_time
    return due_date

if __name__ == "__main__":
    main()
