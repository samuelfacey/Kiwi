from icmplib import ping

class Methods:

    def __init__(self):
        pass

    def ping_host(self, host_ip:str) -> dict:

        '''Pings the host and returns its status in a dictionary'''

        host = ping(host_ip, count=4, interval=1)

        status = {
            'ip': host.address, # IP address of the host
            'min_rtt': host.min_rtt, # Minimum round-trip time in milliseconds
            'avg_rtt': host.avg_rtt, # Average round-trip time in milliseconds
            'max_rtt': host.max_rtt, # Maximum round-trip time in milliseconds
            'rtts': host.rtts, # List of round-trip times in milliseconds
            'packets_sent': host.packets_sent, # Number of packets sent
            'packets_received': host.packets_received, # Number of packets received
            'packet_loss': host.packet_loss, # Percentage of packet loss
            'jitter': host.jitter, # Jitter in milliseconds
            'is_alive': host.is_alive, # Whether the host is up or not
        }

        return status
