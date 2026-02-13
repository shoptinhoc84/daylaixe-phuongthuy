import streamlit as st

# 1. Tạo 2 cột để chia giao diện (Xe máy bên trái, Ô tô bên phải)
col_xe_may, col_oto = st.columns(2)

# 2. Xử lý phần Xe Máy
with col_xe_may:
    st.subheader("🏍️ Hạng Xe Máy")
    st.write("Bộ đề ôn tập 250 câu hỏi lý thuyết thi lái xe máy.")
    # Link 250 câu xe máy của bạn
    st.link_button(
        "Học 250 Câu Xe Máy", 
        "https://daotaolaixehd.com.vn/bo-de-250-cau-ly-thuyet-thi-lai-xe-may",
        use_container_width=True, # Làm nút dài bằng chiều rộng cột cho đẹp
        type="primary"           # Tô màu nổi bật cho nút
    )

# 3. Xử lý phần Ô Tô
with col_oto:
    st.subheader("🚗 Hạng Ô Tô")
    st.write("Bộ đề ôn tập 600 câu hỏi dành cho các hạng bằng B1, B2, C, D, E.")
    # Link 600 câu ô tô của bạn
    st.link_button(
        "Học 600 Câu Xe Ô Tô", 
        "https://daotaolaixehd.com.vn/600-cau-hoc-ly-thuyet-thi-lai-xe",
        use_container_width=True,
        type="primary"
    )
