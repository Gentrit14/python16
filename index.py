import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('avarageIqperCountry.csv')

avg_iq_continent = df.groupby('Continent')['Average IQ'].mean()

plt.figure(figsize=(10,6))

avg_iq_continent.plot(kind='line', marker='o', color='skyblue')

plt.title('Avarage IQ per Continent')
plt.xlabel('Continent')
plt.ylabel('Average IQ')

plt.grid(axis='both', linestyle='--', alpha=0.7)

plt.show()

# filtered_df = df[df['Avarage IQ'] >= 100]
#
# filtered_df = filtered_df.sort_values(by="Avarage IQ", ascending=False)
#
# print(filtered_df)
#
# plt.figure(figsize=(14,8))
#
# bars = plt.bar(filtered_df['Country'], filtered_df['Avarage IQ'], color="skyblue")
#
# plt.title("Avarage Iq by Country (IQ >= 100)", fontsize=16)
#
# plt.xlabel('Country' , fontsize=14)
# plt.ylabel('Avarage IQ', fontsize=14)
#
# plt.xticks(rotation=90, fontsize=10)
# plt.yticks(fontsize=10)
#
# plt.grid(axis='y' , linestyle='--' , alpha=0.8)
#
# plt.bar_label(bars, fmt='%.2f', fontsize=10, color='black')
#
# plt.tight_layout()
#
# plt.show()
