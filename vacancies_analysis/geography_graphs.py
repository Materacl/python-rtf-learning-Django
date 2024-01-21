import pandas as pd
import matplotlib.pyplot as plt


def make_salary_plot(salary_data: pd.DataFrame, name: str, name_plot: str):
    plt.figure(figsize=(12, 6))
    plt.plot(salary_data['area_name'], salary_data['average_salary'], marker='o', label='Average Salary')
    plt.title(name_plot)
    plt.xlabel('Город')
    plt.ylabel('Средняя зарплата')
    plt.xticks(rotation=90)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('data/' + name)
    plt.show()


def make_count_plot(vacancy_data: pd.DataFrame, name: str, name_plot: str):
    plt.figure(figsize=(8, 6))
    plt.pie(vacancy_data['vacancy_count'], labels=vacancy_data['area_name'], autopct='%1.1f%%', startangle=140)
    plt.title(name_plot)
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig('data/' + name)
    plt.show()


def main():
    area_count_all = pd.read_csv('data/area_count_all.csv')
    area_count_prof = pd.read_csv('data/area_count_prof.csv')
    area_salary_all = pd.read_csv('data/area_salary_all.csv')
    area_salary_prof = pd.read_csv('data/area_salary_prof.csv')

    make_salary_plot(area_salary_all, name="area_salary_all_plot",
                     name_plot="Уровень зарплат по городам")
    make_salary_plot(area_salary_prof, name="area_salary_prof_plot",
                     name_plot="Уровень зарплат по городам для С++ Разработчика")
    make_count_plot(area_count_all, name="area_count_all_plot",
                    name_plot="Доля вакансий по городам")
    make_count_plot(area_count_prof, name="area_count_prof_plot",
                    name_plot="Доля вакансий по городам для С++ Разработчика")


if __name__ == "__main__":
    main()
