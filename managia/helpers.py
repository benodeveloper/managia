def parse_form_lists(request):
    """Parse nested form data from a POST request into a list of dicts"""
    form_data = {}
    for list_key, list_value in request.POST.lists():
        list_value = list_value[0]
        if "[][" in list_key:
            key1, key2 = list_key.split("[][")
            key2 = key2.rstrip("]")
            if not form_data.get(key1):
                form_data[key1] = {}
            form_data[key1][key2] = list_value
        else:
            form_data[list_key] = list_value   
    return form_data