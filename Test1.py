import random
from random import randint


class Server:
    "Описание работы серверов в сети"
    counter = 1  # переменная для создания N-количества серверов


    def __init__(self, buffer=None, ip=0):
        self.buffer = []
        self.ip = Server.counter
        Server.counter += 1

    def send_data(self, data: object):
        "Функция добавляет объекты класса Data в (список) атрибут класса Router"
        Router.buffer.append(data)

    def get_data(self):
        "Функция вовзращает список принятых пакетов (экземпляры класса Data)"
        output = self.buffer.copy()  # make a copy as items.clear() will clear the object
        self.buffer.clear()
        return output

    def get_ip(self):
        "Функция возвращает IP экземпляра класса Server"
        return self.ip


class Router:
    "описание работы роутера"

    buffer = []  # список для хранения пакетов (обекты класса Data)
    servers = []

    __stop = None

    #Singleton
    def __new__(cls, *args, **kwargs):  # Ограничение по количеству роутеров. По заданию он только 1.
        if cls.__stop is None:
            cls.__stop = super().__new__(cls)
        return cls.__stop


    def link(self, server: object):
        Router.servers.append(server)

    def unlink(self, server):
        Router.servers.remove(server)

    def send_data(self):
        for i in Router.buffer:
            for j in Router.servers:
                if i.ip == j.ip:
                    j.buffer.append(i)
        Router.buffer.clear()



class Data:
    "Описание пакета информации"

    def __init__(self, data: str, ip):
        self.data = data
        self.ip = ip


#Как должна работать программа
router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
print(msg_lst_from[0].data)



