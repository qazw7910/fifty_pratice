def collect_keys(data, level=1, result=None):
    if result is None:
        result = {}

    if isinstance(data, dict):
        for key, value in data.items():
            if level not in result:
                result[level] = set()
            result[level].add(key)
            collect_keys(value, level + 1, result)
    elif isinstance(data, list):
        for item in data:
            collect_keys(item, level, result)

    return result


if __name__ == '__main__':
    nested_data = {
        "key1": "value1",
        "key2": [
            {"subkey1": "subvalue1"},
            {"subkey2": [
                {"subsubkey1": "subsubvalue1"},
                {"subsubkey2": "subsubvalue2"}
            ]}
        ],
        "key3": {
            "subkey3": "subvalue3",
            "subkey4": [
                {"subsubkey3": "subsubvalue3"},
                "simplevalue"
            ]
        }
    }

    collected_keys = collect_keys(nested_data)

    output = [{f"Level {level}": list(keys)} for level, keys in sorted(collected_keys.items())]
    print(output)
