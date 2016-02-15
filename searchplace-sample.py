
# -*- coding: utf-8 -*-

import json
import urllib2


# get loplat place list
def searchplace():
    appid = 'test'
    appkey = 'test'
    url = 'https://loplatapi.appspot.com/searchplace'
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')

    data = {
        'type': 'searchplace',
        'client_id': appid,
        'client_secret': appkey,
        'scan': [
            {'bssid': 'd8:c7:c8:b8:f5:09', 'ssid': 'D2_Startup_Factory', 'rss': -54, 'frequency': 2437},
            {'bssid': 'd8:c7:c8:b8:ea:f0', 'ssid': 'D2_Startup_Factory', 'rss': -55, 'frequency': 5260},
            {'bssid': 'd8:c7:c8:b8:f5:d0', 'ssid': 'D2_Startup_Factory', 'rss': -56, 'frequency': 5745},
            {'bssid': '06:30:0d:59:11:e6', 'ssid': 'kt_eap_roaming', 'rss': -56, 'frequency': 2462},
            {'bssid': '02:30:0d:59:11:e6', 'ssid': 'ollehWiFi ', 'rss': -57, 'frequency': 2462},
            {'bssid': '00:30:0d:59:11:e6', 'ssid': 'ollehWiFi', 'rss': -60, 'frequency': 2462},
            {'bssid': 'd8:c7:c8:b8:ea:e0', 'ssid': 'D2_Startup_Factory', 'rss': -62, 'frequency': 2437},
            {'bssid': 'd8:c7:c8:b8:ea:00', 'ssid': 'D2_Startup_Factory', 'rss': -64, 'frequency': 2462},
            {'bssid': '90:9f:33:7f:71:56', 'ssid': 'loplat', 'rss': -65, 'frequency': 2427},
            {'bssid': '02:30:0d:59:08:7a', 'ssid': 'ollehWiFi', 'rss': -67, 'frequency': 2412}
        ]

    }

    try:
        response = urllib2.urlopen(req, json.dumps(data))
        string = response.read().decode('utf-8')
        jresponse = json.loads(string)
        print jresponse

    except urllib2.HTTPError as e:
        print e.code
        error = e.read()
        print error


searchplace()




