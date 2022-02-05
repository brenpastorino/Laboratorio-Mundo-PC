from dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contador_teclados = 0

    def __init__(self,tipo_entrada,marca):
        Teclado.contador_teclados += 1
        self._id_teclado = Teclado.contador_teclados
        super().__init__(tipo_entrada,marca)

    def __str__(self):
        return f'Id: {self._id_teclado}, Marca: {self._marca}, Tipo de entrada: {self._tipo_entrada}'

if __name__ == '__main__':
    teclado1 = Teclado('HP','USB')
    print(teclado1)
    teclado2 = Teclado('Gamer','Bluetooth')
    print(teclado2)