# ===========================================================
# Practical No. 2
# BFS, DFS and Cheapest Path Search
# Treasure Hunt Robot
# ===========================================================

print("Hello! I am your treasure-hunt robot. 🤖")
print("Let's find the treasure together! 💎")

# Map of rooms
map_rooms = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": ["G"],
    "G": []
}

# Display map
print("Our map:")
print("            A  (Start)")
print("           / \\")
print("          B   C")
print("           \\ /")
print("            D")
print("            |")
print("            G  (Treasure 💎)")
print()
print("Doors from each room:", map_rooms)


# -----------------------------------------------------------
# Breadth-First Search (BFS)
# -----------------------------------------------------------
def bfs(start, goal):
    to_do = [start]
    visited = []
    order = []

    while to_do:
        room = to_do.pop(0)

        if room in visited:
            continue

        visited.append(room)
        order.append(room)

        if room == goal:
            return order

        for nxt in map_rooms[room]:
            to_do.append(nxt)

    return order


bfs_order = bfs("A", "G")

print()
print("BFS checked the rooms in this order:", bfs_order)
print("Number of rooms BFS checked:", len(bfs_order))


# -----------------------------------------------------------
# Depth-First Search (DFS)
# -----------------------------------------------------------
def dfs(start, goal):
    to_do = [start]
    visited = []
    order = []

    while to_do:
        room = to_do.pop()

        if room in visited:
            continue

        visited.append(room)
        order.append(room)

        if room == goal:
            return order

        for nxt in map_rooms[room]:
            to_do.append(nxt)

    return order


dfs_order = dfs("A", "G")

print()
print("DFS checked the rooms in this order:", dfs_order)
print("Number of rooms DFS checked:", len(dfs_order))


# -----------------------------------------------------------
# Door Costs
# -----------------------------------------------------------
door_cost = {
    ("A", "B"): 1,
    ("B", "D"): 1,
    ("A", "C"): 5,
    ("C", "D"): 1,
    ("D", "G"): 1,
}


# Calculate path cost
def path_cost(path):
    total = 0

    for i in range(len(path) - 1):
        door = (path[i], path[i + 1])
        total = total + door_cost[door]

    return total


# Possible paths
path1 = ["A", "B", "D", "G"]
path2 = ["A", "C", "D", "G"]

cost1 = path_cost(path1)
cost2 = path_cost(path2)

print()
print("Path 1 A -> B -> D -> G -> costs:", cost1)
print("Path 2 A -> C -> D -> G -> costs:", cost2)


# -----------------------------------------------------------
# Find Cheapest Path
# -----------------------------------------------------------
if cost1 < cost2:
    best_path = path1
    best_cost = cost1
else:
    best_path = path2
    best_cost = cost2

print()
print("Path 1 cost:", cost1)
print("Path 2 cost:", cost2)
print()
print("The cheapest path is:", best_path, "with cost", best_cost, "💰")


# -----------------------------------------------------------
# Final Results
# -----------------------------------------------------------
print()
print("RESULTS")
print("-" * 40)
print("BFS  (nearest first) checked:", len(bfs_order),
      "rooms ->", bfs_order)
print("DFS  (deep first) checked:", len(dfs_order),
      "rooms ->", dfs_order)
print("Cheapest path:", best_path, "with cost", best_cost)
print("-" * 40)

print()
print("What we learned:")
print(" * BFS checks the nearest rooms first (spreads out).")
print(" * DFS dives deep down one path first.")
print(" * Cheapest path counts door costs and picks the lowest total.")


# -----------------------------------------------------------
# Change Door Costs and Find Cheapest Path Again
# -----------------------------------------------------------
door_cost[("A", "B")] = 4
door_cost[("A", "C")] = 1

cost1 = path_cost(["A", "B", "D", "G"])
cost2 = path_cost(["A", "C", "D", "G"])

print()
print("After changing the door costs:")
print("Path 1 (through B) costs:", cost1)
print("Path 2 (through C) costs:", cost2)

if cost1 < cost2:
    print("Cheapest path is now Path 1: A -> B -> D -> G")
else:
    print("Cheapest path is now Path 2: A -> C -> D -> G")

print()
print("Practical No. 2 Completed Successfully! ✅")
