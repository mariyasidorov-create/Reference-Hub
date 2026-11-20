import json
d = json.load(open('build/data_en.json'))['files']
r = json.load(open('references.json'))
r['references'] = [dict(topic=t, section=s, name=n, url=u, description=ds, access=a)
                   for t, ss in d.items() for s, it in ss.items() for n, u, ds, a in it]
r['count'] = len(r['references'])
json.dump(r, open('references.json', 'w'), ensure_ascii=False, indent=1)
print(r['count'])
