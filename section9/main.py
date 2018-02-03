print('What is your name')
name = input()

print('Hey {},Which store do you like?'.format(name))

store_name = input()
store_list ={}
store_list.setdefault(store_name, 0)
store_list[store_name] += 1
print(store_list)
print('Thanks! Have a nice day!')
