from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Combobox
import matplotlib.pyplot as plt
main_screen=Tk()
main_screen.title('Sistema Assistência.Técnica')
main_screen.resizable(width=False, height=False)
main_screen_screen_width = main_screen.winfo_screenwidth()
main_screen_screen_height = main_screen.winfo_screenheight()
width_main_screen=600
height_main_screen=380
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
#####################Informações exibidas na tela principal#####################################################
global totalClientes   #total de clientes cadastrados
totalClientes = 0
global totalServicos   #total de serviços feitos  
totalServicos = 0
global totalLucro    #lucro total obtido
totalLucro = sum(lista_valores_servicos) #soma os valores da lista_valores_serviços
global valor
global data
data = ''
global lucroJaneiro 
lucroJaneiro = 0
global lucroFevereiro 
lucroFevereiro = 0
global lucroMarço 
lucroMarço = 0
global lucroAbril 
lucroAbril = 0
global lucroMaio
lucroMaio = 0
global lucroJunho
lucroJunho = 0
global lucroJulho 
lucroJulho = 0
global lucroAgosto
lucroAgosto = 0
global lucroSetembro
lucroSetembro = 0
global lucroOutubro
lucroOutubro = 0
global lucroNovembro 
lucroNovembro = 0
global lucroDezembro 
lucroDezembro = 0
global meses 
global vendas
meses = []
vendas = []
##################################################################################################################

labelsist = Label(main_screen, text="Sistema de Gerenciamento de Assistência Técnica ", font="Arial 18 bold").place(x=10,y=10)
totCadClient = Label(main_screen, text="Total de Clientes Cadastrados:", font="Arial 17").place(x=138,y=60)
totPendServic = Label(main_screen, text="Total de Serviços Pendentes:", font="Arial 17").place(x=142,y=130)
totConcluServic = Label(main_screen, text="Total de Serviços Concluídos:", font="Arial 17").place(x=142,y=210)
totLucro = Label(main_screen, text="Lucro Total:", font="Arial 17").place(x=230,y=290)

totCl = Label(main_screen, text=totalClientes, font="Arial 17")
totCl.place(x=210,y=90)
#totPendServic = Label(main_screen, text="Total de Serviços Pendentes:", font="Arial 17").place(x=142,y=130)
#totConcluServic = Label(main_screen, text="Total de Serviços Concluídos:", font="Arial 17").place(x=142,y=210)
#totLucro = Label(main_screen, text="Lucro Total:", font="Arial 17").place(x=230,y=290)


##################################################################################################################
def clientScreen(): #janela para cadastrar um novo cliente
    client_screen=Toplevel()
    client_screen.title('Sistema Assistência Técnica')
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
        cpf = str(client_cpf.get())
        tel = str(client_tel.get())
        email = str(client_email.get())
        adress = str(client_adress.get())
        if (name=='' or name==' ') or (cpf=='' or cpf==' ') or (tel=='' or tel==' ') or (email=='' or email==' ') or (adress=='' or adress==' '):
            messagebox.showwarning("Erro no Cadastro","Não podem haver campos vazios.")
        else: 
            global totalClientes
            totalClientes += 1
            lista_nome_cliente.append(name)
            lista_cpf_cliente.append(cpf)
            lista_tel_cliente.append(tel)
            lista_email_cliente.append(email)
            lista_endereco_cliente.append(adress)
            client_screen.destroy()
            messagebox.showinfo("Cadastro Cliente","Cliente cadastrado com sucesso!")
            totCl["text"] = totalClientes
            
    clientSave_button = Button(client_screen, text="Salvar", width=12, bd=3, command=client_button_save, cursor="hand2").place(x=155,y=280)
    client_screen.mainloop()
def lista_clientes(): #janela que exibe uma lista com todos os clientes cadastrados
    global totalClientes
    if totalClientes == 0:
        messagebox.showwarning("Erro ao acessar!",'Não tem nenhum cliente cadastrado!')
    else:
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
    def lista_clientes(): #janela que exibe uma lista com todos os clientes cadastrados
        client_list=Toplevel()
        client_list.title('Sistema Assistência.Técnica')
        client_list.resizable(width=False, height=False)
        client_list_screen_width = client_list.winfo_screenwidth()
        client_list_screen_height = client_list.winfo_screenheight()
        width_client_list=340
        height_client_list=420
        x_client_list=(client_list_screen_width/2) - (width_client_list/2)
        y_client_list=(client_list_screen_height/2) - (height_client_list/2)
        client_list.geometry('%dx%d+%d+%d'%(width_client_list,height_client_list,x_client_list,y_client_list-40))
        client_list['bg']='#4f4cce'
        cadListClient = Label(client_list, text="Clientes Cadastrados", bg='#4f4cce', fg='white', font="Arial 18").place(x=50,y=10)
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
        ok_client_list = Button(client_list, text='Ok', width=8, bd=3, command=ok_client_list_button, cursor="hand2").place(x=230,y=380)    
        def verInfo_button(): #janela que exibe as informações do cliente selecionado
            info_client=Toplevel()
            info_client.title('Sistema Assistência.Técnica')
            info_client.resizable(width=False, height=False)
            info_client_screen_width = info_client.winfo_screenwidth()
            info_client_screen_height = info_client.winfo_screenheight()
            width_info_client=380
            height_info_client=234
            info_client['bg']='#4f4cce'
            x_info_client=(info_client_screen_width/2) - (width_info_client/2)
            y_info_client=(info_client_screen_height/2) - (height_info_client/2)
            info_client.geometry('%dx%d+%d+%d'%(width_info_client,height_info_client,x_info_client,y_info_client-40))
            infoLabel = Label(info_client, text="Informações do Cliente", bg='#4f4cce', fg='white', font="Arial 18").place(x=62,y=10)

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
            okInfo_button = Button(info_client, text='Ok', command=fecharInfoClient, width=8, bd=3, cursor="hand2").place(x=158,y=200)
            info_client.mainloop()   
        info_client_button = Button(client_list, text='Informações', bd=3, command=verInfo_button, cursor="hand2").place(x=120,y=380)
        client_list.mainloop()
def serviceScreen():
    service_screen=Toplevel()
    service_screen.title('Sistema Assistência.Técnica')
    service_screen.resizable(width=False, height=False)
    service_screen_screen_width = service_screen.winfo_screenwidth()
    service_screen_screen_height = service_screen.winfo_screenheight()
    width_service_screen=400
    height_service_screen=335
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

    client = Label(service_screen, text="Cliente:", font="Arial").place(x=170, y=238)
    clientes = lista_nome_cliente
    clientes = Combobox(service_screen, values=clientes, width=45, state='readonly')
    if len(lista_nome_cliente) > 0:
        clientes.current(0)
    clientes.place(x=55, y=262)

    def salvarServiço():
        global totalServicos
        global valor
        global data
        totalServicos += 1
        valor = str(client_value.get()).replace(",",".")
        def isnumber(valor):
            try:
                float(valor)
            except ValueError:
                return False
            return True
        if valor == '':
            print('vazio')
        else:
            valor = float(valor)
        lista_valores_servicos.append(valor)
        data = str(client_data.get()).upper()
        lista_datas_servicos.append(data)
        if valor==None:
            print('vazio')
        print(valor,type(valor))

        totalLucro = sum(lista_valores_servicos)       
        print(totalLucro)

        print(lista_valores_servicos)
        service_screen.destroy()
    newService_bt = Button(service_screen, text="Salvar", width=8, bd=3, command=salvarServiço).place(x=165,y=295)
    service_screen.mainloop()
def infoScreen():
    info_screen=Toplevel()
    info_screen.title('Sistema Assistência.Técnica')
    info_screen.resizable(width=False, height=False)
    info_screen['bg']='#6763fd'
    info_screen_screen_width = info_screen.winfo_screenwidth()
    info_screen_screen_height = info_screen.winfo_screenheight()
    width_info_screen=450
    height_info_screen=270
    x_info_screen=(info_screen_screen_width/2) - (width_info_screen/2)
    y_info_screen=(info_screen_screen_height/2) - (height_info_screen/2)
    info_screen.geometry('%dx%d+%d+%d'%(width_info_screen,height_info_screen,x_info_screen,y_info_screen-40))
    info = Label(info_screen, text="Informações:", bg='#6763fd', font="Arial 18", fg='white').place(x=150,y=10)
    more_info = Label(info_screen, text="Sistema de Gerenciamento de Assistência Técnica", bg='#6763fd', font="Arial 15").place(x=0,y=48)
    more_info2 = Label(info_screen, text="Desenvolvido por:", bg='#6763fd', font="Arial 15", fg='white').place(x=141,y=80)
    more_info3 = Label(info_screen, text="Gabriel Monteiro Duete", bg='#6763fd', font="Arial 14").place(x=115,y=110)
    more_info4 = Label(info_screen, text="Rafael Candido Lacerda Carvalho", bg='#6763fd', font="Arial 14").place(x=70,y=140)
    more_info5 = Label(info_screen, text="Samuel Vitor de França Veras", bg='#6763fd', font="Arial 14").place(x=90,y=170)
    more_info6 = Label(info_screen, text="2° Semestre - IFCE CRATO", bg='#6763fd', font="Arial 14", fg='white').place(x=100,y=200)
    def ok_info():
        info_screen.destroy()
    ok = Button(info_screen, text="Ok", width=8, bd=3, command=ok_info).place(x=190, y=235)

    info_screen.mainloop()
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
    if data == '':
        messagebox.showwarning("Erro!", "Nenhum mês foi cadastrado!")
    else:
        if data[3] == '0' and data[4] == '1':
            lucroJaneiro += valor
        elif data[3] == '0' and data[4] == '2':
            lucroFevereiro += valor
        elif data[3] == '0' and data[4] == '3':
            lucroMarço += valor
        elif data[3] == '0' and data[4] == '4':
            lucroAbril += valor
        elif data[3] == '0' and data[4] == '5':
            lucroMaio += valor
        elif data[3] == '0' and data[4] == '6':
            lucroJunho += valor
        elif data[3] == '0' and data[4] == '7':
            lucroJulho += valor
        elif data[3] == '0' and data[4] == '8':
            lucroAgosto += valor
        elif data[3] == '0' and data[4] == '9':
            lucroSetembro += valor
        elif data[3] == '1' and data[4] == '0':
            lucroOutubro += valor
        elif data[3] == '1' and data[4] == '1':
            lucroNovembro += valor
        elif data[3] == '1' and data[4] == '2':
            lucroDezembro += valor
        else:
            messagebox.showwarning("Atenção!", "Nenhum mês foi cadastrado!")
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
    lucros.add_command(label ='Limpa Gráfico', command=limparGrafico)
    
    info = Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='Informações', menu = info)
    info.add_command(label ='Informações sobre o Sistema', command=infoScreen)  
    
    main_screen.config(menu = menubar) 
menu()



main_screen.mainloop()
