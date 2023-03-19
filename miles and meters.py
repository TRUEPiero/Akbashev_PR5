print("Это скрипт для конвертации мили в километры")
miles = int(input("Введите мили:"))
metres = miles * 1852
print("Миль: " + str(miles) )
print("Ответ: " + str(float(metres/1000)) + "(км)")
