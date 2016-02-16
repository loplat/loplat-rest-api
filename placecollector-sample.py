# -*- coding: utf-8 -*-


import urllib2
import json
import time


def gethttprequest():
    url = 'https://loplatapi.appspot.com/placecollector'
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')
    return req


# get loplat place list
def getloplatplaces():

    client_id = 'test'
    client_secret = 'test'
    data = {
        'client_id': client_id,
        'client_secret': client_secret,

        'type': 'getplacelist'
    }

    try:
        response = urllib2.urlopen(gethttprequest(), json.dumps(data))

        string = response.read().decode('utf-8')
        jresponse = json.loads(string)
        result = jresponse['status']
        print result
        print jresponse['reason']
        if result == 'success':
            friends = jresponse['places']
            for friend in friends:
                print '--------'
                for name, value in friend.iteritems():
                    print name, value
            print len(friends)

    except urllib2.HTTPError as e:
        print e.code
        error = e.read()
        print error




# upload wifi scan data & update place info
def registerplace():

    # wifi scans
    footprints = []
    timestampinmillis = int(round(time.time() * 1000))
    scan1 = [{'bssid': '0x1234', 'ssid': 'hello ssid1', 'rss': -77, 'frequency': 2400, 'scantime': timestampinmillis},
             {'bssid': '0xaabc', 'ssid': '이촌 스타벅스', 'rss': -70, 'frequency': 2400, 'scantime': timestampinmillis}]
    timestampinmillis = int(round(time.time() * 1000))
    scan2 = [{'bssid': '0x1234', 'ssid': 'hello ssid1', 'rss': -72, 'frequency': 2400, 'scantime': timestampinmillis},
             {'bssid': '0x4444', 'ssid': 'hello ssid3', 'rss': -71, 'frequency': 2400, 'scantime': timestampinmillis}]
    footprints.append(scan1)
    footprints.append(scan2)

    # ble scans
    bleprints = []
    timestampinmillis = int(round(time.time() * 1000))
    ble_scan1 = [{'mac': '0x1234', 'devicename': 'loplat', 'rss': -77, 'scantime': timestampinmillis, 'devicetype': 1,
                  'uuid': 'xxxx-yyyy', 'major': 897, 'minor': 300},
                 {'mac': '0xabcd', 'devicename': 'sun', 'rss': -80, 'scantime': timestampinmillis, 'devicetype': 1,
                  'uuid': 'xxxx-zzzz', 'major': 899, 'minor': 10}
                 ]
    bleprints.append(ble_scan1)

    # placeinfo
    lat = 37.51945421
    lng = 126.9397389
    placeinfo = {
        'placename': 'starbucks',
        'tags': 'timesquare, manhattan',
        'category': 'Cafe',
        'floor': 1,
        'lat': lat,
        'lng': lng,
        'client_code': '123456789'
    }


    #
    client_id = 'test'
    client_secret = 'test'
    data = {
        'type': 'registerplace',
        'client_id': client_id,
        'client_secret': client_secret,
        'placeinfo': placeinfo,
        'footprints': footprints,
        'bleprints': bleprints
    }

    try:
        response = urllib2.urlopen(gethttprequest(), json.dumps(data))
        string = response.read().decode('utf-8')
        jresponse = json.loads(string)
        print jresponse
        # result = jresponse['status']
        for field, value in jresponse.iteritems():
            print field, value

    except urllib2.HTTPError as e:
        print e.code
        error = e.read()
        print error



def deleteplace(placeid):

    placeinfo = {
        'placeid': placeid,
    }

    client_id = 'test'
    client_secret = 'test'

    data = {
        'type': 'deleteplace',
        'client_id': client_id,
        'client_secret': client_secret,
        'placeinfo': placeinfo,
    }

    try:
        response = urllib2.urlopen(gethttprequest(), json.dumps(data))
        string = response.read().decode('utf-8')
        jresponse = json.loads(string)
        print jresponse
        result = jresponse['status']
        print result

    except urllib2.HTTPError as e:
        print e.code
        error = e.read()
        print error



def modifyplaceinfo(placeid):

    placeinfo = {
        'placeid': placeid,
        'placename': 'McDonald',
        'category': 'Restaurant',
        'tags': '42nd',
        'floor': 99,
        'lat': 37.5,
        'lng': 126.9,
        'client_code': '1234'
    }

    client_id = 'test'
    client_secret = 'test'

    data = {
        'type': 'modifyplaceinfo',
        'client_id': client_id,
        'client_secret': client_secret,
        'placeinfo': placeinfo,
    }

    try:
        response = urllib2.urlopen(gethttprequest(), json.dumps(data))
        string = response.read().decode('utf-8')
        jresponse = json.loads(string)
        print jresponse
        result = jresponse['status']
        print result

    except urllib2.HTTPError as e:
        print e.code
        error = e.read()
        print error




# registerplace()
# deleteplace(8033)
# modifyplaceinfo(8033)
getloplatplaces()





