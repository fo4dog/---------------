import csv
import re


def get_data():
    files = ['task_1/info_1.txt', 'task_1/info_2.txt', 'task_1/info_3.txt']
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    os_prod_list = []
    os_name_list = []
    os_code_list = [] 
    os_type_list = []
    
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            text_file = f.read()

            # Изготовитель системы
            os_prod = re.search('Изготовитель системы:\s*\S*', text_file)[0]
            os_prod_list.append(re.split('\s{2,}', os_prod)[-1])

            # Название ОС
            os_name = re.search('Название ОС:\s*.*', text_file)[0]
            os_name_list.append(re.split('\s{2,}', os_name)[-1])
            
            # Код продукта
            os_code = re.search('Код продукта:\s*\S*', text_file)[0]
            os_code_list.append(re.split('\s{2,}', os_code)[-1])

            # Тип системы
            os_type = re.search('Тип системы:\s*\S*', text_file)[0]
            os_type_list.append(re.split('\s{2,}', os_type)[-1])

    for i in range(len(os_type_list)):
        main_data.append([os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]])
    
    return main_data


def write_to_csv(csv_file):
    main_data = get_data()

    with open(csv_file, 'w') as w_f:
        w_f_writer = csv.writer(w_f)
        for row in main_data:
            w_f_writer.writerow(row)



if __name__ == '__main__':
    csv_file = 'task_1/info.csv'
    write_to_csv(csv_file)