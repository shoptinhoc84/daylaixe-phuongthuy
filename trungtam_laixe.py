import streamlit as st
import pandas as pd

# Cấu hình trang
st.set_page_config(page_title="Dạy Lái Xe Phương Thúy", page_icon="🚗", layout="wide")

# --- PHẦN ĐẦU TRANG ---
[cite_start]st.title("🚗 HỆ THỐNG ĐÀO TẠO LÁI XE PHƯƠNG THÚY") [cite: 2]
[cite_start]st.write(f"📍 Địa chỉ: Khóm 8, P7, Thành Phố Trà Vinh") [cite: 3]

# --- MENU HÀNG NGANG (Thay thế cho Sidebar) ---
# Tạo 5 tab tương ứng với 5 mục chính
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 Giới thiệu", "💰 Bảng giá", "⏰ Giờ học", "✍️ Thi thử", "📞 Liên hệ"])

# --- NỘI DUNG TỪNG TAB ---

with tab1:
    st.header("Chào mừng bạn đến với trung tâm!")
    [cite_start]st.write("Chúng tôi xin gửi đến Quý khách các gói dịch vụ ôn luyện lý thuyết và hồ sơ đăng ký thi sát hạch lái xe máy và ô tô chất lượng nhất.") [cite: 8]
    st.image("https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?w=800")
    [cite_start]st.info("💡 Mẹo: Học viên sẽ được hướng dẫn mẹo ghi nhớ và phương pháp làm bài thi hiệu quả trên máy tính.") [cite: 15]

with tab2:
    [cite_start]st.header("💰 Bảng báo giá dịch vụ") [cite: 5]
    
    # Gói VIP
    [cite_start]st.subheader("I. Gói Ôn Luyện Lý Thuyết Chuyên Sâu (VIP)") [cite: 10]
    [cite_start]st.write("Dành cho học viên cần kèm riêng, đảm bảo kiến thức vững chắc để thi đỗ.") [cite: 10]
    data_vip = {
        [cite_start]"Hạng Mục": ["Ôn lý thuyết Xe máy (A1, A)", "Ôn lý thuyết Ô tô (B1, B2, C1)"], [cite: 10]
        [cite_start]"Mô Tả": ["Áp dụng cho các hạng A1, A", "Áp dụng cho các hạng B0.1, B1, B2, C1"], [cite: 10]
        [cite_start]"Đơn Giá (VNĐ)": ["2.000.000 đ", "2.500.000 đ"] [cite: 10]
    }
    st.table(data_vip)

    # Gói Tiêu Chuẩn
    [cite_start]st.subheader("II. Gói Tiêu Chuẩn (Học phí + Phí nộp hồ sơ)") [cite: 10]
    data_tc = {
        [cite_start]"Hạng Xe": ["Hạng A1 (Xe máy dưới 175cc)", "Hạng A (Mô tô trên 175cc)"], [cite: 10]
        [cite_start]"Học phí": ["240.000 đ", "1.400.000 đ"], [cite: 10]
        [cite_start]"Phí nộp hồ sơ": ["560.000 đ", "800.000 đ"], [cite: 10]
        [cite_start]"Trọn Gói (VNĐ)": ["800.000 đ", "2.200.000 đ"] [cite: 10]
    }
    st.table(data_tc)
    
    [cite_start]st.warning("⚠️ Lưu ý: Giá trên chưa bao gồm VAT, lệ phí thi sát hạch và lệ phí cấp bằng nộp tại sân thi.") [cite: 11, 19]

    st.subheader("📋 Hồ sơ cần chuẩn bị")
    [cite_start]st.write("* 01 Bản CMND/CCCD (không cần công chứng).") [cite: 21]
    [cite_start]st.write("* 01 Giấy khám sức khỏe dành cho người lái xe.") [cite: 22]
    [cite_start]st.write("* 06 Ảnh thẻ 3x4 nền xanh (chụp trực tiếp tại trung tâm).") [cite: 23]

with tab3:
    st.header("⏰ Thời gian học và làm việc")
    col1, col2 = st.columns(2)
    with col1:
        st.info("📅 **Ngày làm việc:** Từ Thứ 2 đến Thứ 7 hàng tuần.")
        st.success("🕒 **Giờ làm việc:** Sáng: 08:00 - 11:00 | Chiều: 13:00 - 17:00")
    with col2:
        [cite_start]st.warning("🎓 **Hình thức học:** Linh hoạt, sắp xếp theo lịch của học viên.") [cite: 14]
        [cite_start]st.write("Được cung cấp tài liệu, phần mềm ôn thi chuẩn của Cục đường bộ.") [cite: 16]

with tab4:
    st.header("✍️ Ôn tập 600 câu hỏi")
    st.write("Hệ thống thi thử đang được kết nối với dữ liệu câu hỏi...")
    # Phần này bạn có thể giữ code bộ câu hỏi trắc nghiệm đã làm ở bước trước

with tab5:
    st.header("📞 Thông tin liên hệ")
    [cite_start]st.write("**Giảng viên:** Phương Thúy") [cite: 2]
    [cite_start]st.write("**Hotline/Zalo:** 0939.838.175") [cite: 4, 24]
    [cite_start]st.write("**Địa chỉ:** Khóm 8, P7, Thành Phố Trà Vinh") [cite: 3]
    st.write("**Hỗ trợ:** Tư vấn dịch vụ công trực tuyến (Hộ chiếu, Lý lịch tư pháp, Đổi bằng lái).")

# --- CHÂN TRANG ---
st.markdown("---")
st.caption("© 2026 Trung Tâm Đào Tạo Lái Xe Phương Thúy - Uy tín và Tận tâm.")
