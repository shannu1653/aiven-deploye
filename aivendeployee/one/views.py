from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Students,Profile


from django.contrib.auth.models import User
# Create your views here.
@csrf_exempt
def create_student(request):
    if request.method=="POST":
        data=json.loads(request.body)

        name=data.get("name")
        age=data.get("age")
        email=data.get("email")
        
        student=Students.objects.create(
            name=name,
            age=age,
            email=email
        )
        return JsonResponse({
            "message":"student create successfully",
            "id":student.id,
            "name":student.name,
            "age":student.age,
            "email":student.email
        })
    


@csrf_exempt
def signup(request):
    if request.method == "POST":
        data = json.loads(request.body)

        user = User.objects.create_user(
            username=data["username"],
            email=data["email"],
            password=data["password"]
        )

        Profile.objects.create(
            user=user,
            dob=data["dob"],
            place=data["place"]
        )

        return JsonResponse({"message": "Signup successful"})
    
    return JsonResponse(
        {"error": "Only POST method allowed"},
        status=405)
    

from django.contrib.auth import authenticate

@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)

        user = authenticate(
            username=data.get("username"),
            password=data.get("password")
        )

        if user is not None:
            return JsonResponse({
                "success": True,
                "message": "Login successful"
            }, status=200)
        else:
            return JsonResponse({
                "success": False,
                "message": "Invalid username or password"
            }, status=401)

    return JsonResponse(
        {"success": False, "message": "Only POST method allowed"},
        status=405
    )
