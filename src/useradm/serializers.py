from rest_framework import serializers
from .models import CtClient


class CtClientSerializer(serializers.HyperlinkedModelSerializer):
    """Basic serializer for CtClient model
    """
    url = serializers.HyperlinkedIdentityField(
        view_name="ctclient-detail",
    )
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = CtClient
        fields = '__all__'


