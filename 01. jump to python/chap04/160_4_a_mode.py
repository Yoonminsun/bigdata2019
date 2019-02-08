f = open('./file2.txt','a')
# f.write("Hello Deagu!!!!!!!!!!!!!!!!!") # 이전 파일의 마지막 위치에서 값을 쓴다 (줄바꿈 없이)
# 따라서 줄 단위로 입력을 하고 싶다면 메세지의 마지막에 \n을 명시적으로 붙인다
# f.write("\nHello Busan!!!!!!!!!!!!!!!!!")
my_message="""Hello Seoul!!!
Hello Jaeju!!!
Hello Incheon!!!
"""
f.write(my_message)
f.close()