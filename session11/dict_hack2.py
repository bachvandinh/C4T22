import random
nhanvat = {
    'name': 'Light',
    'age': 17,
    'strength': 8,
    'defense': 10,
    'hp': 100,
    'backpack': ['Shield, Bread Loaf'],
    'gold': 100,
    'level': 2,
}

skill = [
    {
        'name': 'tackle',
        'Minimum level': 1,
        'Damage': 5,
        'Hit rate': 0.3,
    },
    {
        'name': 'quick attack',
        'Minimum level': 2,
        'Damage': 3,
        'Hit rate': 0.5,
    },
    {
        'name': 'strong kick',
        'Minimum level': 4,
        'Damage': 9,
        'Hit rate': 0.5,   
    }
] 
abc = random.random()
nhanvat['gold'] = 150
nhanvat['backpack'].append('flintstone')
# nhanvat['pocket'] = 'MonsterDex', 'Flashlight'
nhanvat.update({'pocket': ['MonsterDex', 'Flashlight']})
# print(nhanvat)

# for i, item in enumerate(skill):
#     print(i+1, item)

for i, bien in enumerate(range(len(skill))):
    print(i+1, skill[bien]['name'])
    # print(skill[bien]['Damage'])
# while True:
user_input = int(input("Use the attack: "))

if skill[user_input-1]['Minimum level'] > nhanvat['level']:
    print("You have to be minimum level:   ",skill[user_input-1]['Minimum level'])
else:
    # print("Damage: ",skill[user_input]['Damage'] )
    if skill[user_input-1]['Hit rate'] > abc:
        print(skill[user_input-1]['name'])
        print("Damage: ",skill[user_input-1]['Damage'] )
        print(abc)
    else:
        print("Target missed")    
        print(abc)