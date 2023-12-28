# Generated by Django 3.2.13 on 2022-06-03 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recap', '0007_alter_fjcintegrateddatabase_noop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fjcintegrateddatabase',
            name='nature_of_suit',
            field=models.IntegerField(blank=True, choices=[(110, '110 Insurance'), (120, '120 Marine contract actions'), (130, '130 Miller act'), (140, '140 Negotiable instruments'), (150, '150 Overpayments & enforcement of judgments'), (151, '151 Overpayments under the medicare act'), (152, '152 Recovery of defaulted student loans'), (153, '153 Recovery of overpayments of vet benefits'), (160, "160 Stockholder's suits"), (190, '190 Other contract actions'), (195, '195 Contract product liability'), (196, '196 Contract franchise'), (210, '210 Land condemnation'), (220, '220 Foreclosure'), (230, '230 Rent, lease, ejectment'), (240, '240 Torts to land'), (245, '245 Tort product liability'), (290, '290 Other real property actions'), (310, '310 Airplane personal injury'), (315, '315 Airplane product liability'), (320, '320 Assault, libel, and slander'), (330, "330 Federal employers' liability"), (340, '340 Marine personal injury'), (345, '345 Marine - Product liability'), (350, '350 Motor vehicle personal injury'), (355, '355 Motor vehicle product liability'), (360, '360 Other personal liability'), (362, '362 Medical malpractice'), (365, '365 Personal injury - Product liability'), (367, '367 Health care / pharm'), (368, '368 Asbestos personal injury - Prod. Liab.'), (370, '370 Other fraud'), (371, '371 Truth in lending'), (375, '375 False Claims Act'), (380, '380 Other personal property damage'), (385, '385 Property damage - Product liability'), (400, '400 State re-appointment'), (410, '410 Antitrust'), (422, '422 Bankruptcy appeals rule 28 USC 158'), (423, '423 Bankruptcy withdrawal 28 USC 157'), (430, '430 Banks and banking'), (440, '440 Civil rights other'), (441, '441 Civil rights voting'), (442, '442 Civil rights jobs'), (443, '443 Civil rights accomodations'), (444, '444 Civil rights welfare'), (445, '445 Civil rights ADA employment'), (446, '446 Civil rights ADA other'), (448, '448 Education'), (450, '450 Interstate commerce'), (460, '460 Deportation'), (462, '462 Naturalization, petition for hearing of denial'), (463, '463 Habeas corpus - alien detainee'), (465, '465 Other immigration actions'), (470, '470 Civil (RICO)'), (480, '480 Consumer credit'), (490, '490 Cable/Satellite TV'), (510, '510 Prisoner petitions - vacate sentence'), (530, '530 Prisoner petitions - habeas corpus'), (535, '535 Habeas corpus: Death penalty'), (540, '540 Prisoner petitions - mandamus and other'), (550, '550 Prisoner - civil rights'), (555, '555 Prisoner - prison condition'), (560, '560 Civil detainee'), (610, '610 Agricultural acts'), (620, '620 Food and drug acts'), (625, '625 Drug related seizure of property'), (630, '630 Liquor laws'), (640, '640 Railroad and trucks'), (650, '650 Airline regulations'), (660, '660 Occupational safety/health'), (690, '690 Other forfeiture and penalty suits'), (710, '710 Fair Labor Standards Act'), (720, '720 Labor/Management Relations Act'), (730, '730 Labor/Management report & disclosure'), (740, '740 Railway Labor Act'), (751, '751 Family and Medical Leave Act'), (790, '790 Other labor litigation'), (791, '791 Employee Retirement Income Security Act'), (810, '810 Selective service'), (820, '820 Copyright'), (830, '830 Patent'), (835, '835 Patent Abbreviated New Drug Application (ANDA)'), (840, '840 Trademark'), (850, '850 Securities, Commodities, Exchange'), (860, '860 Social security'), (861, '861 HIA (1395 FF) / Medicare'), (862, '862 Black lung'), (863, '863 D.I.W.C. / D.I.W.W.'), (864, '864 S.S.I.D.'), (865, '865 R.S.I.'), (870, '870 Tax suits'), (871, '871 IRS 3rd party suits 26 USC 7609'), (875, '875 Customer challenge 12 USC 3410'), (890, '890 Other statutory actions'), (891, '891 Agricultural acts'), (892, '892 Economic Stabilization Act'), (893, '893 Environmental matters'), (894, '894 Energy Allocation Act'), (895, '895 Freedom of Information Act of 1974'), (896, '896 Arbitration'), (899, '899 Administrative procedure act / review or appeal of agency decision'), (900, '900 Appeal of fee - equal access to justice'), (910, '910 Domestic relations'), (920, '920 Insanity'), (930, '930 Probate'), (940, '940 Substitute trustee'), (950, '950 Constitutionality of state statutes'), (990, '990 Other'), (992, '992 Local jurisdictional appeal'), (999, '999 Miscellaneous')], help_text='A three digit statistical code representing the nature of suit of the action filed.', null=True),
        ),
    ]
