from ex11 import *

def diagnosers_builder(diagnosers: List[Diagnoser]):
    diagnosers_counter = [0]

    def diagnoser_builder(diagno: Diagnoser):
        names = set()
        names_counter = {}

        def diagnoser_builder_helper(node: Node):
            if node is None:
                return
            if node.positive_child is None or node.negative_child is None:
                node.name = f'{node.data}_leaf'
                if node.name not in names:
                    print(f'{node.name} = Node("{node.data}")')
                    names.add(node.name)
                return
            diagnoser_builder_helper(node.positive_child)
            diagnoser_builder_helper(node.negative_child)
            if node.data not in names_counter:
                names_counter[node.data] = 1
            node.name = f'{node.data}_vertex{names_counter[node.data]}'
            print(f'{node.name} = Node("{node.data}", {node.positive_child.name}, {node.negative_child.name})')
            names_counter[node.data] += 1

        diagnoser_builder_helper(diagno.root)

    for diagnoser in diagnosers:
        diagnoser_builder(diagnoser)
        print(f"diagnoser{diagnosers_counter[0]} = Diagnoser({diagnoser.root.name})")
        diagnosers_counter[0] += 1