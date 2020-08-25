from django.http import HttpResponse
from django.shortcuts import render
from house import models
import math


# Create your views here.
def change(page, total_page):
    page = int(page)
    if page < 1:
        page = 1
    elif page > total_page:
        page = total_page

    return page


def house_info(request):
    size = 20

    house = models.Nanjing.objects.all()
    total_page = int(math.ceil(len(house)*1.0/size))

    page = request.GET.get('num', 1)
    page = change(page, total_page)

    show_house = house[((page-1)*size):(page*size)]

    return render(
        request,
        'house.html',
        {
            'house': show_house,
            'now_page': page,
            'pre_page': page-1,
            'next_page': page+1,
            'end_page': total_page
        }
    )
