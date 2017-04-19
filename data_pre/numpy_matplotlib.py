#coding=utf-8
import matplotlib.pyplot as plt 
year=[1950,1970,1990,2010]
pop=[2.159,1.997,1.897,2.180]
# plt.plot(year,pop)
# plt.show()

# plt.scatter(year,pop)
# plt.xlabel('year')
# plt.ylabel('population')
# plt.title('world population')
# plt.yticks([0,2,4,6,8,10])
# plt.show()

plt.fill_between(year,pop,0,color='green')
plt.xlabel('year')
plt.ylabel('population')
plt.title('world population')
plt.yticks([0,2,4,6,8,10],
	['0b','2b','4b','6b','8b','10b'])
plt.show()
