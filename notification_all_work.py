from plyer import notification
import datetime
import date_before
def Notificatios_proccess():
    v = datetime.datetime.now()
    real_date = v.strftime('%d')
    real_month = v.strftime('%m')
    real_year = v.strftime('%Y')
    m = v.strftime('%m')
    Real_year = v.strftime('%Y')
    # print(int(y) -1)
    # print(m)
    d = {}
    namess = []
    datess = []
    notification_name = []
    notification_date = []
    with open('all_brithday_list.txt', 'r') as f1:
        al = f1.readlines()
        # print('Birthday list')
        # [print(f'{j+1})',al[j]) for j in range(len(al))]
        for i in al:
            name = i.split(':')[0].lower()
            date = i.split(':')[-1][:-1]
            d[name] = date
            dates, months, years = date.split('/')
            #todo intha idathula remaind add pannanum >>>>
            with open('remind_setting.txt','r') as f:
                al = f.readlines()
                if int(al[0]) == 1:
                    #print('today coding')
                    D, M, Y = date_before.Remainder_today(dates, months, Real_year)
                    #Y = 2221
                    if f'{D}/{M}/{Y}' == f'{int(real_date)}/{int(real_month)}/{int(real_year)}':
                        notification.notify(title="Birthday Remainder !",
                                            message=f"{name}'s birthday in Today",
                                            app_name='Birthday Remainder !!',
                                            app_icon='code.ico',
                                            # displaying time
                                            timeout=2,
                                            ticker='Bithday Remainder !!!!!')
                if int(al[1]) == 2:
                    print('1 day before')
                    D, M, Y = date_before.Remainder_for_one_day(dates, months, Real_year)
                    #Y = 2221
                    if M == int(m):
                        if f'{D}/{M}/{Y}' == f'{int(real_date)}/{int(real_month)}/{int(real_year)}':
                            notification.notify(title="Birthday Remainder !",
                                                message=f"{name}'s birthday in one day",
                                                app_name='Birthday Remainder !!',
                                                app_icon='code.ico',
                                                # displaying time
                                                timeout=2,
                                                ticker='Bithday Remainder !!!!!')

                if int(al[2]) == 3:
                    D, M, Y = date_before.Remainder(dates, months, Real_year)# two days before remainder date time year !
                    #m = 1
                    if M == int(m):
                        if f'{D}/{M}/{Y}' == f'{int(real_date)}/{int(real_month)}/{int(real_year)}':
                            notification.notify(title="Birthday Remainder !",
                                                message=f"{name}'s birthday in two days",
                                                app_name='Birthday Remainder !!',
                                                app_icon='code.ico',
                                                # displaying time
                                                timeout=2,
                                                ticker='Bithday Remainder !!!!!')
                if int(al[3]) == 4:
                    D, M, Y = date_before.Remainder_for_3day_before(dates, months, Real_year)
                    if M == int(m):
                        if f'{D}/{M}/{Y}' == f'{int(real_date)}/{int(real_month)}/{int(real_year)}':
                            notification.notify(title="Birthday Remainder !",
                                                message=f"{name}'s birthday in Three days",
                                                app_name='Birthday Remainder !!',
                                                app_icon='code.ico',
                                                # displaying time
                                                timeout=2,
                                                ticker='Bithday Remainder !!!!!')

                if int(al[4]) == 5:
                    print('1 week before')
                    D, M, Y = date_before.Remainder_for_1week_before(dates, months, Real_year)
                    print(M, int(m))
                    if M == int(m):
                        if f'{D}/{M}/{Y}' == f'{int(real_date)}/{int(real_month)}/{int(real_year)}':
                            notification.notify(title="Birthday Remainder !",
                                                message=f"{name}'s birthday in one week",
                                                app_name='Birthday Remainder !!',
                                                app_icon='code.ico',
                                                # displaying time
                                                timeout=2,
                                                ticker='Bithday Remainder !!!!!')

            #D, M, Y = date_before.Remainder(dates, months, Real_year)# two days before remainder date time year !
            #D, M, Y = date_before.Remainder_for_3day_before(dates, months, Real_year)
            # print(f'{D}/{M}/{Y}')
            if M == int(m):
                namess.append(name);datess.append(date)
                notification_name.append(name)
                # print(name,f'{D}/{M}/{Y}')
                notification_date.append(f'{D}/{M}/{Y}')
                # print('Notification date',f'{D}/{M}/{Y}')
    # print(namess,datess)
    print(notification_date)
    # for e in notification_date:
    #     #print(e, f'{int(real_date)}/{int(real_month)}/{int(real_year)}')
    #     if e == f'{int(real_date)}/{int(real_month)}/{int(real_year)}':
    #         print(e, 'this is going')
    #         position = notification_date.index(e)
    #         #print(notification_name[position])
    #         notification.notify(title="Birthday Remainder !",
    #                             message=f"{notification_name[position]}'s birthday in two days",
    #                             app_name='Birthday Remainder !!',
    #                             app_icon='code.ico',
    #                             # displaying time
    #                             timeout=2,
    #                             ticker='Bithday Remainder !!!!!')
    #     else:
    #         pass
            # print('this is not notification day')
    #print(notification_name)
    #print(notification_date)