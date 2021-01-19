def process_numbers(my_list):
    if isinstance(my_list, list):
        my_num=[]
        for i in my_list:
            if isinstance(i, int):
                my_num.append(i)
            elif isinstance(i, str) and i.isnumeric():
                my_num.append(int(i))
            else:
                continue
        return my_num
    else:
        return []
    

def process_names(my_list):
    if isinstance(my_list, list):
        my_names=[]
        for i in my_list:
            if isinstance(i, str):
                if i.isnumeric() == False:
                    my_names.append(i)
            else:
                continue
        return my_names
    else:
        return []
