film = {
    'name': 'Star Wars The Last Jedi',
    'year': 2017,
    'actor': ['Daisy Ridley', 'Mark Hamill', 'John Boyega', 
'Kelly Marie Tran', 'Adam Driver', 'Carrie Fischer'],
}

# for i, k in film.items():
#     print(i, k)

film['actor'].append('KhA BaNh') #add dien vien
film.update({'producer': 'Lucasfilms'}) #update
print(film['actor'][1]) #in ra ten actor thu 2
for i in film['actor']:
    print(i)

# print (film, sep= ',')