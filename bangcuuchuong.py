#Khoi lenh co the phat sinh loi
try:
   #Nhap gia tri tu ban phim
   #Ep kieu du lieu sang so nguyen
   n = int(input())
  
   #Su dung cau truc re nhanh xu ly truong hop n nam ngoai (1:9)
   if n<1 or n>9:
       print("Chi tinh duoc bang cuu chuong 1 den 9 thoi!")
   else:   
       #Su dung vong lap for voi 1 <= i <= 9
       for i in range(1, 10):
           #Xuat theo dinh dang de bai yeu cau
           print("{} x {} = {}".format(n, i, n*i))
#Khoi lenh duoc thuc thi khi loi xay ra
except:
   print("Dinh dang dau vao khong hop le!")
