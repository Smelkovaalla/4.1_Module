from application import salary
from db import people
from datetime import datetime, date, time

if __name__ == '__main__':
    print(salary.calculate_salary())
    print(people.get_employees())
    print(datetime.now())