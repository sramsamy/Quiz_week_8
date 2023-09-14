import matplotlib.pyplot as plt
import sqlite3
# connecting to the database
connection = sqlite3.connect(r'climate.db')
cursor = connection.cursor()
# fetching the values from the database
cursor.execute("SELECT * FROM ClimateData")
print("fetchall:")
years = []
co2 = []
temp = []
result = cursor.fetchall()
for r in result:
    print(r)
    # populate the lists above with the values fetched from the db
    years.append(r[0])
    co2.append(r[1])
    temp.append(r[2])
# testing to make sure I correctly populated each list
print(years)
print(co2)
print(temp)

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
plt.savefig("co2_temp_1.png") 
