from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from bs4 import BeautifulSoup


# Create your views here.
@csrf_exempt
def proxy_get(request):
    if request.method == 'GET':
        req_body=request.body
        print(req_body)
        res=requests.get(req_body, headers={"Referer": "https://www.google.com/", "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36", "accept-encoding": "gzip, deflate, br",
                                                              "accept-language": "ru,en-US;q=0.9, en;q=0.8",
        "cache-control": "max-age=0","Connection": "keep-alive", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" ,"host": "www.laptopscreen.com",
                                                              "Sec-Fetch-Dest": "document","Upgrade-Insecure-Requests":"1", "TE":"trailers",
                                                              "Sec-Fetch-User": "?1", "Sec-Fetch-Site":None})
        soup = BeautifulSoup(res.text, 'html.parser')
        clear_test=soup.prettify()
        return HttpResponse(clear_test)