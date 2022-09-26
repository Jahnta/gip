from django.contrib import admin
from .models import Component, Scope

# Register your models here.

class ScopeInLine(admin.TabularInline):
    model = Scope
    extra = 1
    ordering = ('sow',)

class ComponentAdmin(admin.ModelAdmin):
    list_display = ('name', )
    inlines = [ScopeInLine]

class ScopeAdmin(admin.ModelAdmin):
    list_display = ('component', 'sow')

admin.site.register(Component, ComponentAdmin)
admin.site.register(Scope, ScopeAdmin)
