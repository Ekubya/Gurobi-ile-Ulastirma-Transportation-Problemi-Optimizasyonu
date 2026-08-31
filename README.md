##ENGLISH
# Transportation Problem Optimization with Gurobi

This project involves modeling and solving the **Transportation Problem**, a classic problem in operations research, using Python and the Gurobi Optimization Solver (`gurobipy`).
The project is solved using Python + Gurobi.
The main objective of the project is to find the optimal distribution plan that minimizes the cost of transporting products from factories with specific capacities to regions with specific demands.

## 🧮 Mathematical Model

The mathematical formulation of the transportation model is as follows:

### Sets (Indices)
* I: Set of factories (i = 1, 2, ..., 5)
* J: Set of demand regions (j = 1, 2, ..., 4)

### Parameters
* a_i: Total production capacity of factory i (Supply)
* b_j: Total product demand of region j (Demand)
* c_ij: Transportation cost of sending one unit of product from factory i to region j

```python
a = [200, 200, 200, 200, 200] # Capacities of the factories
b = [250, 300, 150, 300]      # Demands of the regions
c = [[4, 3, 5, 2],            # Unit transportation costs from factories to regions
     [5, 8, 2, 7],
     [4, 5, 3, 6],
     [2, 5, 7, 4],
     [4, 4, 3, 2]]          
```

### Decision Variables
* x_ij: Amount of product to be transported from factory i to region j (x_ij ≥ 0)

### Objective Function
The objective is to minimize the total transportation cost:

Min Z = Σ(i) Σ(j) [ c_ij * x_ij ]

### Constraints
**1. Capacity (Supply) Constraints:**
The total amount of products sent from each factory to the regions cannot exceed the capacity of that factory.
* Σ(j) x_ij ≤ a_i   (For each factory i)

**2. Demand Constraints:**
The required product amount for each region must be fully met.
* Σ(i) x_ij = b_j   (For each region j)

**3. Non-negativity Constraint:**
The amount of transported product cannot be negative.
* x_ij ≥ 0          (For all i and j)

## 📊 Example Output

```text
Optimal solution found.
x_1_1: 0.0
x_1_2: 100.0
x_1_3: 0.0
x_1_4: 100.0
x_2_1: 50.0
x_2_2: 0.0
x_2_3: 150.0
x_2_4: 0.0
x_3_1: 0.0
x_3_2: 200.0
x_3_3: 0.0
x_3_4: 0.0
x_4_1: 200.0
x_4_2: 0.0
x_4_3: 0.0
x_4_4: 0.0
x_5_1: 0.0
x_5_2: 0.0
x_5_3: 0.0
x_5_4: 200.0
Optimal value: 2850.0
```

As a result of optimizing the model, the lowest possible transportation cost (Optimal Value) that satisfies all constraints was found to be 2,850.0 units.

## 💻 Installation and Usage

### Requirements
To run this code, you must have Python installed on your computer and have the following library/license:
* `gurobipy` (Gurobi interface for Python)
* A valid Gurobi license (A free license is available for academic use).

##TURKISH
# Gurobi-ile-Ulastırma-Transportation-Problemi-Optimizasyonu

Bu proje, yöneylem araştırmasında klasik bir problem olan **Ulaştırma Probleminin (Transportation Problem)** Python ve Gurobi Optimizasyon Çözücüsü (Gurobipy) kullanılarak modellenmesini ve çözülmesini içermektedir.
Proje gurobi + python ile çözülmüştür.
Projenin temel amacı, belirli kapasitelere sahip fabrikalardan, belirli talepleri olan bölgelere minimum maliyetle ürün taşımını sağlayacak optimum dağıtım planını bulmaktır.

## 🧮 Matematiksel Model

Ulaştırma modelinin matematiksel formülasyonu aşağıdaki gibidir:

### Kümeler (İndisler)
* I: Fabrikalar kümesi (i = 1, 2, ..., 5)
* J: Talep bölgeleri kümesi (j = 1, 2, ..., 4)

### Parametreler
* a_i: i. fabrikanın toplam üretim kapasitesi (Supply)
* b_j: j. bölgenin toplam ürün talebi (Demand)
* c_ij: i. fabrikadan j. bölgeye bir birim ürün göndermenin taşıma maliyeti

a = [200, 200, 200, 200, 200] # Fabrikaların kapasiteleri
b = [250, 300, 150, 300]      # Bölgelerin talepleri
c = [[4, 3, 5, 2],            # Fabrikalardan bölgelere birim taşıma maliyeti
     [5, 8, 2, 7],
     [4, 5, 3, 6],
     [2, 5, 7, 4],
     [4, 4, 3, 2]]          

### Karar Değişkenleri
* x_ij: i. fabrikadan j. bölgeye taşınacak olan ürün miktarı (x_ij ≥ 0)

### Amaç Fonksiyonu
Toplam taşıma maliyetini minimize etmek hedeflenmektedir:

Min Z = Σ(i) Σ(j) [ c_ij * x_ij ]

### Kısıtlar
**1. Kapasite (Arz) Kısıtları:**
Her bir fabrikadan bölgelere gönderilen toplam ürün miktarı, o fabrikanın kapasitesini aşamaz.
* Σ(j) x_ij ≤ a_i   (Her i fabrikası için)

**2. Talep Kısıtları:**
Her bir bölgenin ihtiyacı olan ürün miktarı tam olarak karşılanmalıdır.
* Σ(i) x_ij = b_j   (Her j bölgesi için)

**3. İşaret Kısıtı:**
Taşınan ürün miktarı negatif olamaz.
* x_ij ≥ 0          (Tüm i ve j'ler için)

## 📊 Örnek Çıktı(Example Output)
Optimum çözüm bulundu.
x_1_1: 0.0
x_1_2: 100.0
x_1_3: 0.0
x_1_4: 100.0
x_2_1: 50.0
x_2_2: 0.0
x_2_3: 150.0
x_2_4: 0.0
x_3_1: 0.0
x_3_2: 200.0
x_3_3: 0.0
x_3_4: 0.0
x_4_1: 200.0
x_4_2: 0.0
x_4_3: 0.0
x_4_4: 0.0
x_5_1: 0.0
x_5_2: 0.0
x_5_3: 0.0
x_5_4: 200.0
Optimum değer: 2850.0

Modelin optimize edilmesi sonucunda, tüm kısıtlar sağlanarak elde edilebilecek en düşük taşıma maliyeti (Optimum Değer) 2850.0 birim olarak bulunmuştur.

## 💻 Kurulum ve Kullanım

### Gereksinimler
Bu kodu çalıştırabilmek için bilgisayarınızda Python yüklü olmalı ve aşağıdaki kütüphaneye/lisansa sahip olmalısınız:
* `gurobipy` (Python için Gurobi arayüzü)
* Geçerli bir Gurobi lisansı (Akademik kullanım için ücretsiz lisans alınabilir).
