import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def get_ohlcv(ticker, date_from, date_till):
    P = pd.DataFrame()
    # используем цикл, так как есть ограничение в выдаче значений за один запрос (max = 500)
    for i in range(5):
        url = 'http://iss.moex.com/iss/engines/stock/markets/shares/boards/tqbr/securities/' + ticker + '/candles.csv' \
        '?from=' + date_from + \
        '&till=' + date_till + \
        '&interval=24' \
        '&start=' + str(500*i)
        P = P.append(pd.read_csv(url, ';',skiprows=2))
    P['date'] = P.apply(lambda row: row['begin'][:10], axis =1)
    P['date'] = pd.to_datetime(P['date'], format = '%Y-%m-%d')
    P = P.set_index('date')
    
    #объем умножаем на 2, чтобы получить оборот
    P['volume'] = 2 * P['volume']
    P['value'] = 2 * P['value']
    
    P.drop(['begin', 'end'], axis = 1, inplace = True)
    return P

plt.rcParams['figure.dpi'] = 200

DATE = ['2015-01-01','2015-03-01','2015-04-01','2015-06-01']
COMP=['SBER','GAZP','LKOH']
COMP_inf=[]
COMP_test=[]
i=0
for NAME in COMP:
    COMP_inf.append(get_ohlcv(NAME, DATE[0], DATE[1]))
    COMP_inf[i]['tc']=COMP_inf[i]['close']-COMP_inf[i]['open']
    COMP_test.append(get_ohlcv(NAME, DATE[2], DATE[3]))
    COMP_test[i]['tc']=COMP_test[i]['close']-COMP_test[i]['open']
    i+=1
    

razn=[]
X=[]
Y=[]
for i in range(3):
    Y.append(COMP_inf[i].index)
for i in range(3):
    value=[]
    for a in COMP_inf[i]['open']:
        value.append(a)
    X.append(value)
    razn.append(X[i][len(X[i])-1]-X[i][0])
plt.subplot(2,3,1)
plt.title('SBER')
plt.plot(Y[0],X[0],'r')
plt.subplot(2,3,2)
plt.title('GAZP')
plt.plot(Y[1],X[1],'g')
plt.subplot(2,3,3)
plt.title('LKOH')
plt.plot(Y[2],X[2],'b')

X=[]
Y=[]
for i in range(3):
    Y.append(COMP_test[i].index)
for i in range(3):
    value=[]
    for a in COMP_test[i]['open']:
        value.append(a)
    X.append(value)
    razn.append(X[i][len(X[i])-1]-X[i][0])
plt.subplot(2,3,4)
plt.title('SBER_t')
plt.plot(Y[0],X[0],'r')
plt.subplot(2,3,5)
plt.title('GAZP_t')
plt.plot(Y[1],X[1],'g')
plt.subplot(2,3,6)
plt.title('LKOH_t')
plt.plot(Y[2],X[2],'b')
plt.show()


print(razn)
