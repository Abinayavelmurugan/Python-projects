kuzhi = {1: 6, 2: 6, 3: 6, 4: 6, 5: 6, 6: 6, 7: 6, 8: 6, 9: 6, 10: 6, 11: 6, 12: 6, 13: 6, 14: 6}
p1_points = 0
p2_points = 0
flag = 0  # 0 means it's player 1's turn, 1 means it's player 2's turn

while True:
    if flag == 0:
        # Player 1's turn
        for i in range(1, 15):
            if kuzhi[i] > 0:
                x = kuzhi[i]
                kuzhi[i] = 0  # Remove all stones from the current hole
                for j in range(1, x + 1):
                    z = (i + j) % 14  # Wrapping around the board
                    if z == 0:
                        z = 14
                    kuzhi[z] += 1  # Drop a stone in each subsequent hole
                break  # Player 1 distributes stones from one hole only
        
        # Check for capturing stones
        for i in range(1, 15):
            if kuzhi[i] == 3:
                p1_points += kuzhi[i]
                kuzhi[i] = 0
        
        flag = 1  # Switch to player 2's turn

    else:
        # Player 2's turn
        for i in range(1, 15):
            if kuzhi[i] > 0:
                x = kuzhi[i]
                kuzhi[i] = 0  # Remove all stones from the current hole
                for j in range(1, x + 1):
                    z = (i + j) % 14  # Wrapping around the board
                    if z == 0:
                        z = 14
                    kuzhi[z] += 1  # Drop a stone in each subsequent hole
                break  # Player 2 distributes stones from one hole only
        
        # Check for capturing stones
        for i in range(1, 15):
            if kuzhi[i] == 3:
                p2_points += kuzhi[i]
                kuzhi[i] = 0
        
        flag = 0  # Switch to player 1's turn

    # Check if the game should end (all holes are empty)
    f = all(kuzhi[i] == 0 for i in range(1, 15))
    if f:
        break

print("Player 1 points:", p1_points)
print("Player 2 points:", p2_points)
