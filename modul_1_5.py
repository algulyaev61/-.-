tuple = 1, 2, 'big', 'show', True
immutable_var = (tuple)
print(immutable_var)
#tuple[2] = 'small' # элемент кортежа невозможно изменить(TypeError)
#print(immutable_var)
mutable_list = ['red', 'white', 'blue']
mutable_list.remove('white')
print(mutable_list)
print(mutable_list[0])