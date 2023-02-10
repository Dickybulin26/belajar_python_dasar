# copy dictionary

teman_teman = {
    "cup":'ucup surucup',
    'tong':'otong surotong',
    'dung':'dudung surudung',
    'sep':'asep surasep',
    'cuy':'ucuy surucuy'
}

friends = teman_teman.copy()

print(f'teman_teman : {teman_teman}\n')
print(f'friends : {friends}\n')

teman_teman['cup'] = 'ucup si keren'
print(f'teman_teman : {teman_teman}\n')
print(f'friends : {friends}\n')

# pop dictionary (berdasarkan key)
dataAsep = friends.pop('sep')
print(f'dataAsep : {dataAsep}\n')
print(f"friends = {friends}\n")

# popitem dictionary (yang terakhir saja)
dataTerakhir = friends.popitem()
print(f'dataterakhir : {dataTerakhir}\n')
print(f"friends = {friends}\n")

