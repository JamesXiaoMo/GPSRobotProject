import requests


def get_location():
    # 使用 IP 地址定位服务获取位置数据
    response = requests.get("https://ipinfo.io")
    if response.status_code == 200:
        data = response.json()
        location = data["loc"].split(",")  # "loc" 字段包含纬度和经度
        latitude = float(location[0])
        longitude = float(location[1])
        return latitude, longitude
    else:
        raise Exception("Failed to retrieve location data.")


# 获取并打印经纬度
latitude, longitude = get_location()
print(f"Latitude: {latitude}, Longitude: {longitude}")
