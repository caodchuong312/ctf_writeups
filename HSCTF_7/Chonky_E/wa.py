# -*- coding: utf-8 -*-
# https://yocchin.hatenablog.com/entry/2017/03/05/192000より
from fractions import Fraction

def continued_fractions(n,e):
    cf = [0]
    while e != 0:
        cf.append(int(n/e))
        N = n
        n = e
        e = N%e
    return cf

def calcKD(cf):
    kd = list()
    for i in range(1,len(cf)+1):
        tmp = Fraction(0)
        for j in cf[1:i][::-1]:
            tmp = 1/(tmp+j)
        kd.append((tmp.numerator,tmp.denominator))
    return kd

def int_sqrt(n):
    def f(prev):
        while True:
            m = (prev + n/prev)/2
            if m >= prev:
                return prev
            prev = m
    return f(n)

def calcPQ(a,b):
    if a*a < 4*b or a < 0:
        return None
    c = int_sqrt(a*a-4*b)
    p = (a + c) /2
    q = (a - c) /2
    if p + q == a and p * q == b:
        return (p,q)
    else:
        return None

def wiener(n,e):
    kd = calcKD(continued_fractions(n,e))
    for (k,d) in kd:
        if k == 0:
            continue
        if (e*d-1) % k != 0:
            continue
        phin = (e*d-1) / k
        if phin >= n:
            continue
        ans = calcPQ(n-phin+1,n)
        if ans is None:
            continue
        return (ans[0],ans[1])

e = 91043118409828550796773745518585981151180206101005135117565865602978722878478494447048783557571813980525643725323377488249838860897784683927029906188947001149632101513367258267329961684034661252866484981926055087386190015432964608927947646476193251820354738640453947833718397360834701566765504916472450194494897616371452996381159817427887623703639133290358520498419049175941584678802701606995099241245926884172985004839801270005583030514286561971825047719421487004569752638468907609110285739083279629747310953086535889932550905065172805818862336335628248528993024112446002398466115161473573451161053837400091893285717
n = 156749047558583013960513267351769479915110440411448078412590565797031533622509813352093119636835511977253033854388466854142753776146092587825440445182008237325262012698034419137157047927918635897378973846177552961727126115560551970797370239385129543828686170774323306933202481728884019420422360360849592983818405154473369790181636472137741865440233383956571081122982223602667853668754338360008279002325576495573847568301584365514417593244726435632222027817410359417329310347952169273512510934251453361933794586716533950489973436393834189505450956622286216819440777162804798432330933357058175885674184582816364542591313

(p,q) = wiener(n,e)

print 'p = ', str(p)
print 'q = ', str(q)