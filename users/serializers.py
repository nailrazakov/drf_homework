from rest_framework.serializers import ModelSerializer
from users.models import User, Payments


class PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class UserDetailSerializer(ModelSerializer):
    payments_set = PaymentsSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
