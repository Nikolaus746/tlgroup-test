from django.contrib import admin
from .models import Continent, Country, Region, City, Office, Persons


class CountryInline(admin.TabularInline):
    model = Country
    extra = 0

class RegionInline(admin.TabularInline):
    model = Region
    extra = 0

class CityInline(admin.TabularInline):
    model = City
    extra = 0

class OfficeInline(admin.TabularInline):
    model = Office
    extra = 0


class ContinentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    search_fields = ('pk', 'title',)
    inlines = [CountryInline, ]

class CountryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    search_fields = ('pk', 'title',)
    inlines = [RegionInline, ]

class RegionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    search_fields = ('pk', 'title',)
    inlines = [CityInline, ]

class CityAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    search_fields = ('pk', 'title',)
    inlines = [OfficeInline, ]


class PersonInline(admin.TabularInline):
    model = Persons
    extra = 0

class OfficeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    search_fields = ('pk', 'title',)
    inlines = [PersonInline, ]



class PersonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'salary', 'office')
    list_filter = ('office', 'salary')
    search_fields = ('pk', 'name', 'position', 'office')


admin.site.register(Persons, PersonAdmin)
admin.site.register(Continent, ContinentAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Office, OfficeAdmin)
