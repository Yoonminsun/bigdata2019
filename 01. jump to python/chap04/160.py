# f = open("새파일.txt",'w') # 현재 소스코드 파일이 있는 경로에 파일 생성
                            # 유닉스 계열에서는 실행이 안 될 수도 있다
# f = open("d:\새파일.txt",'w') # 절대경로(absolute path)에 파일 생성
# f = open("d:/새파일.txt",'w')
# f = open("d:\MyPath\새파일.txt",'w')
# f = open("d:/MyPath/새파일.txt",'w')
# f = open("d:\MyPath\new\새파일.txt",'w') # 경로의 \n을 특수문자로 인식하게 되므로 에러발생
# f = open("d:\MyPath\\new\새파일.txt",'w') # 역슬러쉬 두개를 이용하여야 하나가 사용된 경로로 인식
# f = open("d:\\MyPath\\new\\새파일.txt",'w') # 실수를 줄이기 위해서 경로를 표시할때 모든 \를 \\로 표시
f = open("d:/MyPath/new/새파일.txt",'w') # \를 한번만 사용해도 됨 (파이썬에서만,하위버전은 확인 필요)
f.close()