# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars." '\n')
  return estimated_cost

# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name =
"Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)

akira_insurance_cost = estimate_insurance_cost('Akira', 19, 1, 27.1, 0, 0)

# Add your code here
names = ['Maria', 'Rohan', 'Valentina', 'Akira']
insurance_costs = [4150.0, 5320.0, 35210.0, 2930.0]
insurance_data = zip(names, insurance_costs)
print('Here is the actual insurance cost data: ' + str (list(insurance_data)) +'\n')
estimated_insurance_data = []
estimated_insurance_data.append(('Maria', maria_insurance_cost))
estimated_insurance_data.append(('Rohan', rohan_insurance_cost))
estimated_insurance_data.append(('Valentina', valentina_insurance_cost))
print('Here is the estimated insurance cost data: ' + str(list(estimated_insurance_data))+'\n')

maria_cost_difference = insurance_costs[0] - maria_insurance_cost
#-----------
rohan_cost_difference = insurance_costs[1] - rohan_insurance_cost
#----------
valentina_cost_difference = insurance_costs[2] - valentina_insurance_cost
#----------
differences = [maria_cost_difference, rohan_cost_difference, valentina_cost_difference]
#----------
insurance_cost_difference = zip(names, differences)
print('Here are the differences between actual costs and estimates: ' +  str(list(insurance_cost_difference)))
