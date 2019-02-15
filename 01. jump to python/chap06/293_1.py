dic_mos = {'.-':'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E', '..-.':'F', '--.':'G', '....':'H',
           '..':'I', '.---':'J', '-.-':'K', '.-..':'L', '--':'M', '-.':'N', '---':'O', '.--.':'P',
           '--.-':'Q', '.-.':'R', '...':'S', '-':'T', '..-':'U', '...-':'V', '.--':'W', '-..-':'X',
           '-.--':'Y', '--..':'Z'}

str_input = '.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'
# str_input = '-- .. -. ... ..- -.  .--. .-. --- --. .-. .- --'
str_result=''
str_current=''

for i in range(len(str_input)):
    if str_input[i]==' ' and str_input[i+1]!=' ' and str_input[i-1]!=' ':
        str_result = str_result+ dic_mos[str_current]
        str_current = ''
    elif str_input[i]==' 'and str_input[i+1]==' ':
        str_result = str_result+ dic_mos[str_current] + ' '
        str_current=''
    elif str_input[i]==' 'and str_input[i-1]==' ':
        continue
    else:
        str_current += str_input[i]
str_result += dic_mos[str_current]

print(str_result)
