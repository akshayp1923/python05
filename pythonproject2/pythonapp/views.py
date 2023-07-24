from django.http import HttpResponse
from django.shortcuts import render
from.models import places
from.models import individuals



# Create your views here.
def demo(request):
    obj=places.objects.all()
    obj1=individuals.objects.all()


   # item = "hello how r u"
    return render(request, "index.html",{'result':obj,'results':obj1})



#def addition(request):
   # x=int(request.GET["number1"])
   # y=int(request.GET["number2"])
    #res=x*y
    #re=x+y
    #r=x/y

    #return render(request, "thanks.html",{"result":res,"re":re,"res":r})


#def contact(request):
    #return render(request,"contact.html")       }multiple views
#def details(request):
    #return render(request,"details.html")
#def thanks(request):
    #return render(request,"thanks.html")