# looping dictionary

teman_teman = {
    "cup":'ucup surucup',
    'tong':'otong surotong',
    'dung':'dudung surudung',
    'sep':'asep surasep',
    'cuy':'ucuy surucuy'
}

# looping first try(yang keluar adalah keynya)

for teman in teman_teman:
    print(teman)

# operator untuk menganmbil item / iterables
keys = teman_teman.keys()
print(keys)

for keys in teman_teman.keys():
    print(teman_teman.get(keys))

values = teman_teman.values()
print(values)

for value in teman_teman.values():
    print(value)

items = teman_teman.items()
print(items)

for items in teman_teman.items():
    print(items)

    for key,value in teman_teman.items():
        print(f"key = {key}, value = {value}")