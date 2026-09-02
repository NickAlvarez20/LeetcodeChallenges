class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        for elem in image:
            elem.reverse()
            for i in range(len(elem)):
                elem[i] = elem[i] ^ 1

        return image
