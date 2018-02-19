import yaml

with open('./section6/config.yml', 'w') as yaml_file:
    yaml.dump({
        'web_server': {
            'host': '127.0.0.1',
            'port': 80
        },
        'db_server': {
            'host': '127.0.0.1',
            'port': 3306
        }
    }, yaml_file, default_flow_style=False)

with open('config.yml', 'r')as yaml_file:
    data = yaml.load(yaml_file)
    print(data, type(data))

"""
{'db_server': {'host': '127.0.0.1', 'port': 3306}, 'web_server': {'host': '127.0.0.1', 'port': 80}} <class 'dict'>
"""
