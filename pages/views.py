from django.shortcuts import render

def mainpage(request): # 홈 메인
    return render(request, 'pages/mainpage.html')

def company(request): # 회사소개
    return render(request, 'pages/company_info.html')
