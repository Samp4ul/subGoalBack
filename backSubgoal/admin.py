from django.contrib import admin

# Register your models here.
from backSubgoal.models import Subgoal

class SubgoalAdmin(admin.ModelAdmin):
    pass


admin.site.register(Subgoal, SubgoalAdmin)