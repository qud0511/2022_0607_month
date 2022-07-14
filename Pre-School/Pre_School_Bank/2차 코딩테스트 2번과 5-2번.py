# 타블로
# 파워bi
# (주)해달

def input_f(string_input):
   d = [el.strip() for el in string_input.split(':')]
   data.append(d)

def print_f():
   n_members = len(data)
   names = [d[0] for d in data]
   print('등록 회원 수   : {}'.format(n_members))
   print('회원 등록 정보 : {}'.format(' '.join(sorted(names))))
   print('-----------------------')

if __name__ == '__main__':
   data = []
   while True:
      input_f(input())
      print_f()


# ------------------------------------------------------------------------------

def search(data, name_to_idx, code_to_idx, status_to_idx, query):
    # [searched_indices]
    # None : not searched any, yet.
    # Not None : searching is on processing or done.
    searched_indices = [None]

    # [query type]
    # used to return the property which the user want to search.
    query_types = []

    for q_word in query.split(' '):
        if q_word in name_to_idx:
            if len(searched_indices) == 1 and searched_indices[0] == None:
                searched_indices = name_to_idx[q_word]
            else:
                searched_indices = list(set(searched_indices) & set(name_to_idx[q_word]))
            query_types.append('NAME')
        elif q_word in code_to_idx:
            if len(searched_indices) == 1 and searched_indices[0] == None:
                searched_indices = code_to_idx[q_word]
            else:
                searched_indices = list(set(searched_indices) & set(code_to_idx[q_word]))
            query_types.append('CODE')
        elif q_word in status_to_idx:
            if len(searched_indices) == 1 and searched_indices[0] == None:
                searched_indices = status_to_idx[q_word]
            else:
                searched_indices = list(set(searched_indices) & set(status_to_idx[q_word]))
            query_types.append('STATUS')

    results = []
    for result_i, searched_i in enumerate(searched_indices):
        results.append([])
        for p_idx, p_type in enumerate(['NAME', 'CODE', 'STATUS']):
            if p_type not in query_types:
                results[result_i].append(data[searched_i][p_idx])
    if len(results[0]) == 1:
        results = [r[0] for r in results]
    else:
        results = ['{}({})'.format(r[0], ', '.join(r[1:])) for r in results]
    return results


if __name__ == '__main__':
    data = [
        ['홍길동', 'N20123', '합격'],
        ['이철수', 'N20124', '합격'],
        ['이나영', 'N20125', '불합격'],
        ['김민우', 'N20126', '대기'],
        ['박보민', 'N20127', '불합격'],
        ['이나영', 'N20128', '합격'],
        ['김지은', 'N20129', '대기']
    ]

    name_to_idx = {}
    code_to_idx = {}
    status_to_idx = {}
    for i, d in enumerate(data):
        name, code, status = d
        name_to_idx[name] = [i]
        code_to_idx[code] = [i]
        status_to_idx[status] = status_to_idx.get(status, []) + [i]

    searched_result = search(data, name_to_idx, code_to_idx, status_to_idx, input('검색 : '))
    print(' '.join(searched_result))