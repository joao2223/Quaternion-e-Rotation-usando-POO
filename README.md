## Quaternions


Quaternions são números com álgebra não-comutativa (isto é,ab̸=baem geral) que generalizam
números complexos. Um quaternion pode ser representado como:
```math
q_1 +q_2 i +q_3 j +q_4 k ,
```
onde q_1 ,q2 ,q3 e q4 são números reais, enquanto i^2 , j e k são números distintos (imaginários) que
satisfazem as relações:
```math
i^2 = j^2 = k^2 = ijk = − 1 ,
ij =− ji = k ,
jk =− kj = i ,
ki =− ik = j.
```
As três últimas linhas são redundantes com a primeira. O número real xcorresponde a
x+ 0 **i** + 0 **j** + 0 **k** e o número complexoz=a+b **i** corresponde aa+b **i** + 0 **j** + 0 **k**.
O _conjugado_ deq=q 1 +q 2 **i** +q 3 **j** +q 4 **k** é definido como

```math
q ̄=q_1 −q_2 i −q_3 j −q_4 k.
```
A soma de a=a 1 +a 2 **i** +a 3 **j** +a 4 **k** comb=b 1 +b 2 **i** +b 3 **j** +b 4 **k** é

```math
a+b= (a_1 +b_1 ) + (a_2 +b_2 ) i + (a_3 +b_3 ) j + (a_4 +b_4 ) k.
```
O produto é dado por

```math
ab = (a_1 b_1 −a_2 b_2 −a_3 b_3 −a_4 b_4 )
+ (a_1 b_2 +a 2 b_1 +a_3 b_4 −a 4 b_3 ) i
+ (a_1 b_3 −a_2 b_4 +a_3 b_1 +a_4 b_2 ) j
+ (a_1 b_4 +a_2 b_3 −a_3 b_2 +a_4 b_1 ) k.

```
O inverso de um quaternion é definido como:

```math
q^{-1} =q\frac{q} {\bar{q}}
```
e sua norma como:
```math
|q|=\sqrt{q\bar{q}}
```
A partir do inverso podemos definir a divisão:

```math
    \frac{a}{b} = \frac{1}{b \bar{b}} a \bar{b}
```
## Rotações

Quaternions são úteis para representar rotações em espaços tridimensionais. Uma forma de
realizar isso é a seguinte:

1. Considere um ponto P com coordenadas cartesianas (x,y,z). Esse ponto pode ser
    representado pelo quaternionp= 0 +x **i** +y **j** +z **k** (repare na parte real 0 ).
2. Uma rotação é especificada através de um vetor **v** , que indica o eixo da rotação, e por
    um ânguloα, que indica o ângulo de rotação em torno desse eixo. Representamos uma
    rotação definida dessa forma através do quaternion:

```math
r = \frac{\cos(\frac{\alpha}{2})+\sin(\frac{\alpha}{2})}{\lVert\mathbf{v}\rVert}(v_xi+v_yj+v_zk)

```
3. Para realizar uma rotação no ponto representado pelo quaternionp(gerando o novo ponto
    p′), basta fazer:^2
    
 ```math
 p′ = rpr^{−1}.
 ```
