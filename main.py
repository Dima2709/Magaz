import pandas as pd
import random as rd
df = pd.DataFrame({'age': [23, 50, 40, 35],'zp': [35000, 120000, 80000, 65000],'bg': [5000, 20000, 15000, 55000]})

def the(arg):
    zp = [abs(i-arg) for i in df['zp']]
    zp1 = [abs(i - arg) for i in df['zp']]
    minimum = min(zp)
    index = zp.index(minimum)
    zp.sort()

    proc = int(df['bg'][index]/df['zp'][index]*100)
    index2 = [j for j in range(len(zp1)) if zp[1] == zp[j]]
    proc1 = int(df['bg'][index2] / df['zp'][index2] * 100)
    res1 = arg * proc / 100

    if zp[0] != 0:
        if arg > min([i for i in df['zp']]) and arg < max([i for i in df['zp']]):

            res2 = arg*proc1/100

            if res2 > res1:
                res3 = ((res2 - res1)/2) + res1
            else:
                res3 = ((res1 - res2)/2) + res2

            print('Учитывая размер зарплат клиентов, которые зарабытавают примерно столько же, клиент скорее всего потратит', res3)
        elif arg < min([i for i in df['zp']]):

            if proc1 > proc:
                 proc3 = proc1 - proc
            else:
                 proc3 = proc - proc1

            if proc - proc3 > 0:
                print('Учитывая размер зарплат клиентов, которые зарабытавают примерно столько же, клиент скорее всего потратит', (arg*(proc - proc3))/100)
            else:
                print('Учитывая размер зарплат клиентов, которые зарабытавают примерно столько же - данные не надеждные, Бог рандома приказал потратить - ', (arg*(proc - rd.choice([1, 7])))/100)

        elif arg > max([i for i in df['zp']]):

            if proc1 > proc:
                proc3 = proc1 - proc
            else:
                proc3 = proc - proc1

            print('Клиент скорее всего потратит ',(arg * (proc + proc3)) / 100)

    else:
        print('Клиент с такой же зарплатой обнаружен в базе, интересующий вас клиент потратит примерно ',df.iloc[index]['bg'])

    precent = [int(i) for i in (df['bg']/df['zp'])*100]
    print('В среднем по всей базе, клиент потратит ',(arg*int(sum(precent)/len(precent)))/100)
    precent.sort()

    if len(precent) % 2 == 0:
        print('Если смотреть по медиальному значению, клиент потратит ', (arg * (int(precent[int(len(precent)/2)])+int(precent[int(len(precent)/2)+1]))/2)/100)
    else:
        print('Если смотреть по медиальному значению, клиент потратит ', (arg * precent[int(len(precent)/2)+1])/100)


the(55000)
