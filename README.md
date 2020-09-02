# BUcodeChange
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Changes on the server

1. Otvori sa terminal kde zadam IP,username,password            								#done
2. Vypise hostname																				#done
3. Spyta sa ktore z nazvu chcem nahradit														#done
4. Spyta sa ktore za ake ich chcem nahradit														#done
5. Sedne hostname a hosts																		#done
	-pomocou zadaneho BU kodu a current hostname name spravi sed hostname						#done
	-pomoocu zadaneho BU kodu a noveho Bu kodu sedne hosts										#done
6. Vypise sucessfull a novy hostname a nove hosts 												#done ;mozno bude treba zmenit slicing na regular expresion
7. Vypise IP adresu																				#done
8. reboot																						#done



//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Changes on the repo server
9. spyta sa ci chcem urobit zmeny na repo servera														#done
10. ak nie ide dalej ak ano tak si vypyta heslo															#done									
	otvori ssh kanal novy																				#tu treba zmenit password v main2 na password repa
11. Vezme stary hostname a z neho vytvori skratku														#done
12. pomocou skratky urobi sed 																			#done
	-input pre password repo pridat																		#done

13. premenuje file na novu skratku																		#done
14. zavre ssh kanal repo servera 																		#done
15. urobit prehladnejsi terminal
	-pridat lines kde co zacina a konci																	#done
	-specifikovat v akom tvare zadat 																	#done

/////////////////////////////////////////
Debugging na centOS
1.Funguje vsetko az po reboot										
2.Nefungujuci reboot v prvej casti kodu 				#fixed, bolo 																										treba aby pockal 0.1s na terminal odpoved


3.repo server nesedne
4. repo server nemovne



//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Changes on the ILO of the server







