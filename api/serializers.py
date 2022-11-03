from rest_framework import serializers



class InputSerializer(serializers.Serializer):
    operation_type = serializers.CharField(required=True,max_length=200,allow_blank=False)
    x = serializers.IntegerField(required=True)
    y = serializers.IntegerField(required=True)