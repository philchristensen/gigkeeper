# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

from modu import util

# states dictionary used in state select fields.
states = util.OrderedDict([
	('AL', 'Alabama'),
	('AK', 'Alaska'),
	('AZ', 'Arizona'),
	('AR', 'Arkansas'),
	('CA', 'California'),
	('CO', 'Colorado'),
	('CT', 'Connecticut'),
	('DE', 'Delaware'),
	('DC', 'District of Columbia'),
	('FL', 'Florida'),
	('GA', 'Georgia'),
	('HI', 'Hawaii'),
	('ID', 'Idaho'),
	('IL', 'Illinois'),
	('IN', 'Indiana'),
	('IA', 'Iowa'),
	('KS', 'Kansas'),
	('KY', 'Kentucky'),
	('LA', 'Louisiana'),
	('ME', 'Maine'),
	('MD', 'Maryland'),
	('MA', 'Massachusetts'),
	('MI', 'Michigan'),
	('MN', 'Minnesota'),
	('MS', 'Mississippi'),
	('MO', 'Missouri'),
	('MT', 'Montana'),
	('NE', 'Nebraska'),
	('NV', 'Nevada'),
	('NH', 'New Hampshire'),
	('NJ', 'New Jersey'),
	('NM', 'New Mexico'),
	('NY', 'New York'),
	('NC', 'North Carolina'),
	('ND', 'North Dakota'),
	('OH', 'Ohio'),
	('OK', 'Oklahoma'),
	('OR', 'Oregon'),
	('PA', 'Pennsylvania'),
	('RI', 'Rhode Island'),
	('SC', 'South Carolina'),
	('SD', 'South Dakota'),
	('TN', 'Tennessee'),
	('TX', 'Texas'),
	('UT', 'Utah'),
	('VT', 'Vermont'),
	('VA', 'Virginia'),
	('WA', 'Washington'),
	('WV', 'West Virginia'),
	('WI', 'Wisconsin'),
	('WY', 'Wyoming'),
])

# country dictionary used in country select fields.
countries = util.OrderedDict([
	('AF', 'Afghanistan'),
	('AL', 'Albania'),
	('DZ', 'Algeria'),
	('AS', 'American Samoa'),
	('AD', 'Andorra'),
	('AO', 'Angola'),
	('AI', 'Anguilla'),
	('AQ', 'Antarctica'),
	('AG', 'Antigua & Barbuda'),
	('AN', 'Antilles, Netherlands'),
	('SA', 'Arabia, Saudi'),
	('AR', 'Argentina'),
	('AM', 'Armenia'),
	('AW', 'Aruba'),
	('AU', 'Australia'),
	('AT', 'Austria'),
	('AZ', 'Azerbaijan'),
	('BS', 'Bahamas, The'),
	('BH', 'Bahrain'),
	('BD', 'Bangladesh'),
	('BB', 'Barbados'),
	('BY', 'Belarus'),
	('BE', 'Belgium'),
	('BZ', 'Belize'),
	('BJ', 'Benin'),
	('BM', 'Bermuda'),
	('BT', 'Bhutan'),
	('BO', 'Bolivia'),
	('BA', 'Bosnia and Herzegovina'),
	('BW', 'Botswana'),
	('BV', 'Bouvet Island'),
	('BR', 'Brazil'),
	('IO', 'British Indian Ocean Territory'),
	('VG', 'British Virgin Islands'),
	('BN', 'Brunei Darussalam'),
	('BG', 'Bulgaria'),
	('BF', 'Burkina Faso'),
	('BI', 'Burundi'),
	('KH', 'Cambodia'),
	('CM', 'Cameroon'),
	('CA', 'Canada'),
	('CV', 'Cape Verde'),
	('KY', 'Cayman Islands'),
	('CF', 'Central African Republic'),
	('TD', 'Chad'),
	('CL', 'Chile'),
	('CN', 'China'),
	('CX', 'Christmas Island'),
	('CC', 'Cocos (Keeling) Islands'),
	('CO', 'Colombia'),
	('KM', 'Comoros'),
	('CG', 'Congo'),
	('CD', 'Congo, Democratic Rep. of the'),
	('CK', 'Cook Islands'),
	('CR', 'Costa Rica'),
	('CI', 'Cote D\'Ivoire'),
	('HR', 'Croatia'),
	('CU', 'Cuba'),
	('CY', 'Cyprus'),
	('CZ', 'Czech Republic'),
	('DK', 'Denmark'),
	('DJ', 'Djibouti'),
	('DM', 'Dominica'),
	('DO', 'Dominican Republic'),
	('TP', 'East Timor (Timor-Leste)'),
	('EC', 'Ecuador'),
	('EG', 'Egypt'),
	('SV', 'El Salvador'),
	('GQ', 'Equatorial Guinea'),
	('ER', 'Eritrea'),
	('EE', 'Estonia'),
	('ET', 'Ethiopia'),
	('EU', 'European Union'),
	('FK', 'Falkland Islands (Malvinas)'),
	('FO', 'Faroe Islands'),
	('FJ', 'Fiji'),
	('FI', 'Finland'),
	('FR', 'France'),
	('GF', 'French Guiana'),
	('PF', 'French Polynesia'),
	('TF', 'French Southern Territories'),
	('GA', 'Gabon'),
	('GM', 'Gambia, the'),
	('GE', 'Georgia'),
	('DE', 'Germany'),
	('GH', 'Ghana'),
	('GI', 'Gibraltar'),
	('GR', 'Greece'),
	('GL', 'Greenland'),
	('GD', 'Grenada'),
	('GP', 'Guadeloupe'),
	('GU', 'Guam'),
	('GT', 'Guatemala'),
	('GG', 'Guernsey and Alderney'),
	('GN', 'Guinea'),
	('GW', 'Guinea-Bissau'),
	('GP', 'Guinea, Equatorial'),
	('GF', 'Guiana, French'),
	('GY', 'Guyana'),
	('HT', 'Haiti'),
	('HM', 'Heard and McDonald Islands'),
	('VA', 'Holy See (Vatican City State)'),
	('NL', 'Holland (see Netherlands)'),
	('HN', 'Honduras'),
	('HK', 'Hong Kong, (China)'),
	('HU', 'Hungary'),
	('IS', 'Iceland'),
	('IN', 'India'),
	('ID', 'Indonesia'),
	('IR', 'Iran, Islamic Republic of'),
	('IQ', 'Iraq'),
	('IE', 'Ireland'),
	('IL', 'Israel'),
	('CI', 'Ivory Coast (see Cote d\'Ivoire)'),
	('IT', 'Italy'),
	('JM', 'Jamaica'),
	('JP', 'Japan'),
	('JE', 'Jersey'),
	('JO', 'Jordan'),
	('KZ', 'Kazakhstan'),
	('KE', 'Kenya'),
	('KI', 'Kiribati'),
	('KP', 'Korea, Demo. People\'s Rep. of'),
	('KR', 'Korea, (South) Republic of'),
	('KW', 'Kuwait'),
	('KG', 'Kyrgyzstan'),
	('LA', 'Lao People\'s Democratic Republic'),
	('LV', 'Latvia'),
	('LB', 'Lebanon'),
	('LS', 'Lesotho'),
	('LR', 'Liberia'),
	('LY', 'Libyan Arab Jamahiriya'),
	('LI', 'Liechtenstein'),
	('LT', 'Lithuania'),
	('LU', 'Luxembourg'),
	('MO', 'Macao, (China)'),
	('MK', 'Macedonia, TFYR'),
	('MG', 'Madagascar'),
	('MW', 'Malawi'),
	('MY', 'Malaysia'),
	('MV', 'Maldives'),
	('ML', 'Mali'),
	('MT', 'Malta'),
	('IM', 'Man, Isle of'),
	('MH', 'Marshall Islands'),
	('MQ', 'Martinique'),
	('MR', 'Mauritania'),
	('MU', 'Mauritius'),
	('YT', 'Mayotte'),
	('MX', 'Mexico'),
	('FM', 'Micronesia, Federated States of'),
	('MD', 'Moldova, Republic of'),
	('MC', 'Monaco'),
	('MN', 'Mongolia'),
	('CS', 'Montenegro'),
	('MS', 'Montserrat'),
	('MA', 'Morocco'),
	('MZ', 'Mozambique'),
	('MM', 'Myanmar (ex-Burma)'),
	('NA', 'Namibia'),
	('NR', 'Nauru'),
	('NP', 'Nepal'),
	('NL', 'Netherlands'),
	('AN', 'Netherlands Antilles'),
	('NC', 'New Caledonia'),
	('NZ', 'New Zealand'),
	('NI', 'Nicaragua'),
	('NE', 'Niger'),
	('NG', 'Nigeria'),
	('NU', 'Niue'),
	('NF', 'Norfolk Island'),
	('MP', 'Northern Mariana Islands'),
	('NO', 'Norway'),
	('OM', 'Oman'),
	('PK', 'Pakistan'),
	('PW', 'Palau'),
	('PS', 'Palestinian Territory'),
	('PA', 'Panama'),
	('PG', 'Papua New Guinea'),
	('PY', 'Paraguay'),
	('PE', 'Peru'),
	('PH', 'Philippines'),
	('PN', 'Pitcairn Island'),
	('PL', 'Poland'),
	('PT', 'Portugal'),
	('PR', 'Puerto Rico'),
	('QA', 'Qatar'),
	('RE', 'Reunion'),
	('RO', 'Romania'),
	('RU', 'Russia (Russian Federation)'),
	('RW', 'Rwanda'),
	('EH', 'Sahara'),
	('SH', 'Saint Helena'),
	('KN', 'Saint Kitts and Nevis'),
	('LC', 'Saint Lucia'),
	('PM', 'Saint Pierre and Miquelon'),
	('VC', 'Saint Vincent and the Grenadines'),
	('WS', 'Samoa'),
	('SM', 'San Marino'),
	('ST', 'Sao Tome and Principe'),
	('SA', 'Saudi Arabia'),
	('SN', 'Senegal'),
	('RS', 'Serbia'),
	('SC', 'Seychelles'),
	('SL', 'Sierra Leone'),
	('SG', 'Singapore'),
	('SK', 'Slovakia'),
	('SI', 'Slovenia'),
	('SB', 'Solomon Islands'),
	('SO', 'Somalia'),
	('ZA', 'South Africa'),
	('GS', 'S. Georgia and S. Sandwich Is.'),
	('ES', 'Spain'),
	('LK', 'Sri Lanka (ex-Ceilan)'),
	('SD', 'Sudan'),
	('SR', 'Suriname'),
	('SJ', 'Svalbard and Jan Mayen Islands'),
	('SZ', 'Swaziland'),
	('SE', 'Sweden'),
	('CH', 'Switzerland'),
	('SY', 'Syrian Arab Republic'),
	('TW', 'Taiwan'),
	('TJ', 'Tajikistan'),
	('TZ', 'Tanzania, United Republic of'),
	('TH', 'Thailand'),
	('TL', 'Timor-Leste (East Timor)'),
	('TG', 'Togo'),
	('TK', 'Tokelau'),
	('TO', 'Tonga'),
	('TT', 'Trinidad & Tobago'),
	('TN', 'Tunisia'),
	('TR', 'Turkey'),
	('TM', 'Turkmenistan'),
	('TC', 'Turks and Caicos Islands'),
	('TV', 'Tuvalu'),
	('UG', 'Uganda'),
	('UA', 'Ukraine'),
	('AE', 'United Arab Emirates'),
	('UK', 'United Kingdom'),
	('US', 'United States'),
	('UM', 'US Minor Outlying Islands'),
	('UY', 'Uruguay'),
	('UZ', 'Uzbekistan'),
	('VU', 'Vanuatu'),
	('VA', 'Vatican City State (Holy See)'),
	('VE', 'Venezuela'),
	('VN', 'Viet Nam'),
	('VG', 'Virgin Islands, British'),
	('VI', 'Virgin Islands, U.S.'),
	('WF', 'Wallis and Futuna'),
	('EH', 'Western Sahara'),
	('YE', 'Yemen'),
	('ZM', 'Zambia'),
	('ZW', 'Zimbabwe'),
])
