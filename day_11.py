import datetime

def calculate_diff_in_days(dt1: datetime, dt2: datetime) -> int:
    return abs(dt2 - dt1).days


if __name__ == "__main__":

    try:
        date1 = input("Enter the first date (DD/MM/YYYY): ")
        date2 = input("Enter the second date (DD/MM/YYYY): ")
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)

    try:
        date1_obj = datetime.datetime.strptime(date1, "%d/%m/%Y")
        date2_obj = datetime.datetime.strptime(date2, "%d/%m/%Y")
        print(f"The number of days between {date2} and {date1} is {calculate_diff_in_days(date1_obj, date2_obj)} days.")
    except ValueError as e:
        print(f"Error: {e}")