from django.shortcuts import render
from .models import Accueil_msg, Accueil_photo
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required()
def accueil(request):
    mess = Accueil_msg.objects.filter()
    photo = Accueil_photo.objects.filter()
    return render(request, 'accueil.html', {'mess': mess,
                                            'photo': photo,})
