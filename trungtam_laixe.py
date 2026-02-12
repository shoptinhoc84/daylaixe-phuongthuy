import streamlit as st

# Cấu hình trang
st.set_page_config(page_title="Học Lái Xe Online", page_icon="🚗")

# --- MENU BÊN TRÁI ---
st.sidebar.title("DANH MỤC")
menu = st.sidebar.selectbox("Chọn tính năng:", ["Giới thiệu", "Thi thử lý thuyết", "Liên hệ"])

# --- PHẦN 1: GIỚI THIỆU ---
if menu == "Giới thiệu":
    st.title("🚗 Trung Tâm Đào Tạo Lái Xe")
    st.write("Chào mừng bạn! Web này giúp bạn ôn tập 600 câu hỏi lý thuyết dễ dàng nhất.")
    st.image("https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?w=800")

# --- PHẦN 2: THI THỬ LÝ THUYẾT ---
elif menu == "Thi thử lý thuyết":
    st.title("✍️ Kiểm tra kiến thức")
    st.info("Hãy chọn đáp án đúng cho các câu hỏi dưới đây:")

    # Câu hỏi 1
    st.subheader("Câu 1: Khi gặp biển báo 'Cấm đi ngược chiều', bạn phải làm gì?")
    cau1 = st.radio("Chọn đáp án:", 
                    ["Đi chậm lại rồi đi tiếp", 
                     "Không được đi vào đường đó", 
                     "Được đi vào nếu là xe máy"], key="q1")
    
    # Câu hỏi 2
    st.subheader("Câu 2: Người lái xe phải làm gì khi điều khiển xe ra khỏi đường cao tốc?")
    cau2 = st.radio("Chọn đáp án:", 
                    ["Phải thực hiện chuyển dần sang làn đường bên phải", 
                     "Phanh gấp để rẽ", 
                     "Quay đầu xe lại"], key="q2")

    # Nút chấm điểm
    if st.button("Nộp bài và xem kết quả"):
        score = 0
        if cau1 == "Không được đi vào đường đó": score += 5
        if cau2 == "Phải thực hiện chuyển dần sang làn đường bên phải": score += 5
        
        st.write(f"### Tổng điểm của bạn: {score}/10")
        if score == 10:
            st.balloons()
            st.success("Xuất sắc! Bạn đã nắm vững kiến thức.")
        else:
            st.warning("Bạn cần ôn tập thêm một chút nhé!")

# --- PHẦN 3: LIÊN HỆ ---
elif menu == "Liên hệ":
    st.title("📞 Hỗ trợ học viên")
    st.write("Nếu có thắc mắc về hồ sơ hoặc lịch thi, hãy liên hệ:")
    st.write("- **Zalo:** 0939.838.175")
    st.success("Hỗ trợ trực tuyến 24/7")
