from log import all_logs
from coffee_machine import Coffee_machine
from resumption_of_work import Resumption_of_work

log = all_logs()
log.info_log("start programs", 'main')
coffee_machine = Coffee_machine()  # initialization class coffee_machine
coffee_machine.barrist()

print("Начало работы выбрать из ассортимента:")

als_cofe = coffee_machine.acceptance_of_order()
print(als_cofe)

cofe = eval(input())
cof_int = int(cofe)
cofe_name = als_cofe['cofe_name'][cof_int]
gram_of_coffee = als_cofe['gram_of_coffee'][cof_int]
print(f"Выбрали кофе '{cofe_name}' в наличие {gram_of_coffee} грамм.")

resumption = Resumption_of_work()

res = resumption.dosage_cofe('small', gram_of_coffee, 260)
print(res)
