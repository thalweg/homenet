#!/usr/bin/env python
from __future__ import print_function
from netaddr import IPAddress, EUI, AddrFormatError
import yaml


with open("hosts.yml", 'r') as stream:
    try:
        hosts = yaml.load(stream)['hosts']
    except yaml.YAMLError as exc:
        print(exc)

hosts_valid = []

for host in hosts:
    name = host.get('name')
    try:
        ip = IPAddress(host.get('ip'))
        mac = EUI(host.get('mac'))
    except AddrFormatError as exc:
        print("Error parsing host '%(name)s': %(exc)s" % locals())
    hosts_valid.append(host)

for host in hosts_valid:
  print('set system static-host-mapping host-name %(name)s inet %(ip)s' % host)
  print('set service dhcp-server shared-network-name LAN1 subnet 192.168.239.0/24 static-mapping %(name)s ip-address %(ip)s' % host)
  print('set service dhcp-server shared-network-name LAN1 subnet 192.168.239.0/24 static-mapping %(name)s mac-address %(mac)s' % host)
