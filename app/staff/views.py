import random
from random import randrange
from datetime import timedelta
from datetime import datetime
from russian_names import RussianNames

from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404

from django.views import View
from .models import Continent, Country, Region, City, Office, Persons


def createDeps():
    dep = {"Азия": {"Китай":
                        {"Центральный": {"Пекин": ["off-165", "off-166"], "Шанхай": ["off-167", "off-168"]}},
                    "Тайланд": {"Южный": {"Бангкок": ["off-170", "off-171"], "Паттайя": ["off-172", "off-173"]}}},
           "Европа": {"Германия":
                          {"Бавария": {"Мюнхен": ["off-181", "off-182"], "Берлин": ["off-183", "off-184"]}},
                      "Франция": {"Южная": {"Париж": ["off-185", "off-186"], "Госконь": ["off-187", "off-188"]}}},
           "Южная Америка": {"Колумбия":
                                 {"Центральная": {"Богота": ["off-191", "off-192"],
                                                  "Медельин": ["off-193", "off-194"]}},
                             "Эквадор": {
                                 "Горный": {"Кито": ["off-200", "off-201"], "Острова": ["off-203", "off-204"]}}},
           "Северная Америка": {"США":
                                    {"Запад": {"Сан Франциско": ["off-303", "off-304"],
                                               "Лос-Анжелес": ["off-305", "off-306"]}},
                                "Канада": {
                                    "Леса": {"Оттава": ["off-307", "off-308"], "Аля-ля": ["off-400", "off-401"]}}},
           }

    for contin, contin_dict in dep.items():
        continent = contin
        for countr, countr_dict in contin_dict.items():
            country = countr
            for reg, reg_dict in countr_dict.items():
                region = reg
                for tow, tow_dict in reg_dict.items():
                    town = tow
                    print(continent, country, region, town, tow_dict)
                    new_con, created = Continent.objects.get_or_create(title=continent)
                    new_contr, created = Country.objects.get_or_create(title=country, continent=new_con)
                    new_reg, created = Region.objects.get_or_create(title=region, country=new_contr)
                    new_town, created = City.objects.get_or_create(title=town, region=new_reg)
                    for of in tow_dict:
                        office = Office(title=of, city=new_town)
                        office.save()


def del_dep():
    Continent.objects.all().delete()
    Country.objects.all().delete()
    Region.objects.all().delete()
    City.objects.all().delete()
    Office.objects.all().delete()



def delete_persons():
    Persons.objects.all().delete()

def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def create_persons():
    rn = RussianNames(count=50000, patronymic=False, name_reduction=True)
    batch = rn.get_batch()
    print(batch)
    persons = []
    for name in batch:
        print("--------")
        dt = random_date( datetime.strptime("2020-10-02", "%Y-%M-%d"),
                          datetime.strptime("2022-10-02", "%Y-%M-%d"))
        pos_index = random.randint(0, 6)
        office = Office.objects.order_by('?').first()
        salary = random.randint(1, 5)
        person = Persons(name=name, office = office, position = pos_index,
                         employment_date = dt, salary = salary*5000)
        persons.append(person)
    print("start bulking...")
    Persons.objects.bulk_create(persons)

class Endpoint(View):
    def get(self, request):
        # createDeps()
        # del_dep()
        # create_persons()
        # delete_persons()
        return HttpResponse('Request Get')


class IndexView(TemplateView):
    template_name = "index.html"

def person_list(request):
    continent = Continent.objects.all()


    # paginator = Paginator(f.qs, 30)
    #
    # page = request.GET.get('page')
    # try:
    #     response = paginator.page(page)
    # except PageNotAnInteger:
    #     response = paginator.page(1)
    # except EmptyPage:
    #     response = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'continent': continent })