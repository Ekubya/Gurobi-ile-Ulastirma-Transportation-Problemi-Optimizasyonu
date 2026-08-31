##ENGLISH
# 🚀 Multi-Objective Preemptive Goal Programming with GAMS

This project is a Mixed Integer Programming (MIP) model developed to solve **Multi-Objective Optimization** problems frequently encountered in supply chain and logistics network planning. 

The model uses the **Preemptive Goal Programming** approach to manage conflicting objectives. The problem is modeled in GAMS (General Algebraic Modeling System) and solved using the CPLEX solver.

## 📖 Business Case: Logistics Network Optimization

A company needs to urgently transfer a total of **7,000 pallets** of products from its main distribution center to a regional warehouse. There are **4 different logistics fleets / transportation routes** agreed upon for this shipment. Each fleet has:
* A different maximum carrying capacity 
* A transportation cost per unit pallet 
* A **Delivery Reliability Score** calculated based on past delivery times and damage-free rates. *(Note: Low-cost fleets generally have relatively lower scores).*

**Decision Problem:** How many pallets should be allocated to which fleet?

Management wants the transportation budget for this operation not to exceed **13,700** units (Cost Objective); while to ensure customer satisfaction, they demand the average delivery reliability score of the shipment not to fall below **4.71** (Service Level Objective). The model optimally balances the conflicting cost and delivery quality objectives.

## 🎯 Methodology

This model is solved using a **two-stage (Preemptive)** approach:
* **Stage 1:** The deviation from the first priority, the cost objective (positive deviation - $s2p$), is minimized.
* **Stage 2:** While preserving the optimal value of the first objective (adding it as a hard constraint), the deviation from the second priority, the average score objective (negative deviation - $s1n$), is minimized.

## 📊 Mathematical Model

**Parameters:**
* $k_i$: Maximum carrying capacity of fleet $i$ (Respectively: 4,000, 2,000, 3,000, 5,000)
* $c_i$: Unit transportation cost of fleet $i$ (Respectively: 2, 1.8, 2.1, 2.2)
* $q_i$: Unit reliability score of fleet $i$ (Respectively: 3, 2, 4, 5)
* $t$: Total amount of pallets to be transported (7,000)

**Decision Variables:**
* $x_i$: Amount of pallets to be assigned to fleet $i$ (Integer)
* $s1n, s1p$: Negative and positive deviation variables for Objective 1 (Reliability Score)
* $s2n, s2p$: Negative and positive deviation variables for Objective 2 (Cost)

**Constraints:**
1. **Capacity Constraint:** Each fleet is limited by its own maximum carrying capacity, and due to safety/infrastructure requirements, no fleet can be loaded with more than 5,000 units.
2. **Demand Constraint:** The total transfer demand must be met exactly.

## 🛠️ Technologies Used
* **Language/Platform:** GAMS (General Algebraic Modeling System)
* **Solver:** IBM ILOG CPLEX (for MIP)
* **Optimization Type:** Mixed Integer Programming (MIP)

## 🚀 Installation and Usage

1. Ensure [GAMS](https://www.gams.com/) is installed on your system.
2. Open the related `.gms` model file in GAMS Studio or GAMS IDE.
3. Run the code (`F9` or the Run button).

## 📈 Outputs

When the model runs successfully, it generates a report file in the code's directory. This file lists:
* The realized average service score (F1), realized total cost (F2), and cost deviation values achieved as a result of **Stage 1**,
* The final F1, F2, and score deviation variables achieved as a result of **Stage 2** (after the cost objective is preserved).

Thanks to this structure, managers and decision-makers can clearly see the trade-off between cost and quality (service level) objectives in a data-driven manner.

---
*This project was prepared to demonstrate the integration of Operations Research techniques into business problems and algorithmic modeling competencies using GAMS/CPLEX.*

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
