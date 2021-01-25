class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, name, age, tipo):
        if str(tipo)=='leon':
            self.animals.append(Leones(name, age))
        elif str(tipo)=='tigre':
            self.animals.append(Tigres(name, age))
        elif str(tipo) == 'oso':
            self.animals.append(Osos(name, age))
        return self.animals[len(self.animals)-1]

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

class Animals(Zoo):
    def __init__(self, name, age, salud, felicidad):
        self.name = name
        self.age =age
        self.nivel_salud=salud
        self.nivel_felicidad=felicidad

    def display_info(self):
        print('\nNombre:\t', self.name, '\nEdad:\t', self.age, '\nNivel de salud:\t', self.nivel_salud, '\nNivel de felicidad:\t', self.nivel_felicidad)
        return self

    def alimentacion(self):
        self.nivel_salud += 10
        self.nivel_felicidad += 10

class Leones(Animals):
    def __init__(self, name, age):
        super().__init__(name, age, 30, 100)

    def display_info(self):
        print('\nNombre:\t', self.name, '\nEdad:\t', self.age, '\nNivel de salud:\t', self.nivel_salud, '\nNivel de felicidad:\t', self.nivel_felicidad)
        return self

    def alimentacion(self):
        self.nivel_salud += 50
        self.nivel_felicidad += 200

class Tigres(Animals):
    def __init__(self, name, age):
        super().__init__(name, age, 30, 100)

    def alimentacion(self):
        self.nivel_salud += 20
        self.nivel_felicidad += 180

class Osos(Animals):
    def __init__(self, name, age):
        super().__init__(name, age, 200, 600)
    def alimentacion(self):
        self.nivel_salud += 30
        self.nivel_felicidad += 20


zoologico=Zoo("Zoologico Temuco")
zoologico.add_animal('Nala',4,'leon').alimentacion()
zoologico.add_animal('Rajah',10, 'tigre')
zoologico.add_animal('Baloo',1,'oso').alimentacion()
zoologico.print_all_info()