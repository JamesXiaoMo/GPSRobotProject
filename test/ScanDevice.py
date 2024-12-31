import socket
from concurrent.futures import ThreadPoolExecutor


def is_port_open(host, port):
    """
    测试目标主机的指定端口是否开放
    :param host: 目标 IP 地址
    :param port: 目标端口号
    :return: True 如果端口开放，否则 False
    """
    try:
        with socket.create_connection((host, port), timeout=2):
            return True
    except (socket.timeout, socket.error):
        return False


def scan_ip(ip, port):
    """
    测试单个 IP 的端口是否开放
    :param ip: 目标 IP 地址
    :param port: 目标端口号
    :return: (IP, 是否开放)
    """
    if is_port_open(ip, port):
        print(f"{ip}:{port} 端口开放")
        return ip
    return None


def scan_network_with_port(ip_range, port, max_threads=50):
    """
    扫描指定网段，测试每个设备的指定端口是否开放
    :param ip_range: 网段范围（如 "192.168.0."）
    :param port: 目标端口号
    :param max_threads: 最大线程数量
    :return: 在线且端口开放的设备列表
    """
    print(f"扫描网段: {ip_range}*，目标端口: {port}")

    devices = []
    with ThreadPoolExecutor(max_threads) as executor:
        futures = [executor.submit(scan_ip, f"{ip_range}{i}", port) for i in range(1, 255)]
        for future in futures:
            result = future.result()
            if result:  # 如果端口开放，添加到设备列表
                devices.append(result)
    return devices


def scanDevices():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print(f"本地 IP 地址: {local_ip}")  # 调试输出本地 IP 地址

        ip_parts = local_ip.split('.')
        network = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}."  # 修正为网段前缀格式
        print(f"扫描网段: {network}*")  # 调试输出网段前缀

        devices = scan_network_with_port(network, 7769)
        print(f"发现的设备: {devices}")
    except Exception as e:
        print(f"错误: {e}")


if __name__ == '__main__':
    scanDevices()