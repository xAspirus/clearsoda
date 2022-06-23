def stage_target(variables: dict, lists: dict):
    return {
        "isStage": True,
        "name": "Stage",
        "variables": variables,
        "lists": lists,
        "broadcasts": {},
        "blocks": {},
        "comments": {},
        "currentCostume": 0,
        "costumes": [
            {
                "assetId": "cd21514d0531fdffb22204e0ec5ed84a",
                "name": "__blank__",
                "md5ext": "cd21514d0531fdffb22204e0ec5ed84a.svg",
                "dataFormat": "svg",
                "rotationCenterX": 240,
                "rotationCenterY": 180,
            }
        ],
        "sounds": [],
        "volume": 100,
        "layerOrder": 0,
        "tempo": 60,
        "videoTransparency": 50,
        "videoState": "on",
        "textToSpeechLanguage": None,
    }


def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])


def project(blocks):
    return {
        "targets": [
            stage_target({}, {}),
            {
                "isStage": False,
                "name": "Main",
                "variables": {},
                "lists": {},
                "broadcasts": {},
                "blocks": blocks,
                "comments": {},
                "currentCostume": 0,
                "costumes": [
                    {
                        "assetId": "cd21514d0531fdffb22204e0ec5ed84a",
                        "name": "__blank__",
                        "bitmapResolution": 1,
                        "md5ext": "cd21514d0531fdffb22204e0ec5ed84a.svg",
                        "dataFormat": "svg",
                        "rotationCenterX": 0,
                        "rotationCenterY": 0,
                    }
                ],
                "sounds": [],
                "volume": 100,
                "layerOrder": 1,
                "visible": True,
                "x": 0,
                "y": 0,
                "size": 100,
                "direction": 90,
                "draggable": False,
                "rotationStyle": "all around",
            },
        ],
        "monitors": [],
        "extensions": [],
        "meta": {"semver": "3.0.0", "vm": "0.2.0", "agent": ""},
    }
