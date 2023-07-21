from django.shortcuts import render
from .models import Data
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    if 'q' in request.GET:
        q = request.GET['q']
        # data = Data.objects.filter(first_name__icontains=q)
        multiple_q = Q(Q(Department__icontains=q) | Q(Section__icontains=q))
        data = Data.objects.filter(multiple_q)

    else:
        data = Data.objects.all()
    page = Paginator(data, 3)

    # datam = Paginator(data,3)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {
        'data': data,
        'page': page,

    }
    return render(request, 'Extensions/index.html', context)
