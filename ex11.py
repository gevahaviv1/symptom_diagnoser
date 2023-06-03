
import itertools


class Node:
    def __init__(self, data, positive_child=None, negative_child=None):
        self.data = data
        self.positive_child = positive_child
        self.negative_child = negative_child


class Record:
    def __init__(self, illness, symptoms):
        self.illness = illness
        self.symptoms = symptoms


def parse_data(filepath):
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.strip().split()
            records.append(Record(words[0], words[1:]))
        return records


class Diagnoser:
    def __init__(self, root: Node):
        self.root = root

    def _diagnose_helper(self, symptoms, root):
        """
        This function is helper for diagnose function,
        we use helper because we want to save the structure of the tree.
        :param symptoms: List of symptoms, type List.
        :param root: The root of the tree, type Node.
        :return: The name of the illness, type string.
        """
        if root.positive_child is None and root.negative_child is None:
            return root.data
        if root.data in symptoms:
            return self._diagnose_helper(symptoms, root.positive_child)
        else:
            return self._diagnose_helper(symptoms, root.negative_child)

    def diagnose(self, symptoms):
        """
        This function diagnose which illness you have according to the symptoms.
        :param symptoms: List of symptoms, type List.
        :return: The name of the illness, type string.
        """
        return self._diagnose_helper(symptoms, self.root)

    def calculate_success_rate(self, records):
        """
        This function calculate the success rate of the records.
        In order to calculate the success rate,
        we go over the records iterative and check if the illness from the record is in our tree.
        :param records: List of records, type List[Record].
        :return: The success rate, type float.
        """
        if len(records) == 0:
            raise ValueError('Records is empty.')

        success = [1 for record in records if record.illness == self.diagnose(record.symptoms)]
        return sum(success) / len(records)

    def _all_illnesses_helper(self, root):
        """
        This function is helper for the all_illnesses function.
        The function go over the tree and add to a list all the leaf.
        :param root: The root of the tree, type Node.
        :return: List of disease, type List.
        """
        disease_list = []
        if root.positive_child is None and root.negative_child is None:
            if root.data is not None:
                disease_list.append(root.data)
            return disease_list

        if root.positive_child is not None:
            disease_list.extend(self._all_illnesses_helper(root.positive_child))
        if root.negative_child is not None:
            disease_list.extend(self._all_illnesses_helper(root.negative_child))

        return disease_list

    def all_illnesses(self):
        """
        This function using helper and get a list of disease from it.
        The function take the list, convert it to dictionary,
        sort it by the value and return the result as list.
        :return: Sorted list of disease, type List.
        """
        all_illnesses_lst = self._all_illnesses_helper(self.root)
        all_illnesses_dict = {key: all_illnesses_lst.count(key) for key in all_illnesses_lst}
        return sorted(all_illnesses_dict, key=all_illnesses_dict.get, reverse=True)

    def _path_to_illness_helper(self, root, illness, paths, single_path):
        """
        This function is helper for the path_to_illness function.
        The function go over all the paths and check if the path is leading to the illness.
        If there is a match we do append of the path to paths and return paths.
        If the illness is None, we return all the paths of the leaf's.
        If there is no path found we return empty list.
        :param root: The root of the tree, type Node.
        :param illness: The illness we search, type string.
        :param paths: List of the paths we got (we can have more then one), type List.
        :param single_path: List of single path, type List.
        :return: List of lists, type List.
        """
        if root.positive_child is None and root.negative_child is None and illness == root.data:
            paths.append(single_path.copy())
            return paths

        if root.positive_child is not None:
            single_path.append(True)
            self._path_to_illness_helper(root.positive_child, illness, paths, single_path)
            single_path.pop()

        if root.negative_child is not None:
            single_path.append(False)
            self._path_to_illness_helper(root.negative_child, illness, paths, single_path)
            single_path.pop()

        return paths

    def paths_to_illness(self, illness):
        """
        This function call to helper and return list of paths of the illness.
        :param illness: The illness we search, type string.
        :return: List of lists, type List.
        """
        return self._path_to_illness_helper(self.root, illness, [], [])

    def _check_leaf(self, pos, neg):
        """
        This function check the leaf's.
        :param pos: The positive leaf, type Node.
        :param neg: The negative leaf, type Node.
        :return: Bool.
        """
        if pos is None and neg is None:
            return True

        if pos.data == neg.data:
            return True and self._check_leaf(pos.positive_child, neg.positive_child) and \
                   self._check_leaf(pos.negative_child, neg.negative_child)
        return False

    def _minimize_helper(self, root, remove_empty):
        """
        This function is the helper for the minimize function.
        The function using recursion.
        :param root: The root of the tree, type Node.
        :param remove_empty: Bool.
        :return: Tree with root, type Node.
        """
        if root.positive_child is None and root.negative_child is None:
            return root

        pos = self._minimize_helper(root.positive_child, remove_empty)
        neg = self._minimize_helper(root.negative_child, remove_empty)
        if self._check_leaf(pos, neg) or remove_empty and (pos.data is None or neg.data is None):
            if pos.data:
                root.data = pos.data
                root.positive_child, root.negative_child = pos.positive_child, pos.negative_child
            else:
                root.data = neg.data
                root.positive_child, root.negative_child = neg.positive_child, neg.negative_child
        return root

    def minimize(self, remove_empty=False):
        """
        This function minimize the tree according to the remove_empty parameter.
        :param remove_empty: Bool.
        :return: None.
        """
        self._minimize_helper(self.root, remove_empty)


def get_max(records_copy):
    """
    This function return the max record from the records.
    :param records_copy: List of records, List.
    :return: String.
    """
    dictionary = dict()
    illness_set = set([record.illness for record in records_copy])
    records_copy = [record.illness for record in records_copy]

    for cell in illness_set:
        dictionary[cell] = records_copy.count(cell)

    if len(dictionary) == 0:
        return None
    return max(dictionary, key=dictionary.get)


def build_tree_helper(root, symptoms, records_copy):
    """
    This function is helper for build tree.
    The function create the tree with symptoms and leaf's from the root.
    :param root: The root of the tree, type Node.
    :param symptoms: The symptoms of the illness's, type List.
    :param records_copy: List of records, type List.
    :return: None.
    """
    if len(symptoms) == 0:
        # Positive child.
        records_copy_pos = list(filter(lambda record: root.data in record.symptoms, records_copy))
        root.positive_child = Node(get_max(records_copy_pos), None, None)

        # Negative child.
        records_copy_neg = list(filter(lambda record: root.data not in record.symptoms, records_copy))
        root.negative_child = Node(get_max(records_copy_neg), None, None)
        return

    root.positive_child = Node(symptoms[0], None, None)
    root.negative_child = Node(symptoms[0], None, None)

    build_tree_helper(root.positive_child, symptoms[1:], list(filter(lambda record: root.data in record.symptoms,
                                                                     records_copy)))
    build_tree_helper(root.negative_child, symptoms[1:], list(filter(lambda record: root.data not in record.symptoms,
                                                                     records_copy)))


def build_tree(records, symptoms):
    """
    This function build a tree with symptoms and illness's according to the records.
    The function use helper to do it recursively.
    :param records: The records of of each illness, type List.
    :param symptoms: The symptoms of the tree, type list.
    :return: Tree, type Diagnoser.
    """
    if False in [type(record) == Record for record in records]:
        raise TypeError('You have non Record object in records list.')
    if False in [type(symptom) == str for symptom in symptoms]:
        raise TypeError('You have non string object in symptoms list.')
    if not symptoms:
        root = Node(get_max(records), None, None)
        return Diagnoser(root)

    root = Node(symptoms[0], None, None)
    build_tree_helper(root, symptoms[1:], records.copy())
    return Diagnoser(root)


def optimal_tree(records, symptoms, depth):
    """
    This function choose the optimal tree from all the tree's.
    :param records: The records of of each illness, type List.
    :param symptoms: The symptoms of the tree, type list.
    :param depth: Int.
    :return: Tree, type Diagnoser.
    """
    if not len(symptoms) >= depth >= 0:
        raise ValueError('Your depth should be: len(symptoms) >= depth >= 0')
    dictionary = {}

    for symptoms_lst in itertools.combinations(symptoms, depth):
        tree = build_tree(records, symptoms_lst)
        dictionary[tree] = tree.calculate_success_rate(records)

    return max(dictionary, key=dictionary.get)
