# input
N = int(input())
tree = dict()

for _ in range(N):
	root, left, right = map(str, input().split())
	tree[root] = (left, right)

# solve
def preorder(n):
	if n != '.':
		left, right = tree[n]

		print(n, end='')
		preorder(left)
		preorder(right)

def inorder(n):
	if n != '.':
		left, right = tree[n]

		inorder(left)
		print(n, end='')
		inorder(right)

def postorder(n):
	if n != '.':
		left, right = tree[n]

		postorder(left)
		postorder(right)
		print(n, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')