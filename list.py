demo_list = [1,'hello',1.34,True,1,2,3]
colors = ['red','blue','green']
numbres_list = ( (1,2,3,4))

#print(numbres_list)
#print(type(numbres_list))

#r= list(range(1,10))

#print(r)

#print(type(colors))

#print(dir(colors))
#print(len(colors))
#print(colors[1])
#print("blue" in colors)
#print("ljfkdl" in colors)
#colors[1]="yellow"
#colors.append('blue')
#colors.extend(['black','white'])
#colors.extend(('pink','orange'))
#print(colors)

#colors.insert(len(colors),'new')
#print(colors)
#colors.pop()
#print(colors)
#colors.remove('blue')
#print(colors)
#colors.pop(2)
#print(colors)

colors.sort()
print(colors)
colors.sort(reverse=True)
print(colors)
colors.index('red')
print(colors.index('red'))
print(colors.count('red'))