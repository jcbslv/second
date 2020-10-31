names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here
names.append('Priscilla')
insurance_costs.append(8320.0)

medical_records = list(zip(insurance_costs, names))
abc_records = list(zip(names, insurance_costs))

print(str(medical_records) + '\n') 

num_medical_records = len(medical_records)
print('There are ' + str(num_medical_records) + ' medical records' + '\n')

first_medical_record = medical_records[0]
print('Here is the first medical record: ' + str(first_medical_record) + '\n')

medical_records.sort()
print('Here are the medical records sorted by insurance cost: ' + str(medical_records) + '\n')

abc_records.sort()
print('Here are the medical records sorted alphabetically: ' + str(abc_records) + '\n')

cheapest_three = medical_records[0:3]
print('Here are the three cheapest insurance costs in our medical records: ' + str(cheapest_three) + '\n')

priciest_three = medical_records[-3:]
print('Here are the three moes expensive insurance cost in our medical records: ' + str(priciest_three) + '\n')

occurences_paul = names.count('Paul')
print('There are ' + str(occurences_paul) + ' individuals with the name Paul in our medical records')
