import datetime
from application.db.people import get_employees
from application.salary import calculate_salary
from petrovich.main import Petrovich
from petrovich.enums import Case, Gender

def home_work_task_4(Last_Name):
    p = Petrovich()
    cased_lname = p.lastname(f'{Last_Name}', Case.GENITIVE, Gender.MALE)
    print(cased_lname)

def data_today():
    print(datetime.date.today())

if __name__ == '__main__':

    data_today()
    calculate_salary()
    get_employees()

    Last_Name = 'Иванов'
    home_work_task_4(Last_Name)


