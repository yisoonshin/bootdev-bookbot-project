#!/usr/bin/env python3

def count_chars(str):
    chars = [*str]
    counts = {i:chars.count(i) for i in set(chars)} 
    return dict(sorted(counts.items(), key = lambda x: x[1], reverse=True))

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        counts = count_chars(file_contents.lower())
        for char, count in counts.items():
            if char.isalpha():
                print(f'The \'{char}\' character was found {count} times')

if __name__ == '__main__':
    main()