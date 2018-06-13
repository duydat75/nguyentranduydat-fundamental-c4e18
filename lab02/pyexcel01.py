import pyexcel
a_list_of_dictionaries = [
 {'x':1,'y':2},
 {'x':3,'y':4}
]
pyexcel.save_as(records=a_list_of_dictionaries, dest_file_name="your_file.")