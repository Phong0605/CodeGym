class QuanLySanPham:
    def __init__(self,msp,ten,hang,gia):
        self.msp=msp
        self.ten=ten
        self.hang=hang
        self.gia=gia
        self.dssp=[]

    def tim_san_pham(self,msp):
        if len(self.dssp)==0:
            return -1
        else:
            for i in range(len(self.dssp)):
                if msp==self.dssp[i]["Mã sản phẩm: "]:
                    return 0
                else:
                    return -1


    def them_san_pham(self):
        msp=input("Nhập vào mã sản phẩm: ")
        if self.tim_san_pham(msp)==0:
            msp=input("Mã sản phẩm đã tồn tại, vui lòng nhập mã khác: ")
        ten=input("Tên sản phẩm: ")
        hang=input("Hãng sản xuất: ")
        gia=input("Giá thành của sản phẩm: ")
        sp=[f"Mã sản phẩm: {msp}",f"Tên sản phẩm: {ten}",f"Hãng: {hang}",f"Giá thành: {gia}"]
        self.dssp.append(sp)

    def hien_thi_danh_sach(self):
        if len(self.dssp)==0:
            print("Danh sách rỗng")
        else:
            for i in range(len(self.dssp)):
                print(self.dssp[i])

    def xoa_san_pham(self):
        if len(self.dssp)==0:
            print("Danh sách rỗng, vui lòng chọn chức năng khác")
        else:
            for i in range(len(self.dssp)):
                print(str(i + 1) + ". " + self.dssp[i])
            n = int(input("Chọn STT sản phẩm bạn muốn xóa: "))
            while n <= 0 or n > len(self.dssp):
                n = int(input("Vui lòng nhập lại stt: "))
            self.dssp.pop(n - 1)
            print("Xóa thành công")


    def cap_nhat_thong_tin(self):
        if len(self.dssp)==0:
            print("Danh sách rỗng, vui lòng chọn chức năng khác")
        else:
            for i in range(len(self.dssp)):
                print(i+1,end=". ")
                print(self.dssp[i])
            n = int(input("Chọn STT sản phẩm bạn muốn thay đổi: "))
            while n <= 0 or n > len(self.dssp):
                n = int(input("Vui lòng nhập lại stt: "))
            print("1. Mã sản phẩm")
            print("2. Tên sản phẩm")
            print("3. Hãng sản xuất")
            print("4. Giá thành")
            m = int(input("Chọn thông tin cần sửa: "))
            while m <= 0 or m > 4:
                m = int(input("Vui lòng nhập lại thông tin từ 1 đến 4: "))
            if m == 1:
                msp = input("Mã sản phẩm mới: ")
                self.dssp[n - 1][0] = f"Mã sản phẩm: {msp}"
                print("Cập nhật thành công")
            elif m == 2:
                ten = input("Tên mới của sản phẩm: ")
                self.dssp[n - 1][1] = f"Tên sản phẩm: {ten}"
                print("Cập nhật thành công")
            elif m == 3:
                hang = input("Hãng sản xuất mới: ")
                self.dssp[n - 1][2] = f"Hãng: {hang}"
                print("Cập nhật thành công")
            else:
                gia = input("Giá mới của sản phẩm: ")
                self.dssp[n - 1][3] = f"Giá thành: {gia}"
                print("Cập nhật thành công")


print("1.Thêm sản phẩm")
print("2.Hiển thị danh sách sản phẩm")
print("3.Xóa sản phẩm")
print("4.Cập nhật thông tin sản phẩm")
print("Bất kỳ số nào khác: Thoát chương trình")

chucnang= QuanLySanPham("K214060409","Phong","0886524023","25000")
while True:
    print("_______________________________________________")
    nhapchucnang = int(input("Chọn chức năng : "))

    if nhapchucnang==1:
        print("_______________________________________________")
        chucnang.them_san_pham()

    elif nhapchucnang==2:
        print("_______________________________________________")
        chucnang.hien_thi_danh_sach()

    elif nhapchucnang==3:
        print("_______________________________________________")
        chucnang.xoa_san_pham()

    elif nhapchucnang==4:
        print("_______________________________________________")
        chucnang.cap_nhat_thong_tin()

    else:
        print("_______________________________________________")
        print("Thoát chương trình")
        break

