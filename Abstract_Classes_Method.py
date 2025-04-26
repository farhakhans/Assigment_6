import matplotlib.pyplot as plt

# Rectangle ka area calculation
width = 4
height = 5
area = width * height  # Rectangle ka area

# Plotting the graph
plt.bar(['Rectangle'], [area], color='blue')  # Bar graph for Rectangle area
plt.title('Area of Rectangle')  # Graph ka title
plt.xlabel('Shape')  # X-axis label
plt.ylabel('Area')  # Y-axis label
plt.show()  # Graph show karna
