def hello():
  print('hellow world')
  
def pack(one, two, three):
  list = [one, two, three]
  print(list)
def eat_lunch(lunch_list):
  for i in lunch_list:
    if lunch_list.index(i) == 0:
      print('first i will eat ' + i + ',')
    else:
      print('then i will eat ' + i + '.')  
  
hello()
pack('pencil', 'shorts' , 'green')
eat_lunch(['beets', 'cheese', 'raw beef'])