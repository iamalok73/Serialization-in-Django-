from rest_framework import serializers



class Studentseriealizers(serializers.Serializer):
    name = serializers.CharField(max_length = 100)
    rollno = serializers.IntegerField()
    city = serializers.CharField(max_length =100)
