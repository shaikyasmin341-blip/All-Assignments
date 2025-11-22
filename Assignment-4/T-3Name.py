#Write a Python function that formats full names as ‘Last, First’.
#Example 1: ‘Shaik Yasmin’ → ‘Yasmin, Shaik’
#Example 2: ‘Potti Baby’ → ‘Baby, Potti’
#Example 3: ‘Shaik Yakub’ → ‘Yakub, Shaik’
#Example 4: ‘Shaik Shabana’ → ‘Shabana, Shaik’

def format_name(full_name):
    name_parts = full_name.split()
    first_names = " ".join(name_parts[:-1])
    last_name = name_parts[-1]
    formatted_name = f"{last_name}, {first_names}"
    return formatted_name
print(format_name("Shaik Yasmin"))
print(format_name("Potti Baby"))
print(format_name("Shaik Yakub"))
print(format_name("Shaik Shabana"))
