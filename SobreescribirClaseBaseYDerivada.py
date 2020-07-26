"""Funcion super()"""

class Libro:
    def __init__(self, autor, titulo):
        self.autor = autor;
        self.titulo = titulo;

    def info_libro(self):
        print(f"{self.titulo} fue creado por el autor {self.autor}")

class Ficcion(Libro):
    def __init__(self, autor, titulo, editorial):
        super().__init__(autor, titulo)
        self.editorial = editorial

    def info_libro(self):
        print(f"{self.titulo} fue creado por {self.autor} y la editorial es {self.editorial}")

    def invocar_clase_base(self):
        super().info_libro()

def main():
    print("Clase Derivada")
    libro_silva = Ficcion("Daniel Silva", "Principe de Fuego", "Berkley")
    libro_silva.info_libro()
    libro_silva.invocar_clase_base()
    print("-----------------------------------------")
    print("Clase Base")
    libro_reacher = Libro("Lee Child", "Un disparo")
    libro_reacher.info_libro()

if __name__ == "__main__":
    main()
