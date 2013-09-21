# -*- coding:utf-8 -*-
from monthdelta import MonthDelta
import datetime


def prev_month(date, length):
    """Back one month and preserve day if possible"""
    return date + MonthDelta(-length)


def add_month(date, length):
    return date + MonthDelta(+ length)


def prev_year(date):
    return date + MonthDelta(-12)


def convert_to_list_month(start_date, stop_date):
    range_month = stop_date.month - start_date.month + 1
    if range_month < 0:
        first_month = 12 - start_date.month
        range_month = first_month + stop_date.month
    months_choices = []
    for i in range(1, range_month):
        month = add_month(start_date, i)
        months_choices.append((month.month, datetime.date(start_date.year, month.month, 1).strftime('%B')))
    return months_choices

def french_month(number_month):
    list_month = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre','Decembre']
    return list_month[number_month - 1]
