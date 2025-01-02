import asyncio

from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QDialog
from bleak import BleakScanner
from windows.BLEUI import Ui_BLE
class BLEHandle:
    def __init__(self):
        super().__init__()
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
            return True
        else:
            print(f"No devices found with service UUID {self.TARGET_SERVICE_UUID}.")
            return False

    async def ConnectBLEDevice(self, contents):
        print(f"Connecting to device at address: {self.device_address}...")
        async with BleakClient(self.device_address) as client:
            print(f"Connected to device: {self.device_address}")

            services = await client.get_services()
            print("Services and Characteristics:")
            for service in services:
                print(f"- Service: {service.uuid}")
                for char in service.characteristics:
                    print(f"  - Characteristic: {char.uuid} (Properties: {char.properties})")

            if self.TARGET_CHARACTERISTIC_UUID in [char.uuid for char in services.characteristics]:
                # 读取特征值
                value = await client.read_gatt_char(self.TARGET_CHARACTERISTIC_UUID)
                print(f"Read from characteristic {self.TARGET_CHARACTERISTIC_UUID}: {value}")

                # 写入特征值
                await client.write_gatt_char(self.TARGET_CHARACTERISTIC_UUID, bytes(contents))
                print(f"Data written to characteristic {self.TARGET_CHARACTERISTIC_UUID}")
            else:
                print(f"Characteristic {self.TARGET_CHARACTERISTIC_UUID} not found on this device.")

            print("Disconnected.")



class BLEScanThread(QThread):
    scan_finished = Signal(list)  # 扫描完成信号，发送设备列表

    def __init__(self, target_service_uuid):
        super().__init__()
        self.target_service_uuid = target_service_uuid

    async def scan_ble(self):
        devices = await BleakScanner.discover(service_uuids=[self.target_service_uuid])
        return devices

    def run(self):
        # 在独立线程中运行异步任务
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        devices = loop.run_until_complete(self.scan_ble())
        self.scan_finished.emit(devices)


class BLEDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_BLE()
        self.ui.setupUi(self)
        self.BLEHandle = BLEHandle()
        self.scan_thread = None

        self.ui.pushButton_2.clicked.connect(self.start_scan)

    def start_scan(self):
        self.scan_thread = BLEScanThread(self.BLEHandle.TARGET_SERVICE_UUID)
        self.scan_thread.scan_finished.connect(self.handle_scan_finished)
        self.scan_thread.start()

    def handle_scan_finished(self, devices):
        if devices:
            self.ui.label.setText(f"Found {len(devices)} devices")
        else:
            self.ui.label.setText("No devices found.")
