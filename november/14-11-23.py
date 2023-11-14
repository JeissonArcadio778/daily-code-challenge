"""
https://www.hackerrank.com/challenges/day-of-the-programmer/problem?isFullScreen=true
"""
import math
import os
import random
import re
import sys



def redondear(n: float, decimals: int = 0) -> float:
    expoN = n * 10 ** decimals
    if abs(expoN) - abs(math.floor(expoN)) < 0.1:
        return math.floor(expoN) / 10 ** decimals
    return math.ceil(expoN) / 10 ** decimals

def date_transform(days, year):
    months = (12 * days) / 365
    _months = (12 * days) // 365
    months_int = int(redondear(months))
    
    days = int(redondear(30 * (months - _months)))
    
    return f"{days}.0{months_int}.{year}"
    

def dayOfProgrammer(year):
    jul_years = list(range(1699, 1918))
    gre_years = list(range(1918, 2701))
    adjustment_year = 1918
    
    if year == adjustment_year:
        if year % 4 == 0:
            print(date_transform(255 + 14, year))
            return (date_transform(255 + 14, year))
        else:
            print(date_transform(256 + 13, year))
            return (date_transform(256 + 13, year))
                
    
    for jul_year in jul_years:
        if year == jul_year:
            if year % 4 == 0:
                print(date_transform(255, year))
                return (date_transform(255, year))
            else:
                print(date_transform(256, year))
                return (date_transform(256, year))

    for gre_year in gre_years:
        if year == gre_year:
            if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
                print("Bisiesto, grego")
                print(date_transform(255, year))
                return (date_transform(255, year))
            else:
                print("Normal, grego")
                print(date_transform(256, year))
                return (date_transform(256, year))
    


dayOfProgrammer(1918)

