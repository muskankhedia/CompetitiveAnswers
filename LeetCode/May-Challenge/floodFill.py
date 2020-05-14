class Solution:
    def floodFill(self, screen: List[List[int]], x: int, y: int, newC: int) -> List[List[int]]:
        def floodFillUtil(screen, x, y, prevC, newC): 
            # Base cases 
            if (x < 0 or x >= len(screen) or y < 0 or 
                y >= len(screen[0]) or screen[x][y] != prevC or 
                screen[x][y] == newC): 
                return

            # Replace the color at (x, y) 
            screen[x][y] = newC 

            # Recur for north, east, south and west 
            floodFillUtil(screen, x + 1, y, prevC, newC) 
            floodFillUtil(screen, x - 1, y, prevC, newC) 
            floodFillUtil(screen, x, y + 1, prevC, newC) 
            floodFillUtil(screen, x, y - 1, prevC, newC) 
        
        prevC = screen[x][y] 
        floodFillUtil(screen, x, y, prevC, newC) 
        return screen
        