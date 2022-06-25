
def open_file(filename_input,chats=[],name= None):
  with open(filename_input,'r',encoding = 'utf-8-sig') as file :
    for line in file :
      if (u'\u0041'<= line <= u'\u005a') or (u'\u0061'<= line <= u'\u007a') :
        name = line.strip()
      else:
        chat = [name,line.strip()]
        chats.append(chat)
  return chats

def write_file(filename_output, chats ):
  with open(filename_output,'w',encoding = 'utf-8' ) as file :
    for line in chats:
      file.write(str(line[0]) + ':' + line[1] + '\n'  )

def main(filename_input, filename_output):
  chats = open_file(filename_input)
  write_file(filename_output,chats)

main(input('請輸入要整理的對話檔案'),input('請輸入要產生的文字檔名稱'))