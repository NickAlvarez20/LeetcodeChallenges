class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        col = 0
        row = 0

        for move in commands:
            if move == "UP":
                col += 1
            if move == "DOWN":
                col -= 1
            if move == "LEFT":
                row -= 1
            if move == "RIGHT":
                row += 1
        return (abs(col) * n) + row

# Thanks CC 