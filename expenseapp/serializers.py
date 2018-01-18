from django.contrib.auth.models import User
from expenseapp.models import Category, Expense
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
    	instance = User.objects.create_user(**validated_data)
    	return instance

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class CategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = Category
		fields = ['name']

class ExpenseSerializer(serializers.ModelSerializer):

	category = serializers.SlugRelatedField(
		queryset = Category.objects.all(),
		slug_field = 'name'
	);
	user = serializers.SlugRelatedField(
		queryset = User.objects.all(),
		slug_field = 'username'
	)

	payment_type = serializers.SerializerMethodField()
	status = serializers.SerializerMethodField()

	class Meta:
		model = Expense
		fields = ('amount', 'payment_date', 'payment_type', 'payee', 'category', 'description', 'user', 'status')

	def get_payment_type(self, obj):
		return obj.get_payment_type_display()

	def get_status(self, obj):
		return obj.get_status_display()
