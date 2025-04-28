#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Node
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel

def create_network():
    net = Mininet(link=TCLink)

    # Routers
    rA = net.addHost('rA', ip=None)
    rB = net.addHost('rB', ip=None)
    rC = net.addHost('rC', ip=None)

    # Hosts
    hA1 = net.addHost('hA1', ip='20.10.172.1/26')
    hA2 = net.addHost('hA2', ip='20.10.172.2/26')

    hB1 = net.addHost('hB1', ip='20.10.172.65/25')
    hB2 = net.addHost('hB2', ip='20.10.172.66/25')

    hC1 = net.addHost('hC1', ip='20.10.172.129/27')
    hC2 = net.addHost('hC2', ip='20.10.172.130/27')

    # LAN Links (hosts to routers)
    net.addLink(hA1, rA)
    net.addLink(hA2, rA)

    net.addLink(hB1, rB)
    net.addLink(hB2, rB)

    net.addLink(hC1, rC)
    net.addLink(hC2, rC)

    # Router interconnections
    net.addLink(rA, rB)
    net.addLink(rB, rC)
    net.addLink(rC, rA)

    net.start()

    # Configure router interfaces manually

    # Router A
    rA.setIP('20.10.172.3/26', intf=rA.defaultIntf())  # LAN A
    rA_intfB = rA.connectionsTo(rB)[0][0]
    rA_intfC = rA.connectionsTo(rC)[0][0]
    rA.setIP('20.10.100.1/24', intf=rA_intfB)
    rA.setIP('20.10.100.2/24', intf=rA_intfC)

    # Router B
    rB.setIP('20.10.172.67/25', intf=rB.defaultIntf())  # LAN B
    rB_intfC = rB.connectionsTo(rC)[0][0]
    rB_intfA = rB.connectionsTo(rA)[0][0]
    rB.setIP('20.10.100.3/24', intf=rB_intfC)
    rB.setIP('20.10.100.4/24', intf=rB_intfA)

    # Router C
    rC.setIP('20.10.172.131/27', intf=rC.defaultIntf())  # LAN C
    rC_intfA = rC.connectionsTo(rA)[0][0]
    rC_intfB = rC.connectionsTo(rB)[0][0]
    rC.setIP('20.10.100.5/24', intf=rC_intfA)
    rC.setIP('20.10.100.6/24', intf=rC_intfB)

    # Enable IP forwarding on routers
    for router in [rA, rB, rC]:
        router.cmd('sysctl -w net.ipv4.ip_forward=1')

    # Testing basic LAN connectivity
    print("*** Testing same LAN host connectivity (pingall)")
    net.pingAll()

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_network()
