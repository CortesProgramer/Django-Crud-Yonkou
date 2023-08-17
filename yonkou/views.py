from django.shortcuts import render, redirect, get_object_or_404
from .forms import ShanksForm, LuffyForm, TeachForm, BuggyForm
from .models import Shanks, Luffy, Teach, Buggy


# Create your views here.

def home(request):
    return render(request, "home.html")


def shanks_view(request):
    if request.method == "GET":
        return render(request, "shanks/shanks_form.html", {
            "shanksForm": ShanksForm
        })
    else:
        Shanks.objects.create(haki=request.POST["haki"], nombre=request.POST["nombre"], edad=request.POST["edad"], dia=request.POST["dia"], hora=request.POST["hora"])
        return redirect("shanksInfo")


def shanks_info(request):
    if request.method == "POST":
        shanks_id = request.POST.get("shanks_id")
        toDelete = Shanks.objects.get(idShanks=shanks_id)
        toDelete.delete()
        return redirect("shanksInfo")
    else:
        getInfo = Shanks.objects.all()
        return render(request, "shanks/shanks_page.html", {
            "shanksdb": getInfo
        })
    


def luffy_view(request):
    if request.method == "GET":
        return render(request, "luffy/luffy_form.html", {
            "luffyForm": LuffyForm
        })
    else:
        Luffy.objects.create(nombre=request.POST["nombre"], haki=request.POST["haki"], edad=request.POST["edad"], dia=request.POST["dia"], hora=request.POST["hora"])
        return redirect("luffyInfo")
    
    
def luffy_info(request):
    if request.method == "POST":
        luffy_id = request.POST.get("luffy_id")
        idToDelete = Luffy.objects.get(idLuffy=luffy_id)
        idToDelete.delete()
        return redirect("luffyInfo")
    else:    
        getInfo = Luffy.objects.all()
        return render(request, "luffy/luffy_page.html", {
            "luffydb": getInfo
        })


def teach_view(request):
    if request.method == "GET":
        return render(request, "teach/teach_form.html", {
            "teachForm": TeachForm
        })
    else:
        Teach.objects.create(haki=request.POST["haki"], nombre=request.POST["nombre"], edad=request.POST["edad"], dia=request.POST["dia"], hora=request.POST["hora"])
        return redirect("teachInfo")
    

def teach_info(request):
    if request.method == "POST":
        teach_id = request.POST.get("teach_id")
        idToDelete = Teach.objects.get(idTeach=teach_id)
        idToDelete.delete()
        return redirect("teachInfo")
    else:
        teachdb = Teach.objects.all()
        return render(request, "teach/teach_page.html", {
            "teachdb": teachdb
        })


def buggy_view(request):
    if request.method == "GET":
        return render(request, "buggy/buggy_form.html", {
            "buggyForm": BuggyForm
        })
    else:
        Buggy.objects.create(nombre=request.POST["nombre"], haki=request.POST["haki"], edad=request.POST["edad"], dia=request.POST["dia"], hora=request.POST["hora"])
        return redirect("buggyInfo")
    
    
def buggy_info(request):
    if request.method == "POST":
        id_buggy = request.POST.get("id_buggy")
        idToDelete = Buggy.objects.get(idBuggy=id_buggy)
        idToDelete.delete()
        return redirect("buggyInfo")
    else:
        getInfo = Buggy.objects.all()
        return render(request, "buggy/buggy_page.html", {
            "buggydb": getInfo
        })