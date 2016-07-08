# WARNING: this takes a while to run
# Uses the tricolor algorithm
class Node:
	# Color can be w,g,b
	def __init__(self, num, out=None):
		self.color = "w"
		self.id = num
		if (out is None):
			self.out = []
		else:
			self.out = out
	def __repr__(self):
		return self.color + ' Node ' + str(self.id)

# Returns a node if there is a node of 0 in-degree and removes it
# otherwise returns None.
def find_unvisited_node(nodes):
	node = None
	i = 1
	while node == None and i < 6:
		if nodes[i].color == "w":
			node = nodes[i]
		else:
			i += 1
	return node

def DFS(node, nodes, ordering):
	stack = [node]
	while len(stack) != 0:
		print len(stack)
		n = stack.pop()
		n.color = 'g'
		for nn in n.out:
			if (nodes[nn].color == 'w'):
				stack.append(nodes[nn])
		n.color = 'b'
		ordering.insert(0, n.id)
	return ordering

nodes = {}
for i in range(1,875715):
	nodes[i] = Node(i)
with open("SCC.txt","r") as f:
	for l in f.readlines():
		ll = map(int, l.split())
		nodes[ll[0]].out.append(ll[1])

orderings = []
while (find_unvisited_node(nodes) != None):
	ordering = []
	n = find_unvisited_node(nodes)
	DFS(n, nodes, ordering)
	orderings.append(ordering)
for o in orderings:
	print len(o)