import requests


apiurl="http://proxy.tinsoftsv.com/api/changeProxy.php?key=[api_key]&location=[location_id]"
api ="TLf0osBGAbm6yLtwqvLme9zb5B9tYZq7d1pFAe"
location =1
#{"success":true,"data":[{"location":0,"name":"Random"},{"location":"1","name":"Ha Noi"},{"location":"2","name":"Phu Tho"},{"location":"3","name":"Ho Chi Minh"},{"location":"4","name":"Dak Lak"},{"location":"5","name":"Hai Duong"},{"location":"6","name":"Binh Dinh"},{"location":"7","name":"Nghe An"},{"location":"8","name":"Nam Dinh"},{"location":"10","name":"Thai Binh"},{"location":"11","name":"Ha Tinh"},{"location":"14","name":"Bac Ninh"},{"location":"12","name":"Gia Lai"},{"location":"13","name":"Yen Bai"},{"location":"15","name":"Ha Nam"}]}
def getproxy(api,location):
    response = requests.get(f"http://proxy.tinsoftsv.com/api/changeProxy.php?key=[{api}]&location=[{location}")
    response_json = response.json()
    # print(type(response_json))
    proxy = (response_json["proxy"])
    print(proxy)

def statusproxy():
    response = requests.get(f"http://proxy.tinsoftsv.com/api/getProxy.php?key=[{api}]")
    response_json = response.json()
    # print(type(response_json))
    proxy = response_json["proxy"]
    status = response_json["success"]
    timeout = response_json["timeout"]
    location = response_json["location"]
    print(f"Proxy có IP {proxy} tình trạng {status} địa điểm {location} thời gian hết hạn {timeout}")

getproxy("TLf0osBGAbm6yLtwqvLme9zb5B9tYZq7d1pFAe",1)