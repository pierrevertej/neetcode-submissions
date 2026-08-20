class Solution:
    def trap(self, height: List[int]) -> int:
        volume=0
        hl=[height[0]]
        hr=[height[-1]]
        for i in range(1,len(height)):
            hr.append(max(hr[i-1],height[len(height)-i-1]))
        for i in range(1,len(height)):
            hl.append(max(hl[i-1],height[i]))
            volume+=min(hl[i],hr[len(height)-i-1])-height[i]
        return volume