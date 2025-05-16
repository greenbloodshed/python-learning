# *Looping through a list:

'''for item_variable in list_name:
    Action to perform with item_variable'''

# You're essentially saying here ^, "For each item in this list, perform the following actions."
# 'item_variable' is the name you assign to each item in the list as the loop iterates through it. This name can be anything you choose.

  # Example:
networks_LAN = ["192.168.0.0", "172.16.0.0", "10.0.0.0"]
for network in networks_LAN:
    print(f"{network} is a private network address")

# *Looping through a dictionary:
# Dictionaries: Collections of key-value pairs.
    
  # Example, Keys:
'''for key_variable in dictionary_name:
    Action to perform w/ key_variable'''

ip_addresses = {
    "public": "156.132.10.4",
    "private": "192.168.10.45",
    "apipa": "169.254.0.1"
}

for key in ip_addresses: # 'key' can be anything. This is the name you are assigning to each key in the dictionary.
    print(key)

# Example, Values:
# Same as keys, only add '.values()' after you call the dictionary.
    
for value in ip_addresses.values(): # 'value' can be anything. This is the value_variable, the name you assign to each value in the called dictionary.
    print(value)

# Example, Both Keys and Values:
# Same as Keys and Values. Seperate the variables with a comma, and add '.items()' when you call the dictionary.

for key, value in ip_addresses.items(): # Remember, the vars can be named anyting. This stands for the items in the dictionary or list your calling.
    print(f"{key}: {value}")
