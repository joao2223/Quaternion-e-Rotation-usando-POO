## Quaternions

```
Quaternions são números com álgebra não-comutativa (isto é,ab̸=baem geral) que generalizam
números complexos. Um quaternion pode ser representado como:
```
```
q 1 +q 2 i +q 3 j +q 4 k ,
```
```
onde q1 ,q2 ,q3 e q4 são números reais, enquanto i , j e k são números distintos (imaginários) que
satisfazem as relações:
```
```
i^2 = j^2 = k^2 = ijk = − 1 ,
ij =− ji = k ,
jk =− kj = i ,
ki =− ik = j.
```
As três últimas linhas são redundantes com a primeira. O número real xcorresponde a
x+ 0 **i** + 0 **j** + 0 **k** e o número complexoz=a+b **i** corresponde aa+b **i** + 0 **j** + 0 **k**.
O _conjugado_ deq=q 1 +q 2 **i** +q 3 **j** +q 4 **k** é definido como

```
q ̄=q 1 −q 2 i −q 3 j −q 4 k.
```
A soma dea=a 1 +a 2 **i** +a 3 **j** +a 4 **k** comb=b 1 +b 2 **i** +b 3 **j** +b 4 **k** é

```
a+b= (a 1 +b 1 ) + (a 2 +b 2 ) i + (a 3 +b 3 ) j + (a 4 +b 4 ) k.
```
```
O produto é dado por
```
```
ab = (a 1 b 1 −a 2 b 2 −a 3 b 3 −a 4 b 4 )
+ (a 1 b 2 +a 2 b 1 +a 3 b 4 −a 4 b 3 ) i
+ (a 1 b 3 −a 2 b 4 +a 3 b 1 +a 4 b 2 ) j
+ (a 1 b 4 +a 2 b 3 −a 3 b 2 +a 4 b 1 ) k.
```
```
Note que, seaé real, entãoa 2 =a 3 =a 4 = 0ea 1 =a, e portanto a expressão acima simplifica
paraab=ab 1 +ab 2 i +ab 3 j +ab 4 k .Também dá para verificar queqq ̄=qq ̄ =q^21 +q^22 +q^23 +q 42 é
sempre real.^1
```
(^1) Esta expressão, apesar de uma consequência da fórmula de multiplicação, **deve ser usada em calculos
em computador sempre que for adequada** : Os valores dos coeficientes de **i** _,_ **j** _,_ **k** se anulam, mas devido
a problemas de arredondamento, se _q_ ̄ _q_ for calculado pela fórmula de multiplicação podem restar coeficientes
imaginários não-nulos (o que ocasiona problema, por exemplo, no cálculo da norma).


```
O inverso de um quaternion é definido como:
```
```
q−^1 =
```
#### 1

```
qq ̄
```
```
q ̄
```
```
e sua norma como:
|q|=
```
#### √

```
qq. ̄
```
A partir do inverso podemos definir a divisão:

```
a
b
```
```
=ab−^1 =
```
#### 1

```
b ̄b
```
```
a ̄b.
```
## Rotações

```
Quaternions são úteis para representar rotações em espaços tridimensionais. Uma forma de
realizar isso é a seguinte:
```
1. Considere um ponto P com coordenadas cartesianas (x,y,z). Esse ponto pode ser
    representado pelo quaternionp= 0 +x **i** +y **j** +z **k** (repare na parte real 0 ).
2. Uma rotação é especificada através de um vetor **v** , que indica o eixo da rotação, e por
    um ânguloα, que indica o ângulo de rotação em torno desse eixo. Representamos uma
    rotação definida dessa forma através do quaternion:

```
r= cos
```
```
α
2
```
```
+ sin
```
```
α
2
```
#### 1

```
∥ v ∥
```
```
(v x i +v y j +v z k ),
```
```
onde(v x ,v y ,v z )são as componentes de v e∥ v ∥=
```
```
√
v^2 x +v y^2 +v z^2.
```
3. Para realizar uma rotação no ponto representado pelo quaternionp(gerando o novo ponto
    p′), basta fazer:^2
       p′=rpr−^1.
(Lembre-se que o produto não é comutativo!)

## Trabalho

1. Escreva uma classe para lidar com quaternions, cuidando para que objetos dessa classe
    possam trabalhar conjuntamente com valores inteiros, reais e complexos, quando adequado
(i.e. deve-se definir operações aritméticas tanto de quaternions entre si como com esses
outros tipos).
A implementação deve ser feita num módulo denominado quaternion , implementado em
um arquivo quaternion.py , e a classe deve se chamar Quaternion.
2. Escreva um programa que realize o seguinte:

```
(a) Cria um cubo com vértices nos pontos(1, 1 ,1), (1, 1 ,−1), (1,− 1 ,1), (− 1 , 1 ,1),
(1,− 1 ,−1),(− 1 , 1 ,−1),(− 1 ,− 1 ,1)e(− 1 ,− 1 ,−1).
```
(^2) Você consegue mostrar que _p_ ′terá parte real 0 , como adequado para a representação de um ponto? Não é
necessário entregar esta demonstração.

#### 2


```
(b) Repetidamente pede ao usuário um eixo e um ângulo de rotação. Realiza a rotação
especificada no cubo (acumuladamente, isto é, sobre a posição do cubo após a última
rotação) e mostra os novos valores dos vértices (para cada rotação). Devem ser
mostradas as coordenadasx,y,z, e não os quaternions correspondentes.
```
```
Algumas observações:
```
- Note que foi pedida uma classe para quaternions sem se referir ao programa de rotação.
    _Você deve implementar uma classe que se baseie nos conceitos básicos de quaternions_
       _expostos, e não apenas o que será necessário para o programa de rotação._
- Use sobrecarga de operadores.
- No programa de rotação, use uma classe para representar o cubo, com um método para
    realizar a rotação especificada por um quaternion dado e métodos para acesso aos vértices.
    A classe para cubo não precisa ser geral, pode ter apenas o que é necessário ao programa.
- Você pode usar para a implementação qualquer característica da linguagem que desejar,
    bem como módulos pré-definidos no Python, mas não outros módulos da comunidade.
    Veja a lista de módulos do Python.
- Para testar, aplique rotações de múltiplos de 90 o, que devem resultar no mesmo cubo,
    apenas com os vértices posicionados em outra ordem.
- Você pode fazer o programa mais flexível ou geral do que o pedido.
- Entregue os arquivos com os códigos do módulo de quaternions e o programa de rotação
    do cubo, empacotados em um único .zip ou .tar.gz.

#### 3

