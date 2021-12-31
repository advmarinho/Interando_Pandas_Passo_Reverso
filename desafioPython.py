import pandas as pd


print('\n\n\n\nSiga as instruções  ')
print('Software by ADS - Anderson Marinho  \n\n')

abrirWS = input(r'Digite Caminho do excel: ') + str('\\desafio.xlsx')
abrirWS = pd.read_excel(abrirWS, sheet_name='aba')
pd.set_option('float_format', '{:.0f}'.format)
quantidade = str(len(abrirWS))
print(abrirWS.head(int(quantidade)))
dfini = abrirWS
print('-->| ',str(len(abrirWS)) + str(' - ') + str('Qtd linha(s)'))
input('Enter para continuar...')


print('\nDataFrame com passo de 4 em 4, reverso sem zero: \n')
dfini.drop_duplicates(subset=['coluna base'], keep='last', inplace=True)
dfinia = dfini.shape
print('Antes exclusão', dfinia)
dfini.dropna(subset=['coluna base'], inplace=True)
dfinia = dfini.shape
print('Depois Exclusão', dfinia)
dfinia = dfini.loc[::-3]
quantidadeini = str(len(dfini))
print(dfinia.head(int(quantidadeini)))
input('Enter para continuar...')

print('\nDataFrame como lista')
df0 = abrirWS.loc[::-3]
lista = df0['coluna base'].to_list()
*n, n1 =  lista
print(n)
print('\n')
input('Enter para continuar...')

print('\nDataFrame retirando duplicadas')
abrirWS[:]
df2 = abrirWS[:]
quantidade2 = str(len(df2))
print(df2.head(int(quantidade2)))

print('\nDataFrame com passo de 4 em 4, reverso')
dfini[::-1]
dfini.drop_duplicates(subset=['coluna base'], keep='first', inplace=True)
df3 = dfini[::-3]
quantidade3 = str(len(df3))
print(df3.head(int(quantidade3)))

print('\nDataFrame união')
df4 = pd.merge(df2, df3, on='coluna base', how='outer', indicator=True)
quantidade4 = str(len(df4))
print(df4.head(int(quantidade4)))
input('Enter para continuar...')

print('\nDataFrame reverso após união')
df4[::-1]
df5 = df4[::-3]
quantidade5 = str(len(df5))
print(df5.head(int(quantidade5)))
input('Enter para finalizar...')