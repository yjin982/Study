from django.shortcuts import render
from sangpum.models import Maker, Product

# Create your views here.
def Main(request):
    return render(request, 'main.html')

def List1(request):    #제조사 전체 목록 보기
    makers = Maker.objects.all()
    return render(request, 'list1.html', {'makers':makers})
    

def List2(request):    #상품 전체 자료 보기
    products = Product.objects.all()
    pcount = len(products)
    return render(request, 'list2.html', {'products':products, 'pcount':pcount})

def List3(request):    #제조사별 상품 자료 보기
    mid = request.GET['id']
    #print(mid)
    mproducts = Product.objects.all().filter(maker_name=mid)
    pcount = len(mproducts)
    return render(request, 'list2.html', {'products':mproducts, 'pcount':pcount})
    