from django.contrib import admin
from drawit.models import *

class LogStageAdmin(admin.ModelAdmin):
    list_display = ('stage_id', 'try_count', 'success_count')
    

admin.site.register(LogStage, LogStageAdmin)