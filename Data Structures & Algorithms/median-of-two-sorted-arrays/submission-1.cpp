#include <iostream>

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int len=nums1.size()+nums2.size();
        int mid=(len+1)/2;
        double ans=kthSmallest(nums1,0,nums1.size()-1,nums2,0,nums2.size()-1, mid);
        if (len%2==0) {
            return (ans + kthSmallest(nums1,0,nums1.size()-1,nums2,0,nums2.size()-1, mid+1))/2;
        } return ans;
    } double kthSmallest(vector<int>& nums1, int left1, int right1, vector<int>& nums2, int left2, int right2, int k) {
        if (right1-left1<0) {
            return nums2[left2+k-1];
        } if (right2-left2<0) {
            return nums1[left1+k-1];
        } if (k==1) {
            return min(nums1[left1],nums2[left2]);
        } if (k==(right1-left1+right2-left2+2)) {
            return max(nums1[right1],nums2[right2]);
        }
        int median;
        if (right1-left1 >= right2-left2) {
            int mid1=left1+(right1-left1)/2;
            median=nums1[mid1];
            int mid2=bst(nums2,median,left2,right2);
            if (mid1-left1+mid2-left2+2>=k) {
                return kthSmallest(nums1,left1,mid1,nums2,left2,mid2,k);
            } return kthSmallest(nums1,mid1+1,right1,nums2,mid2+1,right2,k-(mid1-left1+mid2-left2+2));
        } 
        int mid2=left2+(right2-left2)/2;
        median=nums2[mid2];
        int mid1=bst(nums1,median,left1,right1);
        if (mid1-left1+mid2-left2+2>=k) {
            return kthSmallest(nums1,left1,mid1,nums2,left2,mid2,k);
        } return kthSmallest(nums1,mid1+1,right1,nums2,mid2+1,right2,k-(mid1-left1+mid2-left2+2));
    } int bst(vector<int>& nums, double target, int left, int right) {
        int mid;
        while (left<=right) {
            mid = left + (right-left) / 2;
            if (nums[mid]==target) {
                return mid;
            } if (nums[mid]<target) {
                left=mid+1;
            } else {
                right=mid-1;
            }
        } if (target>=nums[mid]) {
            return mid;
        } return mid-1;
    }
};