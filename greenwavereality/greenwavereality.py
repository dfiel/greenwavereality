import requests
import xmltodict

def grab_xml(host, token=None):
    if token:
        scheme = "https"
    if not token:
        scheme = "http"
        token = "1234567890"
    url = (scheme + '://' + host + '/gwr/gop.php?cmd=GWRBatch&data=<gwrcmds><gwrcmd><gcmd>RoomGetCarousel</gcmd><gdata><gip><version>1</version><token>' + token + '</token><fields>name,status</fields></gip></gdata></gwrcmd></gwrcmds>&fmt=xml')
    response = requests.get(url, verify=False)
    dict = xmltodict.parse(response.content)
    dict = dict['gwrcmds']['gwrcmd']['gdata']['gip']['room']['device']
    return dict
  
def set_brightness(host, did, value, token=None):
    if token:
        scheme = "https"
    if not token:
        scheme = "http"
        token = "1234567890"
    url = (scheme + '://' + host + '/gwr/gop.php?cmd=DeviceSendCommand&data=<gip><version>1</version><token>' + token + '</token><did>' + did + '</did><value>' + str(value) + '</value><type>level</type></gip>&fmt=xml')
    response = requests.get(url, verify=False)
    if response.status_code == '200':
        return True
    else:
        return False

def hass_brightness(device):
    if 'level' in device:
        level = int((int(device['level'])/100)*255)
        return level
    else:
        return 0

def turn_on(host, did, token=None):
    if token:
        scheme = "https"
    if not token:
        scheme = "http"
        token = "1234567890"
    url = (scheme + '://' + host + '/gwr/gop.php?cmd=DeviceSendCommand&data=<gip><version>1</version><token>' + token + '</token><did>' + did + '</did><value>1</value></gip>&fmt=xml')
    response = requests.get(url, verify=False)
    if response.status_code == '200':
        return True
    else:
        return False

def turn_off(host, did, token=None):
    if token:
        scheme = "https"
    if not token:
        scheme = "http"
        token = "1234567890"
    url = (scheme + '://' + host + '/gwr/gop.php?cmd=DeviceSendCommand&data=<gip><version>1</version><token>' + token + '</token><did>' + did + '</did><value>0</value></gip>&fmt=xml')
    response = requests.get(url, verify=False)
    if response.status_code == '200':
        return True
    else:
        return False

def check_online(device):
    return 'offline' not in device

def grab_token(host, email, password):
    url = ('https://' + host + '/gwr/gop.php?cmd=GWRLogin&data=<gip><version>1</version><email>' + str(email) + '</email><password>' + str(password) + '</password></gip>&fmt=xml')
    response = requests.get(url, verify=False)
    dict = xmltodict.parse(response)
    dict = dict['gzip']['token']
    return dict
