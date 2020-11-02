from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import matplotlib.pyplot as plt
main_screen=Tk()
main_screen.title('Sistema Assist.Tecnica')
main_screen.resizable(width=False, height=False)
main_screen_screen_width = main_screen.winfo_screenwidth()
main_screen_screen_height = main_screen.winfo_screenheight()
width_main_screen=500
height_main_screen=450
x_main_screen=(main_screen_screen_width/2) - (width_main_screen/2)
y_main_screen=(main_screen_screen_height/2) - (height_main_screen/2)
main_screen.geometry('%dx%d+%d+%d'%(width_main_screen,height_main_screen,x_main_screen,y_main_screen-40))
####################Listas que armazenam as informações do cliente/serviços####################################
lista_nome_cliente = []
lista_cpf_cliente = []
lista_tel_cliente = []
lista_email_cliente = []
lista_endereco_cliente = []
lista_valores_servicos = []
lista_datas_servicos = []
#####################Informações exibidas na tela principal###########################################
global totalClientes   #total de clientes cadastrados
totalClientes = 0
global totalServiços   #total de serviços feitos  
totalServiços = 0
global totalLucro    #lucro total obtido
totalLucro = sum(lista_valores_servicos) #somar os valores da lista_valores_serviços

global valor 
global data

global lucroJaneiro 
global lucroFevereiro 
global lucroMarço 
global lucroAbril 
global lucroMaio
global lucroJunho
global lucroJulho 
global lucroAgosto
global lucroSetembro
global lucroOutubro
global lucroNovembro 
global lucroDezembro 

lucroJaneiro = 0
lucroFevereiro = 0
lucroMarço = 0
lucroAbril = 0
lucroMaio = 0
lucroJunho = 0
lucroJulho = 0
lucroAgosto = 0
lucroSetembro = 0
lucroOutubro = 0
lucroNovembro = 0
lucroDezembro = 0

global meses 
global vendas
meses = list()
vendas = list()
#######################################################################################################


################################ JANELA PARA CADASTRAR UM NOVO CLIENTE ###################################
def clientScreen(): 
    client_screen=Toplevel()
    client_screen.title('Sistema Assistência Tecnica')
    client_screen.resizable(width=False, height=False)
    client_screen_screen_width = client_screen.winfo_screenwidth()
    client_screen_screen_height = client_screen.winfo_screenheight()
    width_client_screen=400
    height_client_screen=320
    x_client_screen=(client_screen_screen_width/2) - (width_client_screen/2)
    y_client_screen=(client_screen_screen_height/2) - (height_client_screen/2)
    client_screen.geometry('%dx%d+%d+%d'%(width_client_screen,height_client_screen,x_client_screen,y_client_screen-40))
    cadastroCliente_label = Label(client_screen, text="Cadastrar Cliente", font="Arial 18").place(x=105,y=10)

    name_label = Label(client_screen, text="Nome:", font="Arial").place(x=38,y=46)
    client_name = Entry(client_screen, font="Arial", bd=4, width=35)  #nome do cliente
    client_name.place(x=38,y=70)
    client_name.focus()
    
    cpf_label = Label(client_screen, text="Cpf:", font="Arial").place(x=38,y=101)
    client_cpf = Entry(client_screen, font="Arial", bd=4, width=16)  #cpf do cliente
    client_cpf.place(x=38,y=125)

    tel_label = Label(client_screen, text="Telefone:", font="Arial").place(x=210,y=101)
    client_tel = Entry(client_screen, font="Arial", bd=4, width=16)  #telefone do cliente
    client_tel.place(x=210,y=125)

    email_label = Label(client_screen, text="Email:", font="Arial").place(x=38,y=156)
    client_email = Entry(client_screen, font="Arial", bd=4, width=35) #email do cliente
    client_email.place(x=38,y=180)
    
    adress_label = Label(client_screen, text="Endereço: (Rua/N°/Bairro)", font="Arial").place(x=38,y=211)
    client_adress = Entry(client_screen, font="Arial", bd=4, width=35) #endereço do cliente
    client_adress.place(x=38,y=235)

    def client_button_save(): #janela para cadastrar um novo cliente
        name = str(client_name.get())
        lista_nome_cliente.append(name)
        cpf = str(client_cpf.get())
        lista_cpf_cliente.append(cpf)
        tel = str(client_tel.get())
        lista_tel_cliente.append(tel)
        email =str(client_email.get())
        lista_email_cliente.append(email)
        adress =str(client_adress.get())
        lista_endereco_cliente.append(adress)
        if (name=='' or name==' ') or (cpf=='' or cpf==' ') or (tel=='' or tel==' ') or (email=='' or email==' ') or (adress=='' or adress==' '):
            print('nao pode')
        else: 
            global totalClientes
            totalClientes+=1
            messagebox.showinfo("Cadastro Cliente","Cliente cadastrado com sucesso!")
            client_screen.destroy()
    clientSave_button = Button(client_screen, text="Salvar", width=12, bd=3, command=client_button_save, cursor="hand2").place(x=155,y=280)
    client_screen.mainloop()
def lista_clientes(): #janela que exibe uma lista com todos os clientes cadastrados
    client_list=Toplevel()
    client_list.title('Sistema Assist.Tecnica')
    client_list.resizable(width=False, height=False)
    client_list_screen_width = client_list.winfo_screenwidth()
    client_list_screen_height = client_list.winfo_screenheight()
    width_client_list=430
    height_client_list=400
    x_client_list=(client_list_screen_width/2) - (width_client_list/2)
    y_client_list=(client_list_screen_height/2) - (height_client_list/2)
    client_list.geometry('%dx%d+%d+%d'%(width_client_list,height_client_list,x_client_list,y_client_list-40))
    cadListClient = Label(client_list, text="Clientes Cadastrados", font="Arial 18").place(x=92,y=10)

    scrollbar = Scrollbar(client_list)
    scrollbar.pack(side=RIGHT, fill=Y)
    listaClientes = Listbox(client_list, font="Arial 15", height=13, width=25)
    listaClientes.place(x=20,y=55)
    for cliente_add in lista_nome_cliente:
        listaClientes.insert(END, cliente_add)
        listaClientes.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listaClientes.yview)
    def ok_client_list_button():
        client_list.destroy()
    ok_client_list = Button(client_list, text='Ok', width=6, command=ok_client_list_button, cursor="hand2").place(x=328,y=270)    
    def verInfo_button(): #janela que exibe as informações do cliente selecionado
        info_client=Toplevel()
        info_client.title('Sistema Assist.Tecnica')
        info_client.resizable(width=False, height=False)
        info_client_screen_width = info_client.winfo_screenwidth()
        info_client_screen_height = info_client.winfo_screenheight()
        width_info_client=380
        height_info_client=234
        x_info_client=(info_client_screen_width/2) - (width_info_client/2)
        y_info_client=(info_client_screen_height/2) - (height_info_client/2)
        info_client.geometry('%dx%d+%d+%d'%(width_info_client,height_info_client,x_info_client,y_info_client-40))
        infoLabel = Label(info_client, text="Informações do Cliente", font="Arial 18").place(x=62,y=10)

        indice = listaClientes.curselection()[0]
        indiceNome = lista_nome_cliente[indice]
        indiceCPF = lista_cpf_cliente[indice]
        indiceTel = lista_tel_cliente[indice]
        indiceEmail = lista_email_cliente[indice]
        indiceAdress = lista_endereco_cliente[indice]

        name = StringVar() 
        name.set(indiceNome) 
        client_name = Entry(info_client, textvariable=name, font="Arial", bd=4, width=35, state=DISABLED).place(x=28,y=55)

        cpf = StringVar() 
        cpf.set(indiceCPF)
        client_cpf = Entry(info_client, textvariable=cpf, font="Arial", bd=4, width=16, state=DISABLED).place(x=28,y=90)

        tel = StringVar() 
        tel.set(indiceTel)
        client_tel = Entry(info_client, textvariable=tel, font="Arial", bd=4, width=16, state=DISABLED).place(x=200,y=90)

        email = StringVar() 
        email.set(indiceEmail)
        client_email = Entry(info_client, textvariable=email, font="Arial", bd=4, width=35, state=DISABLED).place(x=28,y=125)
            
        adress = StringVar() 
        adress.set(indiceAdress)
        client_adress = Entry(info_client, textvariable=adress, font="Arial", bd=4, width=35, state=DISABLED).place(x=28,y=160)

        def fecharInfoClient():
            info_client.destroy()
        okInfo_button = Button(info_client, text='Ok', command=fecharInfoClient, width=8, cursor="hand2").place(x=158,y=200)
        info_client.mainloop()
    info_client_button = Button(client_list, text='Informações', command=verInfo_button, cursor="hand2").place(x=318,y=170)
    client_list.mainloop()
def serviceScreen():
    service_screen=Toplevel()
    service_screen.title('Sistema Assist.Tecnica')
    service_screen.resizable(width=False, height=False)
    service_screen_screen_width = service_screen.winfo_screenwidth()
    service_screen_screen_height = service_screen.winfo_screenheight()
    width_service_screen=400
    height_service_screen=280
    x_service_screen=(service_screen_screen_width/2) - (width_service_screen/2)
    y_service_screen=(service_screen_screen_height/2) - (height_service_screen/2)
    service_screen.geometry('%dx%d+%d+%d'%(width_service_screen,height_service_screen,x_service_screen,y_service_screen-40))
    newService = Label(service_screen, text="Novo Serviço", font="Arial 18").place(x=130,y=10)

    service = Label(service_screen, text="Descrição do Serviço:", font="Arial").place(x=38,y=46)
    client_service = scrolledtext.ScrolledText(service_screen, width=35, height=5, font="Arial") #essa é aquela caixa grande que aparece, é pra a gente descrever o problema do pc do cliente e tals
    client_service.place(x=38,y=70)

    data = Label(service_screen, text="Data:", font="Arial").place(x=38,y=176)
    client_data = Entry(service_screen, font="Arial", bd=4, width=14) #coloca a data do dia ( queria ver se eu colocava pro service_screen pegar a data atual do dia, usando alguma biblioteca ou sla)
    client_data.place(x=38,y=200)

    value = Label(service_screen, text="Valor:", font="Arial").place(x=230,y=176)
    rs = Label(service_screen, text="R$:", font="Arial").place(x=200,y=202)
    client_value = Entry(service_screen, font="Arial", bd=4, width=14)  #esse campo pega o valor que vai custar pra ajeitar o problema do cliente
    client_value.place(x=230,y=200)

    def salvarServiço():
        global totalServiços
        global valor
        global data
        totalServiços += 1
        valor = str(client_value.get()).replace(",",".")
        def isnumber(valor):
            try:
                float(valor)
            except ValueError:
                return False
            return True
        if valor=='':
            print('vazio')
        else:
            valor = float(valor)
        lista_valores_servicos.append(valor)
        data = str(client_data.get()).upper()
        lista_datas_servicos.append(data)
        if valor==None:
            print('vazio')
        print(valor,type(valor))
        print(totalLucro)
        service_screen.destroy()
            
    newService_bt = Button(service_screen, text="Salvar", width=8, command=salvarServiço).place(x=165,y=245)
    service_screen.mainloop()

######################## FUNÇÃO DO GRÁFICO #########################
def graficoLucros():
    global valor
    global data
    global lucroJaneiro 
    global lucroFevereiro 
    global lucroMarço 
    global lucroAbril 
    global lucroMaio
    global lucroJunho
    global lucroJulho 
    global lucroAgosto
    global lucroSetembro
    global lucroOutubro
    global lucroNovembro 
    global lucroDezembro
    global meses
    global vendas
    if "JANEIRO" in data:
        lucroJaneiro += valor
    elif "FEVEREIRO" in data:
        lucroFevereiro += valor
    elif "MARÇO" in data:
        lucroMarço += valor
    elif "ABRIL" in data:
        lucroAbril += valor
    elif "MAIO" in data:
        lucroMaio += valor
    elif "JUNHO" in data:
        lucroJunho += valor
    elif "JULHO" in data:
        lucroJulho += valor
    elif "AGOSTO" in data:
        lucroAgosto += valor
    elif "SETEMBRO" in data:
        lucroSetembro += valor
    elif "OUTUBRO" in data:
        lucroOutubro += valor
    elif "NOVEMBRO" in data:
        lucroNovembro += valor
    elif "DEZEMBRO" in data:
        lucroDezembro += valor
    meses = ['JANEIRO','FEVEREIRO','MARÇO','ABRIL','MAIO','JUNHO','JULHO','AGOSTO','SETEMBRO','OUTUBRO','NOVEMBRO','DEZEMBRO']
    vendas = [lucroJaneiro, lucroFevereiro, lucroMarço, lucroAbril, lucroMaio, lucroJunho, lucroJulho, lucroAgosto, lucroSetembro, lucroOutubro, lucroNovembro, lucroDezembro]
    print(lucroJaneiro)
    plt.title('Gráfico de ganhos do ano')
    plt.xlabel('Meses')
    plt.ylabel('Valores das vendas')
    plt.barh(meses, vendas, color='blue')
    plt.show()

def limparGrafico():
    global lucroJaneiro 
    global lucroFevereiro 
    global lucroMarço 
    global lucroAbril 
    global lucroMaio
    global lucroJunho
    global lucroJulho 
    global lucroAgosto
    global lucroSetembro
    global lucroOutubro
    global lucroNovembro 
    global lucroDezembro
    global meses
    global vendas
    lucroJaneiro = 0
    lucroFevereiro = 0
    lucroMarço = 0
    lucroAbril = 0
    lucroMaio = 0
    lucroJunho = 0
    lucroJulho = 0
    lucroAgosto = 0
    lucroSetembro = 0
    lucroOutubro = 0
    lucroNovembro = 0
    lucroDezembro = 0
    vendas = [lucroJaneiro, lucroFevereiro, lucroMarço, lucroAbril, lucroMaio, lucroJunho, lucroJulho, lucroAgosto, lucroSetembro, lucroOutubro, lucroNovembro, lucroDezembro]
    print(lucroJaneiro)
 

def menu(): #barra de menus, onde cada opção irá abrir uma janela
    menubar = Menu(main_screen) 
    clientes = Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='Clientes', menu = clientes) 
    clientes.add_command(label ='Novo Cliente', command=clientScreen)
    clientes.add_separator()
    clientes.add_command(label ='Lista de Clientes', command=lista_clientes)

    serviços = Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='Serviços', menu = serviços)
    serviços.add_command(label ='Novo Serviço', command=serviceScreen)
    serviços.add_separator()
    serviços.add_command(label ='Serviços Pendentes', command=print('rafa'))
    serviços.add_command(label ='Serviços Concluídos', command=print('rafa'))

    lucros = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = 'Lucros', menu = lucros)
    lucros.add_command(label ='Gráfico de Lucros', command=graficoLucros)
    lucros.add_command(label ='Limpar Gráfico', command=limparGrafico)
    
    info = Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='Informações', menu = info) 
    info.add_command(label ='Informações sobre o Sistema', command=print('rafa'))  
    
    main_screen.config(menu = menubar) 
totClient = Label(main_screen, text="Total de Clientes Cadastrados:", font="Arial 18").place(x=105,y=50)
'''totCl = Label(main_screen, text=totalClientes, font="Arial 18").place(x=150,y=80)
totCl ["text"] = totalClientes'''
menu()
main_screen.mainloop()

#colocar o cursor do dedo nos botoes e listas
