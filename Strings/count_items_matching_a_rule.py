class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        map_keys = {0: "type", 1: "color", 2: "name"}
        count = 0
        for boxes in items:
            for i in range(len(boxes)):
                # butter knot twister ~o.O~
                if map_keys[i] == ruleKey and ruleValue == boxes[i]:
                    count += 1
        return count
