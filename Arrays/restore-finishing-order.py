class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        winning_order = []
        for friend in range(len(order)):
            if order[friend] in friends:
                winning_order.append(order[friend])
        return winning_order
