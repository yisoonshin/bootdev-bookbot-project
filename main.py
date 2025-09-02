#!/usr/bin/env python3
import sys,stats

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    path = sys.argv[1]
    file_contents = get_book_text(path)
    print('============ BOOKBOT ============')
    print('Analyzing book found at ...')
    print('----------- Word Count ----------')
    print(f'Found {stats.get_num_words(file_contents)} total words')
    print('----------- Character Count ----------')
    counts = stats.count_chars(file_contents.lower())
    for char, count in counts.items():
        if char.isalpha():
            print(f'{char}: {count}')

if __name__ == '__main__':
    main()