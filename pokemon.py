class Pokemon:

    def __int__(self, tipo, especie, level=1, nome=None):
        self.tipo = tipo
        self.especie = especie
        self.level = level

        if nome:
            self.nome = nome

    def __str__(self):
        return ('{}({})'.format(self.nome, self.level))

    def atacar(self, pokemon):
        print('{} atacou {}'.format(self, pokemon))


class PokemonEletrico(Pokemon):
    def atacar(self, pokemon):
        print('{}Soltou um raio do trovao e {}'.format(self, pokemon))


meu_pokemon = PokemonEletrico()
amigo_pokemon = Pokemon()
meu_pokemon.atacar(amigo_pokemon)
amigo_pokemon.atacar(meu_pokemon)