import re
pattern = r'1[34578]\d{9}'                       # 定义要替换的模式字符串
string = '中奖号码为：84978981 联系电话为：13611111111'
result = re.sub(pattern,'1XXXXXXXXXX',string)  # 替换字符串
print(result)



string = 'hk400 jhkj6h7k5 jhkjhk1j0k66'     # 需要匹配的字符串
pattern = '[a-z]'                           # 表达式
match = re.sub(pattern,'',string,flags=re.I)  # 匹配字符串,将所有字母替换为空，并区分大小写
print(match)                                # 打印匹配结果



# 需要匹配的字符串
string = 'John,I like you to meet Mr. Wang，Mr. Wang, this is our Sales Manager John. John, this is Mr. Wang.'
pattern = 'Wang'      # 表达式
match = re.subn(pattern,'Li',string)  # 匹配字符串,将所有Wang替换为Li，并统计替换次数
print(match)                                # 打印匹配结果
print(match[1])                             # 打印匹配次数
