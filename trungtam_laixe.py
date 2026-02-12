import streamlit as st
import pandas as pd

# Cấu hình trang web
st.set_page_config(page_title="Dạy Lái Xe Phương Thúy", page_icon="🚗", layout="wide")

# --- THANH MENU BÊN TRÁI ---
st.sidebar.title("DANH MỤC CHÍNH")
# Thêm "Giờ học" vào danh sách menu
menu = st.sidebar.radio("Chọn mục:", ["Giới thiệu", "Bảng giá", "Giờ học", "Thi thử lý thuyết", "Liên hệ"])

# --- TRANG: GIỚI THIỆU ---
if menu == "Giới thiệu":
    st.title("🚗 TRUNG TÂM ĐÀO TẠO LÁI XE PHƯƠNG THÚY")
    st.write("Cung cấp dịch vụ ôn luyện lý thuyết chuyên sâu và hồ sơ thi sát hạch uy tín.")
    st.image("https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?w=800")
    st.info(f"📍 Địa chỉ: Khóm 8, P7, Thành Phố Trà Vinh") # [cite: 3]

# --- TRANG: BẢNG GIÁ ---
elif menu == "Bảng giá":
    st.title("💰 BẢNG BÁO GIÁ DỊCH VỤ") # [cite: 5]
    st.write("Kính gửi Quý học viên thông tin chi tiết các gói ôn luyện và hồ sơ đăng ký thi:") # [cite: 7, 8]

    # Gói VIP
    st.subheader("I. Gói Ôn Luyện Lý Thuyết Chuyên Sâu (VIP)") # [cite: 10]
    st.write("Dành cho học viên cần kèm riêng, đảm bảo kiến thức vững chắc.") # [cite: 10]
    data_vip = {
        "Hạng Mục": ["Ôn lý thuyết Xe máy (A1, A)", "Ôn lý thuyết Ô tô (B1, B2, C1)"],
        "Đơn Giá (VNĐ)": ["2.000.000 đ", "2.500.000 đ"] # [cite: 10]
    }
    st.table(data_vip)

    # Gói Tiêu Chuẩn
    st.subheader("II. Gói Tiêu Chuẩn (Học phí + Phí nộp hồ sơ)") # [cite: 10]
    data_tc = {
        "Hạng Xe": ["Hạng A1 (Xe máy dưới 175cc)", "Hạng A (Mô tô trên 175cc)"],
        "Trọn Gói (VNĐ)": ["800.000 đ", "2.200.000 đ"] # [cite: 10]
    }
    st.table(data_tc)
    
    st.warning("⚠️ Lưu ý: Giá trên chưa bao gồm VAT và lệ phí thi sát hạch tại sân.") # [cite: 11, 19]

# --- TRANG: GIỜ HỌC (Thông tin từ ảnh thoigianhoatdong.jpg) ---
elif menu == "Giờ học":
    st.title("⏰ THỜI GIAN HỌC & LÀM VIỆC")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("### 📅 Ngày làm việc")
        st.write("**Từ Thứ 2 đến Thứ 7 hàng tuần.**")
        
        st.success("### 🕒 Giờ làm việc")
        st.write("* **Sáng:** 08:00 - 11:00")
        st.write("* **Chiều:** 13:00 - 17:00")
        
    with col2:
        st.warning("### 🎓 Hình thức học")
        st.write("**Linh hoạt, sắp xếp theo lịch của học viên.**")
        st.write("Học viên được kèm cặp sát sao, hướng dẫn mẹo ghi nhớ hiệu quả.") # 

# --- TRANG: THI THỬ ---
elif menu == "Thi thử lý thuyết":
    st.title("✍️ Thi Thử Lý Thuyết")
    st.info("Hệ thống đang cập nhật ngân hàng 600 câu hỏi...")

# --- TRANG: LIÊN HỆ ---
elif menu == "Liên hệ":
    st.title("📞 Thông Tin Liên Hệ")
    st.write("**Chủ trung tâm:** Phương Thúy") # [cite: 2]
    st.write("**Hotline/Zalo:** 0939.838.175") # [cite: 4, 24]
    st.write("**Địa chỉ:** Khóm 8, P7, Thành Phố Trà Vinh") # [cite: 3]

# Chân trang
st.markdown("---")
st.caption("© 2026 Phương Thúy - Tận tâm vì sự an toàn của bạn.")
