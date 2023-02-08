id_user = None
input_data = None
result = None

def get_id(num_id):
    global id_user
    id_user = num_id

def get_name(name_value):
    global name
    name = name_value

def get_input_values(values):
    global input_values
    input_values = values

def get_result(res):
    global result
    result = res

def get_time(time):
    global time_value
    time_value = time

def log_save():
    with open('log.txt', 'a', encoding="utf-8") as f:
        f.writelines(f'ID: {id_user}, Name: {name}, Input: {input_values}, Result: {result}, Time entrance: {time_value}\n')