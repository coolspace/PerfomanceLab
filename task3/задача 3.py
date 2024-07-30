#values = input("Введите путь к файлу values: ")
#tests = input("Введите путь к файлу tests: ")
#report = input("Введите путь к файлу report: ")#
import json
values_item=0
with open('tests.json', 'r',) as json_file:
    tests_data = json.load(json_file)
with open('values.json', 'r',) as json_file:
     values_data = json.load(json_file)
def extract_element_from_json(obj, path):
    '''
    Extracts an element from a nested dictionary or
    a list of nested dictionaries along a specified path.
    If the input is a dictionary, a list is returned.
    If the input is a list of dictionary, a list of lists is returned.
    obj - list or dict - input dictionary or list of dictionaries
    path - list - list of strings that form the path to the desired element
    '''
    def extract(obj, path, ind, arr):
        '''
            Extracts an element from a nested dictionary
            along a specified path and returns a list.
            obj - dict - input dictionary
            path - list - list of strings that form the JSON path
            ind - int - starting index
            arr - list - output list
        '''
        key = path[ind]
        if ind + 1 < len(path):
            if isinstance(obj, dict):
                if key in obj.keys():
                    extract(obj.get(key), path, ind + 1, arr)
                else:
                    arr.append(None)
            elif isinstance(obj, list):
                if not obj:
                    arr.append(None)
                else:
                    for item in obj:
                        extract(item, path, ind, arr)
            else:
                arr.append(None)
        if ind + 1 == len(path):
            if isinstance(obj, list):
                if not obj:
                    arr.append(None)
                else:
                    for item in obj:
                        arr.append(item.get(key, None))
            elif isinstance(obj, dict):
                arr.append(obj.get(key, None))
            else:
                arr.append(None)
        return arr
    if isinstance(obj, dict):
        return extract(obj, path, 0, [])
    elif isinstance(obj, list):
        outer_arr = []
        for item in obj:
            outer_arr.append(extract(item, path, 0, []))
        return outer_arr















a=(extract_element_from_json(tests_data, ["tests", "id"]))
b=(extract_element_from_json(tests_data, ["tests", "values",'id']))
c=(extract_element_from_json(tests_data, ["tests", "values","values",'id']))
d=(extract_element_from_json(tests_data, ["tests", "values","values","values",'id']))
a.extend(b)
a.extend(c)
a.extend(d)
result = [x for x in a if x is not None]






for test_item in result:
    if test_item == values_data['values'][values_item]['id']:
        tests_datavalues_item=values_item+1
    else: tests_data['tests'][3]['value']=values_data['values'][values_item]['value']
print(values_item)

with open('report.json', 'w') as report_file:
    json.dump(tests_data,  report_file, indent=4)








