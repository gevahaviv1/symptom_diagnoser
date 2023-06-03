def __repr__(self):
    printble = [""]

    def repr_helper(cur_node: Node, depth: int):
        if cur_node is None:
            return

        if cur_node.positive_child:
            printble[0] += str(cur_node.data) + '?\n'
            printble[0] += '\t' * (depth + 1) + 'yes: '
            repr_helper(cur_node.positive_child, depth + 1)
            printble[0] += '\t' * (depth + 1) + 'no: '
            repr_helper(cur_node.negative_child, depth + 1)
        else:
            printble[0] += str(cur_node.data) + '!\n'

    repr_helper(self.root, 0)
    return printble[0]