import requests
import re
from django.shortcuts import render
from .models import Vacancy


def clear_html(line: str) -> str:
    return re.sub(r'<.*?>', '', line.strip())


def get_hh_vacancies(profession):
    url = f'https://api.hh.ru/vacancies?text={profession}&period=1&per_page=10'
    headers = {'User-Agent': 'urfuproject/1.0 (yurchenko.stas15@gmail.com)'}

    response = requests.get(url, headers=headers)
    data = response.json()

    vacancies = []
    for item in data.get('items', []):
        vacancy_id = item.get('id', '')
        url = f'https://api.hh.ru/vacancies/{vacancy_id}'
        headers = {'User-Agent': 'urfuproject/1.0 (yurchenko.stas15@gmail.com)'}
        response = requests.get(url, headers=headers)
        vacancy_data = response.json()

        skills_list = vacancy_data.get('key_skills', [])
        skills = ', '.join(skill.get('name', '') for skill in skills_list)

        salary_info = vacancy_data.get('salary', {})
        vacancy = {
            'title': vacancy_data.get('name', ''),
            'description': clear_html(vacancy_data.get('description', '')),
            'skills': skills,
            'company': vacancy_data.get('employer', {}).get('name', ''),
            'salary_from': salary_info.get('from', None) if salary_info else None,
            'salary_to': salary_info.get('to', None) if salary_info else None,
            'salary_currency': salary_info.get('currency', None) if salary_info else None,
            'region': vacancy_data.get('area', {}).get('name', ''),
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
