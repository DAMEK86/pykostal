import kostal
import json
import asyncio
from kostal.DxsApi import DxsResponse
from kostal.InfoEvents import InfoEvents
from kostal.StatisticDay import StatisticDay

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
    entry = result.get_entry_by_id(StatisticDay.YIELD)
    print(entry.dxsId, 'corresponds to', entry.value)


def test_parse_event():
    event = InfoEvents.parse_event([36, 90, 91, 106, 98, 17, 83, 0])

    assert event.timestamp == 1784371748
    assert event.date.isoformat() == "2026-07-18T10:49:08+00:00"
    assert event.code == 4450
    assert event.env == "0053h"
    assert event.raw == (36, 90, 91, 106, 98, 17, 83, 0)


def test_parse_empty_event():
    assert InfoEvents.parse_event([0, 0, 0, 0, 0, 0, 0, 0]) is None


def test_events():
    class FakeInverter:
        async def fetch_props(self, *prop_ids):
            assert prop_ids == (
                InfoEvents.EVENT_COUNT,
                *InfoEvents.EVENT_IDS,
            )
            return DxsResponse(
                dxsEntries=[
                    {"dxsId": InfoEvents.EVENT_COUNT, "value": 3},
                    {
                        "dxsId": InfoEvents.FIRST_EVENT,
                        "value": [36, 90, 91, 106, 98, 17, 83, 0],
                    },
                    {
                        "dxsId": InfoEvents.FIRST_EVENT + 1,
                        "value": [164, 25, 91, 106, 98, 17, 94, 0],
                    },
                    {
                        "dxsId": InfoEvents.FIRST_EVENT + 2,
                        "value": [42, 251, 89, 106, 98, 17, 81, 0],
                    },
                ],
                session={"sessionId": 784459231, "roleId": 2},
                status={"code": 0},
            )

    events = asyncio.run(InfoEvents(FakeInverter()).events())

    assert [event.code for event in events] == [4450, 4450, 4450]
    assert [event.env for event in events] == ["0053h", "005Eh", "0051h"]
