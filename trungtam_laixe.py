import streamlit as st
import pandas as pd

# Cấu hình trang
st.set_page_config(page_title="Dạy Lái Xe Phương Thúy", page_icon="🚗", layout="wide")

# --- PHẦN ĐẦU TRANG ---
st.title("🚗 HỆ THỐNG ĐÀO TẠO LÁI XE PHƯƠNG THÚY")
st.write("📍 Địa chỉ: Khóm 8, P7, Thành Phố Trà Vinh")

# --- MENU HÀNG NGANG ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 Giới thiệu", "💰 Bảng giá", "⏰ Giờ học", "✍️ Thi thử", "📞 Liên hệ"])

with tab1:
    st.header("Chào mừng bạn đến với trung tâm!")
    st.write("Chúng tôi chuyên ôn luyện lý thuyết và làm hồ sơ sát hạch lái xe uy tín.")
    st.image("https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?w=800")
    st.info("💡 Học viên được kèm cặp sát sao, hướng dẫn mẹo ghi nhớ và làm bài trên máy tính.")

with tab2:
    st.header("💰 Bảng báo giá dịch vụ")
    # Gói VIP
    st.subheader("I. Gói Ôn Luyện Lý Thuyết Chuyên Sâu (VIP)")
    data_vip = {
        "Hạng Mục": ["Ôn lý thuyết Xe máy (A1, A)", "Ôn lý thuyết Ô tô (B1, B2, C1)"],
        "Đơn Giá": ["2.000.000 đ", "2.500.000 đ"]
    }
    st.table(data_vip)
    # Gói Tiêu Chuẩn
    st.subheader("II. Gói Tiêu Chuẩn (Học phí + Hồ sơ)")
    data_tc = {
        "Hạng Xe": ["Hạng A1 (Xe máy dưới 175cc)", "Hạng A (Mô tô trên 175cc)"],
        "Trọn Gói": ["800.000 đ", "2.200.000 đ"]
    }
    st.table(data_tc)
    st.warning("⚠️ Lưu ý: Giá trên chưa bao gồm lệ phí thi sát hạch nộp tại sân.")

with tab3:
    st.header("⏰ Thời gian học và làm việc")
    col1, col2 = st.columns(2)
    with col1:
        st.info("📅 **Ngày làm việc:** Thứ 2 đến Thứ 7 hàng tuần.")
        st.success("🕒 **Giờ làm việc:** Sáng: 08:00-11:00 | Chiều: 13:00-17:00")
    with col2:
        st.warning("🎓 **Hình thức học:** Linh hoạt theo lịch của học viên.")

with tab4:
    st.header("✍️ Ôn tập 600 câu hỏi")
    st.write("Vui lòng chọn số câu hỏi để bắt đầu thi thử.")
    # Ở đây bạn có thể thêm code load file CSV 600 câu như đã hướng dẫn trước đó

with tab5:
    st.header("📞 Thông tin liên hệ")
    st.write("**Chủ trung tâm:** Phương Thúy")
    st.write("**Hotline/Zalo:** 0939.838.175")
    st.write("**Hỗ trợ:** Hộ chiếu, Lý lịch tư pháp, Đổi bằng lái.")

st.markdown("---")
st.caption("© 2026 Phương Thúy - Tận tâm và Uy tín.")
