import customtkinter as ctk

def validar_login():
   usuario = entrada_usuario.get()
   senha = entrada_senha.get()

   if usuario == 'admin' and senha == 'senha':
      resultado_login.configure(text='Login feito com sucesso',text_color='green')
   elif usuario == '' or senha == '':
      resultado_login.configure(text='Informe usuário e senha',text_color='yellow')
   else:
      resultado_login.configure(text='Login e/ou senha incorretos',text_color='red')


#Configuração aparência
ctk.set_appearance_mode('dark')

#Criação da janela princiapl
app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x300')

#Criação dos campos
label_usuario = ctk.CTkLabel(app, text='Usuário')
label_usuario.pack(pady=10)

entrada_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu usuário')
entrada_usuario.pack()

label_senha = ctk.CTkLabel(app, text='Senha')
label_senha.pack(pady=10)

entrada_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha',show='*')
entrada_senha.pack()

ctk.CTkButton(app, text='Login', command=validar_login).pack(pady=10)

resultado_login = ctk.CTkLabel(app, text='')
resultado_login.pack(pady=10)
#Iniciar a aplicação
app.mainloop()