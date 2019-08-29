i=int(input("enter no. of bottels"))
radius=list(map(int, input().split()))
print(max([radius.count(i) for i in radius]))