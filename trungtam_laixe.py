import streamlit as st

# --- CẤU HÌNH TRANG ---
st.set_page_config(
    page_title="Dạy Lái Xe Phương Thúy",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS TÙY CHỈNH (Làm đẹp font chữ và màu sắc) ---
st.markdown("""
    <style>
        /* Import font chữ đẹp */
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Roboto', sans-serif;
        }
        
        /* Màu tiêu đề chính */
        h1, h2, h3 {
            color: #004e92; /* Màu xanh dương đậm chuyên nghiệp */
            font-weight: 700;
        }
        
        /* Tùy chỉnh Tabs cho nổi bật */
        .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
            font-size: 1.1rem;
            font-weight: 600;
        }
        
        /* Khung viền cho ảnh */
        img {
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        /* Nổi bật thông tin liên hệ */
        .contact-box {
            background-color: #f0f8ff;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #004e92;
        }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("🚗 HỆ THỐNG ĐÀO TẠO LÁI XE PHƯƠNG THÚY")
st.markdown("**📍 Địa chỉ:** Khóm 8, P7, Thành Phố Trà Vinh | **📞 Hotline:** 0939.838.175")
st.divider()

# --- MENU CHÍNH ---
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏠 Trang Chủ", 
    "💰 Bảng Giá", 
    "⏰ Lịch Học", 
    "📖 Học Online", 
    "✍️ Thi Thử", 
    "📞 Liên Hệ"
])

# --- TAB 1: TRANG CHỦ (Logic mới với 3 ảnh thực tế) ---
with tab1:
    st.header("🌟 Vì sao chọn Phương Thúy?")
    st.write("Chúng tôi tự hào sở hữu cơ sở vật chất hiện đại và quy trình đào tạo bài bản nhất Trà Vinh.")
    
    # Chia 3 cột để show 3 ảnh
    col_img1, col_img2, col_img3 = st.columns(3)
    
    with col_img1:
        # Ảnh 1: Sân tập
        try:
            st.image("1.jpg", use_container_width=True)
            st.info("**Sân Tập Đạt Chuẩn**\n\nSân thi sát hạch mô tô rộng rãi, đúng quy chuẩn quốc gia giúp học viên tự tin cầm lái.")
        except:
            st.error("Thiếu file 1.jpg")

    with col_img2:
        # Ảnh 2: Lớp học
        try:
            st.image("2.jpg", use_container_width=True)
            st.success("**Lý Thuyết Chuyên Sâu**\n\nPhòng học thoáng mát, giáo viên nhiệt tình hướng dẫn mẹo thi và luật giao thông.")
        except:
            st.error("Thiếu file 2.jpg")

    with col_img3:
        # Ảnh 3: Phòng máy
        try:
            st.image("3.jpg", use_container_width=True)
            st.warning("**Phòng Máy Hiện Đại**\n\nHệ thống máy tính cấu hình cao, cài đặt phần mềm thi sát hạch giống 100% khi thi thật.")
        except:
            st.error("Thiếu file 3.jpg")

# --- TAB 2: BẢNG GIÁ ---
with tab2:
    st.header("💰 Bảng Báo Giá Dịch Vụ")
    
    col_price1, col_price2 = st.columns(2)
    
    with col_price1:
        st.subheader("🔥 Gói VIP (Ôn Kỹ)")
        st.markdown("""
        *Dành cho học viên cần hỗ trợ tối đa về lý thuyết*
        * **Xe máy (A1, A):** `2.000.000 đ`
        * **Ô tô (B1, B2, C1):** `2.500.000 đ`
        """)
    
    with col_price2:
        st.subheader("✅ Gói Tiêu Chuẩn")
        st.markdown("""
        *Bao gồm học phí + Hồ sơ thi*
        * **Hạng A1 (Xe máy):** `800.000 đ`
        * **Hạng A (Mô tô PKL):** `2.200.000 đ`
        """)

# --- TAB 3: LỊCH HỌC ---
with tab3:
    st.header("⏰ Thời Gian Làm Việc")
    st.info("📅 **Ngày làm việc:** Thứ 2 đến Thứ 7 hàng tuần.")
    
    c1, c2 = st.columns(2)
    with c1:
        st.write("☀️ **Sáng:** 08:00 - 11:00")
    with c2:
        st.write("🌤️ **Chiều:** 13:00 - 17:00")
        
    st.caption("*Lịch học thực hành và lý thuyết có thể linh động theo thời gian rảnh của học viên.*")

# --- TAB 4: HỌC ONLINE (Code đã sửa link) ---
with tab4:
    st.header("📖 Ôn Luyện Trực Tuyến")
    st.write("Truy cập kho đề thi chuẩn của Tổng Cục Đường Bộ ngay tại nhà:")
    
    # Tạo style khung viền cho phần học
    with st.container(border=True):
        col_xe_may, col_oto = st.columns(2)
        
        # Cột Xe Máy
        with col_xe_may:
            st.subheader("🛵 Hạng Xe Máy (A1, A2)")
            st.write("Bộ đề 250 câu hỏi luật giao thông.")
            st.link_button(
                "👉 Vào Học Ngay (250 Câu)", 
                "https://daotaolaixehd.com.vn/bo-de-250-cau-ly-thuyet-thi-lai-xe-may",
                type="primary",
                use_container_width=True
            )
            
        # Cột Ô Tô
        with col_oto:
            st.subheader("🚗 Hạng Ô Tô (B1, B2, C)")
            st.write("Bộ đề 600 câu hỏi luật giao thông.")
            st.link_button(
                "👉 Vào Học Ngay (600 Câu)", 
                "https://daotaolaixehd.com.vn/600-cau-hoc-ly-thuyet-thi-lai-xe",
                type="primary",
                use_container_width=True
            )

# --- TAB 5: THI THỬ ---
with tab5:
    st.header("✍️ Thi Thử Mô Phỏng")
    st.image("3.jpg", caption="Hệ thống thi thử tại trung tâm", width=600)
    st.info("Hiện tại tính năng thi thử trực tiếp trên web đang được cập nhật. Học viên vui lòng đến phòng máy tại trung tâm để được thi thử trên phần mềm sát hạch chuẩn.")

# --- TAB 6: LIÊN HỆ ---
with tab6:
    st.header("📞 Liên Hệ Ghi Danh")
    
    # Sử dụng HTML/CSS để tạo hộp thông tin đẹp
    st.markdown("""
    <div class="contact-box">
        <h3>👤 Trung Tâm Đào Tạo Lái Xe Phương Thúy</h3>
        <p><b>📍 Địa chỉ:</b> Khóm 8, P7, Thành Phố Trà Vinh</p>
        <p><b>☎️ Hotline/Zalo:</b> <span style="color:red; font-weight:bold; font-size:18px">0939.838.175</span></p>
        <p><b>📧 Email:</b> (Đang cập nhật)</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.map(latitude=9.9328, longitude=106.3444, zoom=14) # Ví dụ tọa độ Trà Vinh (Cần chỉnh chính xác nếu có)

# --- FOOTER ---
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: grey;'>© 2026 Hệ Thống Đào Tạo Lái Xe Phương Thúy - Uy Tín Tạo Nên Thương Hiệu</div>", 
    unsafe_allow_html=True
)
