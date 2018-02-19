import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {
    'debug': True
}
config['web_server'] = {
    'host': '127.0.0.1',
    'port': 80
}
config['db_server'] = {
    'host': '127.0.0.1',
    'port': 3306
}

# ファイルが無ければ生成される
with open('./section6/config.ini', 'w') as config_file:
    config.write(config_file)
