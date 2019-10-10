from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """serializers a name field for an apiview
    
    Arguments:

    """ 
    name = serializers.CharField(max_length=10)  
