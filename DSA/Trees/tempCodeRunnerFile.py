    left_height = height(root.left)
        right_height = height(root.right)

        if left_height > right_height:
            return left_height+1  ## 1 for root node
        else:
            return right_height  ## 1 for root Node   