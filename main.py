# input
test_data1 = {
    "k1": "v1",
    "k2": ["v2", "v3", "", {"k21": "v21", "k22": ""}],
    "k3": {"k4": "v4", "k5": ["v5", "v6", None], "k6": {"k7": "v7", "k8": ""}},
    "k9": None,
    "k10": {"k11": "", "k12": "v12"}
}

# desired output example ~ Remove all empty strings and None values from a dictionary
# {"k1": "v1", "k2": ["v2", "v3", {"k21": "v21"}], "k3": {"k4": "v4", "k5": ["v5", "v6"], "k6": {"k7": "v7"}}, "k10": {"k12": "v12"}}

# case without list as a value of a key
test_data2= {
    "k1": "v1",
    "k9": None,
    "k10": {"k11": "", "k12": "v12"}
}

def check_dict(value):
    # filter out the empty strings and None values
    if value=="" or value==None:
        return None
    # check if there's a nested dictionary
    elif isinstance(value,dict):
        r_value={}
        for k,v in value.items():
            return_value=check_dict(v)
            # Add only non None values
            if return_value is not None:
                r_value[k]=return_value
        return r_value
    else:
        return value

output_dict2=check_dict(test_data2)
print(output_dict2)
# current output : {'k1': 'v1', 'k10': {'k12': 'v12'}}
        
    