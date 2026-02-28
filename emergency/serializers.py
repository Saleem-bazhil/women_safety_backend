from rest_framework import serializers
from .models import EmergencyContact, SOSAlert

class EmergencyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyContact
        fields = ['id', 'name', 'phone', 'is_primary']

class SOSAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = SOSAlert
        fields = ['id', 'user', 'latitude', 'longitude', 'timestamp', 'status', 'audio_file']
        read_only_fields = ['user', 'timestamp']
