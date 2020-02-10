class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dicti = {}
        for i in range(len(mat)):
            count = 0
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    count += 1
                else:
                    break
            # dict[i] = count
            dicti.update({i:count}) 
        fi = []
        key_list = list(dicti.keys()) 
        val_list = list(dicti.values()) 
  
        for i in range(0,k):
            tt = val_list.index(min(val_list))
            pos = key_list[tt]
            fi.append(pos)
            del key_list[tt]
            del val_list[tt]
            
        return fi