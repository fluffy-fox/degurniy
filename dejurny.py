#!/usr/bin/python3
# coding: utf8

import datetime
import calendar
import io
import os
from datetime import date, timedelta


def duty_today(man: list):
    """ Определяет кто сегодня дежурный в группе.
    В текстовом файле people указать список людей, задействованных в смене. Очередность указывается
    в соответствии с тем, кто дежурит 1 числа месяца с 8:00 утра, кто 2-ого итд. Смены по 24 часа с 8:00. """
    now = datetime.datetime.now()  # сегодняшнее время с датой
    now_time = now.time()  # время  -  часы и минуты наример datetime.time(8, 00)
    total_days_in_year = 366 if calendar.isleap(date.today().year) else 365  # количество дней в году
    first_day_of_year = datetime.datetime(date.today().year, 1, 1, )  # первый день в году
    day_number = (now - first_day_of_year).days + 1  # порядковый номер дня в году например (38)
    start = datetime.time(8, 00)  # Начало смены
    end_day = datetime.time(23, 59)  # конец суток
    new_day = datetime.time(00, 00)  # начало новых суток
    end = datetime.time(7, 59)  # Конец смены
    list_of_days_in_year = [x for x in range(1, total_days_in_year + 1)]  # список номеров дней в году
    for person_num in range(len(man)):
        if day_number in list_of_days_in_year[person_num::len(man)] and start <= now_time <= end_day:
            print(man[person_num])
    for person_num in range(len(man)):
        if day_number in list_of_days_in_year[person_num::len(man)] and new_day <= now_time <= end:
            if person_num == len(man):
                print(man[1])
            else:
                print(man[person_num - 1])


path = os.path.dirname(os.path.realpath(__file__))
with io.open(os.path.join(path, "people"), encoding='utf-8') as f:
    people = f.read().splitlines()

duty_today(people)
