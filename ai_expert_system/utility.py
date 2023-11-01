import datetime
import time
from django.core.mail import send_mail

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


def alert_system(students_on_probation):
    print(5)
    #
    # while True:
    #     records = database_manager.get_all_students_gpa()
    #     for record in records:
    #         if float(record[6]) <= 2.2:
    #
    #             with open('email_template', 'r') as file:
    #                 message_template = file.read()
    #
    #             customized_message = message_template.replace('[Student Name]', record[1])
    #             customized_message = message_template.replace('[Student id]', record[0])
    #             customized_message = customized_message.replace('[Programme]', record[4])
    #             customized_message = customized_message.replace('[School Name]', record[4])
    #
    #     time.sleep(2629800 * 3)
