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

