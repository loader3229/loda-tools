class TrieNode:
    """Trie树的节点类"""
    def __init__(self):
        self.children = {}  # 键：当前位置的整数元素；值：下一个TrieNode节点
        self.oeis_id = None  # 仅序列最后一个元素的节点存储OEIS ID

class SequenceTrie:
    """用于存储15长度整数序列与OEIS ID映射的Trie树"""
    def __init__(self):
        self.root = TrieNode()  # Trie树的根节点（空节点，不对应任何序列元素）

    def insert(self, sequence: list[int], oeis_id: str) -> None:
        """
        插入序列到Trie树
        :param sequence: 长度为15的整数序列
        :param oeis_id: 序列对应的OEIS ID
        :raises ValueError: 若序列长度不为15则抛出异常
        """
        # 校验序列长度
        if len(sequence) != 15:
            raise ValueError(f"序列长度必须为15，当前为{len(sequence)}")
        
        current_node = self.root
        # 逐层插入序列元素
        for num in sequence:
            # 若当前元素不存在于子节点，创建新节点
            if num not in current_node.children:
                current_node.children[num] = TrieNode()
            # 移动到下一层节点
            current_node = current_node.children[num]
        
        # 序列最后一个元素的节点存储OEIS ID
        if current_node.oeis_id == None:
            current_node.oeis_id = oeis_id
        elif len(current_node.oeis_id)>=80:
            pass
        else:
            current_node.oeis_id += ("," + oeis_id)

    def search(self, sequence: list[int]) -> str | None:
        """
        查找序列对应的OEIS ID
        :param sequence: 待查找的长度为15的整数序列
        :return: 找到则返回OEIS ID，否则返回None
        """
        # 校验序列长度
        if len(sequence) != 15:
            print(f"错误：待查找序列长度为{len(sequence)}，必须为15")
            return None
        
        current_node = self.root
        # 逐层遍历序列元素
        for num in sequence:
            # 若当前元素不存在，直接返回None（序列不存在）
            if num not in current_node.children:
                return None
            # 移动到下一层节点
            current_node = current_node.children[num]
        
        # 返回终点节点的OEIS ID（可能为None，若该路径未插入完整序列）
        return current_node.oeis_id
