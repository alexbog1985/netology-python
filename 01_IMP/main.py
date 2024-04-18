import datetime
from application.salary import calculate_salary
from application.db.people import get_employees
from art import text2art


print(datetime.date.today())


if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print()
    print(text2art("Thanks for checking", font="cybermedium"))
