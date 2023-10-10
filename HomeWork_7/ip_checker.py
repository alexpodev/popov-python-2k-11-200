import requests


def check_ip(ip):
    response = requests.get(f"http://ip-api.com/json/{ip}").json()
    if response.get('status') == 'success':
        return response.get('country')
    else:
        print("This IP doesnt exist")
