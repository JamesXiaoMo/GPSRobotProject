import asyncio
from bleak import BleakScanner

async def scan_with_service_uuid(target_uuid):
    print(f"Scanning for devices with service UUID: {target_uuid}")
    # 扫描设备，指定 service_uuids 参数
    devices = await BleakScanner.discover(service_uuids=[target_uuid])
    if devices:
        print(f"Found {len(devices)} devices with service UUID {target_uuid}:")
        for device in devices:
            print(f"Name: {device.name or 'Unknown'}, Address: {device.address}")
    else:
        print(f"No devices found with service UUID {target_uuid}.")

# 设置目标 Service UUID
target_service_uuid = "66de1d0a-0dd9-44f0-8fa1-85f39668a27c"  # 示例 UUID，表示心率服务

# 运行异步扫描
asyncio.run(scan_with_service_uuid(target_service_uuid))
