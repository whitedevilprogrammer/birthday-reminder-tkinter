import datetime
def start_process():
    #d ={}
    m1 = []
    m2 = []
    m3 = []
    m4 = []
    m5 = []
    m6 = []
    m7 = []
    m8 = []
    m9 = []
    m10 = []
    m11 = []
    m12 = []
    test = []
    list_d = []
    list_n = []
    with open('all_brithday_list.txt', 'r') as f1:
        al = f1.readlines()
        for i in al:
            name = i.split(':')[0].upper()
            date = i.split(':')[-1][:-1]
            dates, months, years = date.split('/')
            #all = datetime.datetime(int(years), int(months), int(dates))
            #v = all.strftime("%d %b %Y")
            #test.append(v)
            list_d.append(date)
            list_n.append(name)
            #d[date] = name
            if 1 == int(months):
                m1.append(str(date))
            elif 2 == int(months):
                m2.append(str(date))
            elif 3 == int(months):
                m3.append(str(date))
            elif 4 == int(months):
                m4.append(str(date))
            elif 5 == int(months):
                m5.append(str(date))
            elif 6 == int(months):
                m6.append(str(date))
            elif 7 == int(months):
                m7.append(str(date))
            elif 8 == int(months):
                m8.append(str(date))
            elif 9 == int(months):
                m9.append(str(date))
            elif 10 == int(months):
                m10.append(str(date))
            elif 11 == int(months):
                m11.append(str(date))
            elif 12 == int(months):
                m12.append(str(date))
    #print(d)
    #print(test)
    #test.sort()
    print(len(test))
    all_months = [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
    for i in all_months:
        print(i)
    M1 = []
    M2 = []
    M3 = []
    M4 = []
    M5 = []
    M6 = []
    M7 = []
    M8 = []
    M9 = []
    M10 = []
    M11 = []
    M12 = []
    all_new_months = [M1,M2,M3,M4,M5,M6,M7,M8,M9,M10,M11,M12]
    for one_month in all_months:
        if len(one_month) == 0:
            pass
            #print('This month is empty !!')
        elif len(one_month) == 1:
            ins = all_months.index(one_month)
            all_new_months[ins].append(one_month[0])
            #print('{} : {}'.format(d[one_month[0]],one_month[0]))
        elif 1 < len(one_month):
            ins = all_months.index(one_month)
            #print(ins)
            #print(one_month)
            for j in one_month:
                ds = j.split('/')[0]
                test.append(int(ds))
            test.sort()
            for k in test:
                for p in one_month:
                    ds = p.split('/')[0]
                    if int(ds) == int(k):
                        all_new_months[ins].append(p)
                        one_month.remove(p)
                        #print()
            #print(test)
            test = []
            #print(test)
            #print(test)

    # for i in all_months:
    #     print(i)
    # for new_months in all_new_months:
    #     print(new_months)
    list_dates = list_d# list(d.keys())
    list_names = list_n #list(d.values())
    print(list_names)
    print(list_dates)
    #with open('all_brithday_list.txt', 'w') as f
    with open('all_brithday_list.txt', 'w') as f:
        for new_months in all_new_months:
            for one_time in new_months:
                for dat in list_dates:
                    if one_time == dat:
                        index_value = list_dates.index(dat)
                        format = f'{list_names[index_value].upper()}:{list_dates[index_value]}\n'
                        f.write(format)
                        #print(f" {count}) {list_names[index_value]} {list_dates[index_value]}")
                        list_dates.pop(index_value)
                        list_names.pop(index_value)



