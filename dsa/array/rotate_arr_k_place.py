

def reverse(arr, left, right):
    while(left<right):
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    print(arr)
    
    

def rotate(arr,k):
    n= len(arr)
    k=k%n
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
    reverse(arr,0,n-1)

arr=[1,12,45,50,6]
k=3    
rotate(arr,k)