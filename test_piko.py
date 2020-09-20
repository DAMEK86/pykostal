import kostal
import json
import asyncio


def piko_statistic_day_yield():
    loop = asyncio.get_event_loop()
    inverter = kostal.Piko('http://192.168.2.31', timeout=1)
    loop.run_until_complete(inverter.day_yield())


def test_json():
    # load the data into an element
    data = {"dxsEntries": [{"dxsId": 251658754, "value": 33101.292969}],
            "session": {"sessionId": 0, "roleId": 0},
            "status": {"code": 0}
            }

    # dumps the json object into an element
    json_str = json.dumps(data)

    # load the json to a string
    resp = json.loads(json_str)

    # print the resp
    print("response:", resp)
    result = kostal.DxsResponse(**resp)
    entry = result.get_entry_by_id(kostal.const.StatisticDay['Yield'])
    print(entry.dxsId, 'corresponds to', entry.value)
