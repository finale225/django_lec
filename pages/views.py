from django.shortcuts import render

def mainpage(request): # 홈 메인
    return render(request, 'pages/mainpage.html')

def company(request): # 회사소개
    return render(request, 'pages/company_info.html')

def news(request): # 소식
    return render(request, 'pages/news.html')

def product_all(request): # 전체 상품
    return render(request, 'pages/product_all.html')

def product_detail(request): # 상품 상세정보
    return render(request, 'pages/product_detail.html')

def newProduct1(request): # 전체 상품
    return render(request, 'pages/newProduct1.html')

def newProduct2(request): # 전체 상품
    return render(request, 'pages/newProduct2.html')

def newProduct3(request): # 전체 상품
    return render(request, 'pages/newProduct3.html')

def ToS(request): # 전체 상품
    return render(request, 'pages/ToS.html')

def privacy_policy(request): # 전체 상품
    return render(request, 'pages/privacy_policy.html')