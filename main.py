import streamlit as st
import sqlite3
import pandas as pd


# Function to initialize the database and create a course table
def create_course_table():
    conn = sqlite3.connect('course_db.db')
    c = conn.cursor()
    c.execute('''
              CREATE TABLE IF NOT EXISTS courses
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
              course_name TEXT,
              instructor TEXT)
              ''')
    conn.commit()
    conn.close()


# Function to insert a course into the database
def insert_course(course_name, instructor):
    conn = sqlite3.connect('course_db.db')
    c = conn.cursor()
    c.execute('INSERT INTO courses (course_name, instructor) VALUES (?, ?)', (course_name, instructor))
    conn.commit()
    conn.close()


# Function to display all courses from the database
def display_courses():
    conn = sqlite3.connect('course_db.db')
    df = pd.read_sql_query('SELECT * FROM courses', conn)
    conn.close()
    return df


def main():
    st.title("Online Course Management System")

    create_course_table()  # Initialize the database and create the course table

    page = st.sidebar.selectbox("Select a page:", ["Home", "Courses", "Add Course"])

    if page == "Home":
        st.write("Welcome to the Online Course Management System.")
    elif page == "Courses":
        st.header("Available Courses")
        courses_df = display_courses()
        st.write(courses_df)
    elif page == "Add Course":
        st.header("Add a New Course")
        course_name = st.text_input("Course Name")
        instructor = st.text_input("Instructor")

        if st.button("Add Course"):
            insert_course(course_name, instructor)
            st.success("Course added successfully!")
            st.text("Course Details:")
            st.write(f"Course Name: {course_name}")
            st.write(f"Instructor: {instructor}")


if __name__ == "__main__":
    main()
