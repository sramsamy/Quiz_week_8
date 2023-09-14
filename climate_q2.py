import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv(r'climate.csv')

years = []
co2 = []
temp = []

# Iterate through each row of the dataframe and append values to the lists
for index, row in df.iterrows():
    years.append(row['Year'])
    co2.append(row['CO2'])
    temp.append(row['Temperature'])

# testing to make sure I've appended the correct values to each list
print(years, co2, temp)

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png") 

