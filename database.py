import mysql.connector

# ---------------- DATABASE CONNECTION ----------------
conn = mysql.connector.connect(
    host="",
    user="",
    password="",
    database="attendance_system"
)

cursor = conn.cursor(buffered=True)

# ---------------- CHECK STUDENT EXISTS ----------------
def student_exists(enrollment):
    try:
        query = "SELECT id FROM students WHERE enrollment = %s"
        cursor.execute(query, (enrollment,))
        result = cursor.fetchone()

        if result:
            return True
        return False

    except Exception as e:
        print("Student Exists Error:", e)
        return False


# ---------------- INSERT STUDENT ----------------
def insert_student(enrollment, name):
    try:
        if student_exists(enrollment):
            print("Student already exists")
            return False

        query = """
        INSERT INTO students (enrollment, name)
        VALUES (%s, %s)
        """

        cursor.execute(query, (enrollment, name))
        conn.commit()

        return True

    except Exception as e:
        print("Student Insert Error:", e)
        return False


# ---------------- GET STUDENT NAME ----------------
def get_student_name(enrollment):
    try:
        query = """
        SELECT name
        FROM students
        WHERE enrollment = %s
        """

        cursor.execute(query, (enrollment,))
        result = cursor.fetchone()

        if result:
            return result[0]

        return None

    except Exception as e:
        print("Get Student Error:", e)
        return None


# ---------------- INSERT ATTENDANCE ----------------
def insert_attendance(enrollment, name, subject, date, time_stamp):
    try:
        query = """
        INSERT INTO attendance
        (enrollment, name, subject, date, time_stamp)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (
                enrollment,
                name,
                subject.lower().strip(),
                date,
                time_stamp
            )
        )

        conn.commit()

    except Exception as e:
        print("Attendance Insert Error:", e)


# ---------------- GET ATTENDANCE ----------------
def get_attendance(subject):
    try:
        query = """
        SELECT enrollment, name, date, time_stamp
        FROM attendance
        WHERE LOWER(subject) = %s
        ORDER BY date DESC, time_stamp DESC
        """

        cursor.execute(
            query,
            (subject.lower().strip(),)
        )

        return cursor.fetchall()

    except Exception as e:
        print("Get Attendance Error:", e)
        return []


# ---------------- GET ALL STUDENTS ----------------
def get_students():
    try:
        query = """
        SELECT enrollment, name
        FROM students
        ORDER BY enrollment
        """

        cursor.execute(query)

        return cursor.fetchall()

    except Exception as e:
        print("Get Students Error:", e)
        return []