from rest_framework import serializers


class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = "Message"
        fields = ("text")

