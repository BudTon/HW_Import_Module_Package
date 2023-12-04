from application.salary import *
from application.db.people import *
from main import data_today

if __name__ == '__main__':

    calculate_salary()
    get_employees()
    data_today()