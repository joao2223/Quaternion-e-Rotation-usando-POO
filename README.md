**Quaternions**

Quaternions são números com álgebra não-comutativa (isto é, *ab* = *ba* em geral) que generalizam números complexos. Um quaternion pode ser representado como:

*q*1 + *q*2**i** + *q*3**j** + *q*4**k***,*

onde *q*1, *q*2, *q*3 e *q*4 são números reais, enquanto **i**, **j** e **k** são números distintos (imaginários) que satisfazem as relações:

**i**2 = **j**2 = **k**2 = **ijk** = −1*,* **ij** = −**ji** = **k***,*

**jk** = −**kj** = **i***,* **ki** = −**ik** = **j***.*

As três últimas linhas são redundantes com a primeira. O número real *x* corresponde a *x* + 0**i** + 0**j** + 0**k** e o número complexo *z* = *a* + *b***i** corresponde a *a* + *b***i** + 0**j** + 0**k**.

O *conjugado* de *q* = *q* + *q* **i** + *q* **j** + *q* **k** é definido como

1 2 3 4

*q*¯= *q* − *q* **i** − *q* **j** − *q* **k***.*

1 2 3 4

A soma de *a* = *a* + *a* **i** + *a* **j** + *a* **k** com *b*= *b* + *b* **i** + *b* **j** + *b* **k** é

1 2 3 4 1 2 3 4

*a* + *b*= ( *a* + *b* ) + ( *a* + *b* )**i** + ( *a* + *b* )**j** + ( *a* + *b* )**k***.*

1 1 2 2 3 3 4 4

O produto é dado por

*ab* = ( *a*1*b*1 − *a*2*b*2 − *a*3*b*3 − *a*4*b*4)

+ ( *a b* + *a b* + *a b* − *a b* )**i**

1 2 2 1 3 4 4 3

+ ( *a b* − *a b* + *a b* + *a b* )**j**

1 3 2 4 3 1 4 2

+ ( *a*1*b*4 + *a*2*b*3 − *a*3*b*2 + *a*4*b*1)**k***.*

Note que, se *a* é real, então *a*2 = *a*3 = *a*4 = 0 e *a*1 = *a*, e portanto a expressão acima simplifica para *ab* = *ab*1 + *ab*2**i** + *ab*3**j** + *ab*4**k***.* Também dá para verificar que *qq*¯= *q*¯*q*= *q*2 + *q*2 + *q*2 + *q*2 é

1 2 3 4

sempre real.[ ](#_page0_x74.63_y737.38)[^1]

O inverso de um quaternion é definido como:

*q*− 1 = 1 *q*¯

*qq*¯

e sua norma como: √ ![](Aspose.Words.6450a7a8-9db1-4554-bfad-9591cfddd970.001.png)

|*q*| = *qq*¯*.*

A partir do inverso podemos definir a divisão:

*a* = *ab*− 1 = *b*1¯*ba*¯*b. b*

**Rotações**

Quaternions são úteis para representar rotações em espaços tridimensionais. Uma forma de realizar isso é a seguinte:

1. Considere um ponto *P* com coordenadas cartesianas (*x,y,z* ). Esse ponto pode ser representado pelo quaternion *p* = 0 + *x***i** + *y***j** + *z***k** (repare na parte real 0).
1. Uma rotação é especificada através de um vetor **v**, que indica o eixo da rotação, e por um ângulo *α*, que indica o ângulo de rotação em torno desse eixo. Representamos uma rotação definida dessa forma através do quaternion:

*α α* 1

*r* = cos 2 + sin 2   **v**  (*vx***i** + *vy***j** + *vz***k**)*,* onde (*v ,v ,v* ) são as componentes de **v** e   **v**  = *v*[^2] + *v*2 + *v*2*. ![](Aspose.Words.6450a7a8-9db1-4554-bfad-9591cfddd970.002.png)x y z x y z*

3. Para realizar uma rotação no ponto representado pelo quaternion *p* (gerando o novo ponto *p* ), basta fazer:[ 2](#_page1_x74.63_y727.20)

*p*  = *rpr*− 1*.*

(Lembre-se que o produto não é comutativo!)

**Trabalho**

1. Escreva uma classe para lidar com quaternions, cuidando para que objetos dessa classe possam trabalhar conjuntamente com valores inteiros, reais e complexos, quando adequado (i.e. deve-se definir operações aritméticas tanto de quaternions entre si como com esses outros tipos).

A implementação deve ser feita num módulo denominado quaternion , implementado em um arquivo quaternion.py , e a classe deve se chamar Quaternion .

2. Escreva um programa que realize o seguinte:
1) Cria um cubo com vértices nos pontos (1*,*1*,*1), (1*,*1*,*−1), (1*,*−1*,*1), (−1*,*1*,*1), (1*,*−1*,*−1), (−1*,*1*,*−1), (−1*,*−1*,*1) e (−1*,*−1*,*−1).
2) Repetidamente pede ao usuário um eixo e um ângulo de rotação. Realiza a rotação especificada no cubo (acumuladamente, isto é, sobre a posição do cubo após a última rotação) e mostra os novos valores dos vértices (para cada rotação). Devem ser mostradas as coordenadas *x,y,z* , e não os quaternions correspondentes.

**Algumas observações:**

- Note que foi pedida uma classe para quaternions sem se referir ao programa de rotação. *Você deve implementar uma classe que se baseie nos conceitos básicos de quaternions expostos, e não apenas o que será necessário para o programa de rotação.*
- Use sobrecarga de operadores.
- No programa de rotação, use uma classe para representar o cubo, com um método para realizar a rotação especificada por um quaternion dado e métodos para acesso aos vértices. A classe para cubo não precisa ser geral, pode ter apenas o que é necessário ao programa.
- Você pode usar para a implementação qualquer característica da linguagem que desejar, bem como módulos pré-definidos no Python, mas não outros módulos da comunidade. Veja a lista de módulos do Python.
- Para testar, aplique rotações de múltiplos de 90o, que devem resultar no mesmo cubo, apenas com os vértices posicionados em outra ordem.
- Você pode fazer o programa mais flexível ou geral do que o pedido.
- Entregue os arquivos com os códigos do módulo de quaternions e o programa de rotação do cubo, empacotados em um único .zip ou .tar.gz .
4

[^1]: <a name="_page0_x74.63_y737.38"></a>Esta expressão, apesar de uma consequência da fórmula de multiplicação, **deve ser usada em calculos em computador sempre que for adequada**: Os valores dos coeficientes de **i***,***j***,***k** se anulam, mas devido a problemas de arredondamento, se *qq*¯ for calculado pela fórmula de multiplicação podem restar coeficientes imaginários não-nulos (o que ocasiona problema, por exemplo, no cálculo da norma).
[^2]: <a name="_page1_x74.63_y727.20"></a>Você consegue mostrar que *p*  terá parte real 0, como adequado para a representação de um ponto? Não é necessário entregar esta demonstração.

