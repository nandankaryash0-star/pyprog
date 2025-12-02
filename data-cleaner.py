raw_data = [34,12,54,65,-34,56,-14,-6]
clean_data = []

for value in raw_data:
    if value >= 0 :
        clean_data.append(value)

print(f"Clean Data is {clean_data}")