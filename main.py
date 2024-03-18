test_data1 = {
    "k1": "v1",
    "k2": ["v2", "v3", "", {"k21": "v21", "k22": ""}],
    "k3": {"k4": "v4", "k5": ["v5", "v6", None], "k6": {"k7": "v7", "k8": ""}},
    "k9": None,
    "k10": {"k11": "", "k12": "v12"}
}

# {"k1": "v1", "k2": ["v2", "v3", {"k21": "v21"}], "k3": {"k4": "v4", "k5": ["v5", "v6"], "k6": {"k7": "v7"}}, "k10": {"k12": "v12"}}


def check_dict(value):
    if value=="" or value==None:
        return None
    elif isinstance(value,dict):
        r_value=value
        for k,v in value.items():
            return_value=check_dict(v)
            if return_value==None:
                del r_value[k]
        return r_value
    return value

test_data2= {
    "k1": "v1",
    # "k2": ["v2", "v3", "", {"k21": "v21", "k22": ""}],
    # "k3": {"k4": "v4", "k5": ["v5", "v6", None], "k6": {"k7": "v7", "k8": ""}},
    # "k9": None,
    "k10": {"k11": "", "k12": "v12"}
}

output_dict=test_data2
for key,value in test_data2.items():
    return_value=check_dict(value)
    if return_value==None:
        del output_dict[key]
        
print(output_dict)

        
    