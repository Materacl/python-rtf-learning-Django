import requests
from django.shortcuts import render
from .models import Vacancy


def get_hh_vacancies(profession):
    url = f'https://api.hh.ru/vacancies?text={profession}&period=1&per_page=10'
    headers = {'User-Agent': 'urfuproject/1.0 (yurchenko.stas15@gmail.com)'}

    response = requests.get(url, headers=headers)
    data = response.json()

    vacancies = []
    for item in data.get('items', []):
        salary_info = item.get('salary', {})
        vacancy = {
            'title': item.get('name', ''),
            'description': item.get('description', ''),
            'skills': ', '.join(item.get('key_skills', [])),
            'company': item.get('employer', {}).get('name', ''),
            'salary_from': salary_info.get('from', None) if salary_info else None,
            'salary_to': salary_info.get('to', None) if salary_info else None,
            'region': item.get('area', {}).get('name', ''),
            'publication_date': item.get('published_at', '')
        }
        vacancies.append(vacancy)

    return vacancies


def latest_vacancies_page(request):
    profession = 'C++'
    vacancies = get_hh_vacancies(profession)
    for vacancy_data in vacancies:
        Vacancy.objects.create(**vacancy_data)

    context = {'vacancies': vacancies, 'profession': profession}
    return render(request, 'latest_vacancies.html', context)
