from banner import *
from utilis import egcd,modinv,Convert
from Factorizations.ecm import *
banner()

"""
c= 3821925911648555519353747434606743159593808677487039861592438384426669998207423450606829031692403202928227703884307291926528640413305346863805555214851644456742958636273721157021584443312591620736285469414067076228984358550669307967587995994219000349054979046909041864106400708453105658165917613077273501
n= 6311257310749529896994764164885908074730315623107218148732436180339784730655096846277587690299624960654670853389184027362495475005388709090759335907428646246751073917955576737663877861242491426053238800688758573959939180213510980211538490409598005851282273664989880554327678869807688158210471903939248513
e= 65537
prime = [2160890461,2247289019,2250778319,2442210431,2458778093,2534226749,2535292559,2546035901,2651829007,2690421313,2737511971,2807722121,2985359177,3074912623,3142693039,3144852421,3159476069,3166527541,3269492927,3328687379,3493484429,3505945799,3538145749,3610828651,3699668617,3715792519,4036077043,4058968889,4089517513,4116792439,4262477123,4291039453]
"""

try:

    c = int(input(">>> c = "))
    n = int(input(">>> n = "))
    e = int(input(">>> e = "))
    prime = primefactors(n)

    phi = 1
    for i in prime:
        phi *= i-1

    d = modinv(e, phi)
    m = pow(c, d, n)
    Convert(m)

except IndexError:
    slowprint("[-] Sorry Can't Factorize n ")
except ImportError:
    slowprint("\n[-] Module Not Setup")
except ValueError:
    slowprint("\n[-] c,n,e Must Be Integar Number")
except KeyboardInterrupt:
    exit()
except:
    slowprint("[-] False Attack !")