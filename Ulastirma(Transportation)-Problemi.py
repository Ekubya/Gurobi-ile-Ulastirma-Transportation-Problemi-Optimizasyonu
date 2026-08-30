import gurobipy as gp

#indis kümesi
i_kumesi=[i for i in range(1,5+1)]
j_kumesi=[j for j in range(1,4+1)]

# Parametreler
a = [200, 200, 200, 200, 200] #fabrikaların kapasiteleri
b = [250, 300, 150, 300] #bölgelerin talepleri
c = [[4, 3, 5, 2],
     [5, 8, 2, 7],
     [4, 5, 3, 6],
     [2, 5, 7, 4],
     [4, 4, 3, 2]] # fabrikalardan bölgelere bir birim ürün taşıma maliyeti

#Model oluşturma
model = gp.Model("ulastirma")

# Karar degiskeni
x = model.addVars(i_kumesi, j_kumesi, vtype=gp.GRB.CONTINUOUS, name='xij')

# Amaç fonksiyonu
z=sum(c[i-1][j-1]*x[i,j] for i in range(1,len(i_kumesi)+1) for j in range(1,len(j_kumesi)+1))

model.setObjective(z, gp.GRB.MINIMIZE)

#Kısıtlar
k1=model.addConstrs(gp.quicksum(x[i,j] for j in range(1,len(j_kumesi)+1)) <= a[i-1] for i in range(1, len(i_kumesi)+1))

#Modelin optimize edilmesi
model.optimize()

# Sonuçları yazdırma
if model.status == gp.GRB.OPTIMAL:
    print("Optimum çözüm bulundu.")
    for i in range(1, len(i_kumesi)+1):
        for j in range(1, len(j_kumesi)+1):
            print(f"x_{i}_{j}:", x[i, j].x)
    print("Optimum değer:", model.objVal)
else:
    print("Optimum çözüm bulunamadı.")
