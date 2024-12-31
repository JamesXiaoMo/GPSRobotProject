import os
import folium


def create_map(center: int, ip_addr: list, gps_addr=0):
    """
    生成Folium地图并保存为HTML文件
    :return: HTML文件地址
    """
    if gps_addr is None:
        gps_addr = []
    GIS = []
    UniversityGIS = [34.457175, 133.231129]
    # 创建地图对象
    if center == 0:
        GIS = ip_addr
    elif center == 1:
        if gps_addr == 0:
            GIS = UniversityGIS
        else:
            GIS = gps_addr
    elif center == 2:
        GIS = UniversityGIS
    # 添加标记点
    folium_map = folium.Map(location=GIS, zoom_start=20)
    folium.Marker(ip_addr, popup="IP測位", tooltip="IP測位", icon=folium.Icon(color="blue")).add_to(folium_map)
    folium.Marker(UniversityGIS, popup="工学部", tooltip="工学部", icon=folium.Icon(color="green")).add_to(folium_map)
    # 保存为 HTML 文件
    map_path = os.path.abspath("map.html")
    folium_map.save(map_path)
    return map_path