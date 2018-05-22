import requests

payload={'key1':'value1','key2':'value2'}

r = requests.get('http://httpbin.org/get',params=payload)
print(r.status_code)
# >200
print(r.text)
# >{"args":{"key1":"value1","key2":"value2"},"headers":{"Accept":"*/*","Accept-Encoding":"gzip, deflate","Connection":"close","Host":"httpbin.org","User-Agent":"python-requests/2.18.4"},"origin":"219.116.186.91","url":"http://httpbin.org/get?key1=value1&key2=value2"}
print(r.json())
# >{'args': {'key1': 'value1', 'key2': 'value2'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'close', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.18.4'}, 'origin': '219.116.186.91', 'url': 'http://httpbin.org/get?key1=value1&key2=value2'}

r2=requests.post('http://httpbin.org/post',data=payload)
print(r2.status_code)
# > 200
print(r2.text)
# >{"args":{},"data":"","files":{},"form":{"key1":"value1","key2":"value2"},"headers":{"Accept":"*/*","Accept-Encoding":"gzip, deflate","Connection":"close","Content-Length":"23","Content-Type":"application/x-www-form-urlencoded","Host":"httpbin.org","User-Agent":"python-requests/2.18.4"},"json":null,"origin":"219.116.186.91","url":"http://httpbin.org/post"}
print(r2.json())
# > {'args': {}, 'data': '', 'files': {}, 'form': {'key1': 'value1', 'key2': 'value2'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'close', 'Content-Length': '23', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.18.4'}, 'json': None, 'origin': '219.116.186.91', 'url': 'http://httpbin.org/post'}

r3=requests.put('http://httpbin.org/put',data=payload)
print(r3.status_code)
#> 200
print(r3.text)
#> {"args":{},"data":"","files":{},"form":{"key1":"value1","key2":"value2"},"headers":{"Accept":"*/*","Accept-Encoding":"gzip, deflate","Connection":"close","Content-Length":"23","Content-Type":"application/x-www-form-urlencoded","Host":"httpbin.org","User-Agent":"python-requests/2.18.4"},"json":null,"origin":"219.116.186.91","url":"http://httpbin.org/put"}
print(r3.json())
#> {'args': {}, 'data': '', 'files': {}, 'form': {'key1': 'value1', 'key2': 'value2'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'close', 'Content-Length': '23', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.18.4'}, 'json': None, 'origin': '219.116.186.91', 'url': 'http://httpbin.org/put'}

#timeoutも指定できる
r4=requests.get('http://httpbin.org/get',params=payload,timeout=1)
print(r4.status_code)
#> 200
