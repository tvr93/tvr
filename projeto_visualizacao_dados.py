import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df = pd.read_csv('ecommerce_preparados.csv')
print(df.head(5).to_string())
print('Qtd: ', df.shape)
print('Valores nulos: \n', df.isnull().sum())
print('Estatisticas dos dados: \n', df.describe())

count_marca = df['Marca'].value_counts()
count_marca_top10 = df['Marca'].value_counts().head(10)
count_marca_top9 = df['Marca'].value_counts().head(9)
print(count_marca_top9)
outras_marcas = count_marca.iloc[9:].sum()
count_marca_top9['Outras'] = outras_marcas
print('Top 9 marcas:\n',count_marca_top9)
print('Top 9 + outros: \n', outras_marcas)

# #Gráfico top dez marcas - Pizza
plt.figure(figsize=(12, 8))
plt.pie(count_marca_top10.values, labels=count_marca_top10.index, autopct='%1.1f%%', startangle=90)
plt.title('Top 10 Marcas')
plt.show()

# #Gráfico com outros - Pizza
plt.figure(figsize=(12, 8))
plt.pie(count_marca_top9.values, labels=count_marca_top9.index, autopct='%1.1f%%', startangle=90)
plt.title('Top 9 Marcas e outras')
plt.show()
#

# Gráfico Mapa de Calor
matriz_correlação = df[['Nota', 'N_Avaliações', 'Desconto', 'Preço', 'Qtd_Vendidos_Cod']].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(matriz_correlação, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0)
plt.title('Correlação Heatmap')
plt.tight_layout()
plt.show()
#

# # Grafico Distribuição Nota
plt.figure(figsize=(10, 6))
sns.histplot(df['Nota'], bins=20, kde=True)
plt.title('Distribuição Qtd/Nota')
plt.xlabel('Nota')
plt.ylabel('Quantidade')
plt.show()

# Grafico barras - Marca x Temporada
count_marca_top10_2 = df['Marca'].value_counts().head(10).index
sns.countplot(x='Marca', hue='Temporada', data=df[df['Marca'].isin(count_marca_top10_2)], palette='pastel', order=count_marca_top10_2)
plt.xlabel('Marcas')
plt.ylabel('Quantidade Clientes')
plt.legend(title='Qtd Clientes x Top 10 Marcas - Temporada')
plt.show()

# Gráfico de Barras
plt.figure(figsize=(10,6))
df['Nota'].value_counts().plot(kind='bar', color='#98ee78')
plt.title('Qtd x Notas')
plt.xlabel('Notas')
plt.ylabel('Quantidade')
plt.xticks(rotation=0)
plt.show()

# Gráfico de Densidade
plt.figure(figsize=(10,6))
sns.kdeplot(df['Preço'],fill=True, color='#863e9c')
plt.title('Densidade de Preços')
plt.xlabel('Preço')
plt.show()

#Gráfico Dispersão - Qtd Vendidos x Preço
sns.jointplot(x='Qtd_Vendidos_Cod', y='Preço',data=df, kind='scatter')
plt.xlabel('Qtd Vendidos')
plt.ylabel('Preço')
plt.tight_layout()
plt.show()

