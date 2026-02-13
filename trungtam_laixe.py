import streamlit as st
import os
import pandas as pd # Thêm thư viện để hiển thị bảng đẹp hơn

# --- CẤU HÌNH TRANG ---
st.set_page_config(
    page_title="Dạy Lái Xe Phương Thúy",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS TÙY CHỈNH ---
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
        html, body, [class*="css"] { font-family: 'Roboto', sans-serif; }
        h1, h2, h3 { color: #004e92; font-weight: 700; }
        .contact-box { background-color: #f0f8ff; padding: 20px; border-radius: 10px; border-left: 5px solid #004e92; }
        .price-card { border: 1px solid #e0e0e0; padding: 15px; border-radius: 8px; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- HÀM KIỂM TRA ẢNH AN TOÀN ---
def hien_thi_anh(ten_file, caption=None):
    duong_dan_1 = ten_file
    duong_dan_2 = f"images/{ten_file}"
    if os.path.exists(duong_dan_1):
        st.image(duong_dan_1, caption=caption, use_container_width=True)
    elif os.path.exists(duong_dan_2):
        st.image(duong_dan_2, caption=caption, use_container_width=True)
    else:
        st.warning(f"⚠️ Chưa có ảnh: {ten_file}")

# --- HEADER ---
st.title("🚗 HỆ THỐNG ĐÀO TẠO LÁI XE PHƯƠNG THÚY")
st.markdown("**📍 Địa chỉ:** Khóm 8, P7, Thành Phố Trà Vinh | **📞 Hotline:** 0939.838.175")
st.divider()

# --- MENU CHÍNH ---
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏠 Trang Chủ", "💰 Bảng Giá", "⏰ Lịch Học", "📖 Học Online", "✍️ Thi Thử", "📞 Liên Hệ"
])

# --- TAB 1: TRANG CHỦ ---
with tab1:
    st.header("🌟 Vì sao chọn Phương Thúy?")
    st.write("Chúng tôi tự hào sở hữu cơ sở vật chất hiện đại và quy trình đào tạo bài bản nhất Trà Vinh.")
    
    col_img1, col_img2, col_img3 = st.columns(3)
    with col_img1:
        hien_thi_anh("1.jpg", caption="Sân Tập Đạt Chuẩn")
        st.info("Sân thi sát hạch mô tô rộng rãi, đúng quy chuẩn quốc gia.")
    with col_img2:
        hien_thi_anh("2.jpg", caption="Lý Thuyết Chuyên Sâu")
        st.success("Phòng học thoáng mát, giáo viên nhiệt tình hướng dẫn mẹo thi.")
    with col_img3:
        hien_thi_anh("3.jpg", caption="Phòng Máy Hiện Đại")
        st.warning("Hệ thống máy tính cấu hình cao, phần mềm thi sát hạch chuẩn.")

# --- TAB 2: BẢNG GIÁ (CẬP NHẬT MỚI THEO FILE PDF) ---
with tab2:
    st.header("💰 Bảng Báo Giá Dịch Vụ")
    st.caption("Lưu ý: Giá trên chưa bao gồm VAT (nếu cần xuất hóa đơn).")

    # Mục A: Gói VIP
    with st.container(border=True):
        st.subheader("🅰️ GÓI VIP: ÔN LUYỆN LÝ THUYẾT CHUYÊN SÂU")
        st.info("💡 **Quyền lợi:** Học kèm riêng 1-1, đảm bảo kiến thức vững chắc, cung cấp tài liệu & phần mềm chuẩn.")
        
        df_vip = pd.DataFrame({
            "Hạng Mục": ["Ôn lý thuyết Xe máy (A1, A)", "Ôn lý thuyết Ô tô (B1, B2, C1)"],
            "Đối Tượng": ["Học viên thi A1, A", "Học viên thi B1, B2, C1"],
            "Đơn Giá": ["2.000.000 đ", "2.500.000 đ"]
        })
        st.table(df_vip)

    # Mục B: Gói Tiêu Chuẩn
    with st.container(border=True):
        st.subheader("🅱️ GÓI TIÊU CHUẨN: HỌC PHÍ + HỒ SƠ")
        st.write("✅ **Bao gồm:** Học phí đào tạo (Lý thuyết + Thực hành) và Lệ phí hoàn thiện hồ sơ đăng ký thi.")
        
        df_std = pd.DataFrame({
            "Hạng Xe": ["Hạng A1 (Xe máy dưới 175cc)", "Hạng A (Mô tô PKL trên 175cc)"],
            "Chi Tiết Phí": ["Học phí: 240.000đ + Phí hồ sơ: 560.000đ", "Học phí: 1.400.000đ + Phí hồ sơ: 800.000đ"],
            "Tổng Trọn Gói": ["800.000 đ", "2.200.000 đ"]
        })
        st.table(df_std)
        
        st.warning("""
        ⛔ **Lưu ý quan trọng:** Gói tiêu chuẩn CHƯA BAO GỒM:
        * Lệ phí thi sát hạch.
        * Lệ phí cấp bằng lái xe.
        *(Hai khoản này học viên nộp trực tiếp tại sân thi theo quy định nhà nước)*
        """)

    # Mục Hồ sơ
    with st.expander("📋 HỒ SƠ CẦN CHUẨN BỊ (Xem chi tiết)", expanded=False):
        st.markdown("""
        1.  **01 Bản CMND/CCCD** (photo không cần công chứng).
        2.  **01 Giấy khám sức khỏe** dành cho người lái xe (theo mẫu Bộ Y Tế).
        3.  **06 Ảnh thẻ 3x4 nền xanh** (Được chụp trực tiếp tại trung tâm khi đăng ký).
        """)

# --- TAB 3: LỊCH HỌC ---
with tab3:
    st.header("⏰ Thời Gian Làm Việc")
    st.info("📅 **Ngày làm việc:** Thứ 2 đến Thứ 7 hàng tuần.")
    st.write("☀️ **Sáng:** 08:00 - 11:00 | 🌤️ **Chiều:** 13:00 - 17:00")
    st.write("Học viên học Lý thuyết chuyên sâu được sắp xếp lịch linh hoạt.")

# --- TAB 4: HỌC ONLINE ---
with tab4:
    st.header("📖 Ôn Luyện Trực Tuyến")
    with st.container(border=True):
        c_xm, c_oto = st.columns(2)
        with c_xm:
            st.subheader("🛵 Hạng Xe Máy")
            st.link_button("👉 Học 250 Câu Xe Máy", "https://daotaolaixehd.com.vn/bo-de-250-cau-ly-thuyet-thi-lai-xe-may", type="primary", use_container_width=True)
        with c_oto:
            st.subheader("🚗 Hạng Ô Tô")
            st.link_button("👉 Học 600 Câu Ô Tô", "https://daotaolaixehd.com.vn/600-cau-hoc-ly-thuyet-thi-lai-xe", type="primary", use_container_width=True)

# --- TAB 5: THI THỬ ---
with tab5:
    st.header("✍️ Thi Thử Mô Phỏng")
    hien_thi_anh("3.jpg", caption="Hệ thống thi thử tại trung tâm") 
    st.info("Học viên vui lòng đến phòng máy tại trung tâm để được thi thử trên phần mềm sát hạch chuẩn.")

# --- TAB 6: LIÊN HỆ ---
with tab6:
    st.header("📞 Liên Hệ Ghi Danh")
    st.markdown("""
    <div class="contact-box">
        <h3>👤 Trung Tâm Đào Tạo Lái Xe Phương Thúy</h3>
        <p><b>📍 Địa chỉ:</b> Khóm 8, P7, Thành Phố Trà Vinh</p>
        <p><b>☎️ Hotline/Zalo:</b> <span style="color:red; font-weight:bold; font-size:18px">0939.838.175</span></p>
    </div>
    """, unsafe_allow_html=True)
    st.map(latitude=9.9328, longitude=106.3444, zoom=14)

# --- FOOTER ---
st.markdown("---")
st.markdown("<div style='text-align: center; color: grey;'>© 2026 Hệ Thống Đào Tạo Lái Xe Phương Thúy</div>", unsafe_allow_html=True)
