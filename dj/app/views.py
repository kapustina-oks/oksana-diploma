from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# from app.models import Drags, First_tab
from app.models import First_tab, Second_tab, Common_tad
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _, activate
import random


# def name_med(request):
#     ls = Drags.objects.all()
#     s = ''
#     for x in ls:
#         s = s + '<br>' + x.name_of_drags
#     return HttpResponse(s)


def name_med_2(request):
    return render_to_response('index.html', {'greet': request.user.is_authenticated, 'name': request.user.username})


def login_user(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is None:
        return render_to_response('error.html', {})
    else:
        login(request, user)
        return HttpResponseRedirect('/')


def do_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('Вам необходимо залогиниться.')

def register(request):
    user = User.objects.create_user(
        request.POST['username'],
        password=request.POST['password'],
        first_name=request.POST['login']
    )
    return HttpResponse('Вы успешно зарегистрировались')


# def name_med_3(request):
#     return render_to_response('1_th.html')
#
# def name_med_4(request):
#     return render_to_response('2_th.html')

def name_med_5(request):
    return render_to_response('registration.html')

def name_med_6(request):
    return render_to_response('patient.html')

# def name_med_7(request):
#     drug_1 = request.POST['drug']

# # вьшка по первой и второй таблице
# def name_med_8(request):
#     d = request.POST['drug'].lower()
#     b = request.POST['drug'].lower()
#     name_1 = First_tab.objects.filter(drug=d)
#     name_2 = Second_tab.objects.filter(drug=b)
#     if len(name_1) == 0:
#         return HttpResponse('такого вещества нет.')
#     elif len(name_2) > 0 and name_1[0].drug == name_2[0].drug:
#         return render_to_response('patient_2.html', {'drug_1': name_1[0], 'drug_2': name_2[0]})
#     else:
#         return render_to_response('patient_2.html', {'drug_1': name_1[0]})

def name_med_8(request):
    common = request.POST['drug'].lower()
    name_common = Common_tad.objects.filter(drug=common)
    if len(name_common) == 0:
        return HttpResponse('такого вещества нет.')
    else:
        return render_to_response('patient_2.html', {'drug_1': name_common[0]})




def name_med_9(request):
    return render_to_response('doctor.html')

def name_med_10(request):
    return render_to_response('farm.html')

# вьшка по первой и второй таблице
# def name_med_11(request):
#     d = request.POST['drug'].lower()
#     b = request.POST['drug'].lower()
#     name_1 = First_tab.objects.filter(drug=d)
#     name_2 = Second_tab.objects.filter(drug=b)
#     if len(name_1) == 0:
#         return HttpResponse('такого вещества нет.')
#     elif len(name_2) > 0 and name_1[0].drug == name_2[0].drug:
#         return render_to_response('doctor_2.html', {'drug_1': name_1[0], 'drug_2': name_2[0]})
#     else:
#         return render_to_response('doctor_2.html', {'drug_1': name_1[0]})

def name_med_11(request):
    common = request.POST['drug'].lower()
    name_common = Common_tad.objects.filter(drug=common)
    if len(name_common) == 0:
        return HttpResponse('такого вещества нет.')
    else:
        return render_to_response('doctor_2.html', {'drug_1': name_common[0]})


# вьшка по первой и второй таблице
# def name_med_12(request):
#     d = request.POST['drug'].lower()
#     b = request.POST['drug'].lower()
#     name_1 = First_tab.objects.filter(drug=d)
#     name_2 = Second_tab.objects.filter(drug=b)
#     if len(name_1) == 0:
#         return HttpResponse('такого вещества нет.')
#     elif len(name_2) > 0 and name_1[0].drug == name_2[0].drug:
#         return render_to_response('farm_2.html', {'drug_1': name_1[0], 'drug_2': name_2[0]})
#     else:
#         return render_to_response('farm_2.html', {'drug_1': name_1[0]})

def name_med_12(request):
    common = request.POST['drug'].lower()
    name_common = Common_tad.objects.filter(drug=common)
    if len(name_common) == 0:
        return HttpResponse('такого вещества нет.')
    else:
        return render_to_response('farm_2.html', {'drug_1': name_common[0]})


# def main(request):
#     activate(random.choice(['en', 'ru']))
#     return render_to_response(
#         'index.html',
#         {'title': _('Пациент')}
#     )

def name_med_13(request):
    return render_to_response('about_us.html')

def name_med_14(request):
    return render_to_response('know.html')