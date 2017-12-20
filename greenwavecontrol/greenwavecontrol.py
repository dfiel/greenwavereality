import requests
import xmltodict

def grab_xml(scheme, host):
    url = (str(scheme) + '://' + host + '/gwr/gop.php?cmd=GWRBatch&data=<gwrcmds><gwrcmd><gcmd>RoomGetCarousel</gcmd><gdata><gip><version>1</version><token>1234567890</token><fields>name,status</fields></gip></gdata></gwrcmd></gwrcmds>&fmt=xml')
    response = requests.get(url)
    dict = xmltodict.parse(response.content)
    dict = dict['gwrcmds']['gwrcmd']['gdata']['gip']['room']['device']
    return dict
  
def set_brightness(scheme, host, did, value):
    value = ((int(value)/255)*100)
    url = (str(scheme) + '://' + host + '/gwr/gop.php?cmd=DeviceSendCommand&data=<gip><version>1</version><token>1234567890</token><did>' + did + '</did><value>' + str(value) + '</value><type>level</type></gip>&fmt=xml')
    response = requests.get(url)
    if response.status_code == '200':
        return True
    else:
        return False

def get_brightness(device):
    if 'level' in device:
        level = ((int(device['level'])/100)*255)
        return level
    else:
        return 0

def turn_on(scheme, host, did):
    url = (str(scheme) + '://' + host + '/gwr/gop.php?cmd=DeviceSendCommand&data=<gip><version>1</version><token>1234567890</token><did>' + did + '</did><value>1</value></gip>&fmt=xml')
    response = requests.get(url)
    if response.status_code == '200':
        return True
    else:
        return False

def turn_off(scheme, host, did):
    url = (str(scheme) + '://' + host + '/gwr/gop.php?cmd=DeviceSendCommand&data=<gip><version>1</version><token>1234567890</token><did>' + did + '</did><value>0</value></gip>&fmt=xml')
    response = requests.get(url)
    if response.status_code == '200':
        return True
    else:
        return False

def check_online(device):
    return 'offline' not in device

def grab_token(scheme, host, email, password):
    url = (str(scheme) + '://' + host + '/gwr/gop.php?cmd=GWRLogin&data=<gip><version>1</version><email>' + str(email) + '</email><password>' + str(password) + '</password></gip>&fmt=xml')
    response = requests.get(url)
    return response
