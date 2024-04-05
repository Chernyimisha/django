from django.contrib import admin
from .models import Throws, Bones, Numbers


class ThrowsAdmin(admin.ModelAdmin):
    list_display = ['res_throws', 'time_throws']
    ordering = ['-time_throws']


class BonesAdmin(admin.ModelAdmin):
    list_display = ['res_bones', 'time_bones']
    ordering = ['-time_bones']


class NumbersAdmin(admin.ModelAdmin):
    list_display = ['res_random', 'time_random']
    ordering = ['-time_random']


admin.site.register(Throws, ThrowsAdmin)
admin.site.register(Bones, BonesAdmin)
admin.site.register(Numbers, NumbersAdmin)

