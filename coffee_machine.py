from log import all_logs
from bd import Bd_pg
from check import checkses
import time
from resumption_of_work import Resumption_of_work
log = all_logs() #initialization log
pg = Bd_pg() #initialization bd
connect = pg.create_connection("postgres", "postgres", "123456", 'localhost', "5432")  #initialization connect to bd
checks = checkses()
res_of_work = Resumption_of_work()
# class coffee_machine
"""
Кофе машина (прием заказа, помол кофе, проверка есть ли кофе (нет выдать сигнал, нет помол), 
функция дозировка (small, Large, Extra ), добавить (сливки, молоко), узор (сердце, и т д делаем random) , 
после выдачи заказа формируем чек + к чеку одно из 5 умных пожеланий random + , 
запросить (кофе, сахар, сливки) );
"""
class Coffee_machine():

    log.info_log("object initialization", 'coffee_machine')
    def acceptance_of_order(self):
        select = pg.Get_the_result_two(
            "SELECT trim(cofe_name) as cofe_name, gram_of_coffee FROM  public.coffee_machine",
            connect
        )
        return select

    def barrist(self):
        rezult = 0
        grinding_coffee = checks.check_grinding_coffee(0, 1)
        if grinding_coffee == False:
            print("Вызвать Барри ста")
            barist = eval(input())
            if barist == 1:
                print("loading....")
                rezult = res_of_work.updates()
                time.sleep(1)
        return rezult