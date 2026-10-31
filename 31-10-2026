class Solution {
    public int check(int[] nums,int capacity,int days){
        int sum=nums[0],can_day=1;
        for(int i=1;i<nums.length;i++){
            sum+=nums[i];
            if(sum>capacity){
                can_day++;
                sum=nums[i];
            }
        }
        if(can_day<=days)return 1;
        return 0;
    }
    public int shipWithinDays(int[] nums, int days) {
        int st=nums[0],en=nums[0];
        for(int i=1;i<nums.length;i++){
            en+=nums[i];
            if(nums[i]>st)
            st=nums[i];
        }
        int ans=en;
        while(st<en){
            int capacity=(st+en)/2;
            int res=check(nums,capacity,days);
            if(res==1){
                en=capacity;
                if(capacity<ans)
                ans=capacity;
            }
            else{
                st=capacity+1;
            }
        }
        return ans;
    }
}
