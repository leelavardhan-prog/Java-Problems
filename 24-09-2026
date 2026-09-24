/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxSum = Integer.MIN_VALUE;
    public int find(TreeNode cur){
        if(cur==null) return 0;
        int lSum = Math.max(find(cur.left), 0);
        int rSum = Math.max(find(cur.right), 0);
        int cSum = cur.val+lSum+rSum;
        maxSum = Math.max(maxSum,cSum);
        return cur.val+Math.max(rSum,lSum);
    }
    public int maxPathSum(TreeNode root) {
        find(root);
        return maxSum;
        
    }
}
