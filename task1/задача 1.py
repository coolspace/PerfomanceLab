n = int(input())
m = int(input())
one_List = m * [int(i) for i in range(1, n + 1)]
two_List = [' ']
three_List = []
cnt = 0
while two_List[-1] != 1:
    two_List.clear()
    for j in range(cnt, m + cnt):
        two_List.append(one_List[j])
        cnt += 1
    two_List_copy = two_List.copy()
    three_List.append(two_List_copy)
    cnt -= 1
for k in range(len(three_List)):
    print(three_List[k][0], end='')








core=extract_element_from_json(tests_data, ["tests", "id"])





for value_item in values_data["values"]:
                if core == test_id:
                 test_item['value']=value_item['value']
print(test_id)



with open('report.json', 'w') as report_file:
    json.dump(tests_data,  report_file, indent=4)



