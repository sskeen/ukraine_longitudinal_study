"""
Ukraine administrative unit mappings for ULS pipeline.

ADMIN_UNIT_TO_OBLAST: Postal code prefix (2 digits) → Oblast name
RAION_UA_TO_EN: Ukrainian raion names → English translations

Sources:
- Ukrposhta postal code system: https://en.wikipedia.org/wiki/Postal_codes_in_Ukraine
- Raions of Ukraine (post-2020 reform): https://en.wikipedia.org/wiki/Raions_of_Ukraine
"""

# Postal code prefix → Oblast
# Source: https://en.wikipedia.org/wiki/Postal_codes_in_Ukraine

ADMIN_UNIT_TO_OBLAST = {
    # Kyiv city (01-06)
    '01': 'Kyiv', '02': 'Kyiv', '03': 'Kyiv',
    '04': 'Kyiv', '05': 'Kyiv', '06': 'Kyiv',
    # Kyiv Oblast (07-09)
    '07': 'Kyiv Oblast', '08': 'Kyiv Oblast', '09': 'Kyiv Oblast',
    # Zhytomyr Oblast (10-13)
    '10': 'Zhytomyr Oblast', '11': 'Zhytomyr Oblast',
    '12': 'Zhytomyr Oblast', '13': 'Zhytomyr Oblast',
    # Chernihiv Oblast (14-17)
    '14': 'Chernihiv Oblast', '15': 'Chernihiv Oblast',
    '16': 'Chernihiv Oblast', '17': 'Chernihiv Oblast',
    # Cherkasy Oblast (18-22)
    '18': 'Cherkasy Oblast', '19': 'Cherkasy Oblast', '20': 'Cherkasy Oblast',
    '21': 'Cherkasy Oblast', '22': 'Cherkasy Oblast',
    # Vinnytsia Oblast (23-24)
    '23': 'Vinnytsia Oblast', '24': 'Vinnytsia Oblast',
    # Kirovohrad Oblast (25-28)
    '25': 'Kirovohrad Oblast', '26': 'Kirovohrad Oblast',
    '27': 'Kirovohrad Oblast', '28': 'Kirovohrad Oblast',
    # Khmelnytskyi Oblast (29-32)
    '29': 'Khmelnytskyi Oblast', '30': 'Khmelnytskyi Oblast',
    '31': 'Khmelnytskyi Oblast', '32': 'Khmelnytskyi Oblast',
    # Rivne Oblast (33-35)
    '33': 'Rivne Oblast', '34': 'Rivne Oblast', '35': 'Rivne Oblast',
    # Poltava Oblast (36-39)
    '36': 'Poltava Oblast', '37': 'Poltava Oblast',
    '38': 'Poltava Oblast', '39': 'Poltava Oblast',
    # Sumy Oblast (40-42)
    '40': 'Sumy Oblast', '41': 'Sumy Oblast', '42': 'Sumy Oblast',
    # Volyn Oblast (43-45)
    '43': 'Volyn Oblast', '44': 'Volyn Oblast', '45': 'Volyn Oblast',
    # Ternopil Oblast (46-48)
    '46': 'Ternopil Oblast', '47': 'Ternopil Oblast', '48': 'Ternopil Oblast',
    # Dnipropetrovsk Oblast (49-53)
    '49': 'Dnipropetrovsk Oblast', '50': 'Dnipropetrovsk Oblast',
    '51': 'Dnipropetrovsk Oblast', '52': 'Dnipropetrovsk Oblast',
    '53': 'Dnipropetrovsk Oblast',
    # Mykolaiv Oblast (54-57)
    '54': 'Mykolaiv Oblast', '55': 'Mykolaiv Oblast',
    '56': 'Mykolaiv Oblast', '57': 'Mykolaiv Oblast',
    # Chernivtsi Oblast (58-60)
    '58': 'Chernivtsi Oblast', '59': 'Chernivtsi Oblast', '60': 'Chernivtsi Oblast',
    # Kharkiv Oblast (61-64)
    '61': 'Kharkiv Oblast', '62': 'Kharkiv Oblast',
    '63': 'Kharkiv Oblast', '64': 'Kharkiv Oblast',
    # Odesa Oblast (65-68)
    '65': 'Odesa Oblast', '66': 'Odesa Oblast',
    '67': 'Odesa Oblast', '68': 'Odesa Oblast',
    # Zaporizhzhia Oblast (69-72)
    '69': 'Zaporizhzhia Oblast', '70': 'Zaporizhzhia Oblast',
    '71': 'Zaporizhzhia Oblast', '72': 'Zaporizhzhia Oblast',
    # Kherson Oblast (73-75)
    '73': 'Kherson Oblast', '74': 'Kherson Oblast', '75': 'Kherson Oblast',
    # Ivano-Frankivsk Oblast (76-78)
    '76': 'Ivano-Frankivsk Oblast', '77': 'Ivano-Frankivsk Oblast',
    '78': 'Ivano-Frankivsk Oblast',
    # Lviv Oblast (79-82)
    '79': 'Lviv Oblast', '80': 'Lviv Oblast',
    '81': 'Lviv Oblast', '82': 'Lviv Oblast',
    # Donetsk Oblast (83-87)
    '83': 'Donetsk Oblast', '84': 'Donetsk Oblast', '85': 'Donetsk Oblast',
    '86': 'Donetsk Oblast', '87': 'Donetsk Oblast',
    # Zakarpattia Oblast (88-90)
    '88': 'Zakarpattia Oblast', '89': 'Zakarpattia Oblast', '90': 'Zakarpattia Oblast',
    # Luhansk Oblast (91-94)
    '91': 'Luhansk Oblast', '92': 'Luhansk Oblast',
    '93': 'Luhansk Oblast', '94': 'Luhansk Oblast',
    # AR Crimea (95-98) & Sevastopol (99)
    '95': 'AR Crimea', '96': 'AR Crimea', '97': 'AR Crimea', '98': 'AR Crimea',
    '99': 'Sevastopol',
}


# Ukrainian raion names → English translations
# Source: https://en.wikipedia.org/wiki/Raions_of_Ukraine (post-2020 reform: 136 raions)

RAION_UA_TO_EN = {
    # Cherkasy Oblast
    'Звенигородський район': 'Zvenyhorodka Raion',
    'Золотоніський район': 'Zolotonosha Raion',
    'Уманський район': 'Uman Raion',
    'Черкаський район': 'Cherkasy Raion',
    # Chernihiv Oblast
    'Корюківський район': 'Koriukivka Raion',
    'Ніжинський район': 'Nizhyn Raion',
    'Новгород-Сіверський район': 'Novhorod-Siverskyi Raion',
    'Прилуцький район': 'Pryluky Raion',
    'Чернігівський район': 'Chernihiv Raion',
    # Chernivtsi Oblast
    'Вижницький район': 'Vyzhnytsia Raion',
    'Дністровський район': 'Dnistrovskyi Raion',
    'Чернівецький район': 'Chernivtsi Raion',
    # Dnipropetrovsk Oblast
    'Дніпровський район': 'Dnipro Raion',
    'Кам\'янський район': 'Kamianske Raion',
    'Криворізький район': 'Kryvyi Rih Raion',
    'Нікопольський район': 'Nikopol Raion',
    'Новомосковський район': 'Novomoskovsk Raion',
    'Павлоградський район': 'Pavlohrad Raion',
    'Синельниківський район': 'Synelnykove Raion',
    # Donetsk Oblast
    'Бахмутський район': 'Bakhmut Raion',
    'Волноваський район': 'Volnovakha Raion',
    'Горлівський район': 'Horlivka Raion',
    'Донецький район': 'Donetsk Raion',
    'Кальміуський район': 'Kalmius Raion',
    'Краматорський район': 'Kramatorsk Raion',
    'Маріупольський район': 'Mariupol Raion',
    'Покровський район': 'Pokrovsk Raion',
    # Ivano-Frankivsk Oblast
    'Верховинський район': 'Verkhovyna Raion',
    'Івано-Франківський район': 'Ivano-Frankivsk Raion',
    'Калуський район': 'Kalush Raion',
    'Коломийський район': 'Kolomyia Raion',
    'Косівський район': 'Kosiv Raion',
    'Надвірнянський район': 'Nadvirna Raion',
    # Kharkiv Oblast
    'Богодухівський район': 'Bohodukhiv Raion',
    'Ізюмський район': 'Izium Raion',
    'Красноградський район': 'Krasnohrad Raion',
    'Куп\'янський район': 'Kupiansk Raion',
    'Лозівський район': 'Lozova Raion',
    'Харківський район': 'Kharkiv Raion',
    'Чугуївський район': 'Chuhuiv Raion',
    # Kherson Oblast
    'Бериславський район': 'Beryslav Raion',
    'Генічеський район': 'Henichesk Raion',
    'Каховський район': 'Kakhovka Raion',
    'Скадовський район': 'Skadovsk Raion',
    'Херсонський район': 'Kherson Raion',
    # Khmelnytskyi Oblast
    'Кам\'янець-Подільський район': 'Kamianets-Podilskyi Raion',
    'Хмельницький район': 'Khmelnytskyi Raion',
    'Шепетівський район': 'Shepetivka Raion',
    # Kirovohrad Oblast
    'Голованівський район': 'Holovanivsk Raion',
    'Кропивницький район': 'Kropyvnytskyi Raion',
    'Новоукраїнський район': 'Novoukrainka Raion',
    'Олександрійський район': 'Oleksandriia Raion',
    # Kyiv Oblast
    'Білоцерківський район': 'Bila Tserkva Raion',
    'Бориспільський район': 'Boryspil Raion',
    'Броварський район': 'Brovary Raion',
    'Бучанський район': 'Bucha Raion',
    'Вишгородський район': 'Vyshhorod Raion',
    'Обухівський район': 'Obukhiv Raion',
    'Фастівський район': 'Fastiv Raion',
    # Luhansk Oblast
    'Алчевський район': 'Alchevsk Raion',
    'Довжанський район': 'Dovzhansk Raion',
    'Луганський район': 'Luhansk Raion',
    'Ровеньківський район': 'Rovenky Raion',
    'Сватівський район': 'Svatove Raion',
    'Сєвєродонецький район': 'Sievierodonetsk Raion',
    'Старобільський район': 'Starobilsk Raion',
    'Щастинський район': 'Shchastia Raion',
    # Lviv Oblast
    'Дрогобицький район': 'Drohobych Raion',
    'Золочівський район': 'Zolochiv Raion',
    'Львівський район': 'Lviv Raion',
    'Самбірський район': 'Sambir Raion',
    'Стрийський район': 'Stryi Raion',
    'Червоноградський район': 'Chervonohrad Raion',
    'Яворівський район': 'Yavoriv Raion',
    # Mykolaiv Oblast
    'Баштанський район': 'Bashtanka Raion',
    'Вознесенський район': 'Voznesensk Raion',
    'Миколаївський район': 'Mykolaiv Raion',
    'Первомайський район': 'Pervomaisk Raion',
    # Odesa Oblast
    'Білгород-Дністровський район': 'Bilhorod-Dnistrovskyi Raion',
    'Березівський район': 'Berezivka Raion',
    'Болградський район': 'Bolhrad Raion',
    'Ізмаїльський район': 'Izmail Raion',
    'Одеський район': 'Odesa Raion',
    'Подільський район': 'Podilsk Raion',
    'Роздільнянський район': 'Rozdilna Raion',
    # Poltava Oblast
    'Кременчуцький район': 'Kremenchuk Raion',
    'Лубенський район': 'Lubny Raion',
    'Миргородський район': 'Myrhorod Raion',
    'Полтавський район': 'Poltava Raion',
    # Rivne Oblast
    'Вараський район': 'Varash Raion',
    'Дубенський район': 'Dubno Raion',
    'Рівненський район': 'Rivne Raion',
    'Сарненський район': 'Sarny Raion',
    # Sumy Oblast
    'Конотопський район': 'Konotop Raion',
    'Охтирський район': 'Okhtyrka Raion',
    'Роменський район': 'Romny Raion',
    'Сумський район': 'Sumy Raion',
    'Шосткинський район': 'Shostka Raion',
    # Ternopil Oblast
    'Кременецький район': 'Kremenets Raion',
    'Тернопільський район': 'Ternopil Raion',
    'Чортківський район': 'Chortkiv Raion',
    # Vinnytsia Oblast
    'Вінницький район': 'Vinnytsia Raion',
    'Гайсинський район': 'Haisyn Raion',
    'Жмеринський район': 'Zhmerynka Raion',
    'Могилів-Подільський район': 'Mohyliv-Podilskyi Raion',
    'Тульчинський район': 'Tulchyn Raion',
    'Хмільницький район': 'Khmilnyk Raion',
    # Volyn Oblast
    'Володимирський район': 'Volodymyr Raion',
    'Камінь-Каширський район': 'Kamin-Kashyrskyi Raion',
    'Ковельський район': 'Kovel Raion',
    'Луцький район': 'Lutsk Raion',
    # Zakarpattia Oblast
    'Берегівський район': 'Berehove Raion',
    'Мукачівський район': 'Mukachevo Raion',
    'Рахівський район': 'Rakhiv Raion',
    'Тячівський район': 'Tiachiv Raion',
    'Ужгородський район': 'Uzhhorod Raion',
    'Хустський район': 'Khust Raion',
    # Zaporizhzhia Oblast
    'Бердянський район': 'Berdiansk Raion',
    'Василівський район': 'Vasylivka Raion',
    'Запорізький район': 'Zaporizhzhia Raion',
    'Мелітопольський район': 'Melitopol Raion',
    'Пологівський район': 'Polohy Raion',
    # Zhytomyr Oblast
    'Бердичівський район': 'Berdychiv Raion',
    'Житомирський район': 'Zhytomyr Raion',
    'Звягельський район': 'Zviaghel Raion',
    'Коростенський район': 'Korosten Raion',
}
