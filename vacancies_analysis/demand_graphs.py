import pandas as pd
import matplotlib.pyplot as plt


def make_salary_plot(salary_data: pd.DataFrame, name: str, name_plot: str):
    plt.figure(figsize=(10, 6))
    plt.plot(salary_data['year'], salary_data['average_salary'], marker='o', label='Average Salary')
    plt.title(name_plot, color='white')
    plt.xlabel('Год', color='white')
    plt.ylabel('Средняя зарплата', color='white')
    plt.legend()
    plt.grid(True, color='white')  # Цвет сетки
    plt.gca().set_facecolor('#010409')

    # Изменение цвета надписей на сетке
    plt.tick_params(axis='both', colors='white')

    plt.savefig('data/' + name, transparent=True)
    plt.show()


def make_count_plot(vacancy_data: pd.DataFrame, name: str, name_plot: str):
    plt.figure(figsize=(10, 6))
    plt.plot(vacancy_data['year'], vacancy_data['vacancy_count'], marker='o', color='orange', label='Vacancy Count')
    plt.title(name_plot, color='white')
    plt.xlabel('Год', color='white')
    plt.ylabel('Количество вакансий', color='white')
    plt.legend()
    plt.grid(True, color='white')
    plt.gca().set_facecolor('#010409')

    # Изменение цвета надписей на сетке
    plt.tick_params(axis='both', colors='white')

    plt.savefig('data/' + name, transparent=True)
    plt.show()


def main():
    dynamic_count_all = pd.read_csv('data/dynamic_count_all.csv')
    dynamic_count_prof = pd.read_csv('data/dynamic_count_prof.csv')
    dynamic_salary_all = pd.read_csv('data/dynamic_salary_all.csv')
    dynamic_salary_prof = pd.read_csv('data/dynamic_salary_prof.csv')

    make_salary_plot(dynamic_salary_all, name="dynamic_salary_all_plot",
                     name_plot="Динамика уровня зарплат по годам")
    make_salary_plot(dynamic_salary_prof, name="dynamic_salary_prof_plot",
                     name_plot="Динамика уровня зарплат по годам для С++ Разработчика")
    make_count_plot(dynamic_count_all, name="dynamic_count_all_plot",
                    name_plot="Динамика количества вакансий по годам")
    make_count_plot(dynamic_count_prof, name="dynamic_count_prof_plot",
                    name_plot="Динамика количества вакансий по годам для С++ Разработчика")


if __name__ == "__main__":
    main()
