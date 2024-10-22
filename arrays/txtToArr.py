def txtToArr(filename):

  with open(filename, 'r') as file:
      data = file.read().strip('[]')  # Удаляем начальную и конечную скобки
      numbers_str = data.split(',')  # Разделяем строку по запятым
      numbers = [int(num) for num in numbers_str if num.strip()]  # Преобразуем в числа и фильтруем пустые строки
  return numbers
