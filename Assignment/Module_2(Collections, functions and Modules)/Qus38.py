'''Write a Python program to check multiple keys exists in a dictionary '''


marks_dict={"english":75,"math":85,"gujarati":75}


keys_list=["english",'math','hindi',"secince"]

for key in keys_list:
    if key in marks_dict:
        print(f"this key are exists in my dict : {key}")
    else:
        print(f"this key are not exists in my dict : {key}")