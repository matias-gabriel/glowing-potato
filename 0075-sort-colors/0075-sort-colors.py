def swap(i, j, colors):
    aux = colors[i]
    colors[i] = colors[j]
    colors[j] = aux
    
def sort_colors(colors):
    # [0,0,0, 1,1,1 2,2,2]
    # [0,1,2,1,0,1]
    # [0,0,1,1     ,2]
    left_pointer = 0
    right_pointer = len(colors) - 1
    idx = 0
    
    while idx <= right_pointer:
        color = colors[idx]
        if color == 0:
            swap(left_pointer, idx, colors)
            left_pointer+=1
            idx += 1
        elif color == 2:
            swap(right_pointer, idx, colors)
            right_pointer-=1
        else:
            idx+=1
            
            
    return colors
class Solution(object):
    def sortColors(self, nums):
        sort_colors(nums)
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        