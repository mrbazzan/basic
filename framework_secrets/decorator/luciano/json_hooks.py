import json

def _hook(data):  # called for any literal object decode ({})
    print("each dict: ", data)
    if "i" in data:
        return {"i": "J"}

    if "int" in data:
        return {"2": "INT"}

    return data

raw = '[{"i": "j"},{"int": 2},{"mano": "mano"}]'
print(json.loads(raw, object_hook=_hook))
