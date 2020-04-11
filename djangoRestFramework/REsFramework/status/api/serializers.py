from rest_framework import  serializers

from  status.models import  Status

"""
serializers for json
serializers for validations
"""


# class CustomeSerializer(serializers.Serializer):
#     content = serializers.CharField()
#     email = serializers.EmailField()

class StatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id','user','content','image']
        
    def validate_content(self, value):
        if len(value)>10000:
            raise serializers.ValidationError("this is too long serializers data")
        return value
    
    def validate(self,data):
        content =  data.get('content', None)
        if content =="":
            content = None
        image = data.get('image', None)
        if content is None and image is None:
            raise serializers.ValidationError("Content or Image are required")
        return data
         
        