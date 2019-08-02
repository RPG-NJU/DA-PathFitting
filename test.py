import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

X = [-434.9467134877009, -439.09738995679237, -441.7346890153386, -443.0665771867775, -443.708031176537,
     -437.29044055158755, -422.2569202183112, -418.30082519344387, -423.5946156319412, -430.01595967859816,
     -434.49125088300707, -435.6415395145288, -434.9399092679163, -432.95817691649546, -440.7308460840387,
     -447.9161404855113, -441.880410482504, -414.8864849535908, -390.74908212106504, -383.4220020329928,
     -384.51182661498797, -381.93327006357305, -377.902086866576, -373.52645935099133, -358.9355724833168,
     -365.1733356710429, -388.5689852029365, -402.1859072435084, -406.9711419774386, -406.1042707170684,
     -407.1109432485982, -411.1291734264537, -415.0458869045931, -410.4060749985563, -401.13067957847136,
     -399.7859774797719, -406.538051237556, -417.5620486965311, -414.01838250817457, -399.29197968728624,
     -390.2961812024284, -392.2389177603895, -396.906418293867, -400.91422815472475, -406.88301579303794,
     -403.5586333696097, -398.09972552366065, -397.7505029978738, -389.51472433331077, -371.12158641470324,
     -364.8557458751574, -373.6479887570002, -366.287979541528, -364.6330244645154, -391.96409442453626,
     -410.4109985802893, -420.03480608648175, -423.2671535807512, -426.0960960153951, -419.86892211891757,
     -414.099409055154, -415.4059112392623, -425.64468618531185, -440.6863156933028, -451.26919244565573,
     -451.830042147025, -451.830042147025, -459.9268646281468, -475.8457475426408, -480.78702701966813,
     -480.04801761803776, -469.4484696696715, -455.12752990017674, -436.09746201213903, -422.396987147121,
     -410.1210395660793, -405.6631841380058, -394.29353926281533, -386.6710702651103, -381.36920506736385,
     -375.23521503270047, -366.8790518175886, -361.5017696540347, -357.9815077301257, -356.8753479589845,
     -357.751667291401, -357.33088696376984, -355.4337549005638, -356.9263194264583, -358.81581605466863,
     -359.733373019872, -361.5360783281332, -362.01362579606564, -358.24941540525714, -354.85600499850335,
     -354.5831036018908, -355.134712457281, -352.01796224587935, -327.5585214448756, -304.71371625016326,
     -323.0296338632701, -343.2901955114569, -350.00787148326924, -341.4952716831857, -342.4248344997562,
     -348.82391718366796, -344.42380170286543, -333.3646414575029, -326.32666181649114, -317.365084924136,
     -304.7879514090596, -292.7348656893536, -286.5582082824405, -282.19134706904384, -278.8107808852593,
     -270.2812244003246, -264.12611291665445, -259.9614317250665, -255.6960783500157, -248.78038257450993,
     -240.4006781882731, -231.5380259353841, -215.8266830190637, -201.6372704168367, -184.294370543061,
     -173.07397780072816, -170.3047773665185, -173.9944320640709, -166.71171444383765, -156.12891060902547,
     -144.14162160139662, -130.90606974323674, -122.47100551186162, -118.0626388464422, -113.4613867711798,
     -108.41661516368745, -105.06429950218926, -96.90573508348888, -81.50348991917623, -69.2045710919276,
     -59.57480719553393, -50.9444864026082, -38.83757029134564, -24.464350148008855, -12.147520973883893,
     -3.751938205496653, 0.6843944563726064, 4.860637811040127, 11.077154311132343, 21.76645169931103,
     31.50579159499586, 41.479906686416555, 62.96986496827367, 78.269853377442, 79.75501605323, 81.35406601371243,
     130.82394528150851, 121.30082025290766, 130.82394528150851, 136.40018303507767, 141.6066881497925,
     146.54111266076654, 151.98456540747404, 158.1473470216049, 171.68851770302246, 183.19867431818957,
     191.7930438745569, 199.32164796818023, 210.20755590855157, 224.664684111148, 238.33414977761876,
     243.38802990139718, 245.44421553627538, 251.66913905488227, 261.0227632022694, 269.3355551171194,
     276.06167524235286, 279.4015082170202, 285.7466926035217, 295.859464947759, 306.2240500915312, 315.6853933070388,
     321.42099935591006, 331.1115269298287, 337.6130595771388, 345.9382137793641, 350.68840393201714, 358.4616152697759,
     364.8891838553089, 376.00992291846933, 382.8384721740903, 386.4561828193693, 388.8199413479467, 392.24743016399935,
     391.5222779738715, 401.4507356474256, 419.4355314492548, 435.6245332548284, 439.9009050250053, 434.65390335401406,
     439.98254552595904, 436.93823411680887, 440.93257666501887, 447.8854466087519, 458.91314671008377,
     472.03873050495633, 486.6922815419217, 502.1126525462603, 521.9697691998068, 546.70090501417, 554.7651926129407,
     562.9423312248182, 557.3425081830836, 545.7903712008134, 538.3705585849009, 532.962100855803, 520.8693720306637,
     503.07359014717355, 476.37763486528655, 455.5755732359277, 430.45667378870706, 412.9325827161341,
     402.05663137334307, 373.01549641244054, 360.9789563137503, 354.4630955969559, 374.99042465551094,
     389.33875523614375, 394.2843263389041, 396.98396660492847, 394.6731371045496, 400.4280435463014, 405.9473259126666,
     405.0067145679616, 404.72807195083425, 416.372767343472, 437.0290781091249, 449.56987407829877, 441.05186824733124,
     410.8065749452055, 379.08219521599045, 374.52756995136826, 380.3189259280703, 397.3112499627191, 414.4735033146824,
     420.4608198713914, 393.2307371802299, 382.3528343193435, 387.0584554974964, 391.69933034106475, 391.40211223298826,
     397.27722832347763, 420.8697453747578, 455.5553385636935, 454.38619906093305, 423.19597195364514,
     403.5216179874334, 401.2182471097513, 411.0961721068692, 440.2700807279133, 443.945567286867, 426.85397873041126,
     377.2794625331595, 358.3585127433228, 362.28654067376465, 379.23389540579717, 396.35481378801114, 403.36782839188,
     414.0680471329358, 426.3986855456074, 434.23465156614077, 430.300144441088, 419.6920338593725, 418.5170037150336,
     409.93266068919957, 389.56313030323076, 382.0550545974097, 380.50984045163034, 375.7352291529798,
     365.3461283983725, 364.73483247601524, 358.44011049521805, 345.1515467200721, 331.065812210594, 326.8159808617793,
     328.96095104491525, 329.67167929501625, 326.43803635255443, 324.5523057261575, 326.2454744897921,
     333.08207285887676, 338.93521226642605, 346.0391319367161, 352.0267640612106, 351.0390984698491, 341.4605439355798,
     303.0780407574268, 308.50760200181395, 307.575628421315, 303.0780407574268, 301.8128198570859, 292.88607342931107,
     286.3991284384168, 276.96197274961355, 267.2557827918413, 256.79593612419507, 252.39068080533548,
     253.35087421219328, 247.7928850667287, 231.58836737575555, 215.25169334368945, 210.00320428771755,
     209.4510053862837, 202.69875446375391, 190.59312105711953, 178.77600975290602, 162.93290924427447,
     153.932714051379, 149.90659608579602, 144.98021300726379, 141.152327756759, 136.78305221200935, 127.73008210532792,
     121.12866984863497, 112.48592021021834, 88.68967828853958, 55.48196781412674, 40.78273249772672, 43.96534375157191,
     43.22849576159241, 36.43383540359384, 28.628499695427532, 19.337240171599024, 6.098804917161415,
     -7.075458995648611, -18.016924209867604, -26.258301827313463, -28.07533152615961, -32.86012053490624,
     -47.3158710003117, -63.19416715752343, -69.98181719912809, -84.44682439272553, -102.54960104678995,
     -114.60489632171598, -126.52070948734904, -145.945852703636, -160.97666179233596, -171.657194574845,
     -178.58869099272405, -200.35579871449332, -237.52279331025667, -274.6960757633999, -280.27209808684063,
     -266.209618130194, -222.75623514808962, -203.92713995314497, -206.67595696303732, -221.27316989348057,
     -242.0309224954011, -256.6609787898619, -277.38308972216424, -283.13168532269384, -293.56599980053005,
     -311.92898531555863, -336.4111314144758, -364.05655841852064, -386.09990759311347, -406.6893007025042,
     -413.52103970748396, -417.3698768802868, -419.8351058468814, -423.0813479421752, -432.6737046825196,
     -454.9576633029218, -467.3458250024137, -471.53226805335106, -464.4529857187014, -444.90080145345036,
     -438.75423125077134, -436.69873524763324, -440.47455380391807]
Y = [-209.66675282635148, -221.52327433782432, -228.50652457816602, -231.6944620718162, -223.64519288048646,
     -207.36683409796473, -207.99393848342766, -222.84984023923892, -237.7625281106055, -243.42560738099007,
     -247.64550738210343, -249.41419770969782, -248.00460413979408, -245.3903726168456, -245.69212914103275,
     -246.69115451327914, -248.46663968204783, -240.16677373772274, -230.04642273316676, -225.731438459176,
     -224.84165612558405, -218.5762321225104, -213.73801923444003, -213.48343492965788, -210.5228649552985,
     -213.9687174171413, -228.5153037410069, -246.87677942225153, -255.18135073100342, -257.6803920791099,
     -259.34593293574494, -263.269290239176, -270.9247459190831, -276.6187941587459, -282.4808688223039,
     -291.6057440757481, -301.4370524212738, -309.69978041519215, -313.3734536704633, -311.0153823543721,
     -309.3692500891608, -315.13038898198545, -326.1737223146359, -338.2317260875583, -353.5127797475307,
     -362.52148764406087, -363.2436754486359, -348.46753939229575, -328.4736599619941, -316.7643588773423,
     -322.5557060198167, -343.86637712680545, -369.66692934261147, -393.29397909683166, -407.47395309010057,
     -418.68153131406103, -438.3373218652549, -455.9930197016034, -463.79459452367547, -469.24883551441565,
     -486.60634200303224, -506.42193891738077, -526.2656454547637, -541.2689145424981, -553.3077166564624,
     -569.894569640274, -569.894569640274, -583.5528153715967, -598.3610752564956, -607.6888872491077,
     -613.1173308435635, -615.4815269456273, -613.707321290343, -613.3027406098265, -607.7501324393813,
     -616.9228513135663, -639.4185746836487, -638.5710622239864, -639.1153701685353, -637.9559477382378,
     -635.3785273201185, -629.7922537977894, -621.4471904519205, -617.6830793049552, -619.5856849077331,
     -620.2400723933176, -614.2094862075849, -607.7778768053608, -604.4219906922149, -600.1884565958597,
     -596.6012542810967, -599.6952569718452, -601.1443281994502, -594.3805130367357, -590.6270522294535,
     -595.7259773277975, -607.7107784419917, -609.748428706627, -598.5349824624767, -577.8152945161694,
     -567.0021068712662, -588.147235752805, -603.472621774718, -608.7796093264084, -612.4285903136528,
     -611.9557389651724, -610.4392013036611, -611.9069506209291, -617.1939395477432, -614.4494187102711,
     -609.1213414183967, -608.4223320840197, -608.2793853566158, -606.0005992449799, -604.287319468555,
     -601.5711014681904, -602.0638983216562, -608.6627444327015, -617.2688869130341, -620.603380301867,
     -619.91519450906, -619.0409190808, -616.6368944621743, -617.848898284725, -622.0042945978932, -628.1626478814605,
     -632.7121399790743, -635.4205110387378, -634.3791553558331, -627.7983765428909, -612.6105489167278,
     -601.383399698165, -602.9890685124858, -613.1146645777916, -616.1756621113898, -614.6462821090046,
     -611.1524421880421, -613.4701107767179, -617.3042910385448, -616.6408237747385, -614.3514526404322,
     -618.1267007139215, -621.0429029775156, -613.2203387218848, -596.2398966331666, -594.4031005264301,
     -598.9678159409359, -599.3679657320284, -597.7415591019981, -595.7867475091609, -598.54259214484,
     -603.3073839315165, -607.3525815324092, -606.4401032714223, -610.5774888409319, -601.5226053733159,
     -558.0745177310802, -563.8020347636709, -558.0745177310802, -561.1576291148239, -569.2667195455203,
     -591.9404818892401, -604.2150018546666, -609.5781650412112, -610.9809369980089, -611.9738024775231,
     -609.6603229942541, -604.9716266408414, -602.4860846321678, -598.7939074449017, -591.4473111731826,
     -576.7579076178312, -571.5013840850164, -576.7577681672946, -580.7882067714255, -582.7447122842739,
     -588.7176560054113, -597.084220619282, -598.5601671899294, -595.9165968170123, -594.5192926428897,
     -595.2879591842641, -594.3832406169753, -594.1639743987876, -583.8862986867172, -570.48494180549,
     -561.3401300772255, -559.3772520852808, -565.2621182666157, -574.3930241743532, -577.7424937340114,
     -570.8023335394516, -557.8157476620847, -548.036247587557, -539.8496855383538, -529.8028624680277,
     -527.7691330337416, -535.430504013616, -549.0160725725538, -559.7899878454583, -564.0195269542186,
     -581.6971985701624, -597.985423099613, -612.7950279160267, -628.6384521383904, -629.9207062338056,
     -625.9978102990907, -625.6843106545543, -635.2543043392662, -644.6054223477649, -650.7689378760385,
     -651.0796360310526, -647.051377695448, -641.9797898405747, -637.1209230717458, -635.0381285846879,
     -628.4197118304621, -615.5875685356517, -591.7218017296783, -558.1820202019786, -545.9707351433325,
     -563.8762787286496, -572.6668590557315, -539.666189011766, -515.9274313272047, -502.6886434578645,
     -511.2044721257803, -520.2218349230363, -529.7519734632399, -530.9434261538435, -533.7079179689625,
     -537.6178994906537, -531.5851474898627, -522.0430057057611, -518.2897093368084, -528.5190902026354,
     -541.1217966317893, -546.6867270524668, -521.5672897262926, -478.30426123779273, -439.8614151997264,
     -424.83422284820927, -425.71089979049975, -429.7850025408485, -427.55786794198843, -421.48302968211146,
     -409.3992192273901, -400.50223936094346, -395.3530983747693, -388.207821777811, -382.0631528252736,
     -382.0566184026946, -401.70950165315384, -408.7443211809932, -391.14324843014657, -371.89031042676424,
     -351.6284906831962, -336.65369293498594, -324.93232958769204, -316.97444803036535, -302.27860053463326,
     -285.40123268514276, -259.7629187220413, -237.0776129140683, -219.1371967799327, -220.8587082692208,
     -232.4796702757331, -232.5595294256226, -210.44245572642788, -185.36158952071077, -177.63401767361879,
     -178.6675193778186, -178.91972930115318, -168.4283188918546, -165.8577326939319, -165.92991788906753,
     -161.5321153675746, -154.33194625657273, -150.50216455132323, -144.6897849501246, -137.05071326241563,
     -131.16118556259573, -132.97323382707813, -137.62490438675587, -142.56919062113636, -148.00296224368424,
     -152.8029132675289, -156.38066503142383, -160.64017015656742, -164.7360100971713, -171.05600105109232,
     -185.09565197778304, -194.27725106810124, -193.6329693708627, -192.13145888409778, -196.3790321401108,
     -185.68700960852104, -191.49000698932437, -186.3756014926133, -185.68700960852104, -177.86005142959223,
     -171.44646144846732, -170.47496526363767, -172.1197984412846, -173.30034610125685, -179.2501827971068,
     -182.1061015741775, -182.5687732447419, -178.4271726891588, -179.45938225091578, -185.9230914521039,
     -184.34482288654374, -176.34568371304567, -176.01382029124767, -180.9455704662644, -185.3218699018735,
     -185.6692257251767, -183.5930940404005, -181.18597561950384, -181.95692513694505, -180.2142505187199,
     -182.62537992066174, -185.33323997962813, -184.52495255529274, -184.4806208819071, -185.01958415729447,
     -181.30082436624156, -179.3015447382535, -178.21227155268573, -173.02664942609684, -171.37514289830935,
     -172.78715999276213, -170.61493779870005, -168.6425891023559, -170.4166326412405, -171.4885944940959,
     -170.3216038260944, -165.63973272446958, -162.60616928543746, -165.70828578487004, -171.8605257233727,
     -177.65931628409214, -181.467372965539, -183.92325777131944, -186.01803376059516, -192.15334183996484,
     -186.94487411795888, -178.9643154815872, -168.1358070157713, -165.19982089099994, -167.7905446073459,
     -170.61849918223854, -178.80088085727826, -189.64443692257865, -201.64801105938903, -213.82122269044567,
     -221.2385604066943, -223.75549770656352, -210.24643019641204, -187.10396540207384, -178.9783441092338,
     -180.01013392799905, -177.90204122172847, -167.79996493946572, -165.8945176990365, -178.08115334113634,
     -188.28421584420488, -191.97059695608382, -187.87680543347182, -184.1251848525662, -174.16561151437347,
     -172.87411101472856, -176.4068772576329, -176.66024540504154, -174.95073604316931, -178.26672209837045,
     -184.71109487134825, -193.30959755438874, -204.7159024861298, -208.71975193004985, -210.78743181612685,
     -210.6647518907174]

N = len(X)
# required by `bc_type='periodic'`
X[-1] = X[0]
Y[-1] = Y[0]

csX = CubicSpline(np.arange(len(X)),X,bc_type='periodic')
csY = CubicSpline(np.arange(len(Y)),Y,bc_type='periodic')

IN = np.linspace(0,N-1,100*N)

fig,ax=plt.subplots()

ax.scatter(X,Y)
# for i in range(N-1):
#     ax.annotate(f"  {i}",(X[i],Y[i]))
ax.plot(csX(IN),csY(IN))
plt.show()