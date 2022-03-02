from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ProvidersList(APIView):
	def get(self, request, format=None):
		snippets = CustomUser.objects.all()
		serializer = CustomUserSerializer(snippets, many=True)
		return Response(serializer.data)


class ProviderCreateDetail(APIView):
    """
    Create a new user.
    """
    def post(self, request, format=None):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProviderRetriveDetail(APIView):
	def get_object(self, tk):
		try:
			return CustomUser.objects.get(tk=tk)
		except CustomUser.DoesNotExist:
			raise Http404
	def get(self, request, tk, format=None):
		snippet = self.get_object(tk)
		serializer = CustomUserSerializer(snippet)
		return Response(serializer.data)


class ProviderUpdateDetail(APIView):
	def get_object(self, tk):
		try:
			return CustomUser.objects.get(tk=tk)
		except CustomUser.DoesNotExist:
			raise Http404
	def put(self, request, tk, format=None):
		snippet = self.get_object(tk)
		serializer = CustomUserSerializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProviderDeleteDetail(APIView):
	def get_object(self, tk):
		try:
			return CustomUser.objects.get(tk=tk)
		except CustomUser.DoesNotExist:
			raise Http404
	def delete(self, request, tk, format=None):
		snippet = self.get_object(tk)
		snippet.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)







def home(request):
	return render(request, 'users/home.html')


def register(request):
	form = UserRegistrationForm()
	if request.method == "POST":
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = UserRegistrationForm()
	return render(request, 'users/register.html', {'form':form})


class UserLoginView(LoginView):
	template_name = 'users/login.html'
	fields = '__all__'
	redirect_authenticated_user = True

	def get_success_url(self):
		return reverse_lazy('home')
		

class UserLogoutView(LogoutView):
	next_page = 'login'


