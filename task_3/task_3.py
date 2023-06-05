import yaml


def write_to_yaml (DATA_IN):
    with open('task_3/file.yaml', 'w') as f_n:
        yaml.dump(DATA_IN, f_n, default_flow_style=False, allow_unicode = True)


if __name__ == '__main__':
    DATA_IN = {'items': ['computer', 'printer', 'keyboard', 'mouse'],
           'items_quantity': 4,
           'items_ptice': {'computer': '200€-1000€',
                           'printer': '100€-300€',
                           'keyboard': '5€-50€',
                           'mouse': '4€-7€'}
           }
    write_to_yaml(DATA_IN)

