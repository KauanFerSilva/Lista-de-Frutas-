import time 
print("Lista de frutas disponíveis:")
Frutas = ["Banana", "Uva", "Maça", "Pera"]
Frutas.append("Melancia")
for item in Frutas:
    print (item)
    time.sleep(0.5)
Escolha = str(input("Qual fruta você escolhe?: ")).strip()
print (f"Ótima escolha: {Escolha}")
adicionar_frutas = input("Deseja adicionar mais frutas? (sim/não): ").strip().lower()
while adicionar_frutas == "sim":
    nova_fruta = input("Digite o nome da fruta que deseja adicionar: ").strip()
    Frutas.append(nova_fruta)
    print("Frutas disponíveis:")
    for item in Frutas:
        print(item)
        time.sleep(0.5)
    adicionar_frutas = input("Deseja adicionar mais frutas? (sim/não): ").strip().lower()
if adicionar_frutas == "não":
    print("Obrigado por participar!")
