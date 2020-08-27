# BUcodeChange
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Changes on the server

1. Otvori sa terminal kde zadam IP,username,password            								#done
2. Vypise hostname																				#done
3. Spyta sa ktore z nazvu chcem nahradit														#done
4. Spyta sa ktore za ake ich chcem nahradit														#done
5. Sedne hostname a hosts																		#done
	-pomocou zadaneho BU kodu a current hostname name spravi sed hostname
	-pomoocu zadaneho BU kodu a noveho Bu kodu sedne hosts
6. Vypise sucessfull a novy hostname a nove hosts 												#done ;mozno bude treba zmenit slicing na regular expresion
7. Vypise IP adresu																				#done
8. prejde na druhu fazu cize vypne ssh kanal


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Changes on the repo server
9. spyta sa ci chcem urobit zmeny na repo server
10. ak nie ide dalej ak ano tak si vypyta heslo	
	otvori ssh kanal novy																				#tu treba zmenit password v main2 na password repa
11. Vezme stary hostname a z neho vytvori skratku														#done
12. pomocou skratky urobi sed 																			#tu treba zmenit password v main2 na password repa
13. premenuje file na novu skratku
14. zavre ssh kanal repo servera
15. otvori kanal normalneho servera a da reboot 






//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Changes on the ILO of the server







