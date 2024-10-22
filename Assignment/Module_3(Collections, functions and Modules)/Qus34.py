'''Write a Python script to check if a given key already exists in a dictionary.''' 

marks_dict={"english":75,"math":85,"gujarati":75}


key="english"


if key in marks_dict:
    print(f"this key are exists in my dict : {key}")
else:
    print(f"this key are not exists in my dict : {key}")