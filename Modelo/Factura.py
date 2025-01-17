from datetime import date
class Factura:

    def __init__(self) -> None:
        self.__date = date.today()
        self.__objects = []

    @property
    def date(self):
        return self.__date

    @property
    def objects(self):
        return self.__objects

    @objects.setter
    def objects(self, new_object):
        self.__objects.append(new_object)

    def check_in(self, value):
        self.objects.append(value)

    def valor_total(self):
        total = 0
        for articulo in self.objects:
            total = total+articulo.value
        return total