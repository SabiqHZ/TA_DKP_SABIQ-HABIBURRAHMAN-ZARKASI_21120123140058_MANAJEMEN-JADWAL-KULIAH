import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class ScheduleManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen Jadwal Kuliah")
        
        self.schedule = []

        self.label_course = tk.Label(root, text="Masukkan Mata Kuliah:")
        self.label_course.pack(pady=5)
        
        self.label_course_entry = tk.Entry(root, width=30)
        self.label_course_entry.pack(pady=5)

        self.label_day = tk.Label(root, text="Masukkan Hari:")
        self.label_day.pack(pady=5)

        self.day = ["Senin", "Selasa", "Rabu", "Kamis", "jumat", "Sabtu", "Minggu"]
        self.day_combobox = ttk.Combobox(root, values= self.day, width=27, state="readonly")
        self.day_combobox.pack(pady=5)

        self.label_time = tk.Label(root, text="Masukkan Waktu:")
        self.label_time.pack(pady=5)

        self.time_entry = tk.Entry(root, width=30)
        self.time_entry.pack(pady=5)

        self.add_schedule_button = tk.Button(root, text="Tambah Jadwal", command=self.add_schedule)
        self.add_schedule_button.pack(pady=5)

        self.schedule_listbox = tk.Listbox(root, width=50, height=10)
        self.schedule_listbox.pack(pady=5)

        self.remove_schedule_button = tk.Button(root, text="Hapus Jadwal", command=self.remove_schedule)
        self.remove_schedule_button.pack(pady=5)

        self.clear_all_button = tk.Button(root, text="Hapus Semua Jadwal", command=self.clear_all_schedules)
        self.clear_all_button.pack(pady=5)

        self.exit_button = tk.Button(root, text ="EXIT", command=self.close_window)
        self.exit_button.pack(pady=5)
        
        self.label_course_entry.bind('<Return>', self.add_schedule_event)
        self.day_combobox.bind('<Return>', self.add_schedule_event)
        self.time_entry.bind('<Return>', self.add_schedule_event)
        
    def add_schedule(self):
        course = self.label_course_entry.get()
        day = self.day_combobox.get()
        time = self.time_entry.get()
        
        if not course or not day or not time:
            messagebox.showwarning("Peringatan", "Semua kolom harus diisi")
            return
        
        if any(char.isdigit() for char in course):
            messagebox.showwarning("Peringatan", "Mata Kuliah tidak boleh berisi angka")
            return
        
        if not time.isdigit():
            messagebox.showwarning("Peringatan", "waktu harus dalam bentuk angka")
            return
        
        if course and day and time:
            schedule_item = f"{course} - {day} - {time}"
            self.schedule.append(schedule_item)
            self.update_schedule_listbox()
        
            self.label_course_entry.delete(0, tk.END)
            self.day_combobox.set("")
            self.time_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Peringatan", "Semua field harus diisi")
            
    def add_schedule_event(self, event):
        self.add_schedule()


    def remove_schedule(self):
        selected_schedule_index = self.schedule_listbox.curselection()
        if selected_schedule_index:
            selected_schedule_index = selected_schedule_index[0]
            del self.schedule[selected_schedule_index]
            self.update_schedule_listbox()
        else:
            messagebox.showwarning("Peringatan", "Pilih jadwal yang akan dihapus")

    def clear_all_schedules(self):
        self.schedule.clear()
        self.update_schedule_listbox()
        
    def close_window(self):
        self.root.destroy()

    def update_schedule_listbox(self):
        self.schedule_listbox.delete(0, tk.END)
        for schedule_item in self.schedule:
            self.schedule_listbox.insert(tk.END, schedule_item)
            
if __name__ == "__main__":
    root = tk.Tk()
    app = ScheduleManager(root)
    root.mainloop()
