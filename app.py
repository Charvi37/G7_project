
import streamlit as st
import pandas as pd

st.title("Student Record Management System")
st.write("Manage Student Records using CRUD Operations")

# Store student records
if "students" not in st.session_state:
    st.session_state.students = pd.DataFrame(
        columns=["Roll No", "Name", "Age", "Course", "Marks"]
    )

# Menu
menu = st.sidebar.selectbox(
    "Select Operation",
    ["Add Student", "View Students", "Update Student", "Delete Student"]
)

# CREATE
if menu == "Add Student":
    st.subheader("Add New Student")

    roll = st.number_input("Roll Number", min_value=1, step=1)
    name = st.text_input("Student Name")
    age = st.number_input("Age", min_value=1, step=1)
    course = st.text_input("Course")
    marks = st.number_input("Marks", min_value=0, max_value=100)

    if st.button("Add Student"):
        if name and course:
            if roll not in st.session_state.students["Roll No"].values:
                new_student = {
                    "Roll No": roll,
                    "Name": name,
                    "Age": age,
                    "Course": course,
                    "Marks": marks
                }

                st.session_state.students = pd.concat(
                    [st.session_state.students,
                     pd.DataFrame([new_student])],
                    ignore_index=True
                )

                st.success("Student Added Successfully!")
            else:
                st.error("Roll Number Already Exists!")
        else:
            st.warning("Please enter all details.")

# READ
elif menu == "View Students":
    st.subheader("All Student Records")

    st.dataframe(
        st.session_state.students,
        use_container_width=True
    )

# UPDATE
elif menu == "Update Student":
    st.subheader("Update Student Details")

    if not st.session_state.students.empty:

        roll = st.selectbox(
            "Select Roll Number",
            st.session_state.students["Roll No"]
        )

        index = st.session_state.students[
            st.session_state.students["Roll No"] == roll
        ].index[0]

        student = st.session_state.students.loc[index]

        name = st.text_input("Name", student["Name"])
        age = st.number_input("Age", value=int(student["Age"]))
        course = st.text_input("Course", student["Course"])
        marks = st.number_input("Marks", value=int(student["Marks"]))

        if st.button("Update Student"):
            st.session_state.students.loc[index] = [
                roll, name, age, course, marks
            ]

            st.success("Student Updated Successfully!")

    else:
        st.warning("No Student Records Found.")

# DELETE
elif menu == "Delete Student":
    st.subheader("Delete Student Record")

    if not st.session_state.students.empty:

        roll = st.selectbox(
            "Select Roll Number to Delete",
            st.session_state.students["Roll No"]
        )

        if st.button("Delete Student"):
            st.session_state.students = (
                st.session_state.students[
                    st.session_state.students["Roll No"] != roll
                ].reset_index(drop=True)
            )

            st.success("Student Deleted Successfully!")

    else:
        st.warning("No Student Records Found.")
