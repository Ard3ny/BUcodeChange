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
8. Rebootne																						#done
9. Program pocka ak napisem N pri reboote az potom sa vypne


BUGS to fix

1. Vymenit aaa heslo z testu																	#done
2. reboot namiesto pwd 																			#done
3. sed hosts pridat																				#done
4. pridat vypis zo sed hosts																	#done

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Changes on the repo server
1. Terminal ktore si vyziada heslo
2. Podla BU change zadanej z prvej fazy kodu sa najde repo cd config/BUcode
3. Podla noveho BUcode sa vykona sed 
4. Premenovat subor oldBUrepo na newBUrepo
5. Vypise status





//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Changes on the ILO of the server
