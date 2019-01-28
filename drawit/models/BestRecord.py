from django.db import models

class BestRecord(models.Model):
    record_id = models.AutoField(primary_key=True)
    stage_id = models.ForeignKey('LogStage', on_delete=models.CASCADE)
    user = models.OneToOneField('User', on_delete=models.CASCADE, null=True)
    record = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.stage_id) + ' ' + str(self.user) + ' ' + str(self.record)

    class Meta:
        ordering = ('stage_id', 'record',)
