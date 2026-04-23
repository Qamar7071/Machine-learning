n=[1,2,1]
r_n=n.copy()
r_n.reverse()
print(r_n)
if n==r_n:
    print('p')
else:
    print('fale')


st=('A','B','C','A','B','C','A')
print(st.count('A'))
list=list(st)
num=[1,2,3,4,3,1,2]
print(sorted(list))


dic={
    'table':["a piece of furniture","list of fact"],
    'cat':' a small animal',
}
print(dic['table'])


list=['c++','java','python','c','c++','java']
s=set(list)
print(s)

name1=str(input('Enter your name : '))
marks1=int(input('Enter your marks : '))
name2=str(input('Enter your name : '))
marks2=int(input('Enter your marks : '))
name3=str(input('Enter your name : '))
marks3=int(input('Enter your marks : '))
std={
    "name":[name1,name3,name2],
    "marks":[marks3,marks1,marks2]

}
print(std)



