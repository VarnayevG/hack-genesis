import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#функция для получия данных с сата московской биржи

def get_ohlcv(ticker, date_from, date_till):
    P = pd.DataFrame()

    for i in range(5):
        url = 'http://iss.moex.com/iss/engines/stock/markets/shares/boards/tqbr/securities/' + ticker + '/candles.csv' \
                                                                                                        '?from=' + date_from + \
              '&till=' + date_till + \
              '&interval=24' \
              '&start=' + str(500 * i)
        P = P.append(pd.read_csv(url, ';', skiprows=2))
    P['date'] = P.apply(lambda row: row['begin'][:10], axis=1)
    P['date'] = pd.to_datetime(P['date'], format='%Y-%m-%d')
    P = P.set_index('date')


    P['volume'] = 2 * P['volume']
    P['value'] = 2 * P['value']

    P.drop(['begin', 'end'], axis=1, inplace=True)
    return P

#получаем датасет за указанные промежутки даты

DATE = ['2015-01-01', '2015-03-01', '2015-04-01', '2015-06-01']

COMP = ['SBER', 'GAZP', 'LKOH']
COMP_inf = []
COMP_test = []
i = 0
for NAME in COMP:
    COMP_inf.append(get_ohlcv(NAME, DATE[0], DATE[1]))
    COMP_inf[i]['tc'] = COMP_inf[i]['close'] - COMP_inf[i]['open']
    COMP_test.append(get_ohlcv(NAME, DATE[2], DATE[3]))
    COMP_test[i]['tc'] = COMP_test[i]['close'] - COMP_test[i]['open']
    i += 1

# обработка и визулизация данных по абсолютным изменениям за 1-й период
razn = []
razn_o = []
X = []
Y = []
for i in range(3):
    Y.append(COMP_inf[i].index)
for i in range(3):
    value = []
    for a in COMP_inf[i]['open']:
        value.append(a)
    X.append(value)
    razn.append(X[i][len(X[i]) - 1] - X[i][0])

    razn_o.append((X[i][len(X[i]) - 1] - X[i][0]) / X[i][0])

plt.subplots_adjust(wspace=0.5, hspace=0)
plt.tick_params(labelrotation=45)
plt.subplot(2, 3, 1)
plt.title('SBER')
plt.plot(Y[0], X[0], 'r')
plt.tick_params(labelrotation=45)
plt.subplot(2, 3, 2)
plt.title('GAZP')
plt.plot(Y[1], X[1], 'g')
plt.tick_params(labelrotation=45)
plt.subplot(2, 3, 3)
plt.title('LKOH')
plt.plot(Y[2], X[2], 'b')
plt.tick_params(labelrotation=45)
plt.show()

# обработка и визулизация данных по абсолютным изменениям за 2-й период
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
    razn_o.append((X[i][len(X[i])-1]-X[i][0])/X[i][0])
plt.subplots_adjust(wspace=0.5, hspace=0)
plt.tick_params(labelrotation = 45)
plt.subplot(2,3,1)
plt.title('SBER')
plt.plot(Y[0],X[0],'r')
plt.tick_params(labelrotation = 45)
plt.subplot(2,3,2)
plt.title('GAZP')
plt.plot(Y[1],X[1],'g')
plt.tick_params(labelrotation = 45)
plt.subplot(2,3,3)
plt.title('LKOH')
plt.plot(Y[2],X[2],'b')
plt.tick_params(labelrotation = 45)
plt.show()

# обработка и визулизация данных по относительным изменениям за 1-й период

X=[]
Y=[]
for i in range(3):
    Y.append(COMP_inf[i].index)
for i in range(3):
    value=[]
    for a in COMP_inf[i]['tc']:
        value.append(a)
    X.append(value)
    razn.append(X[i][len(X[i])-1]-X[i][0])
    razn_o.append((X[i][len(X[i])-1]-X[i][0])/X[i][0])
plt.subplots_adjust(wspace=0.5, hspace=0)
plt.tick_params(labelrotation = 45)
plt.subplot(2,3,1)
plt.title('SBER')
plt.plot(Y[0],X[0],'r')
plt.tick_params(labelrotation = 45)
plt.subplot(2,3,2)
plt.title('GAZP')
plt.plot(Y[1],X[1],'g')
plt.tick_params(labelrotation = 45)
plt.subplot(2,3,3)
plt.title('LKOH')
plt.plot(Y[2],X[2],'b')
plt.tick_params(labelrotation = 45)
plt.show()

# обработка и визулизация данных по относительным изменениям за 2-й период



X=[]
Y=[]
for i in range(3):
    Y.append(COMP_test[i].index)
for i in range(3):
    value=[]
    for a in COMP_test[i]['tc']:
        value.append(a)
    X.append(value)
    razn.append(X[i][len(X[i])-1]-X[i][0])
    razn_o.append((X[i][len(X[i])-1]-X[i][0])/X[i][0])
plt.subplots_adjust(wspace=0.5, hspace=0)
plt.tick_params(labelrotation = 45)
plt.subplot(2,3,1)
plt.title('SBER')
plt.plot(Y[0],X[0],'r')
plt.tick_params(labelrotation = 45)
plt.subplot(2,3,2)
plt.title('GAZP')
plt.plot(Y[1],X[1],'g')
plt.tick_params(labelrotation = 45)
plt.subplot(2,3,3)
plt.title('LKOH')
plt.plot(Y[2],X[2],'b')
plt.tick_params(labelrotation = 45)
plt.show()

#Вывод абсолютных и относительных изменений по компаниям
print(razn)
print(razn_o)