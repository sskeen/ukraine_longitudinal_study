
		*--------------------------------------------------------------------------------------*
		*																		               *
		*	Ukrainian Longitudinal Study  						   							   *
		*	WIP - NOT FOR DISTRIBUTION 														   *
		*	Proof-of-concept data structure: Bellingcat OSINT Civilian Harm in Ukraine 		   *
		*	geocoded event-level data -> Ukraine Longitudinal Survey (ULS) 					   *
		*	cross-sectional survey data 1:n merge. 											   *
		*																					   *
		*		uls_scratchpad.do										               		   *
		*		Simone J. Skeen (01-29-2026)									               *
		*																		               *
		*--------------------------------------------------------------------------------------*

clear all
set more off


* log

capture log close
log using uls_scratchpad_log.txt, replace

* set scheme, font

set scheme white_tableau
graph set window fontface "Arial"

* wd

cd "~/<my_directory>"
clear

* "child" dataset: import / convert		
		
import spss "<my_lvl_1_filename>.sav", case(lower) clear
*d

* rename / convert to .dta

save uls_2025_child_mheal_en, replace
				
use uls_2025_child_mheal_en, clear
			

	
* /////////// transform for 1:n merge
	
	* extract postcode substrings from num unique `num' identifier
	
	list num in 1/5
	list num in -5/l	
		
	* gen postcode

	tostring num, gen(num_str) format("%14.0f") force
	gen postcode = substr(num_str, 4, 5)

	list postcode num in 1/5
	list postcode num in -5/l  	
	
	* gen admin_unit
	
	gen admin_unit = substr(postcode, 1, 2)

	list admin_unit postcode num in 1/5
	list admin_unit postcode num in -5/l  		
	
	* gen oblast / map admin_unit values to oblast	

	clonevar oblast_pre = admin_unit
	
	define oblastl 01 "Kyiv" 02 "Kyiv" 03 "Kyiv" 04 "Kyiv" 05 "Kyiv" 06 "Kyiv" 07 "Kyiv Oblast" ///
		08 "Kyiv Oblast" 09 "Kyiv Oblast" 10 "Zhytomyr Oblast" 11 "Zhytomyr Oblast" 12 "Zhytomyr Oblast" ///
		13 "Zhytomyr Oblast" 14 "Chernihiv Oblast" 15 "Chernihiv Oblast" 16 "Chernihiv Oblast" ///
		17 "Chernihiv Oblast" 18 "Cherkasy Oblast" 19 "Cherkasy Oblast" 20 "Cherkasy Oblast" ///
		21 "Cherkasy Oblast" 22 "Cherkasy Oblast" 23 "Vinnytsia Oblast" 24 "Vinnytsia Oblast" ///
		25 "Kirovohrad Oblast" 26 "Kirovohrad Oblast" 27 "Kirovohrad Oblast" 28 "Kirovohrad Oblast" ///
		29 "Khmelnytskyi Oblast" 30 "Khmelnytskyi Oblast" 31 "Khmelnytskyi Oblast" 32 "Khmelnytskyi Oblast" ///
		33 "Rivne Oblast" 34 "Rivne Oblast" 35 "Rivne Oblast" 36 "Poltava Oblast" 37 "Poltava Oblast" ///
		38 "Poltava Oblast" 39 "Poltava Oblast" 40 "Sumy Oblast" 41 "Sumy Oblast" 42 "Sumy Oblast" ///
		43 "Volyn Oblast" 44 "Volyn Oblast" 45 "Volyn Oblast" 46 "Ternopil Oblast" 47 "Ternopil Oblast" ///
		48 "Ternopil Oblast" 49 "Dnipropetrovsk Oblast" 50 "Dnipropetrovsk Oblast" 51 "Dnipropetrovsk Oblast" ///
		52 "Dnipropetrovsk Oblast" 53 "Dnipropetrovsk Oblast" 54 "Mykolaiv Oblast" 55 "Mykolaiv Oblast" ///
		56 "Mykolaiv Oblast" 57 "Mykolaiv Oblast" 58 "Chernivtsi Oblast" 59 "Chernivtsi Oblast" ///
		60 "Chernivtsi Oblast" 61 "Kharkiv Oblast" 62 "Kharkiv Oblast" 63 "Kharkiv Oblast" 64 "Kharkiv Oblast" ///
		65 "Odesa Oblast" 66 "Odesa Oblast" 67 "Odesa Oblast" 68 "Odesa Oblast" 69 "Zaporizhzhia Oblast" ///
		70 "Zaporizhzhia Oblast" 71 "Zaporizhzhia Oblast" 72 "Zaporizhzhia Oblast" 73 "Kherson Oblast" ///
		74 "Kherson Oblast" 75 "Kherson Oblast" 76 "Ivano-Frankivsk Oblast" 77 "Ivano-Frankivsk Oblast" ///
		78 "Ivano-Frankivsk Oblast" 79 "Lviv Oblast" 80 "Lviv Oblast" 81 "Lviv Oblast" 82 "Lviv Oblast" ///
		83 "Donetsk Oblast" 84 "Donetsk Oblast" 85 "Donetsk Oblast" 86 "Donetsk Oblast" 87 "Donetsk Oblast" ///
		88 "Zakarpattia Oblast" 89 "Zakarpattia Oblast" 90 "Zakarpattia Oblast" 91 "Luhansk Oblast" ///
		92 "Luhansk Oblast" 93 "Luhansk Oblast" 94 "Luhansk Oblast" 95 "AR Crimea" 96 "AR Crimea" ///
		97 "AR Crimea" 98 "AR Crimea" 99 "Sevastopol"	

	destring admin_unit oblast_pre postcode, replace
	label values oblast_pre oblastl	
	
	decode oblast_pre, gen(oblast)	
	drop num_str oblast_pre	

* save to .dta

save d_uls_lvl1, replace

* convert d_uls_lvl2.csv to .dta

cd "~/<my_directory>"
clear

import delim using "d_uls_lvl2.csv", varnames(1) clear

cd "~/<my_directory>"

save d_uls_lvl2, replace

* merge

use d_uls_lvl1, clear

merge m:1 oblast using d_uls_lvl2

save d_uls_multilvl, replace

		* ------------------------------- *
		*     End of uls_scratchpad.do    *			
		* ------------------------------- *
