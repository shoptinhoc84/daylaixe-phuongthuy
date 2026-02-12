import streamlit as st

# Cấu hình trang
st.set_page_config(page_title="Dạy Lái Xe Phương Thúy", page_icon="🚗", layout="wide")

# --- PHẦN ĐẦU TRANG ---
st.title("🚗 HỆ THỐNG ĐÀO TẠO LÁI XE PHƯƠNG THÚY")
st.write("📍 Địa chỉ: Khóm 8, P7, Thành Phố Trà Vinh")

# --- MENU HÀNG NGANG ---
# Thêm tab "📖 Học Online" vào giữa
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏠 Giới thiệu", "💰 Bảng giá", "⏰ Giờ học", "📖 Học Online", "✍️ Thi thử", "📞 Liên hệ"
])

with tab1:
    st.header("Chào mừng bạn đến với trung tâm!")
    st.write("Cung cấp dịch vụ ôn luyện lý thuyết chuyên sâu và hồ sơ thi sát hạch uy tín.")
    st.image("https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?w=800")

with tab2:
    st.header("💰 Bảng báo giá dịch vụ")
    st.subheader("I. Gói Ôn Luyện Lý Thuyết Chuyên Sâu (VIP)")
    data_vip = {
        "Hạng Mục": ["Ôn lý thuyết Xe máy (A1, A)", "Ôn lý thuyết Ô tô (B1, B2, C1)"],
        "Đơn Giá": ["2.000.000 đ", "2.500.000 đ"]
    }
    st.table(data_vip)
    st.subheader("II. Gói Tiêu Chuẩn (Học phí + Hồ sơ)")
    data_tc = {
        "Hạng Xe": ["Hạng A1 (Xe máy)", "Hạng A (Mô tô PKL)"],
        "Trọn Gói": ["800.000 đ", "2.200.000 đ"]
    }
    st.table(data_tc)

with tab3:
    st.header("⏰ Thời gian học và làm việc")
    col1, col2 = st.columns(2)
    with col1:
        st.info("📅 **Ngày làm việc:** Thứ 2 đến Thứ 7 hàng tuần.")
        st.success("🕒 **Giờ làm việc:** Sáng: 08:00-11:00 | Chiều: 13:00-17:00")
    with col2:
        st.warning("🎓 **Hình thức học:** Linh hoạt theo lịch của học viên.")

# --- TAB MỚI: HỌC ONLINE ---
with tab4:
    st.header("📖 Phần Mềm Học Trực Tuyến")
    st.write("Học viên vui lòng chọn bộ câu hỏi tương ứng với hạng bằng đang thi:")
    
    col_xe_may, col_oto = st.columns(2)
    
    with col_xe_may:
        st.subheader("🛵 Hạng Xe Máy")
        st.write("Bộ đề ôn tập 250 câu hỏi luật giao thông đường bộ mới nhất.")
        # BẠN THAY LINK CỦA BẠN VÀO DÒNG DƯỚI ĐÂY
        st.link_button("Học 250 Câu Xe Máy", "https://duong-link-250-cau-cua-ban.com")
        
    with col_oto:
        st.subheader("🚗 Hạng Ô Tô")
        st.write("Bộ đề ôn tập 600 câu hỏi dành cho các hạng bằng B1, B2, C, D, E.")
        # BẠN THAY LINK CỦA BẠN VÀO DÒNG DƯỚI ĐÂY
        st.link_button("Học 600 Câu Xe Ô Tô", "https://duong-link-600-cau-cua-ban.com")

with tab5:
    st.header("✍️ Thi thử tại web")
    st.write("Tính năng thi thử nội bộ đang được phát triển...")

with tab6:
    st.header("📞 Thông tin liên hệ")
    st.write("**Chủ trung tâm:** Phương Thúy")
    st.write("**Hotline/Zalo:** 0939.838.175")
    st.write("**Địa chỉ:** Khóm 8, P7, Thành Phố Trà Vinh")

st.markdown("---")
st.caption("© 2026 Phương Thúy - Tận tâm và Uy tín.")
