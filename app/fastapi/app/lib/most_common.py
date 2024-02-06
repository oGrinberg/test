from collections import Counter 
  

def mostcommon(data_set, num):
    whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ-1234567890')
    answer = ''.join(filter(whitelist.__contains__, data_set))
    split_it = answer.lower().split() 
    result = Counter(split_it) 
    most_result = result.most_common(num) 
    return most_result
  