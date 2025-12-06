raw_data = [2,5,1,6,76,87,34,-67,-45,34,-45,-98,-65]
clean_data = [ x for x in raw_data if x>=0 and x % 2 == 0]

print(clean_data)