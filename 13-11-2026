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
    public boolean isValidBST(TreeNode root) {
        return verify (root,Long.MIN_VALUE,Long.MAX_VALUE);
    }
    public boolean verify(TreeNode cur, long min,long max){
        if(cur==null) return true;
        if(cur.val<=min||cur.val>=max) return false;
        return verify(cur.left,min,cur.val)&&verify(cur.right,cur.val,max);
    }
}
