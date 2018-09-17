# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 19:01:30 2018

@author: Wei Wu
"""

import datetime
import pandas as pd

# year = 2021
# start = year//100*1000000 + 101
# end = year//100*1000000 + 991231

# dates = pd.date_range(start=str(start), end=str(end), freq='D')

# target = 38
# counter = 0
# target_format = '%m%d%Y'  # The format
# for i in dates:
#     date_string = datetime.datetime.strftime(i.date(), target_format)
#     seven_digits = date_string[1:]
#     if date_string == date_string[::-1] or (seven_digits == seven_digits[::-1] and date_string.startswith('0')):
#         counter += 1
# if date_string == date_string[::-1]:
#     print(date_string)
# else:
#     print(date_string, seven_digits)
# print(counter)


import datetime
import pandas as pd


def num_palindromes(year):
    "create date range for the input year's century"
    start = year//100*1000000 + 101
    end = year//100*1000000 + 991231
    dates = pd.date_range(start=str(start), end=str(end), freq='D')

    counter = 0
    target_format = '%m%d%Y'  # The palindromes date format
    for i in dates:
        # transform datetime to string
        date_string = datetime.datetime.strftime(i.date(), target_format)
        seven_digits = date_string[1:]
        if date_string == date_string[::-1] or (seven_digits == seven_digits[::-1] and date_string.startswith('0')):
            counter += 1

    return counter


print(num_palindromes(2011))
