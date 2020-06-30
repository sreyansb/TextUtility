#Created by ME-> Has to be created here.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")

def analyze(request):
    #get the text
    given_text=request.POST.get('sami','this is the default text')
    #get the values of all checked buttons present in index.html
    removepunc=request.POST.get('removepunc','off')
    uppercaps=request.POST.get('uppercaps','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    # print(removepunc)
    #Check the calues of each checkbox->I think radio button does better
    flag=1
    params={'purpose':" ",'analysed_text':""}
    if removepunc=='on':
        flag=0
        punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyses=''
        for i in given_text:
            if i not in punctuations:
                analyses+=i
        
        params['purpose']+='Remove all punctuations '
        params['analysed_text']=analyses
        given_text=analyses
        #dont return here instead continue with the evaluations
        #return render(request,'analyze.html',params)

    if uppercaps=='on':
        flag=0
        if params['purpose']=="":
            params['purpose']+='Convert to Uppercase '
        else:
            params['purpose']+='and Convert to Uppercase '
        params['analysed_text']=given_text.upper()
        given_text=given_text.upper()
        #return render(request,'analyze.html',params)

    if extraspaceremover=='on':
        flag=0
        prev=' '
        finaltext=''
        for pres in given_text:
            if not(prev==' ' and prev==pres):
                finaltext+=pres
            prev=pres
        given_text=finaltext
        if params['purpose']=="":
            params['purpose']+='Remove Consecutive Space Remover '
        else:
            params['purpose']+='and Remove Consecutive Space Remover '
        params['analysed_text']=finaltext
        #return render(request,'analyze.html',{'purpose':'Consecutive Space Remover','analysed_text':finaltext})

    if flag:
        return HttpResponse("ERROR")
    else:
        return render(request,'analyze.html',params)
