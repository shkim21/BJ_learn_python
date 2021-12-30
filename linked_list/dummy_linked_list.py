class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        dummy = Node("dummy")
        self.head = dummy
        self.tail = dummy
        self.current = None
        self.before = None
        self.num_of_data = 0

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node #이전 tail의 next를 새로 들어온 데이터로 연결
        self.tail = new_node#tail 교체

        self.num_of_data += 1

    #delete: current 노드 삭제, 인접 노드 current, next 변경
    def delete(self):
        pop_data = self.current.data#꺼낼 데이터(현재 데이터)

        if self.current is self.tail:#현재 노드가 맨 뒤이면(하나이면?)
            self.tail = self.before#이전 tail과 연결을 끊는거임. 새로 정의(before로)
        
        
        self.before.next = self.current.next
        self.current = self.before  #중요: current가 next가 아닌 before로 변경된다!!

        self.num_of_data -= 1

        return pop_data

    def first(self):#맨 앞의 노드 검색
        if self.num_of_data == 0:
            return None

        self.before = self.head
        self.current = self.head.next
        
        return self.current.data

    def next(self):#current 노드 다음 노드 검색
        if self.current.next == None:
            return None
        
        self.before = self.current
        self.current = self.current.next

        return self.current.data

    def size(self):
        return self.num_of_data


if __name__ == '__main__':
    l_list = LinkedList()
    l_list.append(5)
    l_list.append(2)
    l_list.append(1)
    l_list.append(2)
    l_list.append(7)
    l_list.append(2)
    l_list.append(11)

    print('first :', l_list.first())      # first : 5
    print('next :', l_list.next())        # next : 2
    print('size :', l_list.size())        # size : 7
    print('delete :', l_list.delete())    # delete : 2
    print('size :', l_list.size())        # size : 6
    print('current:', l_list.current.data)# current: 5
    print('tail:', l_list.tail.data)      # tail: 11
    print('first :', l_list.first())      # first : 5
    print('next :', l_list.next())        # next : 1
    print('next :', l_list.next())        # next : 2
    print('next :', l_list.next())        # next : 7


    # 전체 노드 data 표시하기
    data = l_list.first()

    if data:
        print(data, end=' ')
        while True:
            data = l_list.next()
            if data:
                print(data, end= ' ')
            else:
                break
    # 5 1 2 7 2 11



    # 2만 삭제하기
    data = l_list.first()

    if data and data == 2:
        l_list.delete()
        print('deleted', end=' ')
    else:
        print(data, end= ' ')

    while True:
        data = l_list.next()
        if data == 2:
            l_list.delete()
            print('deleted', end=' ')
        elif data:
            print(data, end=' ')
        else:
            break

    # 5 1 deleted 7 deleted 11