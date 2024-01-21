import pandas as pd
import matplotlib.pyplot as plt


def plot_bar_chart(data, title, xlabel, ylabel, filename):
    plt.figure(figsize=(10, 6))
    plt.bar(data['skill_name'], data['count'], color='skyblue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()


def main():
    skills_all_top = pd.read_csv('data/top_skills_all.csv')
    skills_prof_top = pd.read_csv('data/top_skills_prof.csv')

    unique_years = list(range(2017, 2024))
    for year in unique_years:
        plot_bar_chart(skills_all_top[skills_all_top['year'] == year][['skill_name', 'count']],
                       f'Топ 20 Навыков за {year} год',
                       'Навыки', 'Количество', f'data/bar_chart_all_{year}.png')

        plot_bar_chart(skills_prof_top[skills_prof_top['year'] == year][['skill_name', 'count']],
                       f'Топ 20 Навыков за {year} год для С++ Разработчика',
                       'Навыки', 'Количество', f'data/bar_chart_prof_{year}.png')


if __name__ == "__main__":
    main()
