import requests


def get_ip_location_info():
    """
    使用 IP 地址定位服务获取位置数据
    :return:
    """
    response = requests.get("https://ipinfo.io")
    if response.status_code == 200:
        GIS = []
        data = response.json()
        location = data["loc"].split(",")  # "loc" 字段包含纬度和经度
        latitude = float(location[0])
        longitude = float(location[1])
        GIS.append(latitude)
        GIS.append(longitude)
        return GIS
    else:
        raise Exception("Failed to retrieve location data.")
