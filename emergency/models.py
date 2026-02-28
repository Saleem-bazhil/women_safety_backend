from django.db import models
from django.conf import settings

class EmergencyContact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.user.username}"

class SOSAlert(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sos_alerts')
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='active', choices=[('active','Active'), ('resolved','Resolved')])
    audio_file = models.FileField(upload_to='sos_audio/', null=True, blank=True)

    def __str__(self):
        return f"SOS Alert by {self.user.username} - {self.status}"
