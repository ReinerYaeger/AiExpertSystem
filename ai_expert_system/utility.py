import datetime


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
