class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class solution(object):
    '''
    Add Two Numbers

    You are given two linked lists representing two non-negative numbers.
    The digits are stored in reverse order and each of their nodes contain a
    single digit. Add the two numbers and return it as a linked list.

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    '''

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        """
        extra = 0
        result = ListNode(None)
        resultNext = result
        l1Next = l1
        l2Next = l2

        while True:
            if l1Next and l2Next:
                resultNext.val = (l1Next.val + l2Next.val + extra) % 10
                if l1Next.val + l2Next.val + extra >= 10:
                    extra = 1
                else:
                    extra = 0
                l1Next = l1Next.next
                l2Next = l2Next.next
                if l1Next or l2Next or extra:
                    resultNext.next = ListNode(None)
                    resultNext = resultNext.next
                else:
                    break

            elif not (l1Next and l2Next) and (l1Next or l2Next):
                if l1Next:
                    rest = l1Next
                    l1Next = l1Next.next
                else:
                    rest = l2Next
                    l2Next = l2Next.next

                resultNext.val = (extra + rest.val) % 10
                if extra + rest.val < 10:
                    resultNext.next = rest.next
                    break
                else:
                    extra = 1
                    resultNext.next = ListNode(None)
                    resultNext = resultNext.next
            else:
                resultNext.val = extra
                break
        return result


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

test = solution()
result = test.addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
