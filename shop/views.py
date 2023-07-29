from django.shortcuts import render
import os, urllib, json

# Create your views here.
file_dir = os.path.dirname(__file__)
file_path = os.path.join(file_dir, 'secret.txt')
file = open(file_path, "r").readline().split(" ")

URL = "https://openapi.naver.com/v1/search/shop.json?query="
CLIENT_ID = file[0]
CLIENT_SECRET = file[1]

def search(request):
    return render(request, 'shop_main.html')
def main(request):
    query = "시즌오프"
    query = urllib.parse.quote(query)
    link = URL + query
    
    search_req = urllib.request.Request(link)
    search_req.add_header('X-Naver-Client-Id', CLIENT_ID)
    search_req.add_header('X-Naver-Client-Secret', CLIENT_SECRET)
    
    search_res = urllib.request.urlopen(search_req)
    
    print(search_res.read().decode('utf-8'))

    return render(request, 'shop/shop_main.html')