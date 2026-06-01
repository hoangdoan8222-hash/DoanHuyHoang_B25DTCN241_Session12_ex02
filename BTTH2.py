
# (1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP
# 1. Phân tích Input/Output
# - Input: 
#   + Lựa chọn menu: String (từ '1' đến '7').
#   + Chuỗi văn bản: Mã sổ, Tên khách hàng (String).
#   + Số liệu: Số tiền gửi, Kỳ hạn, Số tháng thực gửi (Integer > 0).
#   + Tỉ lệ: Lãi suất năm (Float > 0).
# - Output: 
#   + Bảng danh sách sổ tiết kiệm.
#   + Thông báo lỗi (validation) hoặc thành công.
#   + Kết quả tính toán: Tiền lãi, Tổng tiền nhận (Float).

# 2. Đề xuất giải pháp
# - Lưu trữ dữ liệu: Sử dụng List chứa các Dictionary.
# - Cấu trúc điều khiển: Dùng 1 vòng lặp `while True` duy nhất. Dùng `match...case` để rẽ nhánh menu. Không sử dụng hàm (def).
# - Xử lý Validation (Không dùng try...except):
#   + Số nguyên: Dùng `.isdigit()` để chặn chữ/số âm, sau đó mới ép kiểu `int()`.
#   + Số thực: Dùng `.replace('.', '', 1).isdigit()` để kiểm tra, sau đó ép kiểu `float()`.
#   + Chuỗi: Dùng `.strip().upper()` để chuẩn hóa mã sổ, kiểm tra chuỗi rỗng `if not...`.
# - Tìm kiếm: Dùng vòng lặp `for` duyệt qua danh sách để tìm `account_id`, nếu lỗi thì dùng `continue` để quay lại menu.

# 3. Thiết kế thuật toán (Luồng chương trình)
# - Bước 1: Khởi tạo danh sách `saving_accounts` chứa dữ liệu mẫu.
# - Bước 2: Bắt đầu vòng lặp vô tận `while True`. Hiển thị Menu.
# - Bước 3: Nhận input `choice` và đưa vào `match choice`:
#   + case '1': Nếu list rỗng -> Báo rỗng. Ngược lại -> Duyệt in danh sách.
#   + case '2': Nhập mã -> Duyệt tìm trùng lặp. Nhập các thông tin khác -> Validate bằng `.isdigit()`. Thêm dictionary mới vào list.
#   + case '3', '4', '5', '6': Nhập mã -> Duyệt list tìm sổ -> Kiểm tra điều kiện (tồn tại, trạng thái "active").
#     * Case 3: Validate input mới -> Ghi đè value vào dictionary.
#     * Case 4: Đổi `status` thành "closed".
#     * Case 5: Tính lãi = Tiền * Lãi/100 * Kỳ hạn/12 -> In kết quả.
#     * Case 6: Nhập số tháng -> Validate. Nếu tháng < kỳ hạn -> Lãi suất 0.5. Ngược lại -> Lãi suất gốc. Tính tiền -> In kết quả.
#   + case '7': In lời chào -> `break` thoát chương trình.
#   + case _: (Bắt lỗi menu) -> Báo lỗi lựa chọn không hợp lệ.


saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====")
    print("1. Xem danh sách sổ tiết kiệm")
    print("2. Mở sổ tiết kiệm mới")
    print("3. Cập nhật thông tin sổ tiết kiệm")
    print("4. Tất toán hoặc xóa sổ tiết kiệm")
    print("5. Tính lãi dự kiến khi đến hạn")
    print("6. Kiểm tra điều kiện rút trước hạn")
    print("7. Thoát chương trình")
    
    choice = input("Mời bạn chọn chức năng (1-7): ").strip()
    
    match choice:
        # *** CHỨC NĂNG 1: XEM DANH SÁCH ***
        case '1':
            if not saving_accounts:
                print("Danh sách sổ tiết kiệm hiện đang trống")
            else:
                print("\nDanh sách sổ tiết kiệm:")
                index = 1
                for acc in saving_accounts:
                    print(f"{index}. Mã sổ: {acc['account_id']} | Khách hàng: {acc['customer_name']} | "
                        f"Số tiền gửi: {acc['balance']} | Kỳ hạn: {acc['term_months']} tháng | "
                        f"Lãi suất: {acc['interest_rate']}%/năm | Trạng thái: {acc['status']}")
                    index += 1

        # *** CHỨC NĂNG 2: MỞ SỔ MỚI ***
        case '2':
            account_id = input("- Nhập mã sổ tiết kiệm: ").strip().upper()
            
            # Bẫy 1
            is_exist = False
            for acc in saving_accounts:
                if acc["account_id"] == account_id:
                    is_exist = True
                    break
            
            if is_exist:
                print("Mã sổ tiết kiệm đã tồn tại!")
                continue

            customer_name = input("- Nhập tên khách hàng: ").strip()
            # Bẫy 2
            if not customer_name:
                print("Tên khách hàng không được để trống")
                continue

            # Bẫy 3 
            balance_str = input("- Nhập số tiền gửi: ").strip()
            term_str = input("- Nhập kỳ hạn gửi theo tháng: ").strip()
            
            if not (balance_str.isdigit() and term_str.isdigit()):
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue
                
            balance = int(balance_str)
            term_months = int(term_str)
            if balance <= 0 or term_months <= 0:
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue

            # Bẫy 4 
            rate_str = input("- Nhập lãi suất năm: ").strip()
            if not rate_str.replace('.', '', 1).isdigit():
                print("Lãi suất không hợp lệ!")
                continue
                
            interest_rate = float(rate_str)
            if interest_rate <= 0:
                print("Lãi suất không hợp lệ!")
                continue

            # Thêm vào danh sách
            new_account = {
                "account_id": account_id,
                "customer_name": customer_name,
                "balance": balance,
                "term_months": term_months,
                "interest_rate": interest_rate,
                "status": "active"
            }
            saving_accounts.append(new_account)
            print("Mở sổ tiết kiệm thành công!")

        # *** CHỨC NĂNG 3: CẬP NHẬT SỔ ***
        case '3':
            account_id = input("- Nhập mã sổ tiết kiệm cần cập nhật: ").strip().upper()
            
            account_to_update = None
            for acc in saving_accounts:
                if acc["account_id"] == account_id:
                    account_to_update = acc
                    break
            
            # Bẫy 5 & 6
            if not account_to_update:
                print("Không tìm thấy mã sổ tiết kiệm!")
                continue
            if account_to_update["status"] == "closed":
                print("Không thể cập nhật sổ tiết kiệm đã tất toán!")
                continue

            new_name = input("- Nhập tên khách hàng mới: ").strip()
            if not new_name:
                print("Tên khách hàng không được để trống")
                continue

            new_balance_str = input("- Nhập số tiền gửi mới: ").strip()
            new_term_str = input("- Nhập kỳ hạn mới theo tháng: ").strip()
            
            if not (new_balance_str.isdigit() and new_term_str.isdigit()):
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue
                
            new_balance = int(new_balance_str)
            new_term = int(new_term_str)
            if new_balance <= 0 or new_term <= 0:
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue

            new_rate_str = input("- Nhập lãi suất năm mới: ").strip()
            if not new_rate_str.replace('.', '', 1).isdigit():
                print("Lãi suất không hợp lệ!")
                continue
                
            new_rate = float(new_rate_str)
            if new_rate <= 0:
                print("Lãi suất không hợp lệ!")
                continue

            account_to_update["customer_name"] = new_name
            account_to_update["balance"] = new_balance
            account_to_update["term_months"] = new_term
            account_to_update["interest_rate"] = new_rate
            print("Cập nhật sổ tiết kiệm thành công!")

        # *** CHỨC NĂNG 4: TẤT TOÁN SỔ ***
        case '4':
            account_id = input("- Nhập mã sổ tiết kiệm cần tất toán/xóa: ").strip().upper()
            
            account_to_close = None
            for acc in saving_accounts:
                if acc["account_id"] == account_id:
                    account_to_close = acc
                    break
                    
            if not account_to_close:
                print("Không tìm thấy mã sổ tiết kiệm")
                continue
            if account_to_close["status"] == "closed":
                print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                continue

            account_to_close["status"] = "closed"
            print(f"Đã tất toán sổ tiết kiệm {account_id} thành công!")

        # *** CHỨC NĂNG 5: TÍNH LÃI DỰ KIẾN ***
        case '5':
            account_id = input("- Nhập mã sổ tiết kiệm cần tính lãi: ").strip().upper()
            
            account_to_calc = None
            for acc in saving_accounts:
                if acc["account_id"] == account_id:
                    account_to_calc = acc
                    break
                    
            if not account_to_calc:
                print("Không tìm thấy mã sổ tiết kiệm")
                continue
            if account_to_calc["status"] == "closed":
                print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                continue

            interest = account_to_calc["balance"] * (account_to_calc["interest_rate"] / 100) * (account_to_calc["term_months"] / 12)
            total_amount = account_to_calc["balance"] + interest
            
            print(f"Tiền lãi dự kiến: {interest:,.0f} VND")
            print(f"Tổng tiền nhận khi đến hạn: {total_amount:,.0f} VND")

        # *** CHỨC NĂNG 6: KIỂM TRA ĐIỀU KIỆN RÚT TRƯỚC HẠN ***
        case '6':
            account_id = input("- Nhập mã sổ tiết kiệm cần kiểm tra: ").strip().upper()
            
            account_to_check = None
            for acc in saving_accounts:
                if acc["account_id"] == account_id:
                    account_to_check = acc
                    break
                    
            if not account_to_check:
                print("Không tìm thấy mã sổ tiết kiệm")
                continue
            if account_to_check["status"] == "closed":
                print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                continue

            # Bẫy 7 
            actual_months_str = input("- Nhập số tháng thực gửi: ").strip()
            if not actual_months_str.isdigit():
                print("Số tháng thực gửi không hợp lệ!")
                continue
                
            actual_months = int(actual_months_str)
            if actual_months <= 0:
                print("Số tháng thực gửi không hợp lệ!")
                continue

            applied_rate = account_to_check["interest_rate"]
            if actual_months < account_to_check["term_months"]:
                applied_rate = 0.5
                print("-> Khách hàng rút trước hạn. Áp dụng lãi suất 0.5%/năm.")
            else:
                print(f"-> Khách hàng rút đúng hạn. Áp dụng lãi suất {applied_rate}%/năm.")

            interest = account_to_check["balance"] * (applied_rate / 100) * (actual_months / 12)
            total_amount = account_to_check["balance"] + interest

            print(f"Tiền lãi thực nhận: {interest:,.0f} VND")
            print(f"Tổng tiền thực nhận: {total_amount:,.0f} VND")

        # *** CHỨC NĂNG 7: THOÁT CHƯƠNG TRÌNH ***
        case '7':
            print("Cảm ơn bạn đã sử dụng hệ thống TechBank. Tạm biệt!")
            break
            
        # *** BẪY 8: LỰA CHỌN KHÔNG HỢP LỆ ***
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại")