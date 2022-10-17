
import sys

num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

if len(num1) > len(num2):
    print('False')
    sys.exit(0)
# ******************************
# Make your Code
# ******************************

is_subset = False

all_subsets = []

# index 2 -> 4
for i in range(len(num1) - 1, len(num2)):
    list_to_append = []
    for x in range(i, i - len(num1), -1):
        list_to_append.insert(0, num2[x])
    all_subsets.append(list_to_append)

for subset in all_subsets:
    if num1 == subset:
        is_subset = True

print(is_subset)
