from box import ConfigBox
my_dict = {'key': 'value'}
print(my_dict['key'])

# Using ConfigBox
my_config = ConfigBox(my_dict)
print(my_config.key)