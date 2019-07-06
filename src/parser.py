from src.testObject import TestObject
import json


def object_decoder(obj):
    if '__type__' in obj and obj['__type__'] == 'TestObject':
        return TestObject(obj['mac'], obj['db'])
    print(obj)
    return obj

data = {
    "Devices": [
        {
            "Device": [
                {
                    "mac": "8C-A5-E3-D2-C9-85",
                    "db": -14,
                    "channel": 10
                },
                {
                    "mac": "19-DC-9C-09-26-E8",
                    "db": -40,
                    "channel": 6
                },
                {
                    "mac": "AE-67-05-FD-12-8E",
                    "db": -56,
                    "channel": 2
                }
            ]
        }
    ]
}
data_string = json.dumps(data)
print('ENCODED:', data_string)

decoded = json.loads(data_string, object_hook=object_decoder)
print('DECODED:', decoded)



