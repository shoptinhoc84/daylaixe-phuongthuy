import streamlit as st
import pandas as pd

# Cấu hình trang web
st.set_page_config(page_title="Dạy Lái Xe Phương Thúy", page_icon="🚗", layout="wide")

# --- THANH MENU BÊN TRÁI ---
st.sidebar.title("DANH MỤC CHÍNH")
# Thêm mục "Bảng giá" vào menu
menu = st.sidebar.radio("Chọn mục:", ["Giới thiệu", "Bảng giá", "Thi thử lý thuyết", "Liên hệ"])

# --- TRANG: GIỚI THIỆU ---
if menu == "Giới thiệu":
    st.title("🚗 TRUNG TÂM ĐÀO TẠO LÁI XE PHƯƠNG THÚY")
    st.write("Cung cấp dịch vụ ôn luyện lý thuyết chuyên sâu và hồ sơ thi sát hạch uy tín.")
    st.image("https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?w=800")
    st.info(f"📍 Địa chỉ: Khóm 8, P7, Thành Phố Trà Vinh")

# --- TRANG: BẢNG GIÁ (Thông tin từ file docx của bạn) ---
elif menu == "Bảng giá":
    st.title("💰 BẢNG BÁO GIÁ DỊCH VỤ")
    st.write("Kính gửi Quý học viên thông tin chi tiết các gói ôn luyện và hồ sơ đăng ký thi:")

    # 1. Gói VIP
    st.subheader("I. Gói Ôn Luyện Lý Thuyết Chuyên Sâu (VIP)")
    st.write("Dành cho học viên cần kèm riêng, đảm bảo kiến thức vững chắc.")
    data_vip = {
        "Hạng Mục": ["Ôn lý thuyết Xe máy (A1, A)", "Ôn lý thuyết Ô tô (B1, B2, C1)"],
        "Mô Tả": ["Kèm cặp sát sao, hướng dẫn mẹo thi", "Hướng dẫn phương pháp làm bài trên máy tính"],
        "Đơn Giá (VNĐ)": ["2.000.000 đ", "2.500.000 đ"]
    }
    st.table(data_vip)

    # 2. Gói Tiêu Chuẩn
    st.subheader("II. Gói Tiêu Chuẩn (Học phí + Phí nộp hồ sơ)")
    data_tc = {
        "Hạng Xe": ["Hạng A1 (Xe máy dưới 175cc)", "Hạng A (Mô tô trên 175cc)"],
        "Chi Tiết": ["Học phí: 240k + Hồ sơ: 560k", "Học phí: 1.400k + Hồ sơ: 800k"],
        "Trọn Gói (VNĐ)": ["800.000 đ", "2.200.000 đ"]
    }
    st.table(data_tc)
    
    st.warning("⚠️ Lưu ý: Giá trên chưa bao gồm VAT và lệ phí thi sát hạch tại sân.")

    # 3. Hồ sơ cần chuẩn bị
    st.subheader("📋 Hồ sơ đăng ký cần chuẩn bị")
    st.write("- 01 Bản CMND/CCCD (không cần công chứng).")
    st.write("- 01 Giấy khám sức khỏe dành cho người lái xe.")
    st.write("- 06 Ảnh thẻ 3x4 nền xanh (chụp trực tiếp tại trung tâm).")

# --- TRANG: THI THỬ ---
elif menu == "Thi thử lý thuyết":
    st.title("✍️ Thi Thử Lý Thuyết")
    st.write("Tính năng này đang được kết nối với ngân hàng 600 câu hỏi...")
    # (Bạn có thể giữ code phần 600 câu ở đây nếu đã làm ở bước trước)

# --- TRANG: LIÊN HỆ ---
elif menu == "Liên hệ":
    st.title("📞 Thông Tin Liên Hệ")
    st.success("Hỗ trợ tư vấn trực tuyến 24/7")
    st.write("**Hotline/Zalo:** 0939.838.175")
    st.write("**Hỗ trợ viên:** Tuấn (Dịch vụ công trực tuyến)")
    st.write("**Địa chỉ:** Khóm 8, P7, Thành Phố Trà Vinh")

# Chân trang
st.markdown("---")
st.caption("© 2026 Phương Thúy - Tận tâm vì sự an toàn của bạn.")
