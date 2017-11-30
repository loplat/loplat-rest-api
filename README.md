#### Note ####
* If you want to see Plengi Android SDK, please refer to https://github.com/loplat/loplat-sdk-android for details
* If you want to see Plengi iOS SDK, please refer to https://github.com/loplat/loplat-sdk-ios for details

# loplat-rest-api
loplat's indoor positioning platform REST API - register a place, recognize a place, and get a place list.

## REST API List
1. Recognize a place (with WiFi Scan)
2. Register/Delete/Modify a place
3. Get a place list


### 1. Recognize a place

* First, scan nearby WiFi APs in Android or IoT Devices.
* Second, deliver the scan result to loplat server.
* Then, loplat server return a recognized place information.

#####request
* Use HTTP POST Method to Recognize a Place
* Request URL: https://loplatapi.appspot.com/searchplace
* Body format (JSON): "scan" 혹은 "blescan" 둘 중 하나만 사용

        "type": "searchplace"        # Mandatory
        "client_id": "test"          # Mandatory
        "client_secret": "test"      # Mandatory
        "scan": [                    # Mandatory
            {
                "bssid": "aa:bb:cc:dd:ee:ff",
                "ssid": "wifi ap's name",
                "rss": -77,
                "frequency": 2420
            },
            {
                "bssid": "aa:bb:cc:dd:ee:dd",
                "ssid": "wifi ap's name2",
                "rss": -87,
                "frequency": 2437
            },
            ...
        ]
        "blescan": [
        	{
            	"uuid": "aaaa-bbbb-cccc-dddd",
                "major": 1,
                "minor": 99,
                "rss": -67
            },
            {
            	"uuid": "eeee-ffff-kkkk-gggg",
                "major": 33,
                "minor": 2734,
                "rss": -88
            },
            ...
        ]

	[주의] ssid에 " 혹은 ' 가 들어가는 경우 데이터 형태가 깨지지 않도록 주의.
	
	* 참고 사항
  	  - 예제에 기입 된 client_id와 client_secret은 test용 임
  	  - 정식 ID와 Secret을 원하시는 분은 아래에 기입 된 Request Key항목 참고 바람



#####response

* 위치획득 성공시 결과 값

        "status": "success",
        "type": "searchplace",
        "place": {
	        "placeid": 1234	  # place id
            "name": "starbucks",  # 학습시 입력한 장소 이름
            "tags": "#heaven",    # tag 항목에 입력한 내용
            "floor": 1,           # 층수, 지하는 -2 와 같이 표시
            "lat": 37.46621630,   # 인식된 장소의 위도
            "lng": 126.8872709,   # 인식된 장소의 경도
            "lat_est": 37.465,    # 예측된 위치의 위도
            "lng_est": 126.8872,  # 예측된 위치의 경도
            "accuracy": 0.8806    # 인식된 장소에 있을 확률값
            "threshold": 0.68
            "client_code": "xxx"  # 장소관리를위해 필요한 임의의 값을 정의해서 사용
            "place_type": "mobile" or "static"
        }

	* accuracy > threshold 인 경우 해당 장소 반경 10m 이내임
	* accuracy 가 0.2 보다 작은경우 통상 30~40m 이상 떨어짐

* client 인증 실패시 오류 값
        "status": "fail",
        "type": "searchplace",
        "reason": "Not Allowed Client"


* 위치획득 실패시 오류 값
        "status": "fail",
        "type": "searchplace",
        "reason": "Location Acquisition Fail"

	**sample code (python): searchplace-sample.py**


### 2. Register a place

* First, scan nearby WiFi APs in Android or IoT Devices.
* Second, register a place with the scan result to loplat server.


#####request
* Use HTTP POST Method to Register a Place
* Request URL: https://loplatapi.appspot.com/placecollector
* Body format (JSON):

        "type": "registerplace",         # Mandatory
        "client_id": "test",             # Mandatory
        "client_secret": "test",         # Mandatory
        "placeinfo": {
        	"placename": "starbucks",   # Mandatory
            "tags": "timesquare, NY",
            "category": "Cafe",         # Mandatory
            "floor": 1,                 # Mandatory
            "lat": 37.5123,             # Mandatory
            "lng": 126.9397,            # Mandatory
            "client_code": "123"
        },
        "footprints": footprints,       # Mandatory
        "bleprints": bleprints

	*client_code* is optional feature. Define any value for your internal usage.

	Allowable *category* list:
    "Cafe", "Company", "Home", "Restaurant", "School", "Theater", "Shop", "Etc"

	[footprints]
    multipl WiFi scans (at least two successive scans)

		[
            # first scan
            [
                # wifi ap 1
                {
                    "bssid": "aa:bb:cc:dd:ee:ff",
                    "ssid": "wifi ap's name",
                    "rss": -77,
                    "frequency": 2420,
                    "scantime": timestamp       # in milliseconds
                },
                # wifi ap 2
                {
                    "bssid": "aa:bb:cc:dd:ee:dd",
                    "ssid": "wifi ap's name2",
                    "rss": -87,
                    "frequency": 2437,
                    "scantime": timestamp       # in milliseconds
                },
                ...
            ],
            # second scan
            [
                {
                    "bssid": "aa:bb:cc:dd:ee:ff",
                    "ssid": "wifi ap's name",
                    "rss": -68,
                    "frequency": 2420,
                    "scantime": timestamp       # in milliseconds
                },
                ...
            ],
        ]

	[bleprints]
    multiple BLE(iBeacon) scans (at least two successive scans).
    each scan collects BLE signals during one second.

        [
            # first scan
            [
                # iBeacon 1
                {
                    "mac": "C3:71:D2:63:2B:A1",
                    "devicename": "EST",
                    "rss": -77,               # averaged strength
                    "scantime": timestamp,    # in milliseconds
                    "devicetype": 1,          # 0: BLE, 1: iBeacon
                    "uuid": "xxxx-1234",      # iBeacon UUID
                    "major": 897,             # iBeacon Major
                    "minor": 300              # iBeacon Minor
                },
                # iBeacon 2
                {
                    "mac": "03:71:D2:63:2B:A1",
                    "devicename": "LOPLAT",
                    "rss": -88,               # averaged strength
                    "scantime": timestamp,    # in milliseconds
                    "devicetype": 1,          # 0: BLE, 1: iBeacon
                    "uuid": "xxxx-yyyy",      # iBeacon UUID
                    "major": 33,              # iBeacon Major
                    "minor": 271              # iBeacon Minor
                },
                ...
            ],
            # second scan
            [
                # iBeacon 1
                {
                    "mac": "C3:71:D2:63:2B:A1",
                    "devicename": "EST",
                    "rss": -73,               # averaged strength
                    "scantime": timestamp,    # in milliseconds
                    "devicetype": 1,          # 0: BLE, 1: iBeacon
                    "uuid": "xxxx-1234",      # iBeacon UUID
                    "major": 897,             # iBeacon Major
                    "minor": 300              # iBeacon Minor
                },
                ...
            ]
        ]

#####response

* 위치획득 성공시 결과 값

        "status": "success",
        "type": "registerplace",
        "placeid": placeid


* client 인증 실패시 오류 값

		"status": "fail",
        "type": "registerplace",
        "reason": "Not Allowed Client"

**sample code (python): placecollector-sample.py**
In sample code, more functions are described.


### 3. Get a place list

#####request
* Use HTTP POST Method to get a place list
* Request URL: https://loplatapi.appspot.com/placehandler
* Body format (JSON):

        "type": "getplacelist"         # Mandatory
        "client_id": "test"             # Mandatory
        "client_secret": "test"         # Mandatory  

#####response
* client 인증 성공시 결과 값

        "status": "success",
        "type": "getplacelist",
        "place": [
	        #first place
		   {
		    	"placeid": 1234
	            "placename": "로플랫",  # 장소 이름
	            "tags": "#D.camp",    # tag
	            "floor": 5,           # 층수
	            "category": "Office"  # 장소 카테고리
	            "lat": 37.46621630,   # 장소의 위도
	            "lng": 126.8872709,   # 장소의 경도
	            "client_code": null  # 장소관리를 위해 필요한 임의의 값
	        }
	        #second place
		   {
   		    	"placeid" = 40552
	            "placename": "starbucks",  # 장소 이름
	            "tags": "#heaven",    # tag
	            "floor": 1,           # 층수
	            "category": "Cafe"    # 장소 카테고리
	            "lat": 37.46621630,   # 장소의 위도
	            "lng": 126.8872709,   # 장소의 경도
	            "client_code": "123" # 장소관리를 위해 필요한 임의의 값
	        }
	        ......
        ]


**sample code (python): placehandler-sample.py**

## Request Key
* If you want to use loplat REST API, please contact US using the guidlines below
 1. Your Name
 2. Your Company
 3. Purpose of your request
* Email Address: Lamen2357@loplat.com
