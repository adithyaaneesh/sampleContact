from django.shortcuts import get_object_or_404, redirect, render
from .models import Contact

# Create your views here.

def add_contact(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        phone_num = request.POST.get('phonenum')
        profile_image = request.FILES.get('profile_image')

        if fname and phone_num:
            Contact.objects.create(
                firstname=fname,
                email=email,
                phonenumber=phone_num,
                profile_image=profile_image

            )
            return redirect('home')
    return render(request, 'add_contact.html')


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_home.html', {'contacts': contacts})

def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == "POST":
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        phone_num = request.POST.get('phonenum')
        profile_image = request.FILES.get('profile_image')
        if fname and phone_num:
            contact.firstname = fname
            contact.email = email
            contact.phonenumber = phone_num
            if profile_image:
                contact.profile_image = profile_image
            contact.save()
            return redirect('home')
    return render(request, 'edit.html', {'contact': contact})


def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    return redirect('home')


# HTTP METHODS CRUD
# from django.http import JsonResponse
# from .models import Student
# import json

# # GET - List students
# def get_students(request):
#     students = list(Student.objects.values())
#     return JsonResponse(students, safe=False)


# # POST - Create student
# def create_student(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         student = Student.objects.create(
#             name=data['name'],
#             age=data['age'],
#             email=data['email']
#         )
#         return JsonResponse({"message": "Student created"}, status=201)


# # PUT - Update student
# def update_student(request, id):
#     if request.method == "PUT":
#         data = json.loads(request.body)
#         student = Student.objects.get(id=id)
#         student.name = data['name']
#         student.age = data['age']
#         student.email = data['email']
#         student.save()
#         return JsonResponse({"message": "Student updated"})


# # DELETE - Delete student
# def delete_student(request, id):
#     if request.method == "DELETE":
#         student = Student.objects.get(id=id)
#         student.delete()
#         return JsonResponse({"message": "Student deleted"})
