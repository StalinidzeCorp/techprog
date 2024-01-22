import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('vb.csv')

vacancy_share_by_city = data['area_name'].value_counts(normalize=True)
selected_cities = vacancy_share_by_city[vacancy_share_by_city > 0.01].index
filtered_data = data[data['area_name'].isin(selected_cities)]

plt.figure(figsize=(10, 6))
filtered_data['area_name'].value_counts(normalize=True).sort_values(ascending=False).plot(kind='bar', color='lightgreen')
plt.title('Доля вакансий по городам (больше 1%)')
plt.xlabel('Город')
plt.ylabel('Доля вакансий')
plt.tight_layout()
plt.savefig(f'diaggeog/geog_dol_sal_city.png')

filtered_data_grouped = filtered_data.groupby('area_name')['salary_from'].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
filtered_data_grouped.plot(kind='bar', color='orange')
plt.title('Уровень зарплат по городам (больше 1%)')
plt.xlabel('Город')
plt.ylabel('Средняя зарплата')
plt.tight_layout()
plt.savefig(f'diaggeog/geog_level_sal_city1.png')

chosen_profession_data = data[data['name'].str.contains('python')]

vacancy_share_by_city_chosen_profession = chosen_profession_data['area_name'].value_counts(normalize=True)
selected_cities_chosen_profession = vacancy_share_by_city_chosen_profession[vacancy_share_by_city_chosen_profession > 0.01].index
filtered_data_chosen_profession = chosen_profession_data[chosen_profession_data['area_name'].isin(selected_cities_chosen_profession)]

plt.figure(figsize=(10, 6))
filtered_data_chosen_profession['area_name'].value_counts(normalize=True).sort_values(ascending=False).plot(kind='bar', color='coral')
plt.title('Доля вакансий по городам для выбранной профессии (больше 1%)')
plt.xlabel('Город')
plt.ylabel('Доля вакансий')
plt.tight_layout()
plt.savefig(f'diaggeog/geog_dol_sal_pr1.png')

filtered_data_chosen_profession_grouped = filtered_data_chosen_profession.groupby('area_name')['salary_from'].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
filtered_data_chosen_profession_grouped.plot(kind='bar', color='purple')
plt.title('Уровень зарплат по городам для выбранной профессии (больше 1%)')
plt.xlabel('Город')
plt.ylabel('Средняя зарплата')
plt.tight_layout()
plt.savefig(f'diaggeog/geog_level_sal_pr1.png')
