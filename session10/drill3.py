pokedex = {
    "bulbasur": '''Bulbasaur can be seen napping in bright sunlight. 
There is a seed on its back. By soaking up the sun's rays, the seed grows progressively larger.''',
    "ivysaur": '''There is a bud on this Pokémon's back. To support its weight, Ivysaur's legs and trunk grow thick and strong.
If it starts spending more time lying in the sunlight, it's a sign that the bud will bloom into a large flower soon.''',
    "charmander": 'The flame that burns at the tip of its tail is an indication of its emotions.',
    "squirtle": '''Squirtle's shell is not merely used for protection.
The shell's rounded shape and the grooves on its surface help minimize resistance in water, 
enabling this Pokémon to swim at high speeds.''',
    "mewtwo": '''Mewtwo is a Pokémon that was created by genetic manipulation. 
However, even though the scientific power of humans created this Pokémon's body, 
they failed to endow Mewtwo with a compassionate heart.''',
    "pikachu": '''Whenever Pikachu comes across something new, it blasts it with a jolt of electricity. 
If you come across a blackened berry, it's evidence that this Pokémon mistook the intensity of its charge.'''
}

while True:
    phantu = input("Enter your Pokemon: ")
    phantu = phantu.lower()
    pokedex[phantu]
    print(pokedex[phantu])

 






