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

def search_item(keyword, category):
    search_word = keyword + category
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
def brand(request, item):
    category = request.GET.get('category')
    if category == None:
        category = ""
    brand_list = models.BRAND_LIST
    category_list = models.CATEGORY_LIST
    productlist = search_item(brand_list[item], category)
    context = {'productlist' : productlist, 'brandlist' : brand_list,
                'categorylist' : category_list, 'category' : category,
                'brand' : brand_list[item]}
    return render(request, 'shop/shop_main.html', context = context)

def main(request):
    brand_list = models.BRAND_LIST
    category_list = models.CATEGORY_LIST
    productlist = search_item("", "outer")
    context = {'productlist' : productlist, 'brandlist' : brand_list, 'categorylist' : category_list}
    return render(request, 'shop/shop_main.html', context=context)