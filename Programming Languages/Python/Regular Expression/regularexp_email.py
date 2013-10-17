# This will take a URL/.txt file, take all the emails out of it and check if they are valid.
# the regular expression library
import re
# Natural Language Toolkit - symbolic and statistical natural language processing.
import nltk   
# opens file objects from the Web by accessing them via their URL (Hence urlopen library)
from urllib import urlopen

true_emails = []
false_emails = []

def main():
	# url that you want to retrieve all the emails from
	url = "http://www.419baiter.com/_scam_emails/scammer-email-addresses.html"    
	# opens URL and stores it into HTML
	# or html = open('file.txt')
	html = urlopen(url).read()   
	# puts the HTML syntax into str 
	str = nltk.clean_html(html)
	# sample emails:
	# str = '0165offad@att.net, a.c.department@hotmail.co.za, a939020011@yahoo.com, aa05547@gmail.com, aarifaebue@hotmail.com, abaldossou@ymail.com, abdelsalamsanusi@rediffmail.com, abdul_ahmedramzi@yahoo.com, abdulahmedramzi@yahoo.com, abigail.edwards10@yahoo.com, abujoseph44@gmail.com, abusalif77@voila.fr, accdetailsss@yahoo.co.jp, ad.keita96@msn.com, adamakeita@voila.fr, adamson.g@myself.com, adnicaptain@blumail.org, affendighani@one.co.il, ahhmedkairo0190@msn.com, ahhmedkairo0206@msn.com, ahmedkairo@voila.fr, akitobakulaje1@yahoo.com, akitobakulaje4@yahoo.com, albetaoure@gmail.com, alexhopkins33@yahoo.com, alhassanemohamedi@gmail.com, ali.buba@yahoo.com, alimata01@gmail.com, aliyiageorge2012@yahoo.com, allexpeters@yahoo.com.ph, allji.muhm@msn.com, almuhammedagencyltd@msn.com, ambassadorhamzatahmadu491@googlemail.com, ambolugashiru@yahoo.co.jp, ambssodorterencemcculley@hotmail.com, amos_utuama@yahoo.com, amoussou.drbruno@yahoo.com, andersondarrelc@yahoo.com, angela_mayer4281@msn.com, anicontact@yeah.net, animationtech@163.com, anmariekone1@yahoo.fr, anna.ibite@yahoo.com, anna_ibite1011141@msn.com, anthonyhill1965@hotmail.co.uk, astralainlot01@aol.com, atm_paymat_department11@yahoo.dk, attorneyteddytucker@gmail.com, attorneytucker3@gmail.com, au.seafa@yahoo.com, aziz_mohamed12@hotmail.com, azizissa181@voila.fr, baby4love31@yahoo.com, baileydaugherty@gmail.com, barrister_victor.otu68@yahoo.com, barristerfelix04@gmail.com, barristergeorgd222@mail.kz, barristergeorgdchambergh25@gmail.com, barristergeorge100@gmail.com, barristergeorgeudumachamber01@yahoo.com, barrmosesedward1980@gmail.com, barrvictor08@hotmail.co.uk, bbcpayslive12@live.co.uk, beanie3479@aol.com, bella1271@live.com, bensonbestman44@centrum.cz, bensonstevekamsi01@yahoo.co.jp, bernie3343@gmail.com, better2net@hotmail.fr, better2net@yahoo.in, bkmake@ymail.com, blandlina@yahoo.co.uk, blessingbashan87@yahoo.co.uk, blessingfranck13@yahoo.com, blessingfranck5@yahoo.com, bnardrussell@gmail.com, boafundunit@yahoo.com, brff.headoffice@yahoo.com, britaincokeukclmwardprize@live.co.uk, brooksloanfirm@gmail.com, brucenorman0@gmail.com, cabinet.aliouattara@gmail.com, camara3434207@msn.com, camaratutu01@adinet.com.uy, camelot.board1@gmail.com, caseprojecth123@gmail.com, cfestuscclark9@msn.com, cgfestusc@msn.com, chairmanmosesedward@ymail.com, charlesalain36@yahoo.com, cheungleung@kimo.com, choonyei.daewoo@hotmail.com, churchillexpresscourier@gmail.com, claims_department23@hotmail.com, coca_colaloto2012@hotmail.co.uk, coca_colaloto2012@rediffmail.com, cocacola347@hotmail.co.uk, cocacola47uk12345@rediffmail.com, cocacola47uk@hotmail.co.uk, cocacolaclaim201277@hotmail.com, cokeuk55.1299@rediffmail.com, cokeukprice23@rediffmail.com, collectiondept@wss-id.org, compensations@365trade.net, coperatesolutions01@yahoo.dk, coperatesolutions0@yahoo.dk, coperatesolutions@yahoo.com.cn, creditalliance@financier.com, cy145wdtsb@yahoo.co.uk, cynthia4woodtsb@yahoo.co.uk, cynthiajam90@msn.com, cynthiamusa01@sify.com, cynthiawalter06@yahoo.it, damdame_hs@msn.com, danbenco40@yahoo.com, dancerchris@rocketmail.com, davidlouw65@yahoo.co.jp, davidlouw65@yahoo.com, davidmark02272@yahoo.com, davidmcclean4@gmail.com, ddes18@yahoo.com, ddggkatanga@gmail.com, deborahevans2012@gmail.com, deltarealinvestmentr@gmail.com, dickola4@yahoo.co.jp, dickola4@yahoo.com.ph, dip_johnedward11@zbavitu.net, dkwesia@ymail.com, dmgal10@mail.com, dmgal10@yahoo.com.ph, dolor.mensah@yahoo.com, dorsos_andwi_di00057@msn.com, douglas0700@gmail.com, dr.abass_williams@rediffmail.com, dr.johnkennedy59@yahoo.co.uk, dr.pbenny@rediffmail.com, dr_john.kennedy@yahoo.co.uk, drabbasmohamedsellam01@gmail.com, drabbasmohamedsellam02@gmail.com, drfarahakumarinvestment3@hotmail.com, dribudon_166@msn.com, dribudonha2001@gmail.com, drjamesmorgan054@gmail.com, drjamesmorgan103@gmail.com, drkc.moghalu@gmx.tm, drlarryforte782@gmail.com, drmcdonaldjames@yahoo.com, duke_amanda@ymail.com, dwatters@xtra.co.nz, eclerk.lloydsbanklondon@yahoo.co.uk, ecobank_bf@voila.fr, edkatanga00@gmail.com, edmk2024@yahoo.com.ph, emiliegraux98@hotmail.fr, emplomentdept@yahoo.co.uk, engmikeanderson@rediffmail.com, engr_collinsbenerd100@yahoo.com.hk, engrbarkindo2010@gmail.com, euro-afro-asian-sweepstakes63@msn.com, euro-afroasiansweepstakeslotto@lawyer.com, euro2012cup@europe.com, evisjohnson1@gmail.com, ezranehemiah63@yahoo.com, ezranj0228@msn.com, fabriceroland03@yahoo.fr, fatim04@zipmail.com.br, fatimnassar@yahoo.co.id, fbi3032@hotmail.com, fbiwatchlight.rog@qatar.io, fc.affairs@hotellos.nl, fcompanybenin@rocketmail.com, fedexservicecompay0401@hotmail.com, fedrick589@yahoo.com, feliciademah@yahoo.com, festusclark66@yahoo.com.hk, finland_b@yahoo.com, florence.williams21@gmx.us, florencewilliams_33@msn.com, florencewilliams_34@msn.com, florince.majzoub@yahoo.com, flowerrobert34@gmail.com, flowerrobert7@gmail.com, foreign_depts@w.cn, frank_morris_claims@yahoo.co.uk, frankolu44@yahoo.com.hk, frankpaulloanfirm@hotmail.com, fredrickandrew@yahoo.cn, gabrielablakwah1@gmail.com, gary-165@msn.com, garydaniel2012@voila.fr, gbakou_sayidou@voila.fr, gbksay11135@msn.com, gdoris@yahoo.cn, georgberhctold@yahoo.com, georgealiyia3@gmail.com, georgebenin4@gmail.com, geri.matthew@yahoo.com, giftbaby201@yahoo.com, global_invitation@globomail.com, goldernfinancedpt01@gmail.com, goldrko@yahoo.com.ph, goldselrs@yahoo.com, golfnduo@aol.com, gonzaloc63@live.com, gorluky@yahoo.com, governor.lamidosanusi@xyan.us, govlamidosan101@admin.in.th, gradouglasz@yahoo.co.jp, grahamdouglas111@gmail.com, grantsonumi12@hotmail.com, guaranteedloanfirm@gmail.com, guaranteetrust45@yahoo.com, h.farlowe@gmail.com, ham.rahman64@gmail.com, harrison.smith14@yahoo.co.uk, harrison.smith@rediffmail.com, hectorgbagbo00@gmail.com, henekenclaim11@googlemail.com, henryjohnloans@gmail.com, hon.dimeji_b@yahoo.com, honarabledrdavidmura@yahoo.com, howanderglobal@gmail.com, ibanicontact@yeah.net, ibanimation@yeah.net, ibrahimalz@e-mail.ua, ibrhkouti@yahoo.fr, ibwallace@yeah.net, idriskazim@gmail.com, ileadsf@aol.com, imagingedit@163.com, imf.imf.agency@qatar.io, info.antifraudsters@gmail.com, info.authorizationdepartment@programmer.net, info@reservebankofindian.net, info_i28@yahoo.com.ph, infolina@sify.com, infoulstergroup@accountant.com, irs.ielott@hotmail.com, isa_ahmed0000078@msn.com, isaahmed48@gmail.com, j.sibiri@voila.fr, j_abbah@cantv.net, james.kirby741@yahoo.co.uk, jamesbarrister26@yahoo.com.hk, jameskirbys082@msn.com, jamesrichard194@gmail.com, jamharperuk@yahoo.com, jeanreply10004@msn.com, jecinta_larry@rambler.ru, jeffmorgand@workmail.co.za, jenkinhui@9.cn, jenkinhui@blumail.org, jenni_des@yahoo.com, jennides@yahoo.com, jenniferfalana201@mail.kz, jeny_4u2009@yahoo.com, joemaxwell00@yahoo.com.ph, john.garry1960@mail.com, johnbkm02@gmail.com, johnpedro2.cbn.ng@gmail.com, johnpetersonandyou@yahoo.com.hk, johnpius61@yahoo.com, johnsonhonko@hotmail.fr, johnsonhonko@yahoo.cn, jones_edward_002@yahoo.com, jones_morris@ymail.com, jonesmercy23@yahoo.in, joy.dunga@yahoo.com.sg, joycewilliam@126.com, joydunga@lybach.com, jrecross10@rediffmail.com, jrecross@rediffmail.com, jsz_zzz2@msn.com, jubrilmacca@gmail.com, junior_smith25@yahoo.com, justin.redfermprivatemail@gmail.com, justinemorgan12@gmail.com, justmo73@gmail.com, kamallee1950@mail.mn, katehooh_1973@yahoo.es, kekiegaii@gmail.com, ken_maduka@yahoo.com, kenmayo2012@hotmail.com, kennethwilliam0@hotmail.com, kfamily_r@yahoo.cn, kk109ra@msn.com, kk110ra@msn.com, koffigoldsite@yahoo.com.ph, kojo2012@breakthru.com, lacykipkalya@gmail.com, lamido_sanusi0098@rediffmail.com, lamido_sanusi023@rediffmail.com, lapointe@blumail.org, larazarck32@msn.com, larrijames1@gmail.com, larryjennifer36@yahoo.com, larrywarrymark@gmail.com, liasha.only@yahoo.com.ph, liashababay@yahoo.com, lilianw84@yahoo.co.uk, lneasthotel@hotmail.co.uk, loans@atlantic-city-bank.com, loantrust@w.cn, londest00smailbox@rediffmail.com, longsammagg@mail.com, lorio68@verizon.net, louisconnor16@msn.com, ltgeneraljamesmorgan.org@gmail.com, lucyloangroup@gmail.com, m.noelle18@yahoo.de, m.of57@msn.com, m.rjohnson.02@msn.com, madueke_okoli2003@yahoo.com, mah_issa68@msn.com, mahahasavadogo6@gmail.com, mahmadouissa@rocketmail.com, mailinf.focus@mailbox.hu, make_33@msn.com, makejasper@yahoo.com, mamula28@msn.com, marcelmichelle57@yahoo.com, marey_janne@yahoo.com, mareyjanne@yahoo.com, marisa_benny@mail.kz, mark20hughes@hotmail.com, marriacool@yahoo.in, martha12@zipmail.com.br, martha2@zipmail.com.br, mary.david32@yahoo.com.ph, mary.kone73@yahoo.com, matveimiroslv@live.com, mega_express@citromail.hu, mercy_dominic94@yahoo.fr, mgtransfer31@live.com, michaeljohn6688@yahoo.com, microsofftofice-dept11033@live.com, mikerobertson13@att.net, mikerobertson2@consultant.com, minoffin1996@yahoo.fr, mkhood7601@msn.com, mofn00114@msn.com, mohamed.alfred@hotmail.fr, mohamedhasan135@hotmail.com, mojones01@msn.com, mojones08@msn.com, money-tree-finance-services@financier.com, moneytree-s@mail.kz, morelducrou@rediffmail.com, morganchambers@consultant.com, mr.d.zouli@voila.fr, mr.danielmminelepayment@gmail.co.za, mr.goodluckegobia@ymail.com, mr.jallowkarim1@rocketmail.com, mr.jamesbrownfrims@hotmail.com, mr.leungcheung@kimo.com, mr.moghalu@gmail.com, mr.samah_shemari@yahoo.com, mr_dz0118@msn.com, mr_micheal_james56@msn.com, mr_micheal_james76@yahoo.com, mrabusa.15@msn.com, mralexandermonayeur@gmail.com, mrlaadrazarck02@gmail.com, mrliuwang1000@9.cn, mrroberthw@aol.com, mrs.chung_sum@cpll.cn, mrs.sabahh@yahoo.com.tw, mrs.sabahhalif@yahoo.com.tw, mrs.stephanietagro@hotmail.com, mrs.stephanietagro@msn.com, mrs.susannajao111@rediffmail.com, mrs.susannajao1950@hotmail.com, mrs.victoriamark02@yahoo.co.uk, mrsingabrittahlenius2012@webmail.co.za, mrsjudithii@yahoo.co.jp, mrskeefe.kucera03@msn.com, mrskeefe.kucera07@msn.com, mrskucera_keefe@hotmail.com, mrsmithportagent@gmail.com, mrspaulinedouglas278@msn.com, mrspaulinedouglas@postafiok.hu, mrsruthbenson70@yahoo.cn, mrssafia02@yahoo.co.jp, mrsstephanie_5@msn.com, mrswilliams_ali2008@yahoo.com, msfaith.family@googlemail.com, muham.ltd@msn.com, munahabib2001@yahoo.com.cn, nanaado9090@rediffmail.com, nataliegolld@yahoo.com.ph, nducastro@rocketmail.com, ngten.thoon@yahoo.com.sg, nicoalsflorance1@yahoo.co.jp, noelle.marie19@yahoo.de, noelle.marie86@yahoo.com, nono_sasa_mawuli@yahoo.fr, oceania.qualityloans@gmail.com, oceanicbankcashtelex@voila.fr, oceanicbankplcbf@voila.fr, office67800@yahoo.co.jp, officer.joewall@e-mail.ua, officer.joewall@yahoo.com.hk, officeweb6623@yahoo.co.jp, officeww.westernunion@yahoo.com, om.di566@msn.com, om.di594@msn.com, omamalik2011@gmail.com, omar_diallo@voila.fr, omarmaliki48@msn.com, onlyliasha@yahoo.com.ph, patricia2love84@yahoo.com, patriciasandra17@yahoo.com.ph, patrick1920@mail.kz, patrickmaduagwuesq7@gmail.com, peterkamara@skymail.mn, philip.cassilas123@gmail.com, post.pgamble102@w.cn, ppppppppp76@yahoo.com, precious.james67@yahoo.com, processing_manager01@live.co.za, processingunit114@w.cn, pt_choki@yahoo.com, purvakumar01@econetmobile.co.zw, quadriwale@sify.com, queencole36@yahoo.com, r.odor@yahoo.com.ph, raphealkoffiodor@yahoo.com, re.pastorcolesify@yahoo.co.uk, rebecca_wilfred_loanlender@yahoo.com, redirection.webmaster42@gmail.com, reginaldokene01@gmail.com, reginaldokene@aol.com, reply2@edpalm.com, rev.david.peter.okoh120@hotmail.com, revfrpetermarkus@gmail.com, revjohnmarthinsophanagenetwork@gmail.com, revpaul1096@msn.com, revpaul1991@mail.kz, rexcapitalinc@gmail.com, richard-west@kpmg-audit.com, richardmurphyesq2@gmail.com, richardmurphyesq@yahoo.com, richardpsmith5@globomail.com, ritajohnson1973b@yahoo.es, roberthookinvestments.links@gmail.com, rosanna04111984@aol.com, ruggirello_josef@libero.it, s.dorso@yahoo.com.br, s_al36@msn.com, safiafarkashal.baraasi01@ymail.com, sahebnasir34539@msn.com, sahebnasir34596@msn.com, sahebnasir@adinet.com.uy, saintagnesscatholic.church@yahoo.co.uk, samahshemmari@mail.am, samtete21@yahoo.fr, sandrababy_24@yahoo.com, sandradede2012@yahoo.fr, sandradede5@bol.com.br, sandradede6@bol.com.br, sanusi.abdelsalam@yahoo.co.nz, sanusi.lami@live.com, sarah_david122@yahoo.fr, sasdsfdsffd@msn.com, segunwilliams001@yahoo.com, shahidafridi3396@yahoo.com, shahrinbin@yahoo.com.hk, shurkri.gha@hotmail.fr, simonhenry14@aol.com, sir.ben_allen@yahoo.com, sis.shasha04@zipmail.com.br, sis.shasha05@zipmail.com.br, skyexpresscourier2012@hotmail.com, smglong@mail.com, smith.harrison@143.ae, smith_jones234@yahoo.com, smithatm@sify.com, solomon-adams57_151@msn.com, solomon_adams01@voila.fr, stephenloancompany007@yahoo.com, steve.gianino1112@hotmail.co.uk, steve_ekeh1112@yahoo.com, steven.darko@adinet.com.uy, stjamesmemorialhospital20@hotmail.co.uk, susanholm58@yahoo.com, susanshbng000@gmail.com, suzancole32@yahoo.com, suzuki.t012@yahoo.com.hk, suzuki.t013@yahoo.com.hk, sweetexloan@gmail.com, sweetexloan@googlemail.com, synderila@sohu.com, thomas.brownprojetc2012@hotmail.com, thomasjeferson01@rediffmail.com, thomasjeferson31@gmail.com, tim.hanson28@yahoo.com, tomcod@verizon.net, tracymoore_22@yahoo.com, treasury_claims4u@msn.com, trichad@yahoo.cn, trustfundun@aim.com, uchenna_collins@yahoo.com, uduma.b15@msn.com, uk.claimsdepartment@yahoo.cn, unitednationp23@yahoo.com, unitednations_remmitance001@collector.org, unitednations_trustfundunited@aol.com, ups-csdman@dgoh.org, usenikoboko@rediffmail.com, uuuuu_004@msn.com, vangtc.state.gov@usa.com, victoria50001@bol.com.br, victoria50005@bol.com.br, victoria_50000@yahoo.com, victoriafinancehome@gmail.com, victoriafinanciallink@gmail.com, viveande@yahoo.com, vvvvvvvvvvvvvvvvvvvvvvvvvvvv_1@msn.com, waltermike20111@yahoo.com, waltermike219@libero.it, web.info_091@btinternet.com, webmaster.emailconfirmation@gmail.com, webweb29@rocketmail.com, webweb79@ymail.com, western_union111@9.cn, westernmoney.westernmoney.tran@gmail.com, westernunion201237@yahoo.com, westernunionheadoffice99966@yahoo.es, wesunion8@gmail.com, william_favour12@yahoo.com, williama_jason_01@yahoo.ca, williams_jason_01@yahoo.ca, womenfoundation@wwjd.ru, womenoffaithsouthafrica@yahoo.com, worlg_reg_focus@mail.com, wubagentofficebf@voila.fr, wungkinyoung@rediffmail.com, wunion-bf@w.cn, ww_western_union1978@9.cn, wwwmcddddd@rediffmail.com, yearw39@skymail.mn, zamasfamily@gmail.com, zenbkplc417@gmail.com, zongo.dawa4@gmail.com, zszjean1001@msn.com'
	# str is the emails: this can be anything from an HTML document to a simple string
	# a@a.gn is the shortest domain, or n.dk is a real domain
	# empty string at first but then gets populated
	strToSearch = ""
	# takes all the stuff from str (website, ect.) and populates it into strToSearch 
	for line in str:
		strToSearch += line
	# checks to find all the emails printed within strToSearch
	email_pattern = re.compile("[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+.[a-zA-Z0-9_.]+") # regular expression
	emails = re.findall(email_pattern, strToSearch)
	testEmails(emails)
	numberofEmailURL(emails, url)
	# numberofEmail(emails) # for if you input string for URL

# function to validate the emails to check if they are true
def validateEmail(emails): # Largest email length is 254: http://www.rfc-editor.org/errata_search.php?rfc=3696&eid=1690
	if len(emails) > 5 and len(emails) < 254: # checking length of email to be greater than 5 (a@a.gn name is 6 in length)
		if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", emails) != None:
			return 1 # smallest domain could be k@k.st
	return 0

def numberofEmailURL(emails, url):
	print "There are " + str(len(emails)) + " emails in the URL: " + url

def numberofEmail(emails):
	print "There are " + str(len(emails)) + " emails."

def numberofFalseEmails():
	print "There are " + str(len(false_emails)) + " fake emails."

# will print all the emails that are valid/invalid in the strlist
def testEmails(emails):
	for i in emails:
		returns = validateEmail(i)
		if (returns == 1):
			true_emails.append(i)
		else:
			false_emails.append(i)

if __name__ == '__main__':
    main()