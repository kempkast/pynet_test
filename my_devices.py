#!/usr/bin/env python
from getpass import getpass

#def device_list():
rtr1_pass = getpass("Enter router password: ")
rtr2_pass = getpass("Enter router password: ")
sw1_pass = getpass("Enter switch password: ")
sw2_pass = getpass("Enter switch password: ")
sw3_pass = getpass("Enter switch password: ")
sw4_pass = getpass("Enter switch password: ")
pynet_rtr1 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.70',
    'username': 'pyclass',
    'password': rtr1_pass,
}
pynet_rtr2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': rtr2_pass,
}
pynet_sw1 = {
    'device_type': 'arista_eos',
    'ip': '184.105.247.72',
    'username': 'pyclass',
    'password': sw1_pass,
}
pynet_sw2 = {
    'device_type': 'arista_eos',
    'ip': '184.105.247.73',
    'username': 'pyclass',
    'password': sw2_pass,
}
pynet_sw3 = {
    'device_type': 'arista_eos',
    'ip': '184.105.247.74',
    'username': 'pyclass',
    'password': sw3_pass,
}
pynet_sw4 = {
    'device_type': 'arista_eos',
    'ip': '184.105.247.75',
    'username': 'pyclass',
    'password': sw4_pass,
}
