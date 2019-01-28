from django.contrib import admin
from drawit.models import *

class LogStageAdmin(admin.ModelAdmin):
    list_display = ('stage_id', 'try_count', 'success_count')

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at') 

class BestRecordAdmin(admin.ModelAdmin):
    list_display = ('record_id', 'stage_id', 'user', 'record', 'created_at')

admin.site.register(LogStage, LogStageAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(BestRecord, BestRecordAdmin)