import pandas as pd

file_path = r'lotto.xlsx'
df_from_excel = pd.read_excel(file_path, engine="openpyxl")

df_from_excel = df_from_excel.drop(index=[0, 1])

df_from_excel.columns = ['년도', '회차', '추첨일', '1등 당첨자수', '2등 당첨자수', '3등 당첨자수', '4등 당첨자수', '5등 당첨자수',
                         '1등 당첨금액', '2등 당첨금액', '3등 당첨금액', '4등 당첨금액', '5등 당첨금액',
                         '당첨번호1', '당첨번호2', '당첨번호3', '당첨번호4', '당첨번호5', '당첨번호6', '보너스번호']

print(df_from_excel.head())

print(df_from_excel['회차'].values)

print(df_from_excel['1등 당첨금액'])