import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('nvb.csv')
data['published_at'] = pd.to_datetime(data['published_at'])


def top_skills_by_year(data, year, profession=None):
    year_data = data[data['published_at'].dt.year == year]
    
    if profession:
        year_data = year_data[year_data['name'].str.contains(profession, case=False)]

    top_skills = year_data['key_skills'].str.split('\n', expand=True).stack().value_counts().head(20)

    plt.figure(figsize=(19.2, 10.8))
    sns.barplot(x=top_skills.values, y=top_skills.index, palette='viridis')
    plt.title(f'TOP-20 навыков за {year} год ({profession if profession else "Все профессии"})')
    plt.xlabel('Количество упоминаний')
    plt.ylabel('Навык')
    if not profession:
      plt.savefig(f'diag/top_skills_{year}.png')
    else:
      plt.savefig(f'diag/top_skills_profession_{year}.png')


top_skills_all_years = pd.DataFrame()

for year in sorted(data['published_at'].dt.year.unique()):
    top_skills_by_year(data, year)

chosen_profession = 'python'
top_skills_chosen_profession = pd.DataFrame()

for year in sorted(data['published_at'].dt.year.unique()):
    top_skills_by_year(data, year, chosen_profession)

