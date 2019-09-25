# -*- coding:utf-8 -*-# \d{11}&#x8868;&#x793A;&#x5341;&#x4E00;&#x4F4D;&#x6570;&#x5B57;  {n}&#x8868;&#x793A;&#x524D;&#x9762;&#x7684;&#x5B57;&#x7B26;&#x8FD8;&#x9700;&#x8981;n&#x4E2A;&#xFF1B;\d&#x8868;&#x793A;&#x6570;&#x5B57;
import re
import json

customer = {
    '&#x59D3;&#x540D;': '',
    '&#x624B;&#x673A;': '',
    '&#x5730;&#x5740;': [],
}

s = input('')

op1 = s.split(r'!')
tag = op1[0]  # &#x63D0;&#x53D6;&#x96BE;&#x5EA6;&#x6807;&#x8BC6;


tel = re.findall(r'\d{11}', s)  # &#x627E;&#x51FA;&#x53F7;&#x7801;
tel = tel[0]  # &#x5C06;&#x53F7;&#x7801;&#x8F6C;&#x5316;&#x4E3A;&#x5B57;&#x7B26;&#x4E32;
s = re.sub(r'\d{11}', '', s)  # &#x5220;&#x53BB;&#x53F7;&#x7801;

num = re.sub(r',.*$', "", s)  # &#x63D0;&#x53D6;&#x4EBA;&#x540D;

s = re.sub(num, '', s)  # &#x5220;&#x53BB;&#x4EBA;&#x540D;
s = re.sub(r',', '', s)  # &#x5220;&#x53BB;&#x9017;&#x53F7;

customer['&#x59D3;&#x540D;'] = num
customer['&#x624B;&#x673A;'] = tel

# &#x4E00;&#x7EA7;&#x5730;&#x5740;
zhixiashi = ['&#x5317;&#x4EAC;', '&#x4E0A;&#x6D77;', '&#x5929;&#x6D25;', '&#x91CD;&#x5E86;']
if "&#x81EA;&#x6CBB;&#x533A;" in s:
    one = re.sub(r'&#x81EA;&#x6CBB;&#x533A;.*$', "", s)  # &#x63D0;&#x53D6;&#x81EA;&#x6CBB;&#x533A;
    one += '&#x81EA;&#x6CBB;&#x533A;'
    s = s.replace(one, '', 1)  # &#x5220;&#x53BB;&#x81EA;&#x6CBB;&#x533A;
elif '&#x7701;' not in s:
    for direc in zhixiashi:
        if direc in s:
            one = direc
            break
        else:
            one = ""  # &#x8BE5;&#x7EA7;&#x5730;&#x5740;&#x4E3A;&#x7A7A;
else:
    one = re.sub(r'&#x7701;.*$', "", s)
    one += '&#x7701;'
    s = s.replace(one, '', 1)  # &#x5220;&#x53BB;&#x4E00;&#x7EA7;&#x5730;&#x5740;
customer['&#x5730;&#x5740;'].append(one)

# &#x4E8C;&#x7EA7;
erji = ['&#x5E02;', '&#x5730;&#x533A;', '&#x76DF;', '&#x81EA;&#x6CBB;&#x5DDE;']
for tw in erji:
    if tw in s:

        two = re.sub(tw + '.*$', "", s)
        two += tw
        s = s.replace(two, '', 1)  # &#x5220;&#x53BB;&#x4E8C;&#x7EA7;&#x5730;&#x5740;
        break
    else:
        two = ""

customer['&#x5730;&#x5740;'].append(two)

# &#x4E09;&#x7EA7;&#x5730;&#x5740;
xianji = ['&#x533A;', '&#x53BF;', '&#x5E02;', '&#x81EA;&#x6CBB;&#x53BF;', '&#x65D7;', '&#x81EA;&#x6CBB;&#x65D7;', '&#x6797;&#x533A;']
for tr in xianji:
    if tr in s:
        three = re.sub(tr + '.*$', "", s)
        three += tr
        s = s.replace(three, '', 1)  # &#x5220;&#x53BB;&#x4E09;&#x7EA7;&#x5730;&#x5740;
        break
    else:
        three = ""

customer['&#x5730;&#x5740;'].append(three)

# &#x56DB;&#x7EA7;&#x5730;&#x5740;
zhenji = ['&#x8857;&#x9053;', '&#x9547;', '&#x4E61;', '&#x6C11;&#x65CF;&#x4E61;', '&#x82CF;&#x6728;', '&#x6C11;&#x65CF;&#x82CF;&#x6728;']
for fr in zhenji:
    if fr in s:
        four = re.sub(fr + '.*$', "", s)
        four += fr
        s = s.replace(four, '', 1)  # &#x5220;&#x53BB;&#x56DB;&#x7EA7;&#x5730;&#x5740;
        break
    else:
        four = ""
customer['&#x5730;&#x5740;'].append(four)

s = s.replace('.', '', 1)  # &#x5220;&#x53BB;&#x53E5;&#x53F7;
# &#x4E94;&#x7EA7;&#x5730;&#x5740;
cunji = ['&#x8857;', '&#x8DEF;', '&#x6751;']
if tag == '1':
    five = s
    customer['&#x5730;&#x5740;'].append(five)
elif tag == '2' or '3':  # &#x7EE7;&#x7EED;&#x5212;&#x5206;&#x4E94;&#x7EA7;&#x4EE5;&#x540E;&#x7684;&#x5730;&#x5740;
    for fv in cunji:
        if fv in s:
            five = re.sub(fv + '.*$', "", s)
            five += fv
            customer['&#x5730;&#x5740;'].append(five)
            s = s.replace(five, '', 1)  # &#x5220;&#x53BB;&#x4E94;&#x7EA7;&#x5730;&#x5740;
            break
        else:
            five = ""
    # &#x516D;&#x7EA7;&#x5730;&#x5740;
    if '&#x53F7;' not in s:
        six = ""
    else:
        six = re.sub(r'&#x53F7;.*$', "", s)
        six += '&#x53F7;'
        s = s.replace(six, '', 1)  # &#x5220;&#x53BB;&#x516D;&#x7EA7;&#x5730;&#x5740;

    customer['&#x5730;&#x5740;'].append(six)

    # &#x4E03;&#x7EA7;&#x5730;&#x5740;
    seven = s
    customer['&#x5730;&#x5740;'].append(seven)

json_str = json.dumps(customer, ensure_ascii=False)
print(json_str)


tel = re.findall(r'\d{11}', s)  # 找出号码
tel = tel[0]  # 将号码转化为字符串
s = re.sub(r'\d{11}', '', s)  # 删去号码

num = re.sub(r',.*$', "", s)  # 提取人名

s = re.sub(num, '', s)  # 删去人名
s = re.sub(r',', '', s)  # 删去逗号

customer['姓名'] = num
customer['手机'] = tel

# 一级地址
zhixiashi = ['北京', '上海', '天津', '重庆']
if "自治区" in s:
    one = re.sub(r'自治区.*$', "", s)  # 提取自治区
    one += '自治区'
    s = s.replace(one, '', 1)  # 删去自治区
elif '省' not in s:
    for direc in zhixiashi:
        if direc in s:
            one = direc
            break
        else:
            one = ""  # 该级地址为空
else:
    one = re.sub(r'省.*$', "", s)
    one += '省'
    s = s.replace(one, '', 1)  # 删去一级地址
customer['地址'].append(one)

# 二级
erji = ['市', '地区', '盟', '自治州']
for tw in erji:
    if tw in s:

        two = re.sub(tw + '.*$', "", s)
        two += tw
        s = s.replace(two, '', 1)  # 删去二级地址
        break
    else:
        two = ""

customer['地址'].append(two)

# 三级地址
xianji = ['区', '县', '市', '自治县', '旗', '自治旗', '林区']
for tr in xianji:
    if tr in s:
        three = re.sub(tr + '.*$', "", s)
        three += tr
        s = s.replace(three, '', 1)  # 删去三级地址
        break
    else:
        three = ""

customer['地址'].append(three)

# 四级地址
zhenji = ['街道', '镇', '乡', '民族乡', '苏木', '民族苏木']
for fr in zhenji:
    if fr in s:
        four = re.sub(fr + '.*$', "", s)
        four += fr
        s = s.replace(four, '', 1)  # 删去四级地址
        break
    else:
        four = ""
customer['地址'].append(four)

s = s.replace('.', '', 1)  # 删去句号
# 五级地址
cunji = ['街', '路', '村']
if tag == '1':
    five = s
    customer['地址'].append(five)
elif tag == '2' or '3':  # 继续划分五级以后的地址
    for fv in cunji:
        if fv in s:
            five = re.sub(fv + '.*$', "", s)
            five += fv
            customer['地址'].append(five)
            s = s.replace(five, '', 1)  # 删去五级地址
            break
        else:
            five = ""
    # 六级地址
    if '号' not in s:
        six = ""
    else:
        six = re.sub(r'号.*$', "", s)
        six += '号'
        s = s.replace(six, '', 1)  # 删去六级地址

    customer['地址'].append(six)

    # 七级地址
    seven = s
    customer['地址'].append(seven)

json_str = json.dumps(customer, ensure_ascii=False)
print(json_str)
