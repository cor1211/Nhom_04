import mysql.connector

      
class StudentModel:
   def __init__(self):
      self.connection = mysql.connector.connect(
         host = 'localhost',
         user = 'root',
         password = '123456',
         database='StudentManagement',
         port=3306
      )
      self.cursor = self.connection.cursor()
      
   def get_all_students(self):
      query = """Select Student.student_id,Student.student_name, 
      Student.student_gender,Student.student_birth, 
      Student.student_generation, Major.major_name, 
      Class.class_name,
      sum(
       Case
      When subject_student.score_regular*0.2 + subject_student.score_midterm *0.3+subject_student.score_final*0.5 >= 8.5 then 4
      When subject_student.score_regular*0.2 + subject_student.score_midterm *0.3+subject_student.score_final*0.5 >= 8 then 3.5
      When subject_student.score_regular*0.2 + subject_student.score_midterm *0.3+subject_student.score_final*0.5 >= 7 then 3
      When subject_student.score_regular*0.2 + subject_student.score_midterm *0.3+subject_student.score_final*0.5 >= 6.5 then 2.5
      When subject_student.score_regular*0.2 + subject_student.score_midterm *0.3+subject_student.score_final*0.5 >= 5.5 then 2
      When subject_student.score_regular*0.2 + subject_student.score_midterm *0.3+subject_student.score_final*0.5 >= 5 then 1.5
      When subject_student.score_regular*0.2 + subject_student.score_midterm *0.3+subject_student.score_final*0.5 >= 4 then 1
      else 0
      end * subject.subject_credit)/sum(subject.subject_credit) as gpa
      from Student
      Join Major on Student.major_id = Major.major_id
      Join Class on Student.class_id = Class.class_id
      LEFT JOIN SUBJECT_STUDENT ON SUBJECT_STUDENT.student_id = Student.student_id
      LEFT JOIN SUBJECT ON SUBJECT.subject_id = Subject_Student.Subject_id
      
      Group by Student.student_id
      """
      self.cursor.execute(query)
      students = self.cursor.fetchall()
      return students
   
   def get_student_by_id(self,student_id):
      query = f"""Select student_id, student_name, student_birth, student_address,
      student_cccd,student_phone, student_email, student_gender,student_generation, 
      student_image, Major.major_name, Class.class_name, Department.department_name 
            from Student 
            Join Major on Student.major_id = Major.major_id
            Join Class on Student.class_id = Class.class_id
            Join Department on Department.department_id = Class.department_id
            Where Student.student_id = {student_id}"""
      self.cursor.execute(query)
      student = self.cursor.fetchall()
      return student[0]
   
   def get_department_name(self):
      query = """Select department_name from Department"""
      self.cursor.execute(query)
      department_name = self.cursor.fetchall()
      return department_name
   
   def get_class_name(self):
      query = """Select class_name from Class"""
      self.cursor.execute(query)
      class_name = self.cursor.fetchall()
      return class_name
   
   def get_major_name(self):
      query = """Select major_name from Major"""
      self.cursor.execute(query)
      major_name = self.cursor.fetchall()
      return major_name
   
   def get_student_name_by_id(self,tuple_student_id):
      cursor = self.connection.cursor()
      query = """
               SELECT student_name
               FROM Student
               WHERE student_id = %s"""
      cursor.execute(query,tuple_student_id)
      student_name = cursor.fetchall()
      cursor.close()
      return student_name
   
   def get_subject_name_credit_by_id(self,tuple_subject_id):
      cursor = self.connection.cursor()
      query = """SELECT subject_name, subject_credit FROM SUBJECT
                  WHERE subject_id = %s"""
      cursor.execute(query,tuple_subject_id)
      subject_name_credit = cursor.fetchall()
      cursor.close()
      return subject_name_credit
   
   def get_gpa(self):
      queru = """
      select
      sum(
      Case
      When subject_student.score_regular*0.2 + subject_student.score_midterm *0.3+subject_student.score_final*0.5 >= 8.5 then 4
      When subject_student.score_regular*0.2 + subject_student.score_midterm *0.3+subject_student.score_final*0.5 >= 8 then 3.5
      When subject_student.score_regular*0.2 + subject_student.score_midterm *0.3+subject_student.score_final*0.5 >= 7 then 3
      When subject_student.score_regular*0.2 + subject_student.score_midterm *0.3+subject_student.score_final*0.5 >= 6.5 then 2.5
      When subject_student.score_regular*0.2 + subject_student.score_midterm *0.3+subject_student.score_final*0.5 >= 5.5 then 2
      When subject_student.score_regular*0.2 + subject_student.score_midterm *0.3+subject_student.score_final*0.5 >= 5 then 1.5
      When subject_student.score_regular*0.2 + subject_student.score_midterm *0.3+subject_student.score_final*0.5 >= 4 then 1
      else 0
      end *subject.subject_credit)/sum(subject.subject_credit) as gpa
      from Student
      left join subject_student on subject_student.student_id = student.student_id
      left join subject on subject.subject_id = subject_student.subject_id
      group by student.student_id
      """
      self.cursor.execute(queru)
      gpa_each_student = self.cursor.fetchall()
      return gpa_each_student
   
   def get_id_by_name(self,talbe_name,name):
      cursor = self.connection.cursor()
      query = f"""Select {talbe_name}.{talbe_name}_id
               From {talbe_name}
               Where {talbe_name}_name = '{name}'
               """
      cursor.execute(query)
      id = cursor.fetchone()
      cursor.close()
      return id

   def get_subject_by_id_semester(self,tuple_id_semester):
      cursor = self.connection.cursor()
      query = """
      Select main.subject_id, main.subject_name, 
      main.ss_semester,main.subject_credit,
      main.score_regular, main.score_midterm, main.score_final,main.dtb,
      Case
      When main.dtb >= 8.5 then 'A'
      When main.dtb >= 8.0 then 'B+'
      When main.dtb >= 7.0 then 'B'
      When main.dtb >= 6.5 then 'C+'
      When main.dtb >= 5.5 then 'C'
      When main.dtb >= 5 then 'D+'
      When main.dtb >= 4 then 'D'
      else 'F'
      end as Xeploai
      From
      (select student.student_id,subject.subject_id, subject.subject_name, 
      subject.subject_credit,subject_student.ss_semester,
      subject_student.score_regular, subject_student.score_midterm,
      subject_student.score_final,
      (subject_student.score_regular*0.2+ subject_student.score_midterm*0.3+ subject_student.score_final*0.5) as dtb
      From Student
      Join Subject_Student on Subject_Student.student_id = student.student_id
      Join Subject on Subject.Subject_id = Subject_student.subject_id) as main
      WHERE main.student_id = %s
      """
   
      if tuple_id_semester[1] == 'Tất cả':
         cursor.execute(query,(tuple_id_semester[0],))
      else:
         query+=""" and main.ss_semester = %s; """
         cursor.execute(query,tuple_id_semester)
      subject = cursor.fetchall()
      cursor.close()
      return subject

   def add_student(self,tuple_student):
      query = f"""Insert into Student
      values
      {tuple_student}
      """
      print(query)
      self.cursor.execute(query)
      self.connection.commit()
      
   def update_student(self,tuple_student):
      cursor = self.connection.cursor()
      query = """
      Update Student
      Set student_name = %s, student_birth = %s, student_address = %s,
      student_cccd = %s, student_phone = %s, student_email = %s, 
      student_gender = %s, student_generation = %s, student_image = %s,
      class_id = %s, major_id = %s
      Where student_id = %s
      """
      cursor.execute(query,tuple_student)
      self.connection.commit()
      cursor.close()
   
   def delete_student(self,student_id):
      cursor = self.connection.cursor()
      query = """DELETE FROM STUDENT
                  WHERE student_id = %s
                  """
      cursor.execute(query,student_id)
      self.connection.commit()
      cursor.close()
   
   def get_id_subject(self):
      cursor = self.connection.cursor()
      query = """SELECT subject_id FROM SUBJECT"""
      cursor.execute(query)
      subjects_id = cursor.fetchall()
      cursor.close()
      return subjects_id
   
   def add_subject_student(self,tuple_new_subject_student):
      cursor = self.connection.cursor()
      query = f"""
      INSERT INTO SUBJECT_STUDENT
      VALUES 
      {tuple_new_subject_student}
      """
      cursor.execute(query)
      self.connection.commit()
      cursor.close()
      
   def get_subject_student(self,tuple_subject_student_semester):
      cursor = self.connection.cursor()
      query = """Select * from Subject_student
                  WHERE subject_id = %s
                  and student_id = %s
                  and ss_semester = %s;"""
      cursor.execute(query,tuple_subject_student_semester)
      result = cursor.fetchall()
      cursor.close()
      return result
   
   def update_subject_student(self,tuple_subject_student):
      cursor = self.connection.cursor()
      query = """UPDATE SUBJECT_STUDENT
      SET score_regular = %s,
      score_midterm = %s, 
      score_final = %s
      WHERE Subject_id = %s and
      student_id = %s and
      ss_semester = %s;
      """
      cursor.execute(query, tuple_subject_student)
      self.connection.commit()
      cursor.close()
   
   def delete_subject_student(self,tuple_subject_student):
      cursor = self.connection.cursor()
      query = """DELETE FROM SUBJECT_STUDENT
                  WHERE subject_id = %s and
                        student_id = %s and
                        ss_semester = %s;"""
      cursor.execute(query,tuple_subject_student)
      self.connection.commit()
      cursor.close()
      
   def close(self):
      self.cursor.close()
      self.connection.close()

