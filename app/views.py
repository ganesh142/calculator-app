from django.shortcuts import render,redirect

# Create your views here.
def calculator(request):
    return render(request,'base.html')
def report(request):
    name=request.POST['expression']
    if name!='':
        val=evaluate(name)
        return render(request,'base.html',{'val1':val})
    else:
        return redirect('/')

def evaluate(str):
    if str[0].isdigit() and str[len(str)-1].isdigit():
        stack=[]
        num=''
        for i in str:
            if i.isdigit() or i=='.':
                num+=i
            else:
                stack.append(num)
                stack.append(i)
                num=''
        stack.append(num)
        while(len(stack)!=1):
            m,pos=found2(stack)
            if m:
                if stack[pos]=='*':
                    val=float(stack[pos-1])*float(stack[pos+1])
                else:
                    val=float(stack[pos-1])/float(stack[pos+1])
                stack[pos-1]=val
                stack=transfer(stack,pos)
            else:
                if stack[1]=='+':
                    val=float(stack[0])+float(stack[2])
                else:
                    val=float(stack[0])-float(stack[2])
                stack[0]=val
                stack=transfer(stack,1)
        return stack[0]
    else:
        return 'Error'
def found2(stack):
    flag=False
    j=0
    for i in range(0,len(stack)):
        if stack[i]=='*'or stack[i]=='/':
            flag=True
            j=i
            break
    return flag,j
def transfer(stack,pos):
    stack.pop(pos)
    stack.pop(pos)
    return stack

    