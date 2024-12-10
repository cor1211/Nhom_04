from views import LoginView,AdminDashboardView,StudentView,SubjectView, TopLeveSubjectlView
from model import StudentModel
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox
import pandas as pd
from fpdf import FPDF
import os

class AppController:
   def __init__(self,root):
      self.root = root
      self.root.title('Student Management')
      self.root.geometry("1280x800")
      self.root.resizable(True,True)
      # Cấu hình khung chính để co giãn
      self.root.grid_rowconfigure(0, weight=1)
      self.root.grid_columnconfigure(0, weight=1)
      
      
      # Model Student
      self.student_model = StudentModel()
      
      self.show_login_view()
      # self.show_admin_dashboard_view('<Button-1>')
      # self.show_student_view('<Button-1>')
      
   def show_login_view(self):
      self.clear_frame()
      self.login_view = LoginView(self.root)
      self.login_view.grid(row=0,column=0)
      self.login_view.configure(width=400,height=200) 
      self.login_view.btn_login.bind('<Button-1>',self.show_admin_dashboard_view)
      
   def show_admin_dashboard_view(self,event):
      self.clear_frame()
      self.admin_dashboard_view = AdminDashboardView(self.root)
      self.admin_dashboard_view.grid(row=0,column=0)      
      self.admin_dashboard_view.configure(width=400,height=200)
      # Listener Event
      self.admin_dashboard_view.btn_students.bind('<Button-1>',self.show_student_view)
      self.admin_dashboard_view.btn_result.bind('<Button-1>',self.show_subject_view)
   
   def show_student_view(self,event):
      # self.clear_frame()
      self.student_view = StudentView(self.root)
      self.student_view.grid(row=0,column=0,sticky='nsew')
      self.student_view.configure(width=400,height=200)
      
      # Event Listener
      self.student_view.tree.bind('<<TreeviewSelect>>',self.on_select_student_view)
      self.student_view.btn_showall.bind('<Button-1>',self.get_all_students)
      self.student_view.btn_select_image.bind('<Button-1>',self.on_select_image)
      self.student_view.student_btn_add.bind('<Button-1>',self.add_student)
      self.student_view.student_btn_update.bind('<Button-1>',self.update_student)
      self.student_view.student_btn_delete.bind('<Button-1>',self.delete_student)
      self.student_view.btn_export.bind('<Button-1>',self.export_file_student)
      
      
      # Add value combobox_department
      department_name = self.student_model.get_department_name()
      department_name = [i[0] for i in department_name]
      self.student_view.combo_department['values'] = department_name
      self.student_view.combo_department.current(0)
      
      # Add value combobox_class
      class_name = self.student_model.get_class_name()
      class_name = [i[0] for i in class_name]
      self.student_view.combo_class['values'] = class_name
      self.student_view.combo_class.current(0)
      
      # Add value combobox_major
      major_name = self.student_model.get_major_name()
      major_name = [i[0] for i in major_name]
      self.student_view.combo_major['values'] = major_name
      self.student_view.combo_major.current(0)
   
   def show_subject_view(self,event):
      # self.clear_frame()
      self.subject_view = SubjectView(self.root)
      self.subject_view.grid(row=0,column=0,sticky='nsew')
      self.subject_view.configure(width=400,height=200)
      
      # Eveny Listener
      self.subject_view.btn_find.bind('<Button-1>',self.get_subject_by_id_semester)
      self.subject_view.btn_add_subject.bind('<Button-1>',self.show_form_subject_add)
      self.subject_view.btn_update_subject.bind('<Button-1>',self.show_form_subject_update)
      self.subject_view.btn_delete_subject.bind('<Button-1>',self.delete_subject_student)
      self.subject_view.btn_export.bind('<Button-1>',self.export_file_subject)
      self.subject_view.tree.bind('<<TreeviewSelect>>',self.on_selected_subject_student_view)
   
   def show_form_subject_add(self,event):
      self.form_subject_view = TopLeveSubjectlView(self.subject_view)
      self.form_subject_view.geometry('800x500')
      
      # Event Listener
      self.form_subject_view.combo_subject_id.bind('<<ComboboxSelected>>',self.set_value_by_subject_id)
      self.form_subject_view.ent_student_id.bind('<FocusOut>',self.set_value_by_student_id)
      self.form_subject_view.btn_add_confirm.bind('<Button-1>',self.add_subject_student)
      self.form_subject_view.btn_add_cancel.bind('<Button-1>',lambda event:self.form_subject_view.destroy())
      # Set value in combobox
         # Subject_id
      subjects_id = self.student_model.get_id_subject()
      subjects_id = [i[0] for i in subjects_id]
      self.form_subject_view.combo_subject_id['values'] =subjects_id
      self.form_subject_view.combo_subject_id.current(0)
       
   def show_form_subject_update(self,event):
      self.form_subject_view = TopLeveSubjectlView(self.subject_view)
      self.form_subject_view.geometry('800x500')
      
      # Event Listerner
      self.form_subject_view.btn_add_confirm.bind('<Button-1>',self.update_subject_student)
      self.form_subject_view.btn_add_cancel.bind('<Button-1>',lambda event:self.form_subject_view.destroy())
      
      # Set value in form
      self.form_subject_view.title1.config(text='Sửa học phần')
      values = self.get_item_on_select_subject_view()[1:]
      print(values)
      # Semester 
      self.form_subject_view.combo_semester.set(values[2])
      self.form_subject_view.combo_semester.config(state='disable')
      # Subject_id
      self.form_subject_view.combo_subject_id.set(values[0])
      # Subject_name
      self.form_subject_view.ent_subject_name.config(state='normal')
      self.form_subject_view.ent_subject_name.insert(0,values[1])
      self.form_subject_view.ent_subject_name.config(state='readonly')
      # Student_id
      self.form_subject_view.ent_student_id.config(state='normal')
      self.form_subject_view.ent_student_id.insert(0,self.subject_view.ent_id.get())
      self.form_subject_view.ent_student_id.config(state='readonly')
      # Student_name
      self.form_subject_view.ent_student_name.config(state='normal')
      self.form_subject_view.ent_student_name.insert(0,self.subject_view.ent_student_name.get())
      self.form_subject_view.ent_student_name.config(state='readonly')
      # Credit
      self.form_subject_view.ent_credit.config(state='normal')
      self.form_subject_view.ent_credit.insert(0,values[3])
      self.form_subject_view.ent_credit.config(state='readonly')
      # Score
      self.form_subject_view.ent_score_regular.insert(0,values[4])
      self.form_subject_view.ent_score_midterm.insert(0,values[5])
      self.form_subject_view.ent_score_final.insert(0,values[6])
      
   
   def on_selected_subject_student_view(self,event):
      if self.subject_view.tree.selection():
         selected_item = self.subject_view.tree.selection()[0]
         values = self.subject_view.tree.item(selected_item,'values')
         self.subject_view.btn_update_subject.config(state='normal')
         self.subject_view.btn_delete_subject.config(state='normal')
         print(values)
      else:
         self.subject_view.btn_update_subject.config(state='disable')
         self.subject_view.btn_delete_subject.config(state='disable')
         
   def get_item_on_select_subject_view(self):
      if self.subject_view.tree.selection():
         select_item = self.subject_view.tree.selection()[0]
         values = self.subject_view.tree.item(select_item,'values')
         return values
         

   
   def set_value_by_subject_id(self,event):
      # Subject name
      # print(self.form_subject_view.subject_id.get())
      subject_name = self.student_model.get_subject_name_credit_by_id((self.form_subject_view.subject_id.get(),))[0][0]
      self.form_subject_view.ent_subject_name.config(state='normal')
      self.form_subject_view.ent_subject_name.delete(0,tk.END)
      self.form_subject_view.ent_subject_name.insert(0,subject_name)
      self.form_subject_view.ent_subject_name.config(state='readonly')
      
      # Subject credit
      subject_credit = self.student_model.get_subject_name_credit_by_id((self.form_subject_view.subject_id.get(),))[0][1]
      self.form_subject_view.ent_credit.config(state='normal')
      self.form_subject_view.ent_credit.delete(0,tk.END)
      self.form_subject_view.ent_credit.insert(0,subject_credit)
      self.form_subject_view.ent_credit.config(state='readonly')
      
   def set_value_by_student_id(self,event):
      if self.student_model.get_student_name_by_id((self.form_subject_view.ent_student_id.get(),)):
         student_name = self.student_model.get_student_name_by_id((self.form_subject_view.ent_student_id.get(),))[0][0]
         print(student_name)
         self.form_subject_view.ent_student_name.config(state='normal')
         self.form_subject_view.ent_student_name.delete(0,tk.END)
         self.form_subject_view.ent_student_name.insert(0,student_name)
         self.form_subject_view.ent_student_name.config(state='readonly')
      else:
         messagebox.showwarning('Lỗi','Mã sinh viên không tồn tại')  
         self.form_subject_view.ent_student_name.config(state='normal')
         self.form_subject_view.ent_student_name.delete(0,tk.END)
         self.form_subject_view.ent_student_name.insert(0,"Không tìm thấy")
         self.form_subject_view.ent_student_name.config(state='readonly')
        
   def on_select_student_view(self,event):
      # Selection return list id of records selected
      if self.student_view.tree.selection():
         selected_item =self.student_view.tree.selection()[0]
         # print(selected_item)
         # 'values' get value in columns
         values = self.student_view.tree.item(selected_item,'values')
         # print(values) # Tuple     
         student_id = values[1]
         # print(student_id)
         student = self.student_model.get_student_by_id(student_id)
         # print(student)
         # Gán giá trị của student đc chọn sang các ent ở frame1_1
            # Id
         self.student_view.ent_id.delete(0,tk.END)
         self.student_view.ent_id.insert(0,student[0])
         
            # Name
         self.student_view.ent_name.delete(0,tk.END)
         self.student_view.ent_name.insert(0,student[1])
         
            # Address
         self.student_view.ent_address.delete(0,tk.END)
         self.student_view.ent_address.insert(0,student[3])
         
            # CCCD
         self.student_view.ent_cccd.delete(0,tk.END)
         self.student_view.ent_cccd.insert(0,student[4])
         
            # Sdt
         self.student_view.ent_phone.delete(0,tk.END)
         self.student_view.ent_phone.insert(0,student[5])
         
            # Email
         self.student_view.ent_email.delete(0,tk.END)
         self.student_view.ent_email.insert(0,student[6])
         
            # Birth
         self.student_view.date_birth.set_date(student[2])
         
            # Gender
         self.student_view.combo_gender.set(student[7])
         
            # Department
         self.student_view.combo_department.set(student[12])
         
            # Major
         self.student_view.combo_major.set(student[10])
         
            # Class
         self.student_view.combo_class.set(student[11])

            # Gen
         self.student_view.combo_gen.set(student[8])
         
            # Image
         # Lấy đường dẫn ảnh
         self.image_path = rf'{student[9]}'
         # print(self.image_path)
         # Mở ảnh
         image = Image.open(self.image_path)
         
         resized_image = image.resize((140,220))
         # Chuyển ảnh về dạng ImageTK
         self.photo = ImageTk.PhotoImage(resized_image)
         # Gán ảnh vào canvas
         self.student_view.canvas.create_image(0,0,anchor=tk.NW, image=self.photo)

   def on_select_image(self,event):
      # Open folder and get path item selected
      self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
      if self.image_path:
         image = Image.open(self.image_path)
         resized_image = image.resize((140,220))
         self.photo  = ImageTk.PhotoImage(resized_image)
         self.student_view.canvas.create_image(0,0,anchor=tk.NW, image=self.photo)
         # print(self.image_path)
         
   def delete_all_items_tree(self,parent):
      for item in parent.tree.get_children():
         parent.tree.delete(item)
      
   def get_all_students(self,event):
      self.delete_all_items_tree(self.student_view)
      students = self.student_model.get_all_students()
      # print(students)
      # print(students[0][3])
      # print(type(students[0][3]))
      
      # Format birth Y/D/M -> M/D/Y
      for i in range(len(students)):
         students[i] = list(students[i])
         for j in range(len(students[i])):
            if j == 3:
               students[i][j] = self.format_birth(str(students[i][j]))
      # print(students)
      # Push value to Tree
      for i in range(len(students)):
         self.student_view.tree.insert('',tk.END,values=((i+1,)+tuple(students[i])))
   
   def format_birth(self,old_birth):
      old_birth = old_birth.replace('/','-')
      # print(old_birth)
      birth = old_birth.split('-')
      birth.reverse()
      new_birth = '/'.join(birth)
      # print(new_birth)
      return new_birth
      
   def get_subject_by_id_semester(self,event):
      # Delete items current in tree
      self.delete_all_items_tree(self.subject_view)
      
      # Get student_id & semester
      student_id = self.subject_view.ent_id.get()
      semester = self.subject_view.semester.get()
      
      # Get items from database
      subjects = self.student_model.get_subject_by_id_semester((student_id,semester))
      # print(self.student_model.get_student_name_by_id((student_id,)))
      
      # Check validation student_id
      if self.student_model.get_student_name_by_id((student_id,)): 
         student_name= self.student_model.get_student_name_by_id((student_id,))[0][0]
      
         # Change state entry -> normal
         self.subject_view.ent_student_name.configure(state='normal')
         # Insert value
         self.subject_view.ent_student_name.delete(0,tk.END)
         self.subject_view.ent_student_name.insert(0,student_name)
         # Change state -> disable
         self.subject_view.ent_student_name.configure(state='disable')

            # Set values into tree
         for i in range(len(subjects)):
            self.subject_view.tree.insert('',tk.END,values=((i+1,)+subjects[i]))
      else:
         messagebox.showwarning('Lỗi', 'Mã sinh viên không tồn tại')
   
   def add_student(self,event):
      new_student = []
      # Get value in form
      student_id = self.student_view.ent_id.get()
      student_name = self.student_view.ent_name.get()
      student_birth = self.student_view.date_birth.get()
      student_address = self.student_view.ent_address.get()
      student_cccd = self.student_view.ent_cccd.get()
      student_phone = self.student_view.ent_phone.get()
      student_email = self.student_view.ent_email.get()
      student_gender = self.student_view.gender.get()
      student_department = self.student_view.department.get()
      student_major = self.student_view.major.get()
      student_class = self.student_view.classs.get()
      student_gen= self.student_view.gen.get()
      # Get id
      id_major = self.student_model.get_id_by_name('Major',student_major)
      id_class = self.student_model.get_id_by_name('Class',student_class)
      # Ask confirm
      ask_confirm = messagebox.askokcancel('Thêm sinh viên', 'Bạn có muốn thêm sinh viên ?')
      print(ask_confirm)
      if ask_confirm: 
         # New_student
         new_student.extend([student_id,student_name,self.format_birth(student_birth),student_address,student_cccd,student_phone,student_email,student_gender,student_gen,self.image_path,id_class[0],id_major[0]])
         # Add student in database
         self.student_model.add_student(tuple(new_student))
         messagebox.showinfo('Thêm thành công', 'Thêm thành công')
         # Display student in treeview
         self.get_all_students('<Button-1>')  
      
   def update_student(self,event):
      student = []
      # Get value in form
      student_id = self.student_view.ent_id.get()
      student_name = self.student_view.ent_name.get()
      student_birth = self.student_view.date_birth.get()
      student_address = self.student_view.ent_address.get()
      student_cccd = self.student_view.ent_cccd.get()
      student_phone = self.student_view.ent_phone.get()
      student_email = self.student_view.ent_email.get()
      student_gender = self.student_view.gender.get()
      student_department = self.student_view.department.get()
      student_major = self.student_view.major.get()
      student_class = self.student_view.classs.get()
      student_gen= self.student_view.gen.get()
      # Get id
      id_major = self.student_model.get_id_by_name('Major',student_major)
      id_class = self.student_model.get_id_by_name('Class',student_class) 
      ask_confirm = messagebox.askokcancel('Sửa sinh viên', 'Bạn có muốn sửa sinh viên ?')
      if ask_confirm:
         student.extend([student_name,self.format_birth(student_birth),student_address,student_cccd,student_phone,student_email,student_gender,student_gen,self.image_path,id_class[0],id_major[0],student_id])
         # Update student
         self.student_model.update_student(tuple(student))
         messagebox.showinfo('Sửa thành công', 'Sửa thành công')
         self.get_all_students('<Button-1>')
      
   def delete_student(self,event):
      student_id = self.student_view.ent_id.get()
      ask_confirm = messagebox.askokcancel('Xóa sinh viên', 'Bạn có muốn xóa sinh viên ?')
      if ask_confirm:
         self.student_model.delete_student((student_id,))
         messagebox.showinfo('Xóa thành công', 'Xóa thành công')
         self.get_all_students('<Button-1>')
      
   def add_subject_student(self,event):
      student_id = self.form_subject_view.ent_student_id.get()
      student_name = self.form_subject_view.ent_student_name.get()
      subject_id = self.form_subject_view.subject_id.get()
      semester = self.form_subject_view.semester.get()
      score_regular = self.form_subject_view.ent_score_regular.get()
      score_midterm = self.form_subject_view.ent_score_midterm.get()
      score_final = self.form_subject_view.ent_score_final.get()
      
      # Check exists student
      if student_name != 'Không tìm thấy':
         new_subject_student = (subject_id,student_id,semester,score_regular,score_midterm,score_final)
         print(new_subject_student)
         if not self.student_model.get_subject_student((new_subject_student[0],new_subject_student[1],new_subject_student[2])):
            self.student_model.add_subject_student(new_subject_student)
            # Xóa hoàn toàn TopLevel
            self.form_subject_view.destroy()
            messagebox.showinfo('Thành công', 'Thêm thành công')
         else:
            messagebox.showwarning('Lỗi','Thông tin đã tồn tại')
         
      else:
         messagebox.showwarning('Lỗi','Mã sinh viên không tồn tại')
   
   def update_subject_student(self,event):
      student_id = self.form_subject_view.ent_student_id.get()
      subject_id = self.form_subject_view.subject_id.get()
      semester = self.form_subject_view.semester.get()
      score_regular = self.form_subject_view.ent_score_regular.get()
      score_midterm = self.form_subject_view.ent_score_midterm.get()
      score_final = self.form_subject_view.ent_score_final.get()
      
      update_ss = (score_regular,score_midterm,score_final,subject_id,student_id,semester)
      print(update_ss)
      self.student_model.update_subject_student(update_ss)
      self.form_subject_view.destroy()
      messagebox.showinfo('Thành công', 'Sửa thành công')
      self.get_subject_by_id_semester('<Button-1>')

   def delete_subject_student(self,event):
      student_id = self.subject_view.ent_id.get()
      values_item = self.get_item_on_select_subject_view()
      self.student_model.delete_subject_student((values_item[1],student_id,values_item[3]))
      messagebox.showinfo('Thành công', 'Xóa thành công')
      self.get_subject_by_id_semester('<Button-1>')
   
   def export_file_student(self,event):
      data = []
      # Get data excel from treeview
      for item in self.student_view.tree.get_children():
         value_item = self.student_view.tree.item(item,'values')
         data.append(value_item)
      
      # Set name columns
      columns_name = ['STT','Mã sinh viên','Họ và tên','Giới tính','Ngày sinh','Khóa','Chuyên ngành','Lớp','GPA']
      
      # Save file dialog
      file_path = filedialog.asksaveasfilename(defaultextension='.xlsx',filetypes=[("Excel files", "*.xlsx"), ("PDF files", "*.pdf"), ("All files", "*.*")])
      
      if file_path:
         # Save file
         _, file_extension = os.path.splitext(file_path)
         
         if file_extension == '.xlsx':
            df = pd.DataFrame(data=data,columns=columns_name)
            df.to_excel(file_path,index=False)
            messagebox.showinfo('Thành công','Xuất EXCEL thành công')
            
         elif file_extension == '.pdf':
            pdf = FPDF()
            pdf.add_page()
            # Thêm font hỗ trợ Unicode
            pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
            pdf.set_font("DejaVu", size=10)
            pdf.cell(0, 10, txt="Danh Sách Sinh Viên", ln=True, align="C")
            pdf.ln(10)
            
            # Heading
            pdf.set_font("DejaVu", size=6)
            for heading in columns_name:
               pdf.cell(22,10,txt=str(heading),border=1,align='C')
            pdf.ln(10)
            
            # Body
            for row in data:
               for cell_data in row:
                  pdf.cell(22,10,str(cell_data),border=1,align='C')
               pdf.ln(10)
            
            # Export
            pdf.output(file_path)
            messagebox.showinfo('Thành công','Xuất PDF thành công')
         else:
            messagebox.showwarning('Lỗi','Định dạng không phù hợp')
            
   def export_file_subject(self,event):
      data = []
      # Get data excel from treeview
      for item in self.subject_view.tree.get_children():
         value_item = self.subject_view.tree.item(item,'values')
         data.append(value_item)
      
      # Set name columns
      columns_name = ['STT','Mã học phần','Tên học phần','Học kì','Số tín chỉ','Điểm thường xuyên','Điểm giữa kì','Điểm cuối kì','Điểm trung bình','Xếp loại']
      
      # Save file dialog
      file_path = filedialog.asksaveasfilename(defaultextension='.xlsx',filetypes=[("Excel files", "*.xlsx"), ("PDF files", "*.pdf"), ("All files", "*.*")])
      
      if file_path:
         # Save file
         _, file_extension = os.path.splitext(file_path)
         
         if file_extension == '.xlsx':
            df = pd.DataFrame(data=data,columns=columns_name)
            df.to_excel(file_path,index=False)
            messagebox.showinfo('Thành công','Xuất EXCEL thành công')
            
         elif file_extension == '.pdf':
            pdf = FPDF()
            pdf.add_page()
            # Thêm font hỗ trợ Unicode
            pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
            pdf.set_font("DejaVu", size=10)
            pdf.cell(0, 10, txt="Danh Sách Học Phần", ln=True, align="C")
            pdf.ln(10)
            
            # Heading
            pdf.set_font("DejaVu", size=5)
            for heading in columns_name:
               pdf.cell(21,10,txt=str(heading),border=1,align='C')
            pdf.ln(10)
            
            # Body
            for row in data:
               for cell_data in row:
                  pdf.cell(21,10,str(cell_data),border=1,align='C')
               pdf.ln(10)
            
            # Export
            pdf.output(file_path)
            messagebox.showinfo('Thành công','Xuất PDF thành công')
         else:
            messagebox.showwarning('Lỗi','Định dạng không phù hợp')

            



   def clear_frame(self):
      for widget in self.root.winfo_children():
         widget.destroy()