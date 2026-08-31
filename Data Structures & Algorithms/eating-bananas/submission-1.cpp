#include <cmath>
#include <algorithm>
#include <iostream>

class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int high=0;
        int total=0;
        for (auto pile : piles) {
            total+=pile;
            high=max(high, pile);
        }
        return answer(piles,h,1,high);
    }
    bool isValid(vector<int> piles, int h, int k) {
        int time=0;
        for (auto pile : piles) {
            time += ceil(pile/k);
            if (pile%k!=0) {
                ++time;
            }
        }
        if (time > h) {
            return false;
        }
        return true;
    }

    int answer(vector<int> piles, int h, int low, int high) {
        int ans=0;
        while (high>=low) {
            int mid=(high+low)/2;
            if (isValid(piles,h,mid)) {
                ans=mid;
                high=mid-1;
            } else {
                low=mid+1;
            }
        }
        return ans;
    }
};
