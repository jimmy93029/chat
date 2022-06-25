chats = []
name = 1
with open('input.txt','r',encoding = 'utf-8-sig') as file :
  for line in file :
    if (u'\u0041'<= line <= u'\u005a') or (u'\u0061'<= line <= u'\u007a') :
      name = line.strip()
    else:
      chat = [name,line.strip()]
      chats.append(chat)
with open('output.txt','w',encoding = 'utf-8' ) as file :
  for line in chats:
    file.write(line[0] + ':' + line[1] + '\n'  )
    