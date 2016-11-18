import urllib2
import json
import time


def gethttprequest():
    url = 'https://loplatapi.appspot.com/placehandler'
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
            places = jresponse['places']
            for place in places:
                print '--------'
                for name, value in place.iteritems():
                    print name, value
            print len(places)

    except urllib2.HTTPError as e:
        print e.code
        error = e.read()
        print error