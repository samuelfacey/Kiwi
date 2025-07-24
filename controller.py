from modules import Methods

app = Methods()

def ping_client(host_ip:str) -> dict:
    return app.ping_host(host_ip)
