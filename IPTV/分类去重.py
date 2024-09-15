import re
import os
import replace
import fileinput
############################################################################排序############################################################################################################
with open('TW.txt', 'r', encoding='UTF-8') as f:
    lines = f.readlines()
lines.sort()
with open('TW.txt', 'w', encoding='UTF-8') as f:
    for line in lines:
        f.write(line)


################################################################定义关键词分割规则
def check_and_write_file(input_file, output_file, keywords):
    # 使用 split(', ') 而不是 split(',') 来分割关键词
    keywords_list = keywords.split(', ')
    first_keyword = keywords_list[0]  # 获取第一个关键词作为头部信息

    pattern = '|'.join(re.escape(keyword) for keyword in keywords_list)
    extracted_lines = False

    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(output_file, 'w', encoding='utf-8') as out_file:
        out_file.write(f'{first_keyword},#genre#\n')  # 使用第一个关键词作为头部信息

        for line in lines:
            if 'genre' not in line and 'epg' not in line:
                if re.search(pattern, line):
                    out_file.write(line)
                    extracted_lines = True

    # 如果没有提取到任何关键词，则不保留输出文件
    if not extracted_lines:
        os.remove(output_file)  # 删除空的输出文件
        print(f"未提取到关键词，{output_file} 已被删除。")
    else:
        print(f"文件已提取关键词并保存为: {output_file}")

# 按类别提取关键词并写入文件
check_and_write_file('TW.txt',  'a0.txt',  keywords="港澳频道, AMC, 功夫台, 戏剧, 中视经典, 影剧, 影视, 影迷, 电影, 龙华电影台, ASTRO, 音乐台, 开码, 影迷, 经典")
check_and_write_file('TW.txt',  'a.txt',  keywords="港澳频道, ,")




###############################################################################################################################################################################################################################
##############################################################对生成的文件进行合并
file_contents = []
file_paths = ["a0.txt", "a.txt"]  # 替换为实际的文件路径列表
for file_path in file_paths:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding="utf-8") as file:
            content = file.read()
            file_contents.append(content)
    else:                # 如果文件不存在，则提示异常并打印提示信息
        print(f"文件 {file_path} 不存在，跳过")
# 写入合并后的文件
with open("TW.txt", "w", encoding="utf-8") as output:
    output.write(''.join(file_contents))#\n

###############################################################################################################################################################################################################################


# 打开文档并读取所有行 
with open('TW.txt', 'r', encoding="utf-8") as file:
 lines = file.readlines()
# 使用列表来存储唯一的行的顺序 
 unique_lines = [] 
 seen_lines = set() 
# 遍历每一行，如果是新的就加入unique_lines 
for line in lines:
 if line not in seen_lines:
  unique_lines.append(line)
  seen_lines.add(line)
# 将唯一的行写入新的文档 
with open('TW.txt', 'w', encoding="utf-8") as file:
 file.writelines(unique_lines)
####################################################
#####################################定义替换规则的字典,对整行内的多余标识内容进行替换
replacements = {
        ",ht": ",ht"
}
# 打开原始文件读取内容，并写入新文件
with open('TW.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
# 创建新文件并写入替换后的内容
with open('TW.txt', 'w', encoding='utf-8') as new_file:
    for line in lines:
        for old, new in replacements.items():
            line = line.replace(old, new)
        new_file.write(line)
print("替换完成，新文件已保存。")


################################################################################################任务结束，删除不必要的过程文件
files_to_remove = ["a0.txt", "a.txt"]

for file in files_to_remove:
    if os.path.exists(file):
        os.remove(file)
    else:              # 如果文件不存在，则提示异常并打印提示信息
        print(f"文件 {file} 不存在，跳过删除。")

print("任务运行完毕，分类频道列表可查看文件夹内综合源.txt文件！")


