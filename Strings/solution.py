def solution(s):
    
    return " ".join([word[-1]+word[:-1] for word in s.split(" ")])
    
 
    
    
    
    

print(solution("abc 123 def ghi"))
