from django.shortcuts import render

# Create your views / Business Logic here 👇.

# Name View
def  name_view(request):  # Name 
    return render(request ,'testapp/name.html')


# Age View
def  age_view(request):  # Age
    name = request.GET['username']
    if name:
        request.session['username']= name
        response = render(request, 'testapp/age.html', {'name':name})
    return response
    
# def age_view(request):
#     name = request.GET('username')
#     if name:
#         request.session['username']= name
#     return render(request, 'testapp/age.html', {'name':name})
   

# Profession View
def profession_view(request):
    # name = request.GET['username']
    age = request.GET['userAge']
    # request.session['username']= name
    request.session['userAge']=age
    name = request.session.get('username')
    return render(request, 'testapp/prof.html', {'age': age, 'name': name})
    
    # response = render(request, 'testapp/prof.html',{'age':age})

    # return response


# Result View
def result_view(request):
    profession = request.GET['uprofession']
    name = request.session.get('username')
    age = request.session.get('userAge')

    
    return render(request, 'testapp/result.html',{
        'name': name, 
        'age': age, 
        'uprofession': profession
    })