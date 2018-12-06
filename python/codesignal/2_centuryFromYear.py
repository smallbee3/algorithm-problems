"""
2_centuryFromYear

Given a year, return the century it is in.
The first century spans from the year 1 up to and including the year 100,
the second - from the year 101 up to and including the year 200, etc.


Example

For year = 1905, the output should be centuryFromYear(year) = 20;
For year = 1700, the output should be centuryFromYear(year) = 17.


"""
"""
181205

Subject - Century calculation

"""


def centuryFromYear(year):
    if year % 100:
        century_year = year // 100 + 1
    else:
        century_year = year // 100
    return century_year

    # return year // 100 + 1 if year % 100 else year // 100


# Che1 - string 으로 할 수 있다는 것을 보여주기 위해서

# 181205
# Error fixed with 'index_num = len(year_str) - 2'


def centuryFromYear(year):

    year_str = str(year)
    if year_str[-2:] > "00":
        return year//100 + 1
    else:
        index_num = len(year_str) - 2
        return int(year_str[:index_num])


# result = centuryFromYear(1905)
# result = centuryFromYear(1234)
# result = centuryFromYear(1700)
# result = centuryFromYear(1)
# result = centuryFromYear(101)
result = centuryFromYear(300)
print(result)
