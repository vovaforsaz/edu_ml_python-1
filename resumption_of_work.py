from log import all_logs
from bd import Bd_pg
log = all_logs() #initialization log
pg = Bd_pg() #initialization bd
connect = pg.create_connection("postgres", "postgres", "123456", 'localhost', "5432")  #initialization connect to bd

class Resumption_of_work():

    def updates(self):
        log.info_log("update all start initialization", 'resumption_of_work')
        e = "update public.coffee_machine set gram_of_coffee = 250 where trim(params) = 'e'"
        a = "update public.coffee_machine set gram_of_coffee = 255 where trim(params) = 'a'"
        b = "update public.coffee_machine set gram_of_coffee = 250 where trim(params) = 'b'"
        c = "update public.coffee_machine set gram_of_coffee = 250 where trim(params) = 'c'"
        work = []
        work.append(pg.update(a, connect))
        work.append(pg.update(e, connect))
        work.append(pg.update(b, connect))
        work.append(pg.update(c, connect))
        log.info_log(f"update final initialization - {work}", 'resumption_of_work')
        return work

    def dosage_cofe(self,name,availability,dosage):
        if name == 'small' and availability - dosage > 0:
            return True
        elif name == 'large' and availability - dosage > 0:
            return True
        elif name == 'extra ' and availability - dosage > 0:
            return True
        else:
            return False