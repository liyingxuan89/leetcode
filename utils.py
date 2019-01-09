# coding = utf8

class ListNode():
	def __init__(self,x):
		self.val = x
		self.next = None

def int2link(integer):
	if integer < 10:
		return ListNode(integer)
    head = ListNode(None)
    cur = ListNode(None)
    head.next = cur
    while(True):
        m,n = divmod(integer,10)
        cur.val = n
        ne = ListNode(None)
        cur.next = ne
        cur = ne
        integer = m
        condition = (divmod(integer,10)[0] == 0)
        if (condition):
            cur.val = m
            break
    return head.next

def link2int(link):
    integer = 0
    power = 0
    while(link):
        integer += link.val*(10**power)
        power += 1
        link = link.next
    return integer

def list2link(List):
    List = List[::-1]
    head = ListNode(None)
    cur = ListNode(None)
    head.next = cur
    while(List):
        cur.val = List.pop()
        if(List):
            ne = ListNode(None)
            cur.next = ne
            cur = ne
    return head.next


def show_link(link):
	while(link):
		print(link.val)
		link = link.next
