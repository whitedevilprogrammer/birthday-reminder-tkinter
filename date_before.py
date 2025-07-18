import datetime

v = datetime.datetime.now()
rd = v.strftime('%d')
rm = v.strftime('%m')
ry = v.strftime('%Y')
dates = '15'
months = '10'
years = '2021'
d = int(dates)
m = int(months)
y = int(years)
def Remainder_today(d,m,y):
    d = int(d);m = int(m);y = int(y)
    return d, m, y
# this is month birthday list showing.
def Remainder_for_one_day(d, m, y):  # 1 day before !
    d = int(d);m = int(m);y = int(y)
    if m == 1 and d == 1:  # first month and also 1 and 2 days than change the before year(example)1/2/2021 then
        m = 12
        y = int(ry) - 1
        if d == 1:
            d = 31
    elif 1 < m and d == 1:
        m = m - 1
        if y % 4 == 0:
            leep_year = True
        else:
            leep_year = False

        if m in (1, 3, 5, 7, 8, 10, 12):
            last_day_num = 31
        elif m in (4, 6, 9, 11):
            last_day_num = 30
        elif leep_year:
            last_day_num = 29
        else:
            last_day_num = 28

        if d == 1:
            d = last_day_num
    else:
        d = d - 1
    return d, m, y


def Remainder(d,m,y): # 2 day before !
    d = int(d);m = int(m);y = int(y)
    if m == 1 and d in [1,2]: # first month and also 1 and 2 days than change the before year(example)1/2/2021 then
        m = 12
        y = int(ry) - 1
        if d == 2:
            d = 31
        elif d == 1:
            d = 30
    elif 1 < m and d in [1,2]:
        m = m - 1
        if y % 4 == 0:
            leep_year = True
        else:
            leep_year = False
            
        if m in (1,3,5,7,8,10,12):
            last_day_num = 31
        elif m in (4,6,9,11):
            last_day_num = 30
        elif leep_year:
            last_day_num = 29
        else:
            last_day_num = 28

        if d == 2:
            d = last_day_num
        elif d == 1:
            d = last_day_num - 1
    else:
        d = d - 2
    return d,m,y


def Remainder_for_3day_before(d, m, y):
    d = int(d)
    m = int(m)
    y = int(y)
    if m == 1 and d in [1, 2, 3]:  # first month and also 1 and 2 days than change the before year(example)1/2/2021 then
        m = 12
        y = int(ry) - 1
        if d == 3:
            d = 31
        elif d == 2:
            d = 30
        elif d == 1:
            d = 29
    elif 1 < m and d in [1, 2, 3]:
        m = m - 1
        if y % 4 == 0:
            leep_year = True
        else:
            leep_year = False

        if m in (1, 3, 5, 7, 8, 10, 12):
            last_day_num = 31
        elif m in (4, 6, 9, 11):
            last_day_num = 30
        elif leep_year:
            last_day_num = 29
        else:
            last_day_num = 28

        if d == 3:
            d = last_day_num
        elif d == 2:
            d = last_day_num - 1
        elif d == 1:
            d = last_day_num - 2
    else:
        d = d - 3
    return d, m, y

def Remainder_for_1week_before(d, m, y):
    d = int(d);m = int(m);y = int(y)
    if m == 1 and d in [1, 2,3,4,5,6,7]:  # first month and also 1 and 2 days than change the before year(example)1/2/2021 then
        m = 12
        y = int(ry) - 1
        if d == 7:
            d = 31
        elif d == 6:
            d = 30
        elif d == 5:
            d = 29
        elif d == 4:
            d = 28
        elif d == 3:
            d = 27
        elif d == 2:
            d = 26
        elif d == 1:
            d = 25
    elif 1 < m and d in [1, 2, 3,4,5,6,7]:
        m = m - 1
        if y % 4 == 0:
            leep_year = True
        else:
            leep_year = False

        if m in (1, 3, 5, 7, 8, 10, 12):
            last_day_num = 31
        elif m in (4, 6, 9, 11):
            last_day_num = 30
        elif leep_year:
            last_day_num = 29
        else:
            last_day_num = 28

        if d == 7:
            d = last_day_num
        elif d == 6:
            d = last_day_num - 1
        elif d == 5:
            d = last_day_num - 2
        elif d == 4:
            d = last_day_num - 3
        elif d == 3:
            d = last_day_num - 4
        elif d == 2:
            d = last_day_num - 5
        elif d == 1:
            d = last_day_num - 6
    else:
        d = d - 7
        print(d, 'this is notification function')
    return d, m, y

#f = Remainder(d,m,y)
##print(f)
##print(d)
##print(m)
##print(y)

