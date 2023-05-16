from collections import ChainMap

baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
# print(list(ChainMap(adjustments, baseline)))

combined = baseline.copy()
combined.update(adjustments)
store = []
for key, value in combined.items():
    store.append(f"{key}:{value}")

print(store)
