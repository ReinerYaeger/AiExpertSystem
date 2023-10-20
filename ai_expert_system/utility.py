import datetime
import time

from ai_expert_system import database_manager


def get_year():
    year_list = list(range(1999, int(datetime.datetime.now().strftime("%Y")) + 1))

    previous_year = 1999
    year_str = []
    for i in year_list:
        i += 1
        year_str.append(f'{previous_year}/{i}')
        previous_year += 1

    return year_str


def get_list_of_schools():
    school_list = ['SCIT', 'SOE', 'CSN', 'COBAM', 'CAHW', 'SOP', 'STVE', 'SHSS', 'FOW', 'SBLM', 'CSA', 'SMS', 'CSSS',
                   'SNAS', 'COHS', 'SPHHT']
    return school_list


def alert_system():
    while True:
        print(1)
        time.sleep(2629800 * 3)

    # database_manager.get_all_students_gpa()
