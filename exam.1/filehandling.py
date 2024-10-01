# f=open('exam/alen1.txt','x')
# f.write('welcome to page')

# f=open('exam/alen.txt','x')
# f.write('\ngoodmorning: ')
# f.write('\nhi')
# f=open('exam/alen.txt','a')
# f.write('\nhave a nice day')

f=open('exam/alen.txt','r')
l=len(f.readlines())
f.seek(0)
longest_word=' '

for i in range(l):
    a=f.readline().strip()
    s=a.split(' ')
    for j in s:
        if j!='':
            if len(longest_word)<len(j):
                longest_word=j

    
print('longest_word: ',longest_word)