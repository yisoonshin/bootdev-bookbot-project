def count_chars(str):
    chars = [*str]
    counts = {i:chars.count(i) for i in set(chars)} 
    return dict(sorted(counts.items(), key = lambda x: x[1], reverse=True))

def get_num_words(str):
    return len(str.split())
