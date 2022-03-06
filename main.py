import os
import time, random
import numpy as np
import pandas as pd

def CREATE_MARCKET_DF(marcket_name, init_price):
    columns = ['CODE', 'PRE_PRICE', 'CUR_PRICE', 'RATE']
    data = np.array([[marcket_name, 0, init_price, 0]])
    df = pd.DataFrame(data=data, columns=columns)
    return df

def UPDATE_MARCKET_DF(marcket_name, update_price, df_marcket):
    condition = (df_marcket.CODE == marcket_name)
    update_rate = '{:.2f}'.format((update_price / float(df_marcket.loc[condition, 'CUR_PRICE']) - 1) * 100)
    df_marcket.loc[condition, 'PRE_PRICE'] = df_marcket.loc[condition, 'CUR_PRICE']
    df_marcket.loc[condition, 'CUR_PRICE'] = update_price
    df_marcket.loc[condition, 'RATE'] = update_rate

def CREATE_USER_DF(marcket_name, init_price, quantity, user_money):
    user_money -= init_price * quantity
    columns = ['CODE', 'CUR_PRICE', 'AVG_PRICE', 'QUANTITY', 'RATE']
    data = np.array([[marcket_name, init_price, init_price, quantity, 0]])
    df = pd.DataFrame(data=data, columns=columns)
    return df, user_money

def UPDATE_USER_DF(marcket_name, update_price, df_user):
    # CUR_PRICE, RATE 갱신
    condition = (df_user.CODE == marcket_name)
    df_user.loc[condition, 'CUR_PRICE'] = update_price
    df_user.loc[condition, 'RATE'] = '{:.2f}'.format((float(df_user.loc[condition, 'CUR_PRICE']) /
                                                       float(df_user.loc[condition, 'AVG_PRICE']) - 1) * 100)

def BUY(marcket_name, quantity, df_user, df_marcket, user_money):
    condition1 = (df_user['CODE'] == marcket_name)
    condition2 = (df_marcket['CODE'] == marcket_name)
    if user_money > float(df_marcket.loc[condition2, 'CUR_PRICE']) * quantity:
        user_money -= float(df_marcket.loc[condition2, 'CUR_PRICE']) * quantity
        if not (df_user['CODE'] == marcket_name).any():
            df = CREATE_USER_DF(marcket_name, float(df_marcket.loc[condition2, 'CUR_PRICE']), quantity)
            df_user = df_user.append(df, ignore_idex=True)
        else:
            df_user.loc[condition1, 'CUR_PRICE'] = df_marcket.loc[condition2, 'CUR_PRICE']
            df_user.loc[condition1, 'AVG_PRICE'] =\
                (float(df_user.loc[condition1, 'AVG_PRICE']) * int(df_user.loc[condition1, 'QUANTITY']) +
                 float(df_user.loc[condition1, 'CUR_PRICE']) * quantity) / (int(df_user.loc[condition1, 'QUANTITY']) + quantity)
            df_user.loc[condition1, 'QUANTITY'] = int(df_user.loc[condition1, 'QUANTITY']) + quantity
            df_user.loc[condition1, 'RATE'] = '{:.2f}'.format((float(df_user.loc[condition1, 'CUR_PRICE']) /
                                                                 float(df_user.loc[condition1, 'AVG_PRICE']) - 1) * 100)
    return df_user

def SELL():
    # 매도코드추가
    pass

if __name__ == '__main__':
    # Initial User, Marcket DataFrame
    USER_MONEY = 10000000
    DF_USER = pd.DataFrame()
    DF_MARCKET = pd.DataFrame()
    for idx in range(5):
        df1, USER_MONEY = CREATE_USER_DF(f'MARCKET{idx + 1}', (idx + 1) * 1000, 10, USER_MONEY)
        df2 = CREATE_MARCKET_DF(f'MARCKET{idx+1}', (idx+1) * 1000)
        DF_USER = DF_USER.append(df1, ignore_index=True)
        DF_MARCKET = DF_MARCKET.append(df2, ignore_index=True)

    iteration = 10
    while iteration != 0:
        iteration -= 1
        os.system('cls')
        print(f'==== M A R C K E T ====')
        print(DF_MARCKET, end='\n\n')
        print(f'======= U S E R =======')
        print(DF_USER)
        print('DEPOSIT = {:,}'.format(USER_MONEY))

        # Update Marcket DataFrame
        for row in DF_MARCKET.itertuples():
            update_price = float(row.CUR_PRICE) * random.uniform(0.85, 1.3)
            UPDATE_MARCKET_DF(row.CODE, update_price, DF_MARCKET)
            UPDATE_USER_DF(row.CODE, update_price, DF_USER)

        ############################ DataFrame출력이 여기로 와야할 것 같은 콘솔창결과보고 확인해볼 것

        # Update User DataFrame
        for row in DF_USER.itertuples():
            # User 수익률이 10%이면 절반매도
            if float(row.RATE) > 10:
                print(f'절반매도진행')
            # User 수익률이 -5%이면 절반매수
            if float(row.RATE) < -5:
                print(f'절반매수진행')



    #     # 10% 상승하면 절반매도
    #     if PRICES / USER_PRICES['Avg_Price'] > 1.1:
    #         USER_PRICES['Quantity'] = USER_PRICES['Quantity'] // 2
    #         USER_MONEY += PRICES * USER_PRICES['Quantity']
    #     # 10% 하락하면 두배매수
    #     if PRICES / USER_PRICES['Avg_Price'] < 0.9 and USER_MONEY > PRICES * USER_PRICES['Quantity']:

