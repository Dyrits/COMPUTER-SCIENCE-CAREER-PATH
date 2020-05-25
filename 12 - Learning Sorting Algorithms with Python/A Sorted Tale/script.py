import utils
import sorts
import os

path = os.path.dirname(__file__)
book_small_csv__path = os.path.join(path, 'books_small.csv')
book_large__csv_path = os.path.join(path, 'books_large.csv')

bookshelf = utils.load_books(book_small_csv__path)
bookshelf_copy_one = bookshelf.copy()
bookshelf_copy_two = bookshelf.copy()

print()
for book in bookshelf:
    print(book["title_lower"])

# Title comparison function:
def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']

bubble_sorted_by_title = sorts.bubble_sort(bookshelf, by_title_ascending)

print()
for book in bubble_sorted_by_title:
    print(book['title'])

# Author comparison function:
def by_author_ascending(book_a, book_b):
    return book_a['author_lower'] > book_b['author_lower']

bubble_sorted_by_author = sorts.bubble_sort(bookshelf_copy_one, by_author_ascending)

print()
for book in bubble_sorted_by_author:
    print(f"{book['title']} by {book['author']}")

sorts.quicksort(bookshelf_copy_two, 0, len(bookshelf_copy_two) - 1, by_author_ascending)

print()
for book in bookshelf_copy_two:
    print(f"{book['title']} by {book['author']}")

# Length comparison function:
def by_total_length(book_a, book_b):
    return len(book_a["title"]) + len(book_a["author"]) > len(book_b["title"]) + len(book_b["author"])

long_bookshelf = utils.load_books(book_large__csv_path)

# bubble_sorted_by_length= sorts.bubble_sort(long_bookshelf, by_total_length)

# print()
# for book in bubble_sorted_by_length:
#     print(f"{book['title']} by {book['author']}")

sorts.quicksort(long_bookshelf, 0, len(long_bookshelf) - 1, by_total_length)

print()
for book in long_bookshelf:
    print(f"{book['title']} by {book['author']}")

