#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        res = 0
        try:
            res = (my_list_1[i] / my_list_2[i])
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        except (TypeError, ValueError):
            print("wrong type")
        finally:
            result_list.append(res)

    return result_list
