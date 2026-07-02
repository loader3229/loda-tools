def extract_sequence(file_content):
    # 初始化索引列表和数值列表
    indices = []
    values = []
    
    # 按行处理文件内容
    for line in file_content.split('\n'):
        # 去除行首尾空格
        line = line.strip()
        # 跳过空行和注释行
        if not line or line.startswith('#'):
            continue
        # 去除行中的注释部分，只保留前面的数字
        line_without_comment = line.split('#')[0].strip()
        # 分割索引和数值（处理多个空格的情况）
        parts = line_without_comment.split()
        if len(parts) >= 2:
            index = int(parts[0])
            value = int(parts[1])
            indices.append(index)
            values.append(value)
    
    # 返回第1个数的索引和数值列表
    first_index = indices[0] if indices else None
    return first_index, values


