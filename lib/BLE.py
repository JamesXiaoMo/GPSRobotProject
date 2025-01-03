import asyncio
from bleak import BleakScanner, BleakClient


class BLEHandle:
    def __init__(self):
        self.TARGET_SERVICE_UUID = "66de1d0a-0dd9-44f0-8fa1-85f39668a27c"
        self.TARGET_CHARACTERISTIC_UUID = "6f7e38d5-3acd-42f2-99aa-adf6a410ff92"
        self.devices = []
        self.device_address = None

    async def ScanBLE(self):
        print(f"Scanning for devices with service UUID: {self.TARGET_SERVICE_UUID}")
        self.devices = await BleakScanner.discover(service_uuids=[self.TARGET_SERVICE_UUID])
        if self.devices:
            print(f"Found {len(self.devices)} devices with service UUID {self.TARGET_SERVICE_UUID}:")
            for device in self.devices:
                print(f"Name: {device.name or 'Unknown'}, Address: {device.address}")
            # 自动选择第一个设备
            self.device_address = self.devices[0].address
            return True
        else:
            print(f"No devices found with service UUID {self.TARGET_SERVICE_UUID}.")
            return False

    async def ConnectBLEDevice(self, contents):
        if not self.device_address:
            print("No device address specified. Please scan devices first.")
            return
        print(f"Connecting to device at address: {self.device_address}...")
        async with BleakClient(self.device_address) as client:
            print(f"Connected to device: {self.device_address}")

            # 使用 services 属性获取服务信息
            await client.get_services()  # 确保服务已被解析
            services = client.services
            print("Services and Characteristics:")
            for service in services:
                print(f"- Service: {service.uuid}")
                for char in service.characteristics:
                    print(f"  - Characteristic: {char.uuid} (Properties: {char.properties})")

            # 查找目标特征值
            target_char = None
            for service in services:
                for char in service.characteristics:
                    if char.uuid == self.TARGET_CHARACTERISTIC_UUID:
                        target_char = char
                        break
                if target_char:
                    break

            if target_char:
                # 读取特征值
                value = await client.read_gatt_char(target_char.uuid)
                print(f"Read from characteristic {self.TARGET_CHARACTERISTIC_UUID}: {value}")

                # 写入特征值
                await client.write_gatt_char(target_char.uuid, bytes(contents, 'utf-8'))
                print(f"Data written to characteristic {self.TARGET_CHARACTERISTIC_UUID}")
            else:
                print(f"Characteristic {self.TARGET_CHARACTERISTIC_UUID} not found on this device.")

            print("Disconnected.")


async def main():
    bh = BLEHandle()
    # 扫描设备
    scan_success = await bh.ScanBLE()
    if scan_success:
        # 连接设备并发送数据
        await bh.ConnectBLEDevice("^Jameswu_2.4G|20030521$")


if __name__ == '__main__':
    asyncio.run(main())
