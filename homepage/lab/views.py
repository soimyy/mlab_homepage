from django.shortcuts import render
from .models import Lab
from django.views import generic
from member.models import Member

# Create your views here.


class IndexView(generic.ListView):
    model = Lab

    def get_context_data(self,**kwargs):
        list_assigned_year =  [str(num) for num in range(2016,2100,1)]
        context = super().get_context_data(**kwargs)
        for x in list_assigned_year:
            # print (num)
            context["qs_" + x] = Member.objects.filter(assigned_year=x)
        # context["qs_2016"] = Member.objects.filter(assigned_year="2016")
        return context
