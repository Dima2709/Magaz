import pandas as pd
import random as rd
from collections import Counter
df = pd.DataFrame({'age': [23, 50, 40, 20, 35],'zp': [80000, 120000, 35000, 35000, 65000],'bg': [15000, 20000, 5000, 5000, 10000]})

def the(arg):
    zp = [abs(i-arg) for i in df['zp']]
    zp1 = [abs(i - arg) for i in df['zp']]
    index = zp.index(min(zp))
    zp.sort()
    proc = int(df['bg'][index]/df['zp'][index]*100)
    index2 = [j for j in range(len(zp1)) if zp[1] == zp1[j]]
    proc1 = int(df['bg'][index2[-1]] / df['zp'][index2[-1]] * 100)
    res1 = arg * proc / 100

    if zp[0] != 0:

        if arg > min(i for i in df['zp']) and arg < max(i for i in df['zp']):

            res2 = arg*proc1/100

            res3 = (abs(res2 - res1) / 2) + res1

            if df['zp'][index] - df['zp'][index2[-1]] != 0:
                x = (arg - df['zp'][index]) * abs(proc - proc1)
                x = x / (df['zp'][index2[-1]] - df['zp'][index])

                if res1 > res2:
                    print('Учитывая размер зарплат клиентов, которые зарабатывают примерно столько же, клиент скорее всего потратит - ',int((arg * abs(x) / 100) + res2), ' USD')
                else:
                    print(
                        'Учитывая размер зарплат клиентов, которые зарабатывают примерно столько же, клиент скорее всего потратит - ',int(res1 + (arg * abs(x) / 100)), ' USD')

            else:
                print('Учитывая размер зарплат клиентов, которые зарабатывают примерно столько же, клиент скорее всего потратит - ',
                    int(res3), ' USD')

        elif arg < min(i for i in df['zp']):

            proc3 = abs(proc1 - proc)

            if proc - proc3 > 0:
                print('Клиент с самой низкой зарплатой в нашей базе.','\n','Учитывая размер зарплат клиентов, которые зарабатывают примерно столько же, с учетом потери покупательной способности, клиент скорее всего потратит - ', (arg*(proc - proc3))/100, ' USD')
            elif proc - proc3 == 0:
                print('Клиент с самой низкой зарплатой в нашей базе.','\n', 'Учитывая размер зарплат клиентов, которые зарабатывают примерно столько же, клиент скорее всего потратит - ', (arg*proc/100), ' USD')
            else:
                print('Клиент с самой низкой зарплатой в нашей базе.','\n','Учитывая размер зарплат клиентов, которые зарабатывают примерно столько же - данные не надеждные, с учетом потери покупательной способности, Бог рандома приказал потратить - ', (arg*(proc - rd.choice([1, 4])))/100, ' USD')

        elif arg > max(i for i in df['zp']):

            proc3 = abs(proc1 - proc)

            print('Клиент с самой высокой зарплатой в нашей базе.','\n','Учитывая размер зарплат клиентов, которые зарабатывают примерно столько же, если принимать к сведению - рост покупательной способности, клиент скорее всего потратит - ',(arg * (proc + proc3)) / 100, ' USD')

    else:
        print('Клиент с такой же зарплатой обнаружен в базе, интересующий вас клиент потратит примерно - ',df.iloc[index]['bg'], ' USD')

    precent = [int(i) for i in (df['bg']/df['zp'])*100]
    print('В среднем по всей базе, клиент потратит - ',(arg*int(sum(precent)/len(precent)))/100, ' USD')
    precent.sort()

    if len(precent) % 2 == 0:
        print('Если смотреть по медиальному значению, клиент потратит - ', (arg * (int(precent[int(len(precent)/2)])+int(precent[int(len(precent)/2)-1]))/2)/100, ' USD')

    else:
        print('Если смотреть по медиальному значению, клиент потратит - ', (arg * precent[int(len(precent)/2)+1])/100, ' USD')

    count = Counter(precent)

    a = dict(count)
    print('Чаще всего в нашем магазине тратят, такое процентное соотношение(мода)(бета версия, я бы на нее особо не полагался)- ', arg*[i for i in count.keys()][[count[i] for i in count.keys()].index(max([count[i] for i in count.keys()]))]/100, ' USD')

    count_zp_max = Counter([i for i in df['bg']])
    print('Чаще всего в нашем магазине тратят (мода)(бета версия, я бы на нее особо не полагался)- ', [i for i in count_zp_max.keys()][[count_zp_max[i] for i in count_zp_max.keys()].index(max(count_zp_max[i] for i in count_zp_max.keys()))], ' USD')

the(50000)
