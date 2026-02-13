import streamlit as st
import os

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
    </style>
""", unsafe_allow_html=True)

# --- HÀM KIỂM TRA ẢNH AN TOÀN (CHỐNG SẬP WEB) ---
def hien_thi_anh(ten_file, caption=None):
    """Hàm này kiểm tra xem ảnh có tồn tại không trước khi hiển thị"""
    # Kiểm tra cả 2 trường hợp: nằm ngay bên ngoài hoặc nằm trong thư mục images
    duong_dan_1 = ten_file
    duong_dan_2 = f"images/{ten_file}"
    
    if os.path.exists(duong_dan_1):
        st.image(duong_dan_1, caption=caption, use_container_width=True)
    elif os.path.exists(duong_dan_2):
        st.image(duong_dan_2, caption=caption, use_container_width=True)
    else:
        # Nếu không thấy ảnh thì hiện khung cảnh báo thay vì làm sập web
        st.warning(f"⚠️ Chưa có ảnh: {ten_file} (Hãy upload file này lên cùng thư mục với code)")

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

# --- TAB 2: BẢNG GIÁ ---
with tab2:
    st.header("💰 Bảng Báo Giá Dịch Vụ")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("🔥 Gói VIP (Ôn Kỹ)")
        st.markdown("* **Xe máy (A1, A):** `2.000.000 đ`\n* **Ô tô (B1, B2, C1):** `2.500.000 đ`")
    with c2:
        st.subheader("✅ Gói Tiêu Chuẩn")
        st.markdown("* **Hạng A1:** `800.000 đ`\n* **Hạng A:** `2.200.000 đ`")

# --- TAB 3: LỊCH HỌC ---
with tab3:
    st.header("⏰ Thời Gian Làm Việc")
    st.info("📅 **Ngày làm việc:** Thứ 2 đến Thứ 7 hàng tuần.")
    st.write("☀️ **Sáng:** 08:00 - 11:00 | 🌤️ **Chiều:** 13:00 - 17:00")

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

# --- TAB 5: THI THỬ (Đã sửa lỗi sập web tại đây) ---
with tab5:
    st.header("✍️ Thi Thử Mô Phỏng")
    # Sử dụng hàm an toàn thay vì gọi trực tiếp
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
