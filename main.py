# This is a sample Python script.
import self as self


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
def arr(arr):
    print( len(arr))
    dic={}
    for x in arr:
        dic[x]=1
        print (dic)
        print (chr(ord(x))) #chr ord
def pre_order(root):
    if root==None:
        return
    #code
    pre_order(root.left)
    pre_order(root.right)






if __name__ == '__main__':
    print_hi('PyCharm')
    arr(['a','b'])



