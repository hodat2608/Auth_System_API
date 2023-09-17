from rest_framework.serializers import ModelSerializer 
from .models import Note_User


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note_User 
        fields = '__all__'

    def update(self, instance, validated_data):
        user = self.context.get('request').user
        instance.user = user
        instance.note_title = validated_data.get('note_title', instance.note_title)
        instance.note_conntent = validated_data.get('note_conntent', instance.note_conntent)
        instance.save()
        return instance