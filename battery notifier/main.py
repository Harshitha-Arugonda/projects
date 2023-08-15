'''replit may not support following code, it is working in terminal
'''
import dbus

bus = dbus.SystemBus()
proxy = bus.get_object('org.freedesktop.UPower', '/org/freedesktop/UPower/devices/battery_BAT0')
interface = dbus.Interface(proxy, 'org.freedesktop.DBus.Properties')

battery_info = interface.GetAll('org.freedesktop.UPower.Device')

percentage = battery_info['Percentage']
state = battery_info['State']

print(f'Battery Percentage: {percentage}%')
print(f'Battery State: {state}')
