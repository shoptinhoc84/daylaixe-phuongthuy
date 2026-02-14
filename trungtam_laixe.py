import streamlit as st
import os
import pandas as pd

# --- 1. CẤU HÌNH TRANG (Luôn để đầu tiên) ---
st.set_page_config(
    page_title="Dạy Lái Xe Phương Thúy",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. CSS TÙY CHỈNH (NÂNG CẤP: CHỐNG XUỐNG DÒNG TRÊN MOBILE) ---
st.markdown("""
    <style>
        /* Import font chữ chuẩn đẹp */
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Roboto', sans-serif;
        }
        
        h1, h2, h3 { color: #004e92; font-weight: 800; }

        /* --- CẤU HÌNH CHUNG CHO PC --- */
        .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
            font-size: 1.3rem; 
            font-weight: 700;
        }
        .stTabs [data-baseweb="tab-list"] button { color: #004e92; }
        .stTabs [data-baseweb="tab-list"] button:hover {
            color: #ff4b4b; background-color: #f0f8ff;
        }
        .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
            border-bottom-color: #ff4b4b !important; border-bottom-width: 4px !important;
        }
        
        /* Bảng giá trên PC */
        div[data-testid="stTable"] th {
            background-color: #004e92 !important; color: white !important; font-size: 1.2rem !important;
        }
        div[data-testid="stTable"] td { font-size: 1.15rem !important; }

        /* =============================================
           CẤU HÌNH RIÊNG CHO ĐIỆN THOẠI (MOBILE)
           ============================================= */
        @media only screen and (max-width: 768px) {
            
            /* 1. Menu Tabs: To, Rõ, Lướt ngang */
            .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
                font-size: 18px !important;
                white-space: nowrap; /* Không xuống dòng tên Tab */
            }
            .stTabs [data-baseweb="tab-list"] {
                overflow-x: auto;
                flex-wrap: nowrap;
                scrollbar-width: none; /* Ẩn thanh cuộn cho đẹp */
            }

            /* 2. Tiêu đề to rõ */
            h1 { font-size: 24px !important; text-align: center; }
            h2, h3 { font-size: 20px !important; }

            /* 3. Nội dung văn bản */
            div[class*="stMarkdown"] p, li, .stAlert {
                font-size: 16px !important;
                text-align: justify;
                line-height: 1.5 !important;
            }

            /* 4. XỬ LÝ BẢNG GIÁ (QUAN TRỌNG NHẤT) */
            div[data-testid="stTable"] {
                overflow-x: auto; /* Cho phép lướt ngang */
            }
            div[data-testid="stTable"] table {
                width: 100%;
            }
            div[data-testid="stTable"] th, div[data-testid="stTable"] td {
                white-space: nowrap !important; /* CẤM XUỐNG DÒNG */
                font-size: 16px !important;     /* Chữ to dễ đọc */
                padding: 10px 15px !important;  /* Giãn cách thoáng */
            }
            /* Tô màu cột đầu tiên để dễ nhìn làm mốc */
            div[data-testid="stTable"] td:first-child {
                font-weight: bold;
                color: #004e92;
                position: sticky;
                left: 0;
                background-color: #f9f9f9; /* Cố định cột đầu nếu cần, hoặc để thường */
            }
            
            /* 5. Nút bấm to ra */
            div[data-testid="stLinkButton"] > a {
                font-size: 18px !important;
                padding: 12px 0px !important;
                width: 100% !important; /* Nút bấm full chiều rộng */
                text-align: center !important;
            }
        }

        /* Khung liên hệ */
        .contact-box {
            background-color: #e8f4fd;
            padding: 20px;
            border-radius: 12px;
            border-left: 8px solid #004e92;
        }
    </style>
""", unsafe_allow_html=True)

# --- 3. HÀM KIỂM TRA ẢNH AN TOÀN ---
def hien_thi_anh(ten_file, caption=None):
    duong_dan_1 = ten_file
    duong_dan_2 = f"images/{ten_file}"
    if os.path.exists(duong_dan_1):
        st.image(duong_dan_1, caption=caption, use_container_width=True)
    elif os.path.exists(duong_dan_2):
        st.image(duong_dan_2, caption=caption, use_container_width=True)
    else:
        st.warning(f"⚠️ Chưa có ảnh: {ten_file}")

# --- 4. NỘI DUNG CHÍNH ---

st.title("🚗 HỆ THỐNG ĐÀO TẠO LÁI XE PHƯƠNG THÚY")
st.markdown("**📍 Địa chỉ:** Khóm 8, P7, Thành Phố Trà Vinh | **📞 Hotline:** 0939.838.175")
st.divider()

# Menu Chính
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏠 TRANG CHỦ", "💰 BẢNG GIÁ", "⏰ LỊCH HỌC", "📖 HỌC ONLINE", "✍️ THI THỬ", "📞 LIÊN HỆ"
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

# --- TAB 2: BẢNG GIÁ (FIX LỖI XUỐNG DÒNG) ---
with tab2:
    st.header("💰 Bảng Báo Giá Dịch Vụ")
    st.caption("Lưu ý: Giá trên chưa bao gồm VAT.")

    with st.container(border=True):
        st.subheader("🅰️ GÓI VIP: KÈM RIÊNG")
        st.info("💡 **Quyền lợi:** Học 1 kèm 1, học là đậu lý thuyết, tặng phần mềm.")
        
        # Dữ liệu bảng VIP - Viết gọn hơn để hiển thị đẹp
        df_vip = pd.DataFrame({
            "DỊCH VỤ": ["Ôn lý thuyết Xe máy (A1, A)", "Ôn lý thuyết Ô tô (B, C)"],
            "ĐỐI TƯỢNG": ["Học viên thi A1, A", "Học viên thi B1, B2, C1"],
            "CHI PHÍ": ["2.000.000 đ", "2.500.000 đ"]
        })
        st.table(df_vip)

    st.write("") 

    with st.container(border=True):
        st.subheader("🅱️ GÓI TIÊU CHUẨN (HỌC PHÍ + HỒ SƠ)")
        st.write("✅ **Bao gồm:** Học phí + Phí làm hồ sơ đăng ký thi.")
        
        df_std = pd.DataFrame({
            "HẠNG XE": ["Hạng A1 (< 175cc)", "Hạng A (> 175cc)"],
            "CHI TIẾT PHÍ": ["Học phí: 240k + Hồ sơ: 560k", "Học phí: 1.4tr + Hồ sơ: 800k"],
            "TRỌN GÓI": ["800.000 đ", "2.200.000 đ"]
        })
        st.table(df_std)
        
        st.error("⛔ **Lưu ý:** Gói này CHƯA bao gồm Lệ phí thi sát hạch & Lệ phí cấp bằng (Nộp tại sân thi).")

    with st.expander("📋 XEM HỒ SƠ CẦN CHUẨN BỊ", expanded=False):
        st.markdown("""
        * **01 Bản CMND/CCCD** (photo không cần công chứng).
        * **01 Giấy khám sức khỏe** lái xe (theo mẫu Bộ Y Tế).
        * **06 Ảnh thẻ 3x4 nền xanh** (Chụp miễn phí tại trung tâm).
        """)

# --- TAB 3: LỊCH HỌC ---
with tab3:
    st.header("⏰ Thời Gian Làm Việc")
    
    col_gio1, col_gio2 = st.columns(2)
    with col_gio1:
        st.info("**📅 NGÀY LÀM VIỆC**\n\nThứ 2 đến Thứ 7 hàng tuần\n(Chủ nhật nghỉ)")
    with col_gio2:
        st.warning("**🕒 GIỜ LÀM VIỆC**\n\n* **Sáng:** 08:00 - 11:00\n* **Chiều:** 13:00 - 17:00")
        
    st.success("🎓 **Đặc biệt:** Học viên đăng ký Gói VIP sẽ được sắp xếp lịch học linh động theo thời gian rảnh!")

# --- TAB 4: HỌC ONLINE ---
with tab4:
    st.header("📖 Ôn Luyện Trực Tuyến")
    with st.container(border=True):
        c_xm, c_oto = st.columns(2)
        with c_xm:
            st.subheader("🛵 Hạng Xe Máy")
            st.link_button("👉 Vào Học 250 Câu Xe Máy", "https://daotaolaixehd.com.vn/bo-de-250-cau-ly-thuyet-thi-lai-xe-may", type="primary", use_container_width=True)
        with c_oto:
            st.subheader("🚗 Hạng Ô Tô")
            st.link_button("👉 Vào Học 600 Câu Ô Tô", "https://daotaolaixehd.com.vn/600-cau-hoc-ly-thuyet-thi-lai-xe", type="primary", use_container_width=True)

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
        <p><b>☎️ Hotline/Zalo:</b> <span style="color:red; font-weight:bold; font-size:24px">0939.838.175</span></p>
    </div>
    """, unsafe_allow_html=True)
    st.map(latitude=9.9328, longitude=106.3444, zoom=14)

# --- FOOTER ---
st.markdown("---")
st.markdown("<div style='text-align: center; color: grey;'>© 2026 Hệ Thống Đào Tạo Lái Xe Phương Thúy</div>", unsafe_allow_html=True)
