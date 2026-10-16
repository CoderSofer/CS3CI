import pandas as pd
import random
import math

city_csv_location = "week1/ulysses16.csv"

# --------------------------- Step 1: Data Structure
rows, cols = (4, 4)
adjacency_matrix = [[0]*cols for i in range(rows)]
adjacency_matrix[0][1] = 20 
adjacency_matrix[0][2] = 42
adjacency_matrix[0][3] = 35
adjacency_matrix[1][0] = 20
adjacency_matrix[1][2] = 30
adjacency_matrix[1][3] = 34
adjacency_matrix[2][0] = 42 
adjacency_matrix[2][1] = 30
adjacency_matrix[2][3] = 12
adjacency_matrix[3][0] = 35
adjacency_matrix[3][1] = 34
adjacency_matrix[3][2] = 12
# print(f"Adjacency Matrix compiled:")
# for row in adjacency_matrix:
    # print(row)

# --------------------------- Step 2: Defining and Evaluating Routes
# !!Requires instantiation and padding of adjacency_matrix from task 1 when testing
def evaluate_tsp(adjacency_matrix,route):
    route_list = list(route)
    num_route_list = [int(item) for item in route_list]

    cost = 0
    for counter in range(len(num_route_list)):
        if counter + 1 >= (len(num_route_list)):
               break
        column = num_route_list[counter]
        row = num_route_list[counter+1]
        cost += adjacency_matrix[column][row]
    return cost

route = "0130"
cost = evaluate_tsp(adjacency_matrix,route)
# print(f"Cost of route: {route} is: {cost}")

# ----------------------------------------- Step 3: Generating Random Routes
# !!Requires instantiation and padding of adjacency_matrix from task 1
# and stuff from task2

def random_route(n_cities):
     routeList = [str(x) for x in range(n_cities)]
     random.shuffle(routeList)
     routeList.append(routeList[0])
     route = ''.join(routeList)
     return route
n_cities = 3 # The TSP with 4 cities
route = random_route(n_cities)
# print(f"Random route of length {n_cities} is: {route} ")

cost = evaluate_tsp(adjacency_matrix,route)
# print(f"Cost of route: {route} is: {cost}")

# ----------------------------------------- Step 4: Try a Bigger Problem Instance
# !! Requires ulysses16.csv file to exist
def pad_matrix():
    df = pd.read_csv(city_csv_location)
    print(df)
    rows, cols = (16, 16)
    
    matrix = [[0]*cols for i in range(rows)]
    for x in range(rows):
         for y in range(rows):
            cityAx, cityAy = df.iloc[x,0], df.iloc[x,1]
            cityBx, cityBy = df.iloc[y,0], df.iloc[y,1]
            differenceX = cityBx-cityAx
            differenceY = cityBy-cityAy
            distance = math.sqrt(differenceX**2 + differenceY**2)
            matrix[x][y] = distance
    return matrix

matrix = pad_matrix()
# print(f"Matrix compiled:")
# for row in matrix:
#     print(row)


# ---- Extra: Generating random routes and evaluating these based on this bigger matrix
# !! Requires bigger matrix from task 4, evaluate_tsp from task 2 and random_route from task 3
n_cities = 16 # The TSP with 4 cities
route = random_route(n_cities)
print(f"Random route of length {n_cities} is: {route} ")

cost = evaluate_tsp(matrix,route)
print(f"Cost of route: {route} is: {cost}")