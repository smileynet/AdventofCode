def search_for(dict, lst):
    return [i for i in lst if all(i[target_key] == target_value for target_key, target_value in dict.items())]

dict_to_search_for = {
    'hobby':'skiing',
    'job':'doctor'
}

lst = [{'name':'Mike', 'hobby':'skiing', 'job':'doctor'}, {'name':'Steve', 'hobby':'skiing', 'job':'doctor'}, {'name':'Sally', 'hobby':'chess', 'job':'teacher'} ]

search_for(dict_to_search_for, lst)