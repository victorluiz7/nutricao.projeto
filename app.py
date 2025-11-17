import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("nutricao.csv")

media_calorica = df['calorias_diarias'].mean()
media_imc = df['imc'].mean()

sns.scatterplot(x='calorias_diarias', y='imc', data=df)
plt.xlabel('Calorias diarias')
plt.ylabel("Imc")
plt.title("Grafico de dispersão entre calorias e o imc")
plt.show()

print(df.head())
print(f"A media calorica e:  {media_calorica: .2f}")
print(f"A media de do imc é: {media_imc: .2f}")

corr = df['calorias_diarias'].corr(df['imc'])
print(f"A correlação entre Calorias diarias e o Imc é: {corr:.2f}")

correlacao = df.corr()

print("\n matriz de correlação:  ")
print(correlacao)

plt.figure(figsize=(10,8))
sns.heatmap(correlacao, annot=True, cmap="coolwarm")
plt.title("Mapa de calor referente a correlação")
plt.show()