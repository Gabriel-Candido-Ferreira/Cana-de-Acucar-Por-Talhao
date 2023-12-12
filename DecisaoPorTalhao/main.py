class Node:
    def __init__(self, producao=None, atr=None):
        self.producao = producao
        self.atr = atr
        self.next = None
        self.left = None
        self.right = None
        self.decision = None

def quick_sort_linked_list(head):
    if head is None or head.next is None:
        return head

    pivot = head
    less_head = less_tail = Node(0, 0)
    equal_head = equal_tail = Node(0, 0)
    greater_head = greater_tail = Node(0, 0)

    while head is not None:
        if head.atr < pivot.atr:
            less_tail.next = head
            less_tail = less_tail.next
        elif head.atr == pivot.atr:
            equal_tail.next = head
            equal_tail = equal_tail.next
        else:
            greater_tail.next = head
            greater_tail = greater_tail.next
        head = head.next

    less_tail.next = None
    equal_tail.next = None
    greater_tail.next = None

    sorted_less = quick_sort_linked_list(less_head.next)
    sorted_greater = quick_sort_linked_list(greater_head.next)

    return concat_lists(sorted_less, equal_head.next, sorted_greater)

def concat_lists(less, equal, greater):
    result_head = result_tail = Node(0, 0)

    result_tail.next = less
    result_tail = get_tail(result_tail)

    result_tail.next = equal
    result_tail = get_tail(result_tail)

    result_tail.next = greater
    result_tail = get_tail(result_tail)

    return result_head.next

def get_tail(node):
    while node.next is not None:
        node = node.next
    return node


def build_decision_tree(head):
    if head is None:
        return None

    sorted_nodes = []

    current = head
    while current is not None:
        sorted_nodes.append(Node(current.producao, current.atr))
        current = current.next

    return build_tree_recursive(sorted_nodes)

def insert_node(root, node):
    atr_value = node.atr

    if atr_value > 40:
        if atr_value > 70:
            node.decision = "Açúcar"
        else:
            node.decision = "Etanol"
    else:
        if atr_value > 10:
            node.decision = "Cachaça"
        else:
            node.decision = "Doces"

def build_tree_recursive(sorted_nodes):
    if not sorted_nodes:
        return None

    mid_index = len(sorted_nodes) // 2
    root = sorted_nodes[mid_index]

    insert_node(root, root)

    root.left = build_tree_recursive(sorted_nodes[:mid_index])
    root.right = build_tree_recursive(sorted_nodes[mid_index + 1:])

    return root


def print_decision_tree(node, talhao_number="1"):
    if node is not None:
        insert_node(node, node)

        print(
            f"talhão {talhao_number}: Quantidade produzida: {node.producao}, ATR: {node.atr} boa para {node.decision}")
        print_decision_tree(node.left, talhao_number=talhao_number + "0")
        print_decision_tree(node.right, talhao_number=talhao_number + "1")


num_talhoes = int(input("Digite o número de talhões: "))
head = None

for i in range(num_talhoes):
    producao = float(input(f"Digite a quantidade produzida de cana para o talhão {i + 1}: "))
    atr = float(input(f"Digite o valor da ATR para o talhão {i + 1}: "))
    new_node = Node(producao, atr)
    new_node.next = head
    head = new_node

print("\nLista não ordenada:")
current = head
while current is not None:
    print(f"Quantidade produzida: {current.producao}, ATR: {current.atr}")
    current = current.next

head = quick_sort_linked_list(head)

print("\nLista ordenada:")
current = head
while current is not None:
    print(f"Quantidade produzida: {current.producao}, ATR: {current.atr}")
    current = current.next

decision_tree = build_decision_tree(head)

print("\nÁrvore de Decisão:")
print_decision_tree(decision_tree)
