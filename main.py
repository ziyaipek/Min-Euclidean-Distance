import math

# Function to calculate Euclidean distance
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Defining points
points = [(1, 2), (4, 6), (5, 8), (2, 1), (7, 3)]

# Calculation of distances
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Finding the minimum distance
minimum_distance = min(distances)
print(f'Minimum Öklid Mesafesi: {minimum_distance}')
