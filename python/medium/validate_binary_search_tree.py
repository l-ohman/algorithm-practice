# https://leetcode.com/problems/validate-binary-search-tree/description/


# first attempt - beats 81% time and 18% memory
def isValidBST(root):
    def validate(node, min_val=float("-inf"), max_val=float("inf")):
        if node.val <= min_val or node.val >= max_val:
            return False
        valid_l = valid_r = True
        if node.left is not None:
            valid_l = validate(node.left, min_val, node.val)
        if node.right is not None:
            valid_r = validate(node.right, node.val, max_val)
        return valid_l and valid_r

    return validate(root)
