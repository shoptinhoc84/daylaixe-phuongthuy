# --- CSS TÙY CHỈNH (Nâng cấp giao diện Menu Tab) ---
st.markdown("""
    <style>
        /* Import font chữ đẹp */
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Roboto', sans-serif;
        }
        
        /* Màu tiêu đề chính */
        h1, h2, h3 {
            color: #004e92;
            font-weight: 800;
        }

        /* --- TÙY CHỈNH MENU TAB (To - Rõ - Đẹp) --- */
        
        /* 1. Tăng kích thước chữ trong Tab */
        .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
            font-size: 1.3rem; /* Cỡ chữ to (khoảng 20px) */
            font-weight: 700;  /* Chữ đậm */
            padding-top: 5px;
            padding-bottom: 5px;
        }

        /* 2. Đổi màu chữ Tab mặc định sang Xanh Đậm */
        .stTabs [data-baseweb="tab-list"] button {
            color: #004e92; /* Màu xanh thương hiệu */
        }

        /* 3. Hiệu ứng khi rê chuột vào Tab (Đổi màu đỏ) */
        .stTabs [data-baseweb="tab-list"] button:hover {
            color: #ff4b4b; /* Màu đỏ nổi bật */
            background-color: #f0f8ff; /* Nền xanh nhạt nhẹ */
        }

        /* 4. Tab đang được chọn (Active) */
        .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
            border-bottom-color: #ff4b4b !important; /* Gạch chân màu đỏ */
            border-bottom-width: 3px !important;
        }

        /* --- CÁC THÀNH PHẦN KHÁC --- */
        .contact-box {
            background-color: #f0f8ff;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #004e92;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        /* Khung viền cho các bảng giá */
        [data-testid="stTable"] {
            font-size: 1.1rem; /* Chữ trong bảng giá cũng to hơn xíu */
        }
    </style>
""", unsafe_allow_html=True)
