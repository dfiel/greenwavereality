import requests

def grab_xml(host):
    url = ('http://' + host + '/gwr/gop.php?cmd=GWRBatch&data=<gwrcmds><gwrcmd><gcmd>RoomGetCarousel</gcmd><gdata><gip><version>1</version><token>1234567890</token><fields>name,status</fields></gip></gdata></gwrcmd></gwrcmds>&fmt=xml')
    response = requests.get(url)
    return response
  
def set_brightness(host, did, value):
    url = ('http://' + host + '/gwr/gop.php?cmd=DeviceSendCommand&data=<gip><version>1</version><token>1234567890</token><did>' + did + '</did><value>' + str(value) + '</value><type>level</type></gip>&fmt=xml')
    response = requests.get(url)
    return response

def get_brightness(device):
    if 'level' in device:
        level = ((int(device['level'])/100)*255)
        return level
    else:
        return 0

def turn_on(host, did):
    url = ('http://' + host + '/gwr/gop.php?cmd=DeviceSendCommand&data=<gip><version>1</version><token>1234567890</token><did>' + did + '</did><value>1</value></gip>&fmt=xml')
    response = requests.get(url)
    return response

def turn_off(host, did):
    url = ('http://' + host + '/gwr/gop.php?cmd=DeviceSendCommand&data=<gip><version>1</version><token>1234567890</token><did>' + did + '</did><value>0</value></gip>&fmt=xml')
    response = requests.get(url)
    return response

def check_online(device):
    return 'offline' not in device