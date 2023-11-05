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


def alert_system():

    #print(student_email_information)

    template = """
            Dear [Student Name] [Student id],
            [Programme] [School Name]
            I hope this message finds you well.
            Upon recent evaluation of academic performance, it has been determined that [School Name] has fallen below the expected academic standards. As a result, the student is now placed on academic probation.
            We believe in the potential of every student and are dedicated to assisting them in achieving their academic goals. To this end, the university provides additional resources, including tutoring services and counseling, to support students during their studies. We encourage the student in question to take advantage of these resources and work closely with their advisor to create a plan for improvement.
            We appreciate your understanding and cooperation in this matter. Please remember that our collective efforts play a crucial role in ensuring the success of every student within our institution.
            If you have any questions or concerns, please do not hesitate to reach out to the Academic Affairs Office.
            Best regards, 
            """

    students = [
        {'name': 'John Smith', 'id': '1234567890', 'gpa': 2.2, 'school': 'Scit', 'program': 'Fenc',
            'email': 'john.smith@example.com'},
        #{'name': 'Jane Doe', 'id': '9876543210', 'gpa': 2.0, 'school': 'Arts', 'program': 'Eng','email': 'jane.doe@example.com'},
        {'name': 'Peter Jones', 'id': '0123456789', 'gpa': 3.0, 'school': 'Business', 'program': 'BBA',
            'email': 'peter.jones@example.com'},
        {'name': 'Mary Johnson', 'id': '8901234567', 'gpa': 1.1, 'school': 'Education', 'program': 'BEd',
            'email': 'ea@gmail.com'},
        {'name': 'Susan Williams', 'id': '6789012345', 'gpa': 4.0, 'school': 'Medicine', 'program': 'MBBS',
            'email': 'susan.williams@example.com'}
    ]
    template_copy = None

    for student in students:
        template_copy = str(template)
        for field in ['name', 'id', 'school', 'program', 'gpa']:
            if field == 'gpa':
                template_copy = template_copy.replace(f'[{field}]', str(student['gpa']))
            else:
                template_copy = template_copy.replace(f'[{field}]', student[field])

        # Replace the placeholders in the email template with the student's information
        template_copy = template_copy.replace('[Student Name]', student['name'])
        template_copy = template_copy.replace('[School Name]', student['school'])
        template_copy = template_copy.replace('[Programme]', student['program'])
        template_copy = template_copy.replace('[Student id]', student['id'])
    # Send the email to the student if their GPA is less than or equal to 2.2
        if student['gpa'] <= 2.2:
            send_email('artiintel6@gmail.com', 'vnov zbob lkcu hnxy', 'osnhysjsxqejezpouu@cazlq.com',
                       'Important Notice: Academic Status Update', template_copy)

    time.sleep(26298 * 3)
