from django.shortcuts import render
from .models import TopSkillsAll, TopSkillsProf


def skills_page(request):
    unique_years = list(range(2017, 2024))

    skills_all = {year: list(TopSkillsAll.objects.filter(year=year)) for year in unique_years}
    skills_prof = {year: list(TopSkillsProf.objects.filter(year=year)) for year in unique_years}

    context = {
        'unique_years': unique_years,
        'skills_all': skills_all,
        'skills_prof': skills_prof,
        'prof': 'C++ Разработчик',
    }

    return render(request, 'skills.html', context)
