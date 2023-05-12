import json
from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import User
from django.contrib.auth.hashers import make_password

class SignupView(View):
    def post(self, request):
        data = json.load(request.body)
        # try :
        #     if User.objects.filter(email = data['email']).exists() :
        #         return JsonResponse({'message' : 'EXISTS_EMAIL'}, status= 400)
        User(
            name= data['model'],
            email= data['email'],
            password = data['password'],
            hospital =data['hospital'],
            tel = data['tel'],
            type = data['type'],
            country = data['country']
        ).save()
        return JsonResponse({"message":'등록되지 않은 이메일 입니다.'}, status=200)
class SigninView(View):
    def post(self, request):
        data = json.load(request.body)

        if User.objects.filter(email = data['email']).exists():
            user = User.objects.get(email = data['email'])
            if user.password == data['password'] :
                return JsonResponse({'message':'로그인 성공'}, status=200)
            else:
                return JsonResponse({'message': '비밀번호가 틀렸습니디.'}, status=400)
        return JsonResponse({'message' : '등록되지 않은 이메일 입니다.'}, status=400)

