from banner import *
from utilis import egcd,modinv,Convert
banner()
"""
n1 = 101160013260894210379231391020878154246531211501917641525287013838064105641873685273682200363965750860043980554926996771004697813924018366330613894159009241440066954185337675909482468504824750801346658013253206226485930206600036498618437728843373496089729788328065664820868923399881331844439326306628030735331
n2 = 10210032872259313686164929473710869592253665432474968016181665104415833992599841926829524498430031021642288824945683044264288937821741278527156550423507713336648261819557381748119064650541556448192793186877429032749223390372405186620392499684387407129200331654256366265932387530132500098451224874600895892420947291972547271991706165603868937708772321221206586800972518013238899316242083977031307714803896630612616326248775444788388309984437812243115218989690016673
c1 = 66392227979404854586458510145632770314092785183583016343730600866783415262123689751268136986554015242755982639115194608534311988971825645169411730748186710947220673034519486951708550346274786041388143262608730637962604985755406789741345581700390500478433427709495522821473858104289236940045533583368435030007
c2 = 930631363282343082351877158963544600758567980445720982159124066613164772521801283854718425072511342860751113498013426077785323580215340717638119847338418916957048868138332980175665931485108461262077829550248080371766930777925758187526884947593887945397880426339790518082874861594313920319799945895788141894706108889222173060684161230756671422619830375801046671640406258873119163443168478229210037764301299889548125261094599251838443625348832760001827881979679672
e = 65537
"""
n1 = int(input(">>> n1 = "))
n2 = int(input(">>> n2 = "))
c1 = int(input(">>> c1 = "))
c2 = int(input(">>> c2 = "))
e = int(input(">>> e = "))


if egcd(n1,n2)[0] == 1:
    print("[-] Sorry , gcd(n1,n2) = 1")
    exit()
else:
    p = egcd(n1,n2)[0]
    q1 = n1 // p
    q2 = n2 // p
    phi1 = (p-1) * (q1 - 1)
    phi2 = (p-1) * (q2 - 1)
    d1 = modinv(e,phi1)
    d2 = modinv(e,phi2)
    try:
        m1 = pow(c1,d1,n1)
        Convert(m1)
    except TypeError:
        pass
    try:
        m2 = pow(c2,d2,n2)
        Convert(m2)
    except TypeError:
        pass

