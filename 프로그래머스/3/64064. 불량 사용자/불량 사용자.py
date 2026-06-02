def solution(user_id, banned_id):
    answer = 0
    
    def is_match(user , banned):
        if len(user) != len(banned):
            return False
        
        for i in range(len(user)):
            if banned[i] == '*':
                continue
            if user[i] != banned[i]:
                return False
        return True
    
    candidates = []
    
    for ban in banned_id:
        temp = []
        
        for user in user_id:
            if is_match(user,ban):
                temp.append(user)
        candidates.append(temp)        
            
    result = set()
    selected = []

    def dfs(depth):
        if depth == len(candidates):
            result.add(frozenset(selected))
            return

        for user in candidates[depth]:
            if user not in selected:
                selected.append(user)
                dfs(depth + 1)
                selected.pop()
    dfs(0)
    
    return len(result)