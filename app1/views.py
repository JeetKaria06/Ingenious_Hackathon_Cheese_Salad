from django.http.response import HttpResponse
from django.shortcuts import render
from .form_app1 import loginForm,registerForm,registerForm_1
from .models import Question, User_table
import json
from rake_nltk import Rake
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
# Create your views here.

def sortSecond(val):
    return val[1]

def recommend_users(title, cosine_sim , indices , df):
    recommended_people = []
    idx = indices[indices == title].index[0] # finds the index of the 'title' given in the 'indices' series
    score_series = [[i, cosine_sim[idx][i]] for i in range(0, len(cosine_sim[idx]))]
    score_series.sort(key=sortSecond, reverse=True)
    
    ind_arr = [score_series[index][0] for index in range(1, min(21, len(df)))]
    top_10_indices = list(ind_arr)
    #print(score_series)
    
    for i in top_10_indices:
        recommended_people.append(list(df['mail_id'])[i])
        
    ans = {'recommend_people':recommended_people, 'match_percentage':score_series[1:min(21, len(df))]}
    
    return ans

def Home(request):
    return render(request,'index.html')


def Login(request):    
    if request.method=='POST':
        email=request.POST.get('emailId')
        password=request.POST.get('password')

        if not User_table.objects.filter(pk=email, password=password).exists():
            print("If not Logged in")
            return render(request,'index.html')
        else:
            request.session['mail_id'] = email
            request.session['is_logged_in'] = True
            request.session['username'] = User_table.objects.filter(email=email).values('username')[0]['username']
            print(request.session['username'])
            username = request.session['mail_id']
            user = pd.DataFrame(list(Question.objects.all().values()))
            #print(user.columns)
            df = pd.DataFrame({'mail_id': [], 'Genre': []})
            for i in range(0, len(Question.objects.all())):
                data = []
                for j in range(2, 27):
                    if(user[user.columns[j]][i]==1):
                        data.append(user.columns[j][2:])
                df = df.append({'mail_id': user['mail_id_id'][i], 'Genre':set(data)}, ignore_index=True)

            json_records = df.to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            #context = {'d': data}
        

            #------------------------------------------------------------------
            df['Bag_of_words'] = ''
            columns = ['Genre']
            for index, row in df.iterrows():
                words = ''
                for col in columns:
                    words += ' '.join(row[col]) + ' '
                row['Bag_of_words'] = words
                df['Bag_of_words'][index] = words

            #print(df.head)

            #--------------------------------------------------------------------
            count = CountVectorizer()
            count_matrix = count.fit_transform(df['Bag_of_words'])
            cosine_sim = cosine_similarity(count_matrix, count_matrix)
            #print(cosine_sim)
            indices = pd.Series(df['mail_id'])
            
            
            #---------------------------------------------------------------
            ans = recommend_users(username,cosine_sim,indices,df)
            print(ans)
            range_ = range(0,len(ans['recommend_people']))
            a = []
            for i in range_:
                obj = {
                    'email_id': ans['recommend_people'][i],
                    'username': User_table.objects.filter(email=ans['recommend_people'][i]).values('username')[0]['username'], # user_name
                    'match_p' : round((ans['match_percentage'][i][1]) * 100), # match_percentage
                    'age' : User_table.objects.filter(email = ans['recommend_people'][i]).values('age')[0]['age'] # age
                }
                a.append(obj)
            
            print(a)
            uname = User_table.objects.filter(email=username).values('username')[0]['username']
            context = {'sender_username':uname, 'data':a}
            return render(request,'dashboard.html', context)
    else:
        loginform=loginForm()
        return render(request,'login.html',{'form':loginform})


def Register(request):
    if request.method=='POST':
        full_name = request.POST.get('FullName')
        user_name = request.POST.get('usrName')
        email_id = request.POST.get('emailId')
        password = request.POST.get('password')
        age = request.POST.get('age')
        phonenumber = request.POST.get('phonenumber')
        country = request.POST.get('Country')
        pincode = request.POST.get('pincode')
        gender = request.POST.get('gender')
        insta_link = request.POST.get('insta_link')
        fb_link = request.POST.get('fb_link')

        if User_table.objects.filter(pk=email_id).exists():
            print("User already exists.")
            return render(request, 'index.html')
        else:
            print('User successfully registered.')
            u = User_table(name=full_name, username = user_name, email = email_id, password=password, mobile_number=phonenumber, age=age, gender=gender, pincode=pincode, country=country, instragram_link=insta_link, Facbook_link=fb_link)
            u.save()
            # loginform=loginForm()
            register=registerForm_1()
            return render(request, 'register_step1.html', {'form':register, 'message':'Successfully Registered', 'user_id':email_id})
    else:
        register=registerForm()
        return render(request,'register.html',{'form':register})


def Register_step1(request,userid):
    register=registerForm_1()
    return render(request,'register_step1.html',{'form':register})


def Dashboard(request):
    if 'is_logged_in' in request.session:
        username = request.session['mail_id']
        user = pd.DataFrame(list(Question.objects.all().values()))
        #print(user.columns)
        df = pd.DataFrame({'mail_id': [], 'Genre': []})
        for i in range(0, len(Question.objects.all())):
            data = []
            for j in range(2, 27):
                if(user[user.columns[j]][i]==1):
                    data.append(user.columns[j][2:])
            df = df.append({'mail_id': user['mail_id_id'][i], 'Genre':set(data)}, ignore_index=True)

        json_records = df.to_json(orient ='records')
        data = []
        data = json.loads(json_records)
        #context = {'d': data}
    

        #------------------------------------------------------------------
        df['Bag_of_words'] = ''
        columns = ['Genre']
        for index, row in df.iterrows():
            words = ''
            for col in columns:
                words += ' '.join(row[col]) + ' '
            row['Bag_of_words'] = words
            df['Bag_of_words'][index] = words

        #print(df.head)

        #--------------------------------------------------------------------
        count = CountVectorizer()
        count_matrix = count.fit_transform(df['Bag_of_words'])
        cosine_sim = cosine_similarity(count_matrix, count_matrix)
        #print(cosine_sim)
        indices = pd.Series(df['mail_id'])
        
        
        #---------------------------------------------------------------
        ans = recommend_users(username,cosine_sim,indices,df)
        print(ans)
        range_ = range(0,len(ans['recommend_people']))
        a = []
        for i in range_:
            obj = {
                'email_id': ans['recommend_people'][i],
                'username': User_table.objects.filter(email=ans['recommend_people'][i]).values('username')[0]['username'], # user_name
                'match_p' : round((ans['match_percentage'][i][1]) * 100), # match_percentage
                'age' : User_table.objects.filter(email = ans['recommend_people'][i]).values('age')[0]['age'] # age
            }
            a.append(obj)
        
        print(a)
        uname = User_table.objects.filter(email=username).values('username')[0]['username']
        context = {'sender_username':uname, 'data':a}
        return render(request,'dashboard.html', context)
    else:
        return render(request, 'login.html')


def UserProfile(request,userid):
    print("HELLO[[[", userid)
    name = User_table.objects.filter(username=userid).values('name')[0]['name']
    email = User_table.objects.filter(username=userid).values('email')[0]['email']
    age = User_table.objects.filter(username=userid).values('age')[0]['age']
    phonenumber = User_table.objects.filter(username=userid).values('mobile_number')[0]['mobile_number']
    country = User_table.objects.filter(username=userid).values('country')[0]['country']
    pincode = User_table.objects.filter(username=userid).values('pincode')[0]['pincode']
    insta_link = User_table.objects.filter(username=userid).values('instragram_link')[0]['instragram_link']
    fb_link = User_table.objects.filter(username=userid).values('Facbook_link')[0]['Facbook_link']
    return render(request,'profile.html', {'fb_link':fb_link, 'insta_link':insta_link, 'user_id': userid, 'name':name, 'email':email, 'age':age, 'phone':phonenumber, 'country':country, 'pincode':pincode})

def Logout(request):
    # del request.session['mykey']
    for key in list(request.session.keys()):
        del request.session[key]
    return render(request, 'index.html')

def AboutUs(request):
    return render(request,'about.html')