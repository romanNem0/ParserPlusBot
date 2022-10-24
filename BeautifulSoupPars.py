import requests
import json
from bs4 import BeautifulSoup


def fetch(url, params):
    headers = params["headers"]
    body = params["body"]
    method = params["method"]
    if method == "POST":
        return requests.post(url, headers=headers, data=body)
    if method == "GET":
        return requests.get(url, headers=headers)


amulets = fetch("https://auto.ru/-/ajax/desktop/listing/", {
    "headers": {
        "accept": "*/*",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-type": "application/json",
        "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Linux\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "same-origin",
        "sec-fetch-site": "same-origin",
        "x-client-app-version": "176.0.10156601",
        "x-client-date": "1665592665054",
        "x-csrf-token": "e7b7f19b1abc8b6364ed36a8d1d7d2d2143303aedd189fd6",
        "x-page-request-id": "209131edf9113af0eddcc00d1ca8395e",
        "x-requested-with": "XMLHttpRequest",
        "x-retpath-y": "https://auto.ru/cars/chery/amulet/all/",
        "x-yafp": "{\"a1\":\"k50SxkEd3X4lkQ==;0\",\"a2\":\"fjiD0DfABXvjgLPAUVdm1DhMgCvm2g==;1\",\"a3\":\"l5qhF5PyQMX0A8mx0jNWcQ==;2\",\"a4\":\"lEUyJ2rc3JHpKLnHs+7tr61KlUB6VpWNmkjVLpOuYzVyYQ==;3\",\"a5\":\"hj6bO/Th+STR0w==;4\",\"a6\":\"UiE=;5\",\"a7\":\"mb61YJzTJYEYlg==;6\",\"a8\":\"oPulSPztot0=;7\",\"a9\":\"b59wUBcWZnN3uA==;8\",\"b1\":\"6T2xcKQ6PW4=;9\",\"b2\":\"TkCyYGgEm8kbTw==;10\",\"b3\":\"W3S9w9utxKS5Jg==;11\",\"b4\":\"GGyvDOVNLdA=;12\",\"b5\":\"1C+E1Gp0EJlgVg==;13\",\"b6\":\"gfHSqDMjL/bBdQ==;14\",\"b7\":\"r2XIofXtR6vxzQ==;15\",\"b8\":\"X+8LXdC9eDbDZg==;16\",\"b9\":\"fOfIjH8T2//kpQ==;17\",\"c1\":\"kLXJ3w==;18\",\"c2\":\"q6VjbT52oleeTy6+bzK6ggl3;19\",\"c3\":\"18pndfzYOUJEybLtWRC1CRlE;20\",\"c4\":\"F+yuQLmXUcw=;21\",\"c5\":\"5XcCK7LktN0=;22\",\"c6\":\"JOMQFA==;23\",\"c7\":\"Jd9/Y13FWjo=;24\",\"c8\":\"d8o=;25\",\"c9\":\"znWnC+Bc4xQ=;26\",\"d1\":\"bUuRNlKLFxk=;27\",\"d2\":\"Kxw=;28\",\"d3\":\"iwUSsZvbk9a8HA==;29\",\"d4\":\"jGBfahOalyg=;30\",\"d5\":\"2NQDQQl6qkM=;31\",\"d7\":\"dA/FVyEJP58=;32\",\"d8\":\"8LESb+ZncAI0bM9BDsHuauZTZol1liJ6CXI=;33\",\"d9\":\"w9iakWzvVho=;34\",\"e1\":\"x1HVuDy8Lkdd/w==;35\",\"e2\":\"TIu291xZ7Ew=;36\",\"e3\":\"lfUoIVXsI1M=;37\",\"e4\":\"ZaedY+Qyxms=;38\",\"e5\":\"gy3zS1akF0+r7Q==;39\",\"e6\":\"cH4CnRh2r2M=;40\",\"e7\":\"bron+CT+fBi6FA==;41\",\"e8\":\"RyLLs47imW8=;42\",\"e9\":\"KxNuDTBdKAI=;43\",\"f1\":\"CBhVFIBwmNpaew==;44\",\"f2\":\"/rdPRq2GBzU=;45\",\"f3\":\"bwpNG7DhUVEEnQ==;46\",\"f4\":\"pgzD12gXcjI=;47\",\"f5\":\"w0HvDhKMMeQLrw==;48\",\"f6\":\"f0KTMJzGMuDuBA==;49\",\"f7\":\"AHe/L3MChy+tww==;50\",\"f8\":\"jRNM5Ix0ebcMuQ==;51\",\"f9\":\"m1U/pSivFvM=;52\",\"g1\":\"+Aep/BIpNpn9Gg==;53\",\"g2\":\"LINDaOeBEVVkRw==;54\",\"g3\":\"05IgEHVKQn0=;55\",\"g4\":\"s1U5pgTX+NgGJA==;56\",\"g5\":\"VwQZQ8hdWUE=;57\",\"g6\":\"dI9fifqOOaA=;58\",\"g7\":\"JzbWhr4+DeM=;59\",\"g8\":\"P3FffzvdY3w=;60\",\"g9\":\"f2qgCFUpAD8=;61\",\"h1\":\"xLx+YnM/5KfIVw==;62\",\"h2\":\"sbEB9xaox/lZkw==;63\",\"h3\":\"4sTr3Q2yOHgQsw==;64\",\"h4\":\"HYpRnYkjR7WwBQ==;65\",\"h5\":\"tCx9Yf99waQ=;66\",\"h6\":\"rAZD2yxdEqei9w==;67\",\"h7\":\"sAOYRyE+iWjX1tFaHz4OX9hrdFgf7oNU+a4mk986nnBrnack;68\",\"h8\":\"aCmf67fyI7P64A==;69\",\"h9\":\"rvD/ZRE/Stj+mA==;70\",\"i1\":\"6wEZ0yR/ieU=;71\",\"i2\":\"aP3CNgmna3oKNw==;72\",\"i3\":\"9sEBGephYRXfMg==;73\",\"i4\":\"SKd/puDeeTBA9Q==;74\",\"i5\":\"tz3e5aJacNaKhQ==;75\",\"z1\":\"HuagcV1PHUhCvo4XKHIUcMFiYEB2HLkcXcXD3jQmRHtUuphvQnUDYkT/05Z64XSpEB14wh91VRNSfKsf4agOZw==;76\",\"z2\":\"R4/egmzonhwAc1KcxJSHzF861GEjQJiyxhd13mlX8JVVR7sxoJSbQac7UhqNfxcV+wjXE38PjbenJ1sCad4HJQ==;77\",\"y2\":\"cDaPm44Dhou/zg==;78\",\"y3\":\"NMuMa7rmCtwygA==;79\",\"y6\":\"LAS6r75Sr32/GQ==;80\",\"y8\":\"NC9bRbrF/oyDmw==;81\",\"x4\":\"CLNn26owDNWzTg==;82\",\"z5\":\"2gSrXBIB/sw=;83\",\"z4\":\"nOaQsgd3xSCPQQ==;84\",\"z6\":\"VrNM4wibfm7LKGbh;85\",\"z7\":\"oyvVIwMa+Hy3nGWi;86\",\"z8\":\"w/HxLOuJXAL5F+iQzv4=;87\",\"z9\":\"PIEhkcnfXeZyFADQ;88\",\"y1\":\"oaj3bJRnsIFyOCKJ;89\",\"y4\":\"x7xBOROA4G2+FEkI;90\",\"y5\":\"/Qn2u2WAjvEbYKaCS3Q=;91\",\"y7\":\"ZhCvsxknzPF0S/Uo;92\",\"y9\":\"N82jZzMKEE7KQEJPVmQ=;93\",\"y10\":\"ZfDn3v2LWqjRsiUGTVQ=;94\",\"x1\":\"MZwgjZhNJ519jAU6;95\",\"x2\":\"fi++guvyRJKbQfzTAZ8=;96\",\"x3\":\"0BERXkTgFO3l7VtG;97\",\"x5\":\"676L4pWZvFxZjDll;98\",\"z3\":\"9flxkhIUI5+8IKtMjnR34TEOPdKFWNx/Bk4Q8ANXqyY=;99\",\"v\":\"6.3.1\",\"pgrdt\":\"CGvwa8LJccKIr5TVSIkrscj602g=;100\",\"pgrd\":\"OjlIpQGIq3z43cjk31zxFi8x+7mssXgFkOu4x1G8G4gj4Z82/m+irDaqflIAU4I9HVqMaf1Rs0abxyGtpJhQeZZ7wqf1sSInfq3PtQNA21P7aB6k2qrD1om1SdIR3G+lFaB6g040alR6HFjyRqcU+xLzPa0elvwHxObBPuIe66VdmX6b+uA1TcaItPPSjGWySXVC8skoyTTqoZFs3N8MuYYOZb4=\"}",
        "cookie": "suid=5a87f760726351f7c948a72933dc9174.ac0e60933c4db326b9caa18e9350c03d; autoru_sid=a%3Ag6346df2a2va4sqb4qv2oqefro2o90lh.0555049cb2c97704a18dd189a5cdb607%7C1665589034171.604800.Irp0yLnkNyMUwPcE2ns04A.2BKwkrn0OHrlZGSCBhJQu56Ihmjkr2UOIvjTQx8iP3k; autoruuid=g6346df2a2va4sqb4qv2oqefro2o90lh.0555049cb2c97704a18dd189a5cdb607; autoru_gdpr=1; _csrf_token=e7b7f19b1abc8b6364ed36a8d1d7d2d2143303aedd189fd6; from=direct; yuidlt=1; yandexuid=3219489401665588708; gdpr=0; _ym_uid=1665592620679158121; _ym_visorc=b; spravka=dD0xNjY1NTg5MDQxO2k9MTg1LjIxNS41NC40NDtEPTc4OUFDMDBCMURBRkMwMjIwM0QxMjIxQjZBMDg1NjQzNkZCREVDQzFEODRCQkIyMDRBQTg4N0NBOTcwMEMwQjk3ODZFODZGMTt1PTE2NjU1ODkwNDEyNjIyNzMzNDE7aD1lNTM4NDQ5NTdmYzhlY2IwNjhjZDFkOGQyZmY2NmM0Yw==; counter_ga_all7=2; crookie=+rOYSlCyQ3EwktjoBjSwLRX4R8UAUqtgeqVUCTt/kHbJcKFU87dxEsrO6CmnrBbsgdfX957p034I3LbM4H5iG6z0WN4=; cmtchd=MTY2NTU5MjYyMzcyNg==; _ym_isad=2; _yasc=amANwhMM+2eg7gelUYtB3YzTMgS6O/ZtcaEkINuf118o3FV5; Session_id=noauth:1665589051; yandex_login=; ys=c_chck.3705166096; i=FGfzY+NJlhbbRxQUVs4Wa46MlKiYPHdN8bgmftr9JJ+Qx2KGdt6TddxEGFP/l+aRl8X0+cWbXTqG4wqGuqJWtGBzhjM=; mda2_beacon=1665589051732; sso_status=sso.passport.yandex.ru:synchronized; from_lifetime=1665589058854; _ym_d=1665589074; layout-config={\"win_width\":850,\"win_height\":965}",
        "Referer": "https://auto.ru/cars/chery/amulet/all/",
        "Referrer-Policy": "no-referrer-when-downgrade"
    },
    "body": "{\"catalog_filter\":[{\"mark\":\"CHERY\",\"model\":\"AMULET\"}],\"section\":\"all\",\"category\":\"cars\",\"output_type\":\"list\"}",
    "method": "POST"
})

offers = amulets.json()["offers"]

for offer in offers:
    price = offer["price_info"]["USD"]
    name = offer["vehicle_info"]["model_info"]["name"]
    mileage = offer["state"]["mileage"]
    print(f"Найден {name} стоимостью ${price}, пробег составляет {mileage} непростых километров.")
