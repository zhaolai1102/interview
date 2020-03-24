'''

字符A-Z可以编码为0-25。"A"->"0", "B"->"1", ..., "Z"->"25"
现在输入一个数字序列，计算有多少种方式可以解码成字符A-Z组成的序列。

例如：

输入：19
输出：2

输入：258
输出：2

输入：0219
输出：3


'''

def how_many_ways(digitarray):
    # implement here
    n = 1
    def one_or_two(digit_array):
        nonlocal n
        if len(digit_array) == 1:
            return
        one_or_two(digit_array[1:])
        if digit_array[0] == '1' or digit_array[0] == '2' and digit_array[1] < '6':
            n += 1
            if len(digit_array) > 2:
                one_or_two(digit_array[2:])
    one_or_two(digitarray)
    return n

if __name__ == '__main__':
    print(how_many_ways('0219'))
