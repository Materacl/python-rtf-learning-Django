from django.shortcuts import render


def latest_vacancies_page(request):
    return render(request, 'latest_vacancies.html')