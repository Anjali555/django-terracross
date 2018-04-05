from django.shortcuts import render
from .models import Email
from datetime import datetime
import re

# Create your views here.
def index(request):
    test_date = datetime.fromtimestamp(1518517440)
    r_t = str(datetime.now() - test_date)
    r_t = r_t.split()
    r_t1 = re.split(r'[:]',r_t[2])

    r_t2 = round(float(r_t1[2]))

    d = {'day':r_t[0],'hour':r_t1[0],'min':r_t1[1],'sec':str(r_t2)}
    if request.method == 'POST':
        email = request.POST.get('EMAIL')
        email_obj = Email(email = email)
        email_obj.save()
    return render(request,'polls/index.html')