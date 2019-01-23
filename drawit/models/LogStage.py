from django.db import models

class LogStage(models.Model):
    LOG_TYPE = (
        ('success', 'success'),
        ('star0', 'star0'),
        ('star1', 'star1'),
        ('star2', 'star2'),
        ('fail', 'fail'),
    )

    stage_id = models.CharField(max_length=20, primary_key=True)
    try_count = models.IntegerField(default=0, blank=True)
    success_count = models.IntegerField(default=0, blank=True)
    star0_count = models.IntegerField(default=0, blank=True)
    star1_count = models.IntegerField(default=0, blank=True)
    star2_count = models.IntegerField(default=0, blank=True)
    types = models.CharField(max_length=20, choices=LOG_TYPE, default='fail')

    def __str__(self):
        return self.stage_id

    class Meta:
        ordering = ('stage_id',)
