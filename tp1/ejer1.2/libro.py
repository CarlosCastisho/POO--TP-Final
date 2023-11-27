class Libro:
    def __init__(self,titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def agre_titulo(self):
        return f"Titulo Libro: {self.titulo} \nPrecio: {self.precio}\n--------------------------------------"