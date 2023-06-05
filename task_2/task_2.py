import json


def write_order_to_json(*args):
    order_dict = {
        "item": args[0],
        "quantity": args[1],
        "price": args[2],
        "buyer": args[3],
        "date": args[4]
        }
    try:
        with open('task_2/orders.json', 'r', encoding='utf-8') as f_n:
            objs = json.load(f_n)
            num_order = f'order_{len(objs)}'

    except:
        num_order = f'order_{0}'
        objs = {}

    objs[num_order] =order_dict
    with open('task_2/orders.json', 'w', encoding='utf-8') as f_n:
        f_n.write(json.dumps(objs, ensure_ascii=False))


if __name__ == '__main__':
    write_order_to_json("printer", "10", "6700", "Ivanov I.I.", "24.09.2017")
