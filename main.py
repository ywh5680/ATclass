import os

with open("目录.md", "r", encoding="utf-8") as f:
    data = f.readlines()

num = ''
for line in data:
    line = line.strip()  # 去除首尾空白字符
    if not line:  # 跳过空行
        continue

    try:
        # 情况1: 行首是数字且第3字符不是数字（如 "1. 目录名"）
        if line[0].isdigit() and not line[2].isdigit():
            path = line
            num = line[0]

        # 情况2: 行首匹配当前num且第3字符是数字（如 "1.1 子目录"）
        elif line[0] == num and line[2].isdigit():
            # 规范路径拼接
            full_path = os.path.join(path, line)
            print(full_path, "已创建",path,'666')
            # 创建父目录（如果不存在）
            os.makedirs(os.path.dirname(full_path), exist_ok=True)

            # 写入文件内容
            with open(f"{full_path}.md", "w", encoding="utf-8") as f:
                f.write("AT 课件")
    except IndexError:
        print(f"跳过格式错误的行: {line}")