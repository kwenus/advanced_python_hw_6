
ls_1 = [1,1,1,2,3]
ls_2 = [1,2,3,2,2]
ls_3 = ['b','f','g',1, 1, 3, 'b', 'b', 3, 'b']
ls_4 = ['-2', 2, -4, 3, 'l', 'l', '-2', -4, -4]


def vote(ls):
    dict_nums = {}
    unique_ls = list(set (ls))
    for el in unique_ls:
      dict_nums.setdefault(el, ls.count(el))
    return sorted(dict_nums.items(), key=lambda num: num[1], reverse=True)[0][0]

if __name__ == '__main__':
    print(vote(ls_1))
    print(vote(ls_2))
    print(vote(ls_3))
    print(vote(ls_4))