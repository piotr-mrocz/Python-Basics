config = {
    'website': 'example.com',
    'dbType': 'mysql',
    'dbUser': 'admin',
    'dbPassword': '12345'
    }

print(len(config))
print(config['dbType'])
print()

for key, value in config.items():
    print(f'Key {key} with value {value}')