#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            res = 0
            if i < len(my_list_1) and i < len(my_list_2):
                result = my_list_1[i] / my_list_2[i]
            elif i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
        except ZeroDivisionError:
            print("division by 0")
        except (TypeError, ValueError):
            print("wrong type")
        finally:
            result_list.append(result)
    return result_list
