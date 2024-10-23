from django.contrib import admin
from .models import agent
from import_export.admin import ImportExportModelAdmin

@admin.register(agent)
class AgentAdmin(ImportExportModelAdmin):
    list_display = ('user','agent_name','organisation','phone_number','email')
