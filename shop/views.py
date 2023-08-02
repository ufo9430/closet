from django.shortcuts import render
from . import models
import os, requests

# Create your views here.
file_dir = os.path.dirname(__file__)
file_path = os.path.join(file_dir, 'secret.txt')
file = open(file_path, "r").readline().split(" ")

URL = "https://openapi.naver.com/v1/search/shop"
CLIENT_ID = file[0]
CLIENT_SECRET = file[1]

def search_item(keyword):
    search_word = keyword
    encode_type = "json"
    sort = "sim"
    
    max_display= 100
    start = 1

    productlist = []
    
    headers = {"X-Naver-Client-Id": CLIENT_ID, "X-Naver-Client-Secret": CLIENT_SECRET}

    url = URL+f".{encode_type}?query={search_word}&display={str(int(max_display))}&start={str(int(start))}&sort={sort}"
    r = requests.get(url, headers=headers)

    if "200" in str(r):
        for data in enumerate(r.json()['items']):
            productlist.append(data[1])
    
    return productlist
def brand(request, current_brand):
    brand_list = models.BRAND_LIST.values()
    productlist = search_item(current_brand)
    context = {'productlist' : productlist, 'brandlist' : brand_list}
    return render(request, 'shop/shop_main.html', context = context)

def main(request):
    brand_list = models.BRAND_LIST.values()
    productlist = search_item("유니폼브릿지")
    context = {'productlist' : productlist, 'brandlist' : brand_list}
    return render(request, 'shop/shop_main.html', context=context)