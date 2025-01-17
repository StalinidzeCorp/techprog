from datetime import datetime
from django.shortcuts import render
from django.views.generic import DetailView

from .models import PageContent
import requests


def index(request):
    try:
        index_page = PageContent.objects.get(title='Главная')
    except:
        index_page = PageContent.objects.get(title='404')
    return render(request, 'index.html', {'index_page': index_page})


def demand(request):
    try:
        demand_page = PageContent.objects.get(title='Востребованность')
    except:
        demand_page = PageContent.objects.get(title='404')
    return render(request, 'demand.html', {'demand_page': demand_page})


def geography(request):
    try:
        geography_page = PageContent.objects.get(title='География')
    except:
        geography_page = PageContent.objects.get(title='404')
    return render(request, 'geography.html', {'geography_page': geography_page})


def skills(request):
    try:
        skills_page = PageContent.objects.get(title='Навыки')
    except:
        skills_page = PageContent.objects.get(title='404')
    return render(request, 'skills.html', {'skills_page': skills_page})


def latest(request):
    url = 'https://api.hh.ru/vacancies?ored_cluster=true&order_by=publication_time&enable_snippets=true&search_period=1&hhtmFrom=vacancy_search_list&hhtmFromLable=vacancy_search_line&search_field=name&L_save_area=true&text=python-программист'
    response = requests.get(url).json()['items'][:10]
    lst = []

    for i in response:
        r_v = requests.get(f'https://api.hh.ru/vacancies/{i["id"]}').json()
        skills = ''
        if r_v['key_skills']:
            for j in r_v['key_skills']:
                skills += f"{j['name']}, "
        else:
            skills = '-'

        sal = '-'
        cur = ''
        if i['salary']:
            cur = i['salary']['currency']
            if i['salary']['from'] and not i['salary']['to']:
                sal = f"от {'{0:,}'.format(i['salary']['from']).replace(',', ' ')}"
            elif not i['salary']['from'] and i['salary']['to']:
                sal = f"до {'{0:,}'.format(i['salary']['to']).replace(',', ' ')}"
            else:
                sal = f"{'{0:,}'.format(i['salary']['from']).replace(',', ' ')} - {'{0:,}'.format(i['salary']['to']).replace(',', ' ')}"

        item = {
            'name': i['name'] if i['name'] else '-',
            'description': r_v['description'] if r_v['description'] else '-',
            'skills': skills,
            'company': i['employer']['name'] if i['employer']['name'] else '-',
            'salary': sal,
            'currency': cur,
            'address': i['area']['name'] if i['area'] and i['area']['name'] else '-',
            'published_at': datetime.strptime(i['published_at'], "%Y-%m-%dT%H:%M:%S%z").strftime("%d.%m.%Y %H:%M") if i['published_at'] else '-',
            'url': i['alternate_url'] if i['alternate_url'] else '#'
        }
        lst.append(item)
    return render(request, 'latest.html', {'items': lst})





