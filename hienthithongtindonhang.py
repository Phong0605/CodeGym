n = int(input("Nhập số tiền: "))

if n >= 150:
	print("số tiền thanh toán: ", n - 50)
elif n >= 100:
	print("số tiền thanh toán: ", n - 25)
elif n >= 75:
	print("số tiền thanh toán: ", n - 15)
else:
    print("số tiền thanh toán: ", n)
