from django.db import models


# Department
class Department(models.Model):
    title = models.CharField(max_length=500, null=True, verbose_name="Название", unique=True)

    class Meta:
        abstract = True


# Continent
class Continent(Department):

    class Meta:
        verbose_name = 'Континент'
        verbose_name_plural = 'Континенты'

    def __str__(self):
        return F"{self.title}"


# Country
class Country(Department):
    continent = models.ForeignKey(Continent, verbose_name=("континент"), null=True, blank=True,
                                  on_delete=models.CASCADE, related_name="country_continent")

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return F"{self.title}"


# Region
class Region(Department):
    country = models.ForeignKey(Country, verbose_name=("страна"), null=True, blank=True,
                                on_delete=models.CASCADE, related_name="region_country")

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    def __str__(self):
        return F"{self.title}"


# City
class City(Department):
    region = models.ForeignKey(Region, verbose_name=("регион"), null=True, blank=True,
                               on_delete=models.CASCADE, related_name="city_region")

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return F"{self.title}"


# Office
class Office(Department):
    city = models.ForeignKey(City, verbose_name=("город"), null=True, blank=True,
                             on_delete=models.CASCADE, related_name="office_city")

    class Meta:
        verbose_name = 'Офис'
        verbose_name_plural = 'Офисы'

    def __str__(self):
        return F"{self.title}"


POSITION_CHOICES = [
    ('0', 'Сисадмин'),
    ('1', 'Лентяй'),
    ('2', 'Программист'),
    ('3', 'Уборщик'),
    ('4', 'Охранник'),
    ('5', 'Сторож'),
    ('6', 'Бухгалтер'),

]
# Persons
class Persons(models.Model):
    created = models.DateTimeField(auto_now=True, null=True)
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name="ФИО")
    position = models.CharField(max_length=1, choices=POSITION_CHOICES, default="1")
    employment_date = models.DateField(verbose_name="Дата приёма на работу", null=True, blank=True)
    salary = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=2,
                                 verbose_name="Размер зарплаты")

    office = models.ForeignKey(Office, verbose_name=("офис"), null=True, blank=True,
                               on_delete=models.CASCADE, related_name="person_office")

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return F"{self.name}"
