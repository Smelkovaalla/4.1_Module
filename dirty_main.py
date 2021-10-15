from package import *
from package.people import get_employees
from package.salary import calculate_salary

if __name__ == '__main__':
    print(calculate_salary())
    print(get_employees())
