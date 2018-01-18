from rest_framework.response import Response
from django.contrib.auth.models import User
from expenseapp.models import Category, Expense
from rest_framework import viewsets
from expenseapp.serializers import UserSerializer, CategorySerializer, ExpenseSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
    	serializer = UserSerializer(data=request.data)
    	if serializer.is_valid():
        	user = serializer.create(serializer.validated_data)
        	return Response({'message': 'success'})
    	else:
        	return Response(serializer.errors)

class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class ExpenseViewSet(viewsets.ModelViewSet):
	queryset = Expense.objects.all()
	serializer_class = ExpenseSerializer