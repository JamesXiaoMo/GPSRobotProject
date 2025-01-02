import subprocess

def get_all_ssids():
    result = subprocess.run(["netsh", "wlan", "show", "networks"], capture_output=True, text=True, encoding="utf-8")
    if result.stdout is None:
        print("Error: Failed to retrieve WiFi networks.")
        return []

    ssids = []
    for line in result.stdout.split("\n"):
        if "SSID" in line and "BSSID" not in line:
            # 提取 SSID 的部分，包括空格或特殊字符
            ssid = line.split(":", 1)[-1].strip()
            if ssid:  # 确保不是空字符串
                ssids.append(ssid)

    return ssids

ssids = get_all_ssids()
print("Available WiFi Networks:")
for i, ssid in enumerate(ssids, 1):
    print(f"{i}. {ssid}")

