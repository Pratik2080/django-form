from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from . import forms
from . models import UserInfo,Lenden

def index(request):
    return render(request,'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            verifyMail = form.cleaned_data['verify_email']
            mobile_no = form.cleaned_data['mobile_no']
            pan_no = form.cleaned_data['pan_no']
            dob = form.cleaned_data['dob']

            print(name)

            if email != verifyMail:
                raise forms.ValidationError("MAKE SURE EMAILS MATCH!")

            count = 0
            value = mobile_no
            while value != 0:
                value=value//10
                count+=1

            if count != 10:
                raise ValidationError("Enter valid Moblie No")

            for i in range(10):
                if ((i<=4 or i==9) and (pan_no[i]>='A' and pan_no[i]<='Z')):
                    pass
                elif ((i>=5 and i<=8) and (pan_no[i]>='0' and pan_no[i]<='9')):
                    pass
                else:
                    raise ValidationError("Enter valid Pan No")

            form.save()

            form = forms.FormName()
        else:
            form = forms.FormName()
    return render(request,'basicapp/form_page.html',{'form':form})

def invest_view(request):
    form = forms.lendenform()
    interest = 0
    amount =0
    if request.method == 'POST':
        form = forms.lendenform(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            principal = form.cleaned_data['principal']
            rate = form.cleaned_data['rate']
            time = form.cleaned_data['time']

            interest = (principal*rate*time)/100
            amount = principal+interest

            lendenref = form.save(commit=False)
            lendenref.total_amount=amount

            lendenref.save()

            form = forms.lendenform()
        else:
            form = forms.lendenform()

    mydict ={'form':form }
    return render(request,'basicapp/lenden_page.html',context = mydict)
