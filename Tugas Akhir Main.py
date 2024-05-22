import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class ScheduleManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen Jadwal Kuliah")
        
        self.schedule = []

        self.label = tk.Label(root, text="Masukkan Mata Kuliah:")
        self.label.pack(pady=5)
        
        self.courses = ["Algoritma Pemrograman", "Matematika Teknik", "Kimia", "Biologi", "Sejarah", "Geografi", "Bahasa Indonesia", "Bahasa Inggris"]
        self.course_combobox = ttk.Combobox(root, values=self.courses, width=30, state="readonly")
        self.course_combobox.pack(pady=5)

        self.label_day = tk.Label(root, text="Masukkan Hari:")
        self.label_day.pack(pady=5)

        self.day = ["Senin", "Selasa", "Rabu", "Kamis", "jumat", "Sabtu", "Minggu"]
        self.day_combobox = ttk.Combobox(root, values= self.day, width=30, state="readonly")
        self.day_combobox.pack(pady=5)

        self.time = tk.Label(root, text="Pilih Ruangan:")
        self.time.pack(pady=5)
        
        self.time = ["A201", "A202", "B201", "B202", "B102", "B103", "B104"]
        self.time_combobox = ttk.Combobox(root, values= self.time, width=30, state="readonly")
        self.time_combobox.pack(pady=5)

        self.add_schedule_button = tk.Button(root, text="Tambah Jadwal", command=self.add_schedule)
        self.add_schedule_button.pack(pady=5)

        self.schedule_listbox = tk.Listbox(root, width=50, height=10)
        self.schedule_listbox.pack(pady=5)

        self.remove_schedule_button = tk.Button(root, text="Hapus Jadwal", command=self.remove_schedule)
        self.remove_schedule_button.pack(pady=5)

        self.clear_all_button = tk.Button(root, text="Hapus Semua Jadwal", command=self.clear_all_schedules)
        self.clear_all_button.pack(pady=5)

    def add_schedule(self):
        course = self.course_combobox.get()
        day = self.day_combobox.get()
        time = self.time_combobox.get()
        if course and day and time:
            schedule_item = f"{course} - {day} - {time}"
            self.schedule.append(schedule_item)
            self.update_schedule_listbox()
            self.course_combobox.set('')
            self.day_combobox.set('')
            self.time_combobox.set('')
            self.course_combobox.delete(0, tk.END)
            self.day_combobox.delete(0, tk.END)
            self.time_combobox.delete(0, tk.END)
        else:
            messagebox.showwarning("Peringatan", "Semua field harus diisi")

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

    def update_schedule_listbox(self):
        self.schedule_listbox.delete(0, tk.END)
        for schedule_item in self.schedule:
            self.schedule_listbox.insert(tk.END, schedule_item)
            
if __name__ == "__main__":
     root = tk.Tk()
     app = ScheduleManager(root)
     root.mainloop()
