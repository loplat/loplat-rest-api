# loplat-rest-api
loplat's indoor positioning platform REST API - register a place, recognize a place


* REST API List *
1. Recognize a place (with WiFi Scan)
2. Register/Delete/Modify a place



* Detailed Information *

1. loplat 위치 획득을 위한 REST API 명세

URL: https://loplatapi.appspot.com/searchplace

Body: JSON format

{
    'client_id': 'test'
    'client_secret': 'test'
    'type': 'searchplace'
    'scan': [	# WiFi Scan List
        {'bssid': 'aa:bb:cc:dd:ee:ff', 'ssid': "wifi ap's name", 'rss': -77, 'frequency': 2420},
        {'bssid': 'aa:bb:cc:dd:ee:dd', 'ssid': "wifi ap's name2", 'rss': -87, 'frequency': 2437},
        ...
    ]
}

* 참고: ssid에 " 혹은 ' 가 들어가는 경우 데이터 형태가 깨지지 않도록 잘 처리가 필요합니다.

-- response --
1. 위치획득 성공
{
    'status': 'success',
    'type': 'searchplace',
    'place': {
        'name': '스타벅스 천국점',	// 학습시 입력한 장소 이름
        'tags': '#heaven',		// tag 항목에 입력한 내용
        'floor': 1,				// 층수, 지하는 -2 와 같이 표시
        'lat': 37.46621630730324,	// 인식된 장소의 위도
        'lng': 126.8872709199786,	// 인식된 장소의 경도
        'lat_est': 37.465,			// 예측된 위치의 위도 (리니어블의 경우 이 값을 사용)
        'lng_est': 126.8872,		// 예측된 위치의 경도 (리니어블의 경우 이 값을 사용)
        'accuracy': 0.8806016238854542	// 인식된 장소에 있을 확률값. accuracy 가 0.2 보다 작은경우 통상 3~40m 이상 떨어짐
        'threshold': 0.68				// accuracy > threshold 인 경우 해당 장소 반경 10m 이
    }
}

2. client 인증 실패
{
    'status': 'fail',
    'type': 'searchplace',
    'reason': 'Not Allowed Client'
}

3. 위치획득 실패
{
    'status': 'fail',
    'type': 'searchplace',
    'reason': 'Location Acquisition Fail'
}
"""



