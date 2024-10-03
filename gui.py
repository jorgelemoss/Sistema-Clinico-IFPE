import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from auth import user_validate
from components import button, input_entry, label
from store import create, update, patients, consultations

# Screens

# Dashboard Screens

def show_patients_screen():
    window = tk.Tk()
    window.title("Lista de Pacientes")

    frame = ttk.Frame(window)

    label(frame, "Lista de pacientes", row=0, column=0, padx=10, pady=30, font=("Helvetica", 12))

    columns = ("ID", "Nome", "Data de Nascimento", "CPF", "Sexo", "Endereço")
    tree = ttk.Treeview(frame, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')

    for patient in patients:
        address = f"{patient['address']['street']}, {patient['address']['city']}, {patient['address']['state']}"
        tree.insert("", "end", values=(
            patient["id"],
            patient["name"],
            patient["birthday"],
            patient["cpf"],
            patient["gender"],
            address
        ))

    tree.grid(padx=100, pady=50)
    frame.grid(pady=10, padx=10)
    button(frame, "Fechar", command=window.destroy)
    
    window.mainloop()

def list_consultation_screen():
    window = tk.Tk()
    window.title("Consultas Marcadas")

    frame = ttk.Frame(window)

    label(frame, "Consultas Registradas", row=0, column=0, padx=10, pady=30, font=("Helvetica", 12))

    columns = ("CPF", "Nome", "Data", "Hora")
    tree = ttk.Treeview(frame, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')

    for consultation in consultations:
        patient_name = ""
        for patient in patients:
            if patient["cpf"] == consultation["cpf"]:
                patient_name = patient["name"]
                break
        
        tree.insert("", "end", values=(
            consultation["cpf"],
            patient_name,
            consultation["date"],
            consultation["time"]
        ))

    tree.grid(padx=100, pady=50)
    frame.grid(padx=10, pady=10)

    button(frame, "Fechar", command=window.destroy)

    window.mainloop()

def remove_consultation_screen():
    window = tk.Tk()
    window.title("Remover Consulta")

    frame = ttk.Frame(window)

    label(frame, "Remover Consulta", row=0, column=0, padx=10, pady=30, font=("Helvetica", 12))

    label(frame, "Digite o CPF da Consulta:", row=1, column=0, padx=10, pady=10)
    cpf_input = input_entry(frame, row=1, column=1, padx=10, pady=10)

    label(frame, "Data da Consulta (DD/MM/AAAA):", row=2, column=0, padx=10, pady=10)
    date_input = input_entry(frame, row=2, column=1, padx=10, pady=10)

    label(frame, "Hora da Consulta (HH:MM):", row=3, column=0, padx=10, pady=10)
    time_input = input_entry(frame, row=3, column=1, padx=10, pady=10)

    def remove_consultation():
        cpf = cpf_input.get()
        date = date_input.get()
        time = time_input.get()

        if not (cpf and date and time):
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        for consultation in consultations:
            if consultation["cpf"] == cpf and consultation["date"] == date and consultation["time"] == time:
                consultations.remove(consultation)
                messagebox.showinfo("Sucesso", "Consulta removida com sucesso!")
                window.destroy()
                return

        messagebox.showerror("Erro", "Consulta não encontrada. Verifique os dados.")

    button(frame, "Remover Consulta", row=4, column=0, padx=10, pady=10, command=remove_consultation)
    button(frame, "Fechar", row=5, column=1, padx=10, pady=10, command=window.destroy)

    frame.grid(padx=10, pady=10)
    window.mainloop()

def consultation_screen():
    window = tk.Tk()
    window.title("Marcar Consulta")

    frame = ttk.Frame(window)

    label(frame, "Marcar Consulta", row=0, column=0, padx=10, pady=30, font=("Helvetica", 12))

    label(frame, "Digite o CPF do Paciente:", row=1, column=0, padx=10, pady=10)
    cpf_input = input_entry(frame, row=1, column=1, padx=10, pady=10)

    label(frame, "Data da Consulta (DD/MM/AAAA):", row=2, column=0, padx=10, pady=10)
    date_input = input_entry(frame, row=2, column=1, padx=10, pady=10)

    label(frame, "Hora da Consulta (HH:MM):", row=3, column=0, padx=10, pady=10)
    time_input = input_entry(frame, row=3, column=1, padx=10, pady=10)

    def schedule_consultation():
        cpf = cpf_input.get()
        date = date_input.get()
        time = time_input.get()

        if not (cpf and date and time):
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        for patient in patients:
            if patient["cpf"] == cpf:
                consultation = {
                    "cpf": cpf,
                    "date": date,
                    "time": time
                }
                consultations.append(consultation)
                messagebox.showinfo("Sucesso", "Consulta marcada com sucesso!")
                window.destroy()
                return

        messagebox.showerror("Erro", "Paciente não encontrado. Verifique o CPF.")

    button(frame, "Marcar Consulta", row=4, column=0, padx=10, pady=10, command=schedule_consultation)
    button(frame, "Fechar", row=5, column=1, padx=10, pady=10, command=window.destroy)

    frame.grid(padx=10, pady=10)
    window.mainloop()

def remove_patient_screen():
    window = tk.Tk()
    window.title("Remover Paciente")

    frame = ttk.Frame(window)

    label(frame, "Remover Paciente", row=0, column=0, padx=10, pady=30, font=("Helvetica", 12))

    label(frame, "Digite o CPF do Paciente:", row=1, column=0, padx=10, pady=10)
    cpf_input = input_entry(frame, row=1, column=1, padx=10, pady=10)

    def remove_patient():
        cpf = cpf_input.get()
        if not cpf:
            messagebox.showerror("Erro", "Por favor, insira o CPF do paciente.")
            return
        
        for patient in patients:
            if patient["cpf"] == cpf:
                patients.remove(patient)
                messagebox.showinfo("Sucesso", "Paciente removido com sucesso!")
                window.destroy()
                return
        
        messagebox.showerror("Erro", "Paciente não encontrado. Verifique o CPF.")

    button(frame, "Remover Paciente", row=2, column=0, padx=10, pady=10, command=remove_patient)
    button(frame, "Fechar", row=3, column=1, padx=10, pady=10, command=window.destroy)

    frame.grid(padx=10, pady=10)
    window.mainloop()

def update_patient_screen():
    window = tk.Tk()
    window.title("Editar Dados de Paciente")

    frame = ttk.Frame(window)

    label(frame, "Atualizar Dados do Paciente", row=0, column=0, padx=10, pady=30, font=("Helvetica", 12))
    
    label(frame, "Digite o CPF do Paciente:", row=1, column=0, padx=10, pady=10)
    cpf_input = input_entry(frame, row=1, column=1, padx=10, pady=10)

    label(frame, "Nome: ", row=2, column=0, padx=10, pady=10)
    name_input = input_entry(frame, row=2, column=1, padx=10, pady=10)

    label(frame, "Data de Nascimento: ", row=3, column=0, padx=10, pady=10)
    birthday_input = input_entry(frame, row=3, column=1, padx=10, pady=10)

    label(frame, "Sexo: ", row=4, column=0, padx=10, pady=10)
    gender_input = input_entry(frame, row=4, column=1, padx=10, pady=10)

    label(frame, "Endereço: ", row=5, column=0, padx=10, pady=10)
    street_input = input_entry(frame, row=5, column=1, padx=10, pady=10)

    label(frame, "Cidade: ", row=6, column=0, padx=10, pady=10)
    city_input = input_entry(frame, row=6, column=1, padx=10, pady=10)

    label(frame, "Estado: ", row=7, column=0, padx=10, pady=10)
    state_input = input_entry(frame, row=7, column=1, padx=10, pady=10)

    def update_patient_data():
        if not cpf_input.get():
            messagebox.showerror("Erro", "Por favor, insira o CPF do paciente.")
            return
        
        success = update(
            cpf_input.get(),
            name=name_input.get(),
            birthday=birthday_input.get(),
            gender=gender_input.get(),
            street=street_input.get(),
            city=city_input.get(),
            state=state_input.get()
        )

        if success:
            messagebox.showinfo("Sucesso", "Paciente atualizado com sucesso!")
            window.destroy()
        else:
            messagebox.showerror("Erro", "Paciente não encontrado. Verifique o CPF.")

    button(frame, "Atualizar Paciente", row=8, column=0, padx=10, pady=10, columnspan=2, command=update_patient_data)
    button(frame, "Fechar", row=9, column=1, padx=10, pady=10, command=window.destroy)

    frame.grid(padx=100, pady=60)

    window.mainloop()
    
def register_patient_screen():
    window = tk.Tk()
    window.title("Adicionar Paciente")
    
    frame = ttk.Frame(window)
    
    label(frame, "Dados Pessoais", row=0, column=0, padx=10, pady=30, font=("Helvetica", 12))
        
    label(frame, "Nome: ", row=1, column=0, padx=10, pady=10)
    name_input = input_entry(frame, row=1, column=1, padx=10, pady=10)

    label(frame, "Data de nascimento: ", row=2, column=0, padx=10, pady=10)
    birthday_input = input_entry(frame, row=2, column=1, padx=10, pady=10)

    label(frame, "CPF: ", row=3, column=0, padx=10, pady=10)
    cpf_input = input_entry(frame, row=3, column=1, padx=10, pady=10)

    label(frame, "Sexo: ", row=4, column=0, padx=10, pady=10)
    gender_input = input_entry(frame, row=4, column=1, padx=10, pady=10)
    
    separator = ttk.Separator(frame, orient='horizontal')
    separator.grid(row=5, column=0, columnspan=2, pady=20, sticky='ew')
    
    label(frame, "Endereço:", row=6, column=0, padx=10, pady=30)

    label(frame, "Endereço: ", row=7, column=0, padx=10, pady=10)
    street_input = input_entry(frame, row=7, column=1, padx=10, pady=10)

    label(frame, "Cidade: ", row=8, column=0, padx=10, pady=10)
    city_input = input_entry(frame, row=8, column=1, padx=10, pady=10)

    label(frame, "Estado: ", row=9, column=0, padx=10, pady=10)
    state_input = input_entry(frame, row=9, column=1, padx=10, pady=10)
    
    def add_patient():
        
        if(len(cpf_input.get()) != 11):
            messagebox.showerror("Erro", "CPF Inválido")
            return

        if not (name_input.get() and birthday_input.get() and cpf_input.get() and gender_input.get() and street_input.get() and city_input.get() and state_input.get()):
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return
        
        for patient in patients:
            if patient["cpf"] == cpf_input.get():
                messagebox.showerror("Erro", "CPF já cadastrado. Por favor, use um CPF diferente.")
                return
        
        success = create(
            name_input.get(), 
            birthday_input.get(), 
            cpf_input.get(), 
            gender_input.get(), 
            street_input.get(), 
            city_input.get(), 
            state_input.get()
        )
        
        if success:
            messagebox.showinfo("Sucesso", "Paciente adicionado com sucesso!")
            window.destroy() 
        else:
            messagebox.showerror("Erro", "Falha ao adicionar paciente. Tente novamente.")
    
    button(frame, "Adicionar Paciente", row=10, column=0, padx=10, pady=10, columnspan=2, command=add_patient)
    button(frame, "Fechar", row=11, column=1, padx=10, pady=10, command=window.destroy)

    frame.grid(padx=100, pady=60)
    
    window.mainloop()

def dashboard_screen(username):
    window = tk.Tk()
    window.title("Início")
    frame = ttk.Frame(window, padding=20)
    
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)
    
    label(window, text=f"Olá, {username}", font=("Helvetica", 16), row=0, column=0, padx=20, pady=20, columnspan=2)
    label(window, text="Gerenciar Pacientes", font=("Helvetica", 14, 'bold'), row=1, column=0, columnspan=2, padx=10, pady=10)

    button(window, "Adicionar paciente", row=2, column=0, command=register_patient_screen)
    button(window, "Editar paciente", row=3, column=0, command=update_patient_screen)
    button(window, "Remover paciente", row=4, column=0, command=remove_patient_screen)

    separator1 = ttk.Separator(window, orient='horizontal')
    separator1.grid(row=5, column=0, columnspan=2, pady=10, sticky='ew')

    label(window, text="Gerenciar Consultas", font=("Helvetica", 14, 'bold'), row=6, column=0, columnspan=2, padx=10, pady=10)

    button(window, "Marcar consulta", row=7, column=0, command=consultation_screen)
    button(window, "Remover Consulta", row=8, column=0, command=remove_consultation_screen)
    button(window, "Consultas Marcadas", row=9, column=0, command=list_consultation_screen)

    separator2 = ttk.Separator(window, orient='horizontal')
    separator2.grid(row=10, column=0, columnspan=2, pady=10, sticky='ew')

    label(window, text="Lista de Pacientes", font=("Helvetica", 12), row=11, column=0, columnspan=2, padx=10, pady=10)

    button(window, "Todos os Pacientes", row=12, column=0, command=show_patients_screen)
    
    frame.grid(padx=200, pady=20)
    window.mainloop()

# Login Screens

def app():
    window = tk.Tk()
    window.title("Login")
    
    frame = ttk.Frame(window, padding=200)
    
    label(frame, "Usuário", row=0, column=0, padx=10, pady=10)
    label(frame, "Senha", row=1, column=0, padx=10, pady=10)

    username_input = input_entry(frame, row=0, column=1, padx=10, pady=10)
    password_input = input_entry(frame, row=1, column=1, padx=10, pady=10, show="*")

    button(frame, "Login", row=2, column=0, pady=10, columnspan=2, command=lambda: login_action(username_input, password_input, window))
    
    frame.grid(padx=10, pady=10)

    window.mainloop()

# Actions

def login_action(username_input, password_input, window):
    username = username_input.get()
    password = password_input.get()
    
    if user_validate(username, password):
        messagebox.showinfo("Sucesso", "Login realizado com sucesso")
        window.destroy()
        dashboard_screen(username)
    else:
        messagebox.showinfo("Erro", "Usuário ou senha inválidos.")