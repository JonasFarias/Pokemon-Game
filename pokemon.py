class Pokemon:
    def __int__(self, especie, level=1, nome=None):
        self.especie = especie
        self.level = level

        if nome:
            self.nome = nome
        else:
            self.nome = especie

    def __str__(self):
        return ('{}({})'.format(self.nome, self.level))

    def atacar(self, pokemon):
        print('{} atacou {}'.format(self, pokemon))


class PokemonEletrico(Pokemon):
    tipo = 'eletrico'
    def atacar(self, pokemon):
        print('{}Soltou um raio do trovao e {}'.format(self, pokemon))


class PokemonFogo(Pokemon):
    tipo = 'fogo'
    def atacar(self, pokemon):
        print('{} Soltou um lança chamas em {}'.format(self, pokemon))
class PokemonAgua(Pokemon):
    tipo = 'agua'
    def atacar(self, pokemon):
        print('{} Soltou um jato de agua em {}'.format(self, pokemon))

meu_pokemon = PokemonFogo('charmander')
pokemon_amigo = PokemonEletrico()

print(meu_pokemon)
print(pokemon_amigo)