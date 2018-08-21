f1 = input("원본 파일 이름을 입력하시오:")
f2 = input("복사 파일 이름을 입력하시오:")

ifile = open(f1,"rb")
ofile = open(f2,"wb")

# 입력 파일에서 1024 바이트씩 읽어서 출력파일에 쓴다.
while True:
    copy_buffer = ifile.read(1024)
    if not copy_buffer:
        break
    ofile.write(copy_buffer)

ifile.close()
ofile.close()
print(f1+"을"+f2+"로 복사하였습니다.")