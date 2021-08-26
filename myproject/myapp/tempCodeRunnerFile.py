n  HttpResponse(render(request,"thelastpage.html",succ))
    
    
            
#__________________________________________________________________________________________________________________________________________________________________________________________________

#home page
def home(request):
    return render(request,"homepage.html")

#______________________________________________________________________
def adminpass(request):
    return render(request,"adminpass.html")

#______________________________________________________________________
def checkadmin(request):
    num1=request.GET.get("cars")
    num2=request.GET.get("id")
    if num1=="harsh" and num2=="balaji":
        return HttpResponse(render(request,"result.html",conn()))
    elif num1=="" and num2=="":