from Estrella import Estrella

class Galaxia:

    @staticmethod
    def determinar_galaxia(estrella):
        if estrella.x > 0 and estrella.y > 0 and (estrella.z > 0):
            return 'Galaxia del Primer Octante'
        elif estrella.x < 0 and estrella.y < 0 and (estrella.z < 0):
            return 'Galaxia del Octante Opuesto'
        elif estrella.x == 0 and estrella.y == 0 and (estrella.z == 0):
            return 'Centro del Universo'
        else:
            return 'Galaxia Intermedia'