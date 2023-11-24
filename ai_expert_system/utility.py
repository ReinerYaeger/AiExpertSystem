# Matthew Samuels - 2005744
# Chevaughn Gibson - 1900396
# Gail-Ann Archer - 2002407

import datetime
import smtplib
from email.mime.text import MIMEText
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


def send_email(sender_email, sender_password, recipient_email, subject, body):
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = recipient_email

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())
        server.quit()
        print('Email sent successfully!')
    except Exception as e:
        print(f'Error: {e}')


def alert_system(probation_list):
    while True:
        # print(student_email_information)

        template = """
                Dear [Student Name] [Student id],
                This is an automated message from the probation system.
                [Programme] [School Name]
                I hope this message finds you well.
                Upon recent evaluation of academic performance, it has been determined that [Student Name] has fallen below the expected academic standards. As a result, the student is now placed on academic probation.
                We believe in the potential of every student and are dedicated to assisting them in achieving their academic goals. To this end, the university provides additional resources, including tutoring services and counseling, to support students during their studies. We encourage the student in question to take advantage of these resources and work closely with their advisor to create a plan for improvement.
                We appreciate your understanding and cooperation in this matter. Please remember that our collective efforts play a crucial role in ensuring the success of every student within our institution.
                If you have any questions or concerns, please do not hesitate to reach out to the Academic Affairs Office.
                Best regards, 
                """

        template_copy = None

        for student in probation_list:
            template_copy = str(template)
            for field in ['name', 'id', 'email', 'school', 'program', 'gpa']:
                template_copy = template_copy.replace(f'[{field}]', str(student[field]))
            # Replace the placeholders in the email template with the student's information
            template_copy = template_copy.replace('[Student Name]', student['name'])
            template_copy = template_copy.replace('[School Name]', student['school'])
            template_copy = template_copy.replace('[Programme]', student['program'])
            template_copy = template_copy.replace('[Student id]', student['id'])
            # Send the email to the student if their GPA is less than or equal to 2.2
            recipients = [student['email'], "academic_advisor@utech.edu.jm", 'faculty_administrator@utech.edu.jm', student['program']+'_dir@utech.edu.jm']
            for recipient in recipients:
                send_email('artiintel6@gmail.com', 'vnov zbob lkcu hnxy', recipient,
                           'Important Notice: Academic Status Update', template_copy)

        time.sleep(26298 * 3)
