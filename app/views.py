from django.shortcuts import redirect, render
from .models import MyCard

def home(request):
    get_all_data = MyCard.objects.all()

    if "like" in request.GET:
        like_id = request.GET["like"]
        check_card = MyCard.objects.filter(pk=like_id)

        if check_card.exists():
            like_or_not = check_card.first().like
            check_card.update(like= not like_or_not)
        
        return redirect("home")        

    sent_html_html = {
        "all_data":get_all_data,
    }
    return render(request,"home.html",sent_html_html)