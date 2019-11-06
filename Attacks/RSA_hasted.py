from banner import *
from utilis import inv_pow,mul_inv,Convert
import functools
banner()

"""
N1 = 79608037716527910392060670707842954224114341083822168077002144855358998405023007345791355970838437273653492726857398313047195654933011803740498167538754807659255275632647165202835846338059572102420992692073303341392512490988413552501419357400503232190597741120726276250753866130679586474440949586692852365179
C1 = 34217065803425349356447652842993191079705593197469002356250751196039765990549766822180265723173964726087016890980051189787233837925650902081362222218365748633591895514369317316450142279676583079298758397507023942377316646300547978234729578678310028626408502085957725408232168284955403531891866121828640919987
N2 = 58002222048141232855465758799795991260844167004589249261667816662245991955274977287082142794911572989261856156040536668553365838145271642812811609687362700843661481653274617983708937827484947856793885821586285570844274545385852401777678956217807768608457322329935290042362221502367207511491516411517438589637
C2 = 48038542572368143315928949857213341349144690234757944150458420344577988496364306227393161112939226347074838727793761695978722074486902525121712796142366962172291716190060386128524977245133260307337691820789978610313893799675837391244062170879810270336080741790927340336486568319993335039457684586195656124176
N3 = 95136786745520478217269528603148282473715660891325372806774750455600642337159386952455144391867750492077191823630711097423473530235172124790951314315271310542765846789908387211336846556241994561268538528319743374290789112373774893547676601690882211706889553455962720218486395519200617695951617114702861810811
C3 = 55139001168534905791033093049281485849516290567638780139733282880064346293967470884523842813679361232423330290836063248352131025995684341143337417237119663347561882637003640064860966432102780676449991773140407055863369179692136108534952624411669691799286623699981636439331427079183234388844722074263884842748
"""


def chinese_remainder(n, a):
    sum = 0
    prod = functools.reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

try:
    C1 = int(raw_input(">>> c1 = "))
    C2 = int(raw_input(">>> c2 = "))
    C3 = int(raw_input(">>> c3 = "))
    N1 = int(raw_input(">>> n1 = "))
    N2 = int(raw_input(">>> n2 = "))
    N3 = int(raw_input(">>> n3 = "))

    N = [N1, N2, N3]
    C = [C1, C2, C3]
    e = len(N)
    a = chinese_remainder(N, C)
    for n, c in zip(N, C):
        assert a % n == c
    m = inv_pow(a, e)
    Convert(m)
except ValueError:
    slowprint("\n[-] c1,c2,c3,n1,n2,n3 Must Be Integar Number")
except AssertionError:
    slowprint("\n[-] Wrong Data")
except KeyboardInterrupt:
    exit()
