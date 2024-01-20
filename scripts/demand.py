import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('vb.csv', low_memory=False)
df = df.drop(['key_skills', 'area_name'], axis=1)
df = df.dropna()
df['published_at'] = pd.to_datetime(df['published_at'], utc=True)

df = df[df['salary_from'] <= 10000000]

plt.figure(figsize=(19.2, 10.8))
salary_dynamics = df.groupby(df['published_at'].dt.year)['salary_from'].mean()
salary_dynamics.plot(kind='bar', color='skyblue')
plt.title('Динамика уровня зарплат по годам')
plt.xlabel('Год')
plt.ylabel('Средняя зарплата, RUB')
plt.tight_layout()
plt.savefig(f'diagdemand/demand_salary_year.png')

plt.figure(figsize=(19.2, 10.8))
vacancy_dynamics = df.groupby(df['published_at'].dt.year).size()
vacancy_dynamics.plot(kind='bar', color='lightcoral')
plt.title('Динамика количества вакансий по годам')
plt.xlabel('Год')
plt.ylabel('Количество вакансий')
plt.tight_layout()
plt.savefig(f'diagdemand/demand_count_year.png')

chosen_profession = 'python'

plt.figure(figsize=(19.2, 10.8))
chosen_salary_dynamics = df[df['name'].str.contains(chosen_profession, case=False)].groupby(df['published_at'].dt.year)['salary_from'].mean()
chosen_salary_dynamics.plot(kind='bar', color='lightgreen')
plt.title(f'Динамика уровня зарплат для {chosen_profession} по годам')
plt.xlabel('Год')
plt.ylabel('Средняя зарплата, RUB')
plt.tight_layout()
plt.savefig(f'diagdemand/demand_salary_pr.png')

plt.figure(figsize=(19.2, 10.8))
chosen_vacancy_dynamics = df[df['name'].str.contains(chosen_profession, case=False)].groupby(df['published_at'].dt.year).size()
chosen_vacancy_dynamics.plot(kind='bar', color='orange')
plt.title(f'Динамика количества вакансий для {chosen_profession} по годам')
plt.xlabel('Год')
plt.ylabel('Количество вакансий')
plt.tight_layout()
plt.savefig(f'diagdemand/demand_count_pr.png')