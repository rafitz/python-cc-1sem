tam = float(input("Tamanho do arquivo (Gbyte):"))
vel = int(input("Velocidade da rede (Mbit/s):"))

tam_mb = tam * 1024 * 8
ts = int(tam_mb / vel)
tm = ts // 60
ts %= 60 
print(f"\nTempo gasto de Download = {tm} min e {ts} seg")