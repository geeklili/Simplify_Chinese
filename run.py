from function.opencc import OpenCC


def convert_t2s(input_list):
    """繁体字转换为简体字"""
    list_new = []
    for item in input_list:
        item_new = open_cc.convert(item)
        list_new.append(item_new)
    return list_new


def write_file(complex_dir, simple_dir):
    """写入文件"""
    with open(complex_dir, 'r', encoding='utf-8')as f1:
        with open(simple_dir, 'w', encoding='utf-8')as f2:
            content = f1.readlines()
            for i in content:
                con = ''.join(convert_t2s(i))
                f2.write(con)


if __name__ == '__main__':
    """汉字繁体转简体"""

    complex_path = './data/complex_chinese.txt'
    simple_path = './data/simple_chinese.txt'

    # 设定专成的简体的类型
    open_cc = OpenCC('t2s')

    # 转化并写入文件
    write_file(complex_path, simple_path)
