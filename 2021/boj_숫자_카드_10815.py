import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))[:-1]

M = int(sys.stdin.readline())
test_cards = list(map(int, sys.stdin.readline().split()))[:-1]

for test_card in test_cards:
    if test_card in cards:
        print(1)
    else:
        print(0)

# print(cards)
# print(test_cards)
