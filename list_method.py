def list_sum(data : list[int]) -> int:
    result = sum(data)
    return result


#List comprehension
def list_sqaures(data : list[int]):
    updatedList = [v*v for v in data]
    list_iterator(updatedList)
    
    

def list_iterator(data : list[int]):
    for i in data:
        print(f"{i}")
    

l = [1,2,3,4,5]
print(f"List Answer: {list_sum(l)}")
list_sqaures(l)
