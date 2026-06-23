import java.util.*;
class Solution {
    public void rotate(int[] nums, int k) {
        List<Integer> l = new ArrayList<>();
        for (int num:nums){
            l.add(num);
        }
        Collections.rotate(l,k);
        for(int i=0;i<nums.length;i++){
                nums[i]=l.get(i);
        }
    }
}