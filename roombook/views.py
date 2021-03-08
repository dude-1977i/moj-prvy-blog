from django.shortcuts import render

from roombook.models import Rom

# Create your views here.
def post_list(request):
    return render(request, 'roombook/post_list.html', context={"rooms": Rom.objects.all()})