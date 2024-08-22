import os
from datetime import datetime

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
aviso = ""
def clear_terminal():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para macOS ou Linux
    else:
        os.system('clear')

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

while True:
   clear_terminal() # limpando terminal no vs code
   print("\n" + " SISTEMA DE CONTA CORRENTE - DIÁRIO & MONOUSUÁRIO ".title().center(100,"*"))
   print(f"Saldo atual: {saldo}")
   print("\n"+aviso)
   opcao = input("\nSelecione uma opção: " + menu)
   if opcao == 'd':
      valor = float(input("Informe o valor do depósito: "))
      if valor > 0:
         saldo += valor
         extrato += f"{datetime.now()} - Depósito: R$ {valor:.2f}\n"
      else:
         aviso = "Aviso: Operação de DEPÓSITO falhou. Valor informado inválido. "
   elif opcao == 's':
      valor = float(input("Informe o valor do saque: "))
      excedeu_saldo = valor > saldo
      excedeu_limite = valor > limite
      excedeu_saques = numero_saques >= LIMITE_SAQUES
      if excedeu_saldo:
            aviso ="Aviso: Operação de SAQEUE falhou! Você não tem saldo suficiente. "
      elif excedeu_limite:
            aviso =f"Aviso: Operação de SAQEUE falhou! O valor do saque excede o limite diário: R$ {limite:.2f} "
      elif excedeu_saques:
            aviso =f"Aviso: Operação de SAQEUE falhou! Número máximo de saques diários {LIMITE_SAQUES} excedido. "
      elif valor > 0:
            saldo -= valor
            extrato += f"{datetime.now()} - Saque: R$ {valor:.2f}\n"
            numero_saques += 1
      else:
            aviso ="Aviso: Operação falhou! O valor informado é inválido."
   elif opcao == 'e':
      print("\n=================== EXTRATO ====================")
      print("Não foram realizadas movimentações." if not extrato else extrato)
      print(f"\nSaldo: R$ {saldo:.2f}")
      print("=================================================")
      input("Tecle ENTER P/ CONTINUAR ")
   elif opcao == 'q':
      clear_terminal() # limpando terminal no vs code
      break
   else:
      aviso ="Aviso: Operação inválida, por favor selecione novamente a operação desejada."

