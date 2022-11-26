class Internet():
    def __init__(self, name, mac_address):
        self.name = name
        self.mac_address = mac_address
class PCI():
    def __init__(self, bus, vendor):
        self.bus = bus
        self.vendor = vendor
class USB():
    def __init__(self, device):
        self.device = device
class Wireless(Internet):
    def __init__(self, name, mac_address):
        Internet.__init__(self, name, mac_address)
class PCIinternet(PCI, Internet):
    def __init__(self, bus, vendor, name, mac_address):
        PCI.__init__(self, bus, vendor)
        Internet.__init__(self, name, mac_address)
class USBWireless (USB,Wireless):
    def __init__(self, device, name, mac_address):
        USB.__init__(self, device)
        Wireless.__init__(self, name, mac_address)
enth0 = PCIinternet('pci :0:0:1', 'realtek', 'enthO', '00:11:22:33:44')
wlan0 = USBWireless('usb0', 'wlan0', '00:33:44:55:66')

print('PCIEthernet é uma PCI?', isinstance(enth0, PCI))

print('PCIEthernet é uma Ethernet?', isinstance(enth0, Internet))

print('PCIEthernet é uma USB?', isinstance(enth0, USB))

print('\nUSBWireless é uma USB?', isinstance(wlan0, USB))

print('USBWireless é uma Wireless?', isinstance(wlan0, Wireless))

print('USBWireless é uma Ethernet?', isinstance(wlan0, Internet))

print('USBWireless é uma PCI?', isinstance(wlan0, PCI))
