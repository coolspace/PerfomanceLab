import json
with open('values.json', 'r') as values_file:
    values_data=json.load(values_file)
with open('tests.json', 'r') as tests_file:
    tests_data=json.load(tests_file)


for test_item in tests_data['tests']:
    test_id=test_item['id']
    for values_item in values_data['values']:
        if values_item['id']==test_id:
            test_item['value']=values_item['value']
            break
with open('report.json', 'w') as report_file:
    json.dump(tests_data, report_file, indent=4)

for test_item in tests_data['tests'][2]['values']:
    test_id=test_item['id']
    for values_item in values_data['values']:
        if values_item['id']==test_id:
            test_item['value']=values_item['value']
            break
with open('report.json', 'w') as report_file:
    json.dump(tests_data, report_file, indent=4)


for test_item in tests_data['tests'][3]['values']:
    test_id=test_item['id']
    for values_item in values_data['values']:
        if values_item['id']==test_id:
            test_item['value']=values_item['value']
            break
with open('report.json', 'w') as report_file:
    json.dump(tests_data, report_file, indent=4)

for test_item in tests_data['tests'][2]['values'][0]['values']:
    test_id=test_item['id']
    for values_item in values_data['values']:
        if values_item['id']==test_id:
            test_item['value']=values_item['value']
            break
with open('report.json', 'w') as report_file:
    json.dump(tests_data, report_file, indent=4)

for test_item in tests_data['tests'][2]['values'][1]['values']:
    test_id=test_item['id']
    for values_item in values_data['values']:
        if values_item['id']==test_id:
            test_item['value']=values_item['value']
            break
with open('report.json', 'w') as report_file:
    json.dump(tests_data, report_file, indent=4)

for test_item in tests_data['tests'][2]['values'][0]['values'][0]['values']:
    test_id=test_item['id']
    for values_item in values_data['values']:
        if values_item['id']==test_id:
            test_item['value']=values_item['value']
            break
with open('report.json', 'w') as report_file:
    json.dump(tests_data, report_file, indent=4)

for test_item in tests_data['tests'][2]['values'][1]['values'][0]['values']:
    test_id=test_item['id']
    for values_item in values_data['values']:
        if values_item['id']==test_id:
            test_item['value']=values_item['value']
            break
with open('report.json', 'w') as report_file:
    json.dump(tests_data, report_file, indent=4)
