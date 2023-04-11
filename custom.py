#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=RemoteController,
                      ip='127.0.0.1',
                      protocol='tcp',
                      port=6633)

    info( '*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None)
    h9 = net.addHost('h9', cls=Host, ip='10.0.0.9', defaultRoute=None)
    h10 = net.addHost('h10', cls=Host, ip='10.0.0.10', defaultRoute=None)
    h11 = net.addHost('h11', cls=Host, ip='10.0.0.11', defaultRoute=None)
    h12 = net.addHost('h12', cls=Host, ip='10.0.0.12', defaultRoute=None)
    h13 = net.addHost('h13', cls=Host, ip='10.0.0.13', defaultRoute=None)
    h14 = net.addHost('h14', cls=Host, ip='10.0.0.14', defaultRoute=None)
    h15 = net.addHost('h15', cls=Host, ip='10.0.0.15', defaultRoute=None)
    h16 = net.addHost('h16', cls=Host, ip='10.0.0.16', defaultRoute=None)

    info( '*** Add links\n')
    net.addLink(s5, s7)
    net.addLink(s7, s6)
    net.addLink(s5, s1)
    net.addLink(s5, s2)
    s1h1 = {'bw':100}
    net.addLink(s1, h1, cls=TCLink , **s1h1)
    s1h2 = {'bw':100}
    net.addLink(s1, h2, cls=TCLink , **s1h2)
    s1h3 = {'bw':100}
    net.addLink(s1, h3, cls=TCLink , **s1h3)
    s1h4 = {'bw':100}
    net.addLink(s1, h4, cls=TCLink , **s1h4)
    s2h5 = {'bw':100}
    net.addLink(s2, h5, cls=TCLink , **s2h5)
    s2h7 = {'bw':100}
    net.addLink(s2, h7, cls=TCLink , **s2h7)
    s2h6 = {'bw':100}
    net.addLink(s2, h6, cls=TCLink , **s2h6)
    s2h8 = {'bw':100}
    net.addLink(s2, h8, cls=TCLink , **s2h8)
    s3h9 = {'bw':100}
    net.addLink(s3, h9, cls=TCLink , **s3h9)
    s3h10 = {'bw':100}
    net.addLink(s3, h10, cls=TCLink , **s3h10)
    s3h11 = {'bw':100}
    net.addLink(s3, h11, cls=TCLink , **s3h11)
    s3h12 = {'bw':100}
    net.addLink(s3, h12, cls=TCLink , **s3h12)
    s4h13 = {'bw':100}
    net.addLink(s4, h13, cls=TCLink , **s4h13)
    s4h14 = {'bw':100}
    net.addLink(s4, h14, cls=TCLink , **s4h14)
    s4h15 = {'bw':100}
    net.addLink(s4, h15, cls=TCLink , **s4h15)
    s4h16 = {'bw':100}
    net.addLink(s4, h16, cls=TCLink , **s4h16)
    net.addLink(s6, s4)
    net.addLink(s6, s3)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s1').start([])
    net.get('s2').start([])
    net.get('s3').start([])
    net.get('s4').start([])
    net.get('s5').start([])
    net.get('s6').start([])
    net.get('s7').start([c0])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

