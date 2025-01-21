import time
import requests
import streamlit as st

BACKEND_URL = "http://localhost:5000"
TABLE = "attractions"
# TABLE = "attractions_redis"

class TravelAttraction:
    def __init__(self):
        self.main_page()

    def get_attraction(self):
        st.header('Travel Attraction ', divider = "gray")
        response = requests.get(f"{BACKEND_URL}/{TABLE}")
        if response.status_code == 200:
            destinations = response.json()

            columns_per_row = 3

            for index in range(0, len(destinations), columns_per_row):
                cols = st.columns(columns_per_row)  # columns_per_row 만큼의 열 생성
                for i in range(columns_per_row):
                    with cols[i]:
                        # 배열의 인덱스가 destinations 리스트의 길이를 넘지 않도록 검사
                        if index + i < len(destinations):
                            dest = destinations[index + i]
                            st.subheader(dest['name'])
                            st.write('Location:', dest['location'])
                            st.write('Average Rating:', dest['average_rating'])
                            if dest['photo_url']:  # 사진 URL이 있으면 표시
                                st.image(dest['photo_url'])
                st.markdown("---")

    def put_attraction(self):
        st.subheader("Add New Travel Attraction", divider = "gray")
        get_placeholder = st.container()

        with get_placeholder.container():
            name = st.text_input("Name")
            location = st.text_input("Location")
            average_rating = st.number_input("Average Rating", min_value=0.0, max_value=5.0, step=0.1)
            photo_url = st.text_input("Photo URL")
            

            if st.button("Create Attraction", use_container_width=True):
                # Flask 서버에 여행지 정보를 POST 요청으로 보냄
                response = requests.post(f"{BACKEND_URL}/attractions", 
                                            json={
                                                'name': name,
                                                'location': location,
                                                'average_rating': average_rating,
                                                'photo_url': photo_url})
                if response.status_code == 201:
                    st.success('Travel attraction added successfully')
                    st.rerun()
                else:
                    st.error('An error occurred while adding the travel attraction')

    def delete_attraction(self):
        st.subheader("Delete a Travel Attraction", divider = "gray")

        # 기존 관광지 목록을 불러옴
        response = requests.get(f'{BACKEND_URL}/{TABLE}')
        attractions = response.json()
        delete_placeholder = st.container()

        with delete_placeholder.container():
            # 관광지 이름만으로 구성된 리스트
            attraction_names = [attraction['name'] for attraction in attractions]

            if 'selected_image' not in st.session_state:
                st.session_state.selected_image = attraction_names[0]

            def update_select():
                st.session_state.selected_image = st.session_state.image_select

            # 사용자가 삭제할 관광지 이름을 선택할 수 있는 선택 상자
            st.selectbox('Select an attraction to delete', attraction_names, on_change=update_select, key='image_select')
            selected_name = st.session_state.selected_image

            # 선택된 관광지의 모든 정보를 보여줌
            if selected_attraction := next((attraction for attraction in attractions if attraction['name'] == selected_name), None):
                st.image(selected_attraction['photo_url'], use_column_width='always')

            # 삭제 버튼
            if st.button("Delete Attraction", use_container_width=True):
                # 선택된 관광지 ID를 사용하여 삭제 요청
                delete_response = requests.delete(f'http://localhost:5000/attractions/{selected_attraction["id"]}')
                if delete_response.status_code == 200:
                    st.success('Travel attraction deleted successfully!')
                    st.rerun()  # 정보 삭제 후 페이지 다시 실행
                else:
                    st.error('An error occurred while deleting the attraction.')

    def update_attraction(self):
        st.subheader("Update a Travel Attraction", divider = "gray")

        # 기존 관광지 목록을 불러옴
        response = requests.get(f'{BACKEND_URL}/{TABLE}')
        attractions = response.json()
        update_placeholder = st.empty()

        # with st.form("update_attraction_form"):
        with update_placeholder.container():
            attraction_names = [attraction['name'] for attraction in attractions]

            if 'selected_name' not in st.session_state:
                st.session_state.selected_name = attraction_names[0]

            def update_select():
                st.session_state.selected_name = st.session_state.name_select
            
            st.selectbox('Select an attraction name to update', attraction_names, on_change=update_select, key='name_select')
            selected_name = st.session_state.selected_name
            selected_attraction = next((attraction for attraction in attractions if attraction['name'] == selected_name), None)

            if selected_attraction is not None:
                name = selected_attraction["name"]
                selected_id = selected_attraction["id"]
                location = st.text_input("Location", value=selected_attraction["location"])
                average_rating = st.text_input("Average Rating", value=selected_attraction["average_rating"])
                photo_url = st.text_input("Photo URL", value=selected_attraction["photo_url"])

            if st.button("update_attraction_button", use_container_width=True):
                update_data = {
                    "name" : name,
                    "location": location,
                    "average_rating": average_rating,
                    "photo_url": photo_url,
                    "attraction_id" : selected_id
                }
                response = requests.put(f"{BACKEND_URL}/attractions/{selected_id}", json=update_data)
                if response.status_code == 200:
                    st.success("Attraction updated successfully!")
                else:
                    st.error("An error occurred while updating the attraction.")
                # st.rerun()

    def main_page(self):
        st.title("Trip Advisor")
        
        start_time = time.time()
        self.get_attraction()
        end_time = time.time()
        result = end_time - start_time
        print(f"get_attraction time: {result} 초")

        
        col1, col2, col3 = st.columns(3)

        # 첫 번째 컬럼 (관광지` 추가 기능)
        with col1:
            start_time = time.time()
            self.put_attraction()
            end_time = time.time()
            result = end_time - start_time
            print(f"put_attraction time: {result} 초")

        # 두 번째 컬럼 (관광지 삭제 기능)
        with col2:
            start_time = time.time()
            self.update_attraction()
            end_time = time.time()
            result = end_time - start_time
            print(f"update_attraction time: {result} 초")

        # 세 번째 컬럼 (관광지 수정 기능)
        with col3:
            start_time = time.time()
            self.delete_attraction()
            end_time = time.time()
            result = end_time - start_time
            print(f"delete_attraction time: {result} 초")
            print("---")
        st.subheader("")

