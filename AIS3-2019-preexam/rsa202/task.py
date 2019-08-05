from Crypto.PublicKey import RSA
from Crypto.Util.number import getPrime, isPrime, inverse
from secret import p, r, FLAG1, FLAG2

assert ((p-1) % r)**2 + ((r**5 - 1) % p)**2 == 0
assert isPrime(p) + isPrime(r) == 2

def next_prime(num):
    while True :
        num +=1
        if isPrime(num):
            return num

e = 65537

n1 = r * next_prime(r)
n2 = p * getPrime(1024)

enc1 = pow(FLAG1, e, n1)
enc2 = pow(FLAG2, e, n2)

print('(enc1,n1) =', (enc1,n1) )
print('(enc2,n2) =', (enc2,n2) )


'''

e : 849601849
n1 : r * next_prime(r)
369178955491994534543283686411734413963740180614967352459108514962223797751243469095923350127606489587230605178284811363994452968641734
9268701814383638169371400078109898081468759323
n2 : p * q
188621314280130333370893410058593209053102750453655782557667458043509664967351645676897455214926133506916583662394965908813475500849089
491377855260199108480614158715007265784743730078034325132637962008384158529062417530807107763157234055638356200441831505238099538706844
320501571168542168083149109185985120543146420803481177578075904578164874164064021815507269480928439124388459746183679763322847474300415
519017385200584780398152072494669589155815146808228149844657684147124666002971042107575347910100924854906493633947451107573077420850053
669997296314860825899050544700573275773329182237535643169859159618360437036187146061927112283810840298289221855647056286065113791847995
756068817892705110398318000871432756715640203371
enc : pow(FLAG1, e, n1)
322445927313899713677097597660687356203372995270377296070212501355033273103802346190643908091223790993627415624850502638658069215241526
139586875997055957523478786593137781934663607
enc : pow(FLAG2, e, n2)
972577489838943046300465811783214598981369978276451229186743001367096529989196132002421767015566096552370445599679295776664197539486172
559057708518485625732272235649263577356848722661323089769484597603274692874800735586456834608637389976967377909258917059103448632596041
344039425895205531523586481652748274804370389662409386152065395158006031512719707000906082313085635032658606394664765052228471869366988
285439309517701427388987646755774572968846112611200263016378134841759509627826594051619306895766573226303697920991240124221300776385640
926696836948345001716590394744018515541002639109068904315960779766960970104995345009699961073686186638025967199685100868221202861962739
64379479416757017575455962209572983007246586996

e : 749312579
n1 : r * next_prime(r)
2288173037252956358174284861830091852318838794165959696542441437840799555292504278392798604978883314134152098253018971741313363320340167761617868287997708633048141876797301612771091
n2 : p * q
56191498716292904241249587483607416892424325191459297039091478199470983189409703830770828430961804247211047049913189204217822584639664575171076093426523566535761712777607819520141384056972587366552056023819335923427127023103139732014286957683032241355064079502551623746789374893492209998462919559687861597571994691389179737654603684491501694098631008210064969089044384994504522920382260059979725162550705429156859074362302546593255547726247980414719016739758624110050044363305235366935330416388224760200885475831960532412852542986366283071154530062022508271042100943297703167285342225176664043254434327241323288266904225186329269891451974962465933624098135871905457365590714325458512552382701031666515625467440430502705839
enc : pow(FLAG1, e, n1)
809147962459613545655881695775483562298026675652952199433416544261840310700016027422741958068723892855136246526143295956576035854017715903888763998849758585972220513902444055962297
enc : pow(FLAG2, e, n2)
32114766879965983559421497292433533124766017792736133014283907889732318482609980064056455731658617855612717102377736886243834344505967838046931218833178830519848409216480989907953497473372189315901292340506338162384913803017324377638997628310112467475717485412256014136951322885487515299440517677540305495551246068650560326505649259663837538847589061636075082786298434654164603941854893377813394266497692768835911010822305765072117181407348711121940791245638362105159522452131048613368034546900838159801603861873313273890449405535900704512582688238759855713269865524612010439961236777864635821748519179123998107694899590475029183983995266048296665098088483469263847229260722816192561126836248692177315620994992926955386775

'''