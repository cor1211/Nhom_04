import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import DateEntry

class LoginView(tk.Frame):
   def __init__(self,parent):
      super().__init__(parent)
      self.create_widgets()
      
      
      
   def create_widgets(self):
      self.lb_us = tk.Label(self,text='Tên tài khoản:',anchor='w')
      self.lb_us.grid(row=0,column=0,padx=10,pady=10,sticky='w')

      self.ent_us = tk.Entry(self,width=30)
      self.ent_us.grid(row=0,column=1,padx=10,pady=10) 
      
      self.lb_pw = tk.Label(self,text='Mật khẩu:',anchor='w')
      self.lb_pw.grid(row=1,column=0,padx=10,pady=10,sticky='w')

      self.ent_pw = tk.Entry(self,width=30,show='*')
      self.ent_pw.grid(row=1,column=1,padx=10,pady=10) 
      
      self.show_pw = tk.IntVar(value=0)
      self.checkbtn_showpw = tk.Checkbutton(self,text='Hiển thị mật khẩu',variable=self.show_pw)
      self.checkbtn_showpw.grid(row=2,column=1,pady=10,sticky='w')
      
      self.btn_login = tk.Button(self,text='Đăng nhập',width=10,height=2)
      self.btn_login.grid(row=3,column=0,columnspan=2,pady=10)
      
      # Căn giữa các widget trong LoginView
      self.grid_rowconfigure(0, weight=1)
      self.grid_rowconfigure(1, weight=1)
      self.grid_rowconfigure(2, weight=1)
      self.grid_rowconfigure(3, weight=1)
      self.grid_columnconfigure(0, weight=1)
      self.grid_columnconfigure(1, weight=1)
        
class AdminDashboardView(tk.Frame):
   def __init__(self,parent):
      super().__init__(parent)
      self.create_widgets()
      
   def create_widgets(self):
      self.lbl_welcome = tk.Label(self,font=16)
      self.lbl_welcome.grid(row=0,column=0,sticky='we',padx=5,pady=5,columnspan=2)
      self.btn_students = tk.Button(self,text='🎓\nSinh viên',bg='#E7CBCB',relief='solid',width=18,height=9,font= 16)
      self.btn_students.grid(row=1,column=0,padx=120,pady=80)
      
      self.btn_result = tk.Button(self,text='📝\nKết quả học tập',bg='#92DFC8',relief='solid',width=18,height=9,font= 16)
      self.btn_result.grid(row=1,column=1,padx=120,pady=80)
      
      # self.btn_thongke = tk.Button(self,text='🎓\nSinh viên',bg='#C8EBF3',relief='solid',width=20,height=10,font= 16)
      # self.btn_thongke.grid(row=2,column=0,padx=120,pady=80)
      
      self.btn_logout = tk.Button(self,text='🔓\nĐăng xuất',bg='#C8EBF3',relief='solid',width=18,height=9,font= 16)
      self.btn_logout.grid(row=2,column=0,padx=120,pady=80)
      
      # Đảm bảo các hàng/cột trong main_frame có thể co giãn
      self.grid_rowconfigure(0, weight=10)
      
      for i in range(1,3):  # 2 hàng
         self.grid_rowconfigure(i, weight=45)

      for i in range(2):  # 2 cột
         self.grid_columnconfigure(i, weight=50)
         

class StudentView(tk.Frame):
   def __init__(self,parent):
      super().__init__(parent)
      self.create_widgets()
      
   def create_widgets(self):
      # self.btn1 = tk.Button(self,text='hihi',bg='red')
      # self.btn1.grid(row=0,column=1)
      self.frame1 = tk.Frame(self,bg='#D5F0D4',borderwidth=1.5,relief='solid')
      self.frame1.grid(row=0,column=0,sticky='nsew')
      # Ngăn không cho frame1 mở rộng 
      self.frame1.grid_propagate(False)
      
      # self.btn = tk.Button(self.frame1,text='xx')
      # self.btn.grid(row=0,column=0)
      
      self.frame2 = tk.Frame(self,bg='#83CAFF',borderwidth=1.5,relief='solid')
      self.frame2.grid(row=0,column=2,sticky='nsew')
      # Ngăn không cho frame2 mở rộng 
      self.frame2.grid_propagate(False)
      # self.btn2 = tk.Button(self.frame2,text='yy')
      # self.btn2.grid(row=0,column=0)
      
      self.grid_rowconfigure(0,weight=1)
      self.grid_columnconfigure(0,weight=45)
      self.grid_columnconfigure(1,weight=1)
      self.grid_columnconfigure(2,weight=54)
      
      # Widgets in frame1
         # Frame1_1
      self.frame1_1 = tk.Frame(self.frame1)
      self.frame1_1.grid(row=0,column=0,sticky='nsew')
      self.frame1_1.grid_propagate(False)
      
         #Frame1_2
      self.frame1_2 = tk.Frame(self.frame1)
      self.frame1_2.grid(row=1,column=0,sticky='nsew')
      self.frame1_2.grid_propagate(False)
      
         #Frame1_3
      self.frame1_3 = tk.Frame(self.frame1)
      self.frame1_3.grid(row=2,column=0,sticky='nsew')
      self.frame1_3.grid_propagate(False)
      
      self.frame1.grid_columnconfigure(0,weight=1)
      self.frame1.grid_rowconfigure(0,weight=50)
      self.frame1.grid_rowconfigure(1,weight=40)
      self.frame1.grid_rowconfigure(2,weight=10)
      
      # Widgets in frame1_1
         # Title
      self.title1_1 = tk.Label(self.frame1_1,text="Thông tin cá nhân")
      self.title1_1.grid(row=0,column=0,columnspan=5,pady=10,sticky='we')
         # Content

      # Xử lý ảnh
      self.canvas = tk.Canvas(self.frame1_1,width=140,height=220)
      self.canvas.grid(row=1,column=0, rowspan=6)
      
      self.btn_select_image = tk.Button(self.frame1_1,text='Chọn ảnh')
      self.btn_select_image.grid(row=7,column=0,padx=5,pady=5)
      
      
      self.lbl_id = tk.Label(self.frame1_1,text='Mã sinh viên')
      self.lbl_id.grid(row=1,column=1,padx=5,pady=5,sticky='w')
      
      self.ent_id = tk.Entry(self.frame1_1)
      self.ent_id.grid(row=1,column=2,padx=5,pady=5)
      
      self.lbl_name = tk.Label(self.frame1_1,text='Họ và tên')
      self.lbl_name.grid(row=2,column=1,padx=5,pady=5,sticky='w')
      
      self.ent_name = tk.Entry(self.frame1_1)
      self.ent_name.grid(row=2,column=2,padx=5,pady=5)
      
      self.lbl_birth = tk.Label(self.frame1_1,text='Ngày sinh')
      self.lbl_birth.grid(row=3,column=1,padx=5,pady=5,sticky='w')
      
      # Vấn đề
      self.date_birth = DateEntry(self.frame1_1,date_pattern="dd/mm/yyyy")
      self.date_birth.grid(row=3,column=2,padx=5,pady=5,sticky='w')
      
      self.lbl_address = tk.Label(self.frame1_1,text='Địa chỉ')
      self.lbl_address.grid(row=4,column=1,padx=5,pady=5,sticky='w')
      
      self.ent_address = tk.Entry(self.frame1_1)
      self.ent_address.grid(row=4,column=2,padx=5,pady=5)
      
      self.lbl_cccd = tk.Label(self.frame1_1,text='CCCD')
      self.lbl_cccd.grid(row=5,column=1,padx=5,pady=5,sticky='w')
      
      self.ent_cccd = tk.Entry(self.frame1_1)
      self.ent_cccd.grid(row=5,column=2,padx=5,pady=5)
      
      self.lbl_phone = tk.Label(self.frame1_1,text='Số điện thoại')
      self.lbl_phone.grid(row=6,column=1,padx=5,pady=5,sticky='w')
      
      self.ent_phone = tk.Entry(self.frame1_1)
      self.ent_phone.grid(row=6,column=2,padx=5,pady=5)
      
      self.lbl_email = tk.Label(self.frame1_1,text='Email')
      self.lbl_email.grid(row=1,column=3,padx=5,pady=5,sticky='w')
      
      self.ent_email = tk.Entry(self.frame1_1)
      self.ent_email.grid(row=1,column=4,padx=5,pady=5)
      
      self.lbl_gender = tk.Label(self.frame1_1,text='Giới tính')
      self.lbl_gender.grid(row=2,column=3,padx=5,pady=5,sticky='w')
      
      self.gender = tk.StringVar() # Biến lưu giá trị được chọn
      self.combo_gender = ttk.Combobox(self.frame1_1,textvariable=self.gender,state='readonly')
      self.combo_gender['values'] = ['Nam','Nữ','Khác']
      self.combo_gender.current(0)
      self.combo_gender.grid(row=2,column=4,padx=5,pady=5,sticky='w')
      
      self.frame1_1.grid_columnconfigure(0,weight=40)
      self.frame1_1.grid_columnconfigure(1,weight=15)
      self.frame1_1.grid_columnconfigure(2,weight=15)
      self.frame1_1.grid_columnconfigure(3,weight=15)
      self.frame1_1.grid_columnconfigure(4,weight=15)
      
      # Widgets in frame1_2
      self.frame1_2.grid_columnconfigure(0,weight=25)
      self.frame1_2.grid_columnconfigure(1,weight=25)
      self.frame1_2.grid_columnconfigure(2,weight=25)
      self.frame1_2.grid_columnconfigure(3,weight=25)
      
      
      self.title1_2 = tk.Label(self.frame1_2,text='Thông tin học tập')
      self.title1_2.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
      
         # Department
      self.lbl_department = tk.Label(self.frame1_2,text='Khoa')
      self.lbl_department.grid(row=1,column=0,padx=5,pady=5,sticky='w')
      
      self.department = tk.StringVar()
      self.combo_department = ttk.Combobox(self.frame1_2,textvariable=self.department,state='readonly')
      self.combo_department.grid(row=1,column=1,padx=5,pady=5,sticky='w')
      
         # Major
      self.lbl_major = tk.Label(self.frame1_2,text='Chuyên ngành')
      self.lbl_major.grid(row=2,column=0,padx=5,pady=5,sticky='w')
      
      self.major = tk.StringVar()
      self.combo_major = ttk.Combobox(self.frame1_2,textvariable=self.major,state='readonly')
      self.combo_major.grid(row=2,column=1,padx=5,pady=5,sticky='w')
      
         # Class
      self.lbl_class = tk.Label(self.frame1_2,text='Lớp')
      self.lbl_class.grid(row=1,column=2,padx=5,pady=5,sticky='w')
      
      self.classs = tk.StringVar()
      self.combo_class = ttk.Combobox(self.frame1_2,textvariable=self.classs,state='readonly')
      self.combo_class.grid(row=1,column=3,padx=5,pady=5,sticky='w')
      
         # Generation
      self.lbl_gen = tk.Label(self.frame1_2,text='Khóa')
      self.lbl_gen.grid(row=2,column=2,padx=5,pady=5,sticky='w')
      
      self.gen= tk.StringVar()
      self.combo_gen = ttk.Combobox(self.frame1_2,textvariable=self.gen,state='readonly')
      self.combo_gen.grid(row=2,column=3,padx=5,pady=5,sticky='w')
      self.combo_gen['values']= ['K14','K15','K16','K17','K18','K19']
      self.combo_gen.current(0)
      
         # Widgets in frame1_3
      self.frame1_3.grid_columnconfigure(0,weight=25)
      self.frame1_3.grid_columnconfigure(1,weight=25)
      self.frame1_3.grid_columnconfigure(2,weight=25)
      self.frame1_3.grid_columnconfigure(3,weight=25)
      
      self.student_btn_add = tk.Button(self.frame1_3,text='Thêm',width=15)
      self.student_btn_add.grid(row=0,column=0,padx=5,pady=5,sticky='nsew')
      
      self.student_btn_update = tk.Button(self.frame1_3,text='Sửa',width=15,state='disabled')
      self.student_btn_update.grid(row=0,column=1,padx=5,pady=5,sticky='nsew')
      
      self.student_btn_delete = tk.Button(self.frame1_3,text='Xóa',width=15,state='disabled')
      self.student_btn_delete.grid(row=0,column=2,padx=5,pady=5,sticky='nsew')
      
      self.student_btn_refresh = tk.Button(self.frame1_3,text='Làm mới',width=15)
      self.student_btn_refresh.grid(row=0,column=3,padx=5,pady=5,sticky='nsew')
      
      self.student_btn_back = tk.Button(self.frame1_3,text='Quay lại',width=15)
      self.student_btn_back.grid(row=1,column=0,padx=5,pady=5,sticky='nsew')
      
   # Widgets in frame2
      self.frame2_1 = tk.Frame(self.frame2)
      self.frame2_1.grid(row=0,column=0,sticky='nsew')
      self.frame2_1.grid_propagate(False)
      
      self.frame2_2 = tk.Frame(self.frame2)
      self.frame2_2.grid(row=1,column=0,sticky='nsew')
      self.frame2_2.grid_propagate(False)
      
      self.frame2.grid_columnconfigure(0,weight=1)
      self.frame2.grid_rowconfigure(0,weight=10)
      self.frame2.grid_rowconfigure(1,weight=90)
      
      # Widgets in frame2_1
      self.lbl_find = tk.Label(self.frame2_1,text='Tìm kiếm theo')
      self.lbl_find.grid(row=0,column=0,padx=5,pady=5,sticky='nsew')
      
      self.find = tk.StringVar()
      self.combo_find = ttk.Combobox(self.frame2_1,textvariable=self.find, state='readonly')
      self.combo_find['values'] = ['Mã sinh viên','Tên sinh viên', 'Chuyên ngành','Khóa','Lớp']
      self.combo_find.current(0)
      self.combo_find.grid(row=0,column=1,padx=5,pady=5,sticky='nsew')
      
      self.ent_find = tk.Entry(self.frame2_1)
      self.ent_find.grid(row=0,column=2,padx=5,pady=5,sticky='nsew')
      
      self.btn_find = tk.Button(self.frame2_1,text='Tìm kiếm')
      self.btn_find.grid(row=0,column=3,padx=5,pady=5,sticky='nsew')
      
      self.btn_showall = tk.Button(self.frame2_1,text='Xem tất cả')
      self.btn_showall.grid(row=0,column=4,padx=5,pady=5,sticky='nsew')
      
      self.btn_export = tk.Button(self.frame2_1,text='Xuất danh sách')
      self.btn_export.grid(row=0,column=5,padx=5,pady=5,sticky='nsew')
      
      
      # self.frame2_1.grid_rowconfigure(0,weight=1)
      for i in range(6):
         self.frame2_1.grid_columnconfigure(i,weight=16)
      
      # Widgets in frame2_2
      self.frame2_2.grid_columnconfigure(0,weight=1)
      self.frame2_2.grid_rowconfigure(0,weight=1)
      
      columns = ('stt','student_id','name','gender','birth','generation','major','class','gpa')
      self.tree = ttk.Treeview(self.frame2_2,columns=columns, show='headings')
      self.tree.grid(row=0,column=0,sticky='nsew')
      
      self.tree.heading('stt', text='STT')
      self.tree.heading('student_id', text='Mã sinh viên')
      self.tree.heading('name',text='Họ và tên')
      self.tree.heading('gender',text='Giới tính')
      self.tree.heading('birth',text='Ngày sinh')
      self.tree.heading('generation',text='Khóa')
      self.tree.heading('major',text='Chuyên ngành')
      self.tree.heading('class',text='Lớp')
      self.tree.heading('gpa',text='GPA')
      
      # Điều chỉnh width các cột
      total_width = self.frame2_2.winfo_width()  # Lấy chiều rộng khung cha (frame2_2)
      num_cols = len(self.tree["columns"])      # Số lượng cột
      col_width = total_width // num_cols       # Chia đều cho các cột
      
      for col in self.tree["columns"]:
         self.tree.column(col, width=col_width, stretch=True)
      
      # self.tree.column('stt',width=20,stretch=True,anchor='center')
      # self.tree.column('student_id',width=80,stretch=True,anchor='center')
      # self.tree.column('name',width=100,stretch=True,anchor='w')
      # self.tree.column('gender',width=50,stretch=True,anchor='center')
      # self.tree.column('birth',width=60,stretch=True,anchor='center')
      # self.tree.column('generation',width=25,stretch=True,anchor='center')
      # self.tree.column('major',width=95,stretch=True,anchor='w')
      # self.tree.column('class',width=60,stretch=True,anchor='center')
      
      # Thêm scroll bar
      self.scrollbar_x = ttk.Scrollbar(self.frame2_2, orient="horizontal", command=self.tree.xview)
      self.scrollbar_y = ttk.Scrollbar(self.frame2_2, orient="vertical", command=self.tree.yview)

      self.tree.configure(xscrollcommand=self.scrollbar_x.set, yscrollcommand=self.scrollbar_y.set)

      self.scrollbar_x.pack(side="bottom", fill="x")
      self.scrollbar_y.pack(side="right", fill="y")

class SubjectView(tk.Frame):
   def __init__(self,parent):
      super().__init__(parent)
      self.create_widgets()
      
   def create_widgets(self):
      self.grid_rowconfigure(0,weight=5)
      self.grid_rowconfigure(1,weight=10)
      self.grid_rowconfigure(2,weight=75)
      self.grid_rowconfigure(3,weight=10)
      self.grid_columnconfigure(0,weight=1)
      # self.grid_columnconfigure(1,weight=25)
      # self.grid_columnconfigure(2,weight=25)
      # self.grid_columnconfigure(3,weight=25)
      
      # Frame 1
      self.frame1 = tk.Frame(self)
      self.frame1.grid(row=0,column=0,sticky='nsew')
      self.frame1.grid_propagate(False)
      self.frame1.grid_columnconfigure(0,weight=1)
      self.frame1.grid_rowconfigure(0,weight=1)
      
      # Frame 2
      self.frame2 = tk.Frame(self)
      self.frame2.grid(row=1,column=0,sticky='nsew')
      self.frame2.grid_propagate(False)
      for i in range(5):
         self.frame2.grid_columnconfigure(i,weight=20)
         if i <=1:
            self.frame2.grid_rowconfigure(i,weight=50)
            
      
      # Frame 3
      self.frame3 = tk.Frame(self)
      self.frame3.grid(row=2,column=0,sticky='nsew')
      self.frame3.grid_propagate(False)
      self.frame3.grid_rowconfigure(0,weight=1)
      self.frame3.grid_columnconfigure(0,weight=1)
      
      # Frame 4
      self.frame4 = tk.Frame(self)
      self.frame4.grid(row=3,column=0,sticky='nsew')
      self.frame4.grid_propagate(False)
      self.frame4.grid_rowconfigure(0,weight=1)
      self.frame4.grid_columnconfigure(0,weight=33)
      self.frame4.grid_columnconfigure(1,weight=33)
      self.frame4.grid_columnconfigure(2,weight=33)
      
         # Widgets in frame 1
      self.title = tk.Label(self.frame1,text='Quản lý học phần',anchor='center',font=18)
      self.title.grid(row=0,column=0,padx=5,pady=5,sticky='ew')

         # Widgets in frame 2
      
      # Student_id
      self.lbl_student_id = tk.Label(self.frame2,text='Mã sinh viên')
      self.lbl_student_id.grid(row=0,column=0,padx=5,pady=5,sticky='w')
      
      self.ent_id = tk.Entry(self.frame2)
      self.ent_id.grid(row=0,column=1,padx=5,pady=5,sticky='w')
      
      # Combobox Hoc ki
      self.lbl_semester = tk.Label(self.frame2,text='Học kì')
      self.lbl_semester.grid(row=0,column=2,padx=5,pady=5,sticky='w')
      
      self.semester = tk.StringVar()
      self.combo_semester = ttk.Combobox(self.frame2,textvariable=self.semester,state='readonly')
      self.combo_semester['values'] = ['HK1', 'HK2','HK3','HK4','HK5','HK6','HK7','HK8','HK9','HK10','HK11','HK12','Tất cả']
      self.combo_semester.current(0)
      self.combo_semester.grid(row=0,column=3,padx=5,pady=5,sticky='w')
      
      # Button 'Tim kiem'
      self.btn_find = tk.Button(self.frame2,text='Tìm kiếm')
      self.btn_find.grid(row=0,column=4,padx=5,pady=5,sticky='w')
      
      # Button 'Xuat danh sach'
      self.btn_export = tk.Button(self.frame2,text='Xuất danh sách')
      self.btn_export.grid(row=0,column=5,padx=5,pady=5,sticky='w')
      
      # Tên sinh viên
      self.lbl_student_name = tk.Label(self.frame2,text='Tên sinh viên')
      self.lbl_student_name.grid(row=1,column=0,padx=5,pady=5,sticky='w')
      
      self.ent_student_name = tk.Entry(self.frame2,state='disabled')
      self.ent_student_name.grid(row=1,column=1,padx=5,pady=5,sticky='w')
      
         # Widgets in frame 3
      self.frame3.grid_columnconfigure(0,weight=1)
      self.frame3.grid_rowconfigure(0,weight=1)
      # Tree view
      # Key columns
      columns = ('stt', 'subject_id', 'subject_name', 'semester', 'subject_credit', 'score_regular', 'score_midterm', 'score_final','score_avarage','rating')
      self.tree = ttk.Treeview(self.frame3,columns=columns,show='headings')
      self.tree.grid(row=0,column=0,sticky='nsew')
      # Set column_name
      self.tree.heading('stt',text='STT')
      self.tree.heading('subject_id',text='Mã học phần')
      self.tree.heading('subject_name',text='Tên học phần')
      self.tree.heading('semester',text='Học kì')
      self.tree.heading('subject_credit',text='Số tín chỉ')
      self.tree.heading('score_regular',text='Điểm thường xuyên')
      self.tree.heading('score_midterm',text='Điểm giữa kì')
      self.tree.heading('score_final',text='Điểm cuối kì')
      self.tree.heading('score_avarage',text='Điểm trung bình')
      self.tree.heading('rating',text='Xếp loại')
      
      self.tree.column('stt',anchor='center')
      self.tree.column('subject_id',anchor='center')
      self.tree.column('subject_name')
      self.tree.column('semester',anchor='center')
      self.tree.column('subject_credit',anchor='center')
      self.tree.column('score_regular',anchor='center')
      self.tree.column('score_midterm',anchor='center')
      self.tree.column('score_final',anchor='center')
      self.tree.column('score_avarage',anchor='center')
      self.tree.column('rating',anchor='center')
      # Set width columns
      total_width = self.frame3.winfo_width() # Lấy chiều rộng của frame 3
      num_cols = len(self.tree['columns'])
      col_width = total_width//num_cols
      
      for col in self.tree['columns']:
         self.tree.column(col,width=col_width,stretch=True)
         
         # Widgets in frame 4
      self.btn_add_subject = tk.Button(self.frame4,text='Thêm học phần')
      self.btn_add_subject.grid(row=0,column=0)
      
      self.btn_update_subject = tk.Button(self.frame4,text='Sửa học phần',state='disabled')
      self.btn_update_subject.grid(row=0,column=1)
      
      self.btn_delete_subject = tk.Button(self.frame4,text='Xóa học phần',state='disabled')
      self.btn_delete_subject.grid(row=0,column=2)
      
      self.btn_back= tk.Button(self.frame4,text='Quay lại')
      self.btn_back.grid(row=1,column=0)
      
class TopLeveSubjectlView(tk.Toplevel):
   def __init__(self,parent):
      super().__init__(parent)
      self.title('Form')
      self.create_widgets()
      
   def create_widgets(self):
      
      self.grid_columnconfigure(0,weight=1)
      self.grid_rowconfigure(0,weight=10)
      self.grid_rowconfigure(1,weight=80)
      self.grid_rowconfigure(2,weight=10)
      
      # Frame 1
      self.frame1 = tk.Frame(self)
      self.frame1.grid(row=0,column=0,sticky='nsew')
      self.frame1.grid_propagate(False)
      self.frame1.grid_rowconfigure(0,weight=1)
      self.frame1.grid_columnconfigure(0,weight=1)
      
      # Frame 2
      self.frame2 = tk.Frame(self)
      self.frame2.grid(row=1,column=0,sticky='nsew')
      self.frame2.grid_propagate(False)
      
      for i in range(5):
         self.frame2.grid_rowconfigure(i,weight=20)
         if i <4:
            self.frame2.grid_columnconfigure(i,weight=25)
            
      
      # Frame 3
      self.frame3 = tk.Frame(self)
      self.frame3.grid(row=2,column=0,sticky='nsew')
      self.frame3.grid_propagate(False)
      self.frame3.grid_columnconfigure(0,weight=1)
      self.frame3.grid_columnconfigure(1,weight=1)
      self.frame3.grid_rowconfigure(0,weight=1)
      
         # Widgets in frame 1
      self.title1 = tk.Label(self.frame1,text='Thêm học phần')
      self.title1.grid(row=0,column=0,padx=0,pady=5,sticky='ew')
      
         # Widgets in frame 2
      # Student_id
      self.lbl_student_id = tk.Label(self.frame2,text='Mã sinh viên')
      self.lbl_student_id.grid(row=0,column=0,padx=5,pady=5,sticky='w')
      
      self.ent_student_id = tk.Entry(self.frame2)
      self.ent_student_id.grid(row=0,column=1,padx=5,pady=5,sticky='w')
      
      # Student_name
      self.lbl_student_name= tk.Label(self.frame2,text='Tên sinh viên')
      self.lbl_student_name.grid(row=0,column=2,padx=5,pady=5,sticky='w')
      
      self.ent_student_name= tk.Entry(self.frame2,state='disabled')
      self.ent_student_name.grid(row=0,column=3,padx=5,pady=5,sticky='w')
      
      # Subject_id
      self.lbl_subject_id = tk.Label(self.frame2,text='Mã học phần')
      self.lbl_subject_id.grid(row=1,column=0,padx=5,pady=5,sticky='w')
      
      self.subject_id = tk.StringVar()
      self.combo_subject_id = ttk.Combobox(self.frame2,state='readonly', textvariable=self.subject_id)
      self.combo_subject_id.grid(row=1,column=1,padx=5,pady=5,sticky='w')
      
       # Subject_name
      self.lbl_subject_name = tk.Label(self.frame2,text='Tên học phần')
      self.lbl_subject_name.grid(row=1,column=2,padx=5,pady=5,sticky='w')
      
      self.ent_subject_name= tk.Entry(self.frame2,state='readonly',width=25)
      self.ent_subject_name.grid(row=1,column=3,padx=5,pady=5,sticky='w')
      
      # Semester 
      self.lbl_semester = tk.Label(self.frame2,text='Học kì')
      self.lbl_semester.grid(row=2,column=0,padx=5,pady=5,sticky='w')
      
      
      self.semester= tk.StringVar()
      self.combo_semester = ttk.Combobox(self.frame2,state='readonly',textvariable=self.semester)
      self.combo_semester['values'] = ['HK1', 'HK2','HK3','HK4','HK5','HK6','HK7','HK8','HK9','HK10','HK11','HK12']
      self.combo_semester.grid(row=2,column=1,padx=5,pady=5,sticky='w')
      
       # Credit
      self.lbl_credit = tk.Label(self.frame2,text='Số tín chỉ')
      self.lbl_credit.grid(row=2,column=2,padx=5,pady=5,sticky='w')
      
      self.ent_credit= tk.Entry(self.frame2,state='readonly')
      self.ent_credit.grid(row=2,column=3,padx=5,pady=5,sticky='w')
      
      # Score_regular
      self.lbl_score_regular = tk.Label(self.frame2,text='Điểm thường xuyên')
      self.lbl_score_regular.grid(row=3,column=0,padx=5,pady=5,sticky='w')
      
      self.ent_score_regular= tk.Entry(self.frame2)
      self.ent_score_regular.grid(row=3,column=1,padx=5,pady=5,sticky='w')
      
      # Score_midterm
      self.lbl_score_midterm = tk.Label(self.frame2,text='Điểm giữa kì')
      self.lbl_score_midterm.grid(row=3,column=2,padx=5,pady=5,sticky='w')
      
      self.ent_score_midterm= tk.Entry(self.frame2)
      self.ent_score_midterm.grid(row=3,column=3,padx=5,pady=5,sticky='w')
      
      # Score_final
      self.lbl_score_final = tk.Label(self.frame2,text='Điểm cuối kì')
      self.lbl_score_final.grid(row=4,column=0,padx=5,pady=5,sticky='w')
      
      self.ent_score_final= tk.Entry(self.frame2)
      self.ent_score_final.grid(row=4,column=1,padx=5,pady=5,sticky='w')
      
         # Widgets in frame 3
      self.btn_add_confirm = tk.Button(self.frame3,text='Xác nhận')
      self.btn_add_confirm.grid(row=0,column=0,padx=5,pady=5)
      
      self.btn_add_cancel = tk.Button(self.frame3,text='Hủy bỏ')
      self.btn_add_cancel.grid(row=0,column=1,padx=5,pady=5)
      
      
      
# Test 
if __name__ == '__main__':
   root = tk.Tk()
   root.title('Main')
   root.grid_columnconfigure(0,weight=50)
   root.grid_rowconfigure(0,weight=50)
   root.geometry("1280x800")
   root.resizable(True,True)
   
   # subject_view = SubjectView(root)
   # subject_view.configure(width=400,height=200) 
   # subject_view.grid(row=0,column=0,sticky='nsew')
   toplevelsubjectview = TopLeveSubjectlView(root)
   # toplevelsubjectview.title('Form')
   toplevelsubjectview.geometry('600x400')
   
   
   
   root.mainloop()
   
            
               
      
      
