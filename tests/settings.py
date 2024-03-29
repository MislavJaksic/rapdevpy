test_xml_file_path = "tests/parser/data/example-cro.xml"
test_html_file_path = "tests/parser/data/example.html"
test_xml_file_string = b'<ObrazacURA xmlns:meta="meta-ns-value" xmlns:xsi="xsi-ns-value" xmlns="none-ns-value" verzijaSheme="1.0" xsi:schemaLocation="none-ns-value ObrazacURA-v1-0.xsd">\n    <meta:Metapodaci>\n        <meta:Naslov dc="http://purl.org/dc/elements/1.1/title">Knjiga primljenih (ulaznih) ra&#269;una</meta:Naslov>\n        <meta:Autor dc="http://purl.org/dc/elements/1.1/creator">IVAN HORVAT</meta:Autor>\n        <meta:Datum dc="http://purl.org/dc/elements/1.1/date">2019-02-05T10:55:44</meta:Datum>\n        <meta:Format dc="http://purl.org/dc/elements/1.1/format">text/xml</meta:Format>\n        <meta:Jezik dc="http://purl.org/dc/elements/1.1/language">hr-HR</meta:Jezik>\n        <meta:Identifikator dc="http://purl.org/dc/elements/1.1/identifier">d7716e91-71cd-46cc-beff-d703bfa98295\n        </meta:Identifikator>\n        <meta:Uskladjenost dc="http://purl.org/dc/terms/conformsTo">ObrazacURA-v1-0</meta:Uskladjenost>\n        <meta:Tip dc="http://purl.org/dc/elements/1.1/type">Elektroni&#269;ki obrazac</meta:Tip>\n        <meta:Adresant>Ministarstvo Financija, Porezna uprava, Zagreb</meta:Adresant>\n    </meta:Metapodaci>\n    <Zaglavlje>\n        <Razdoblje>\n            <DatumOd>2019-01-01</DatumOd>\n            <DatumDo>2019-01-31</DatumDo>\n        </Razdoblje>\n        <Obveznik>\n            <OIB>00000000001</OIB>\n            <Naziv>Dobra tvrtka d.o.o.</Naziv>\n            <Adresa>\n                <Mjesto>Zagreb</Mjesto>\n                <Ulica>Radni&#269;ka</Ulica>\n                <Broj>1</Broj>\n                <DodatakKucnomBroju>a</DodatakKucnomBroju>\n            </Adresa>\n            <PodrucjeDjelatnosti>A</PodrucjeDjelatnosti>\n            <SifraDjelatnosti>0111</SifraDjelatnosti>\n        </Obveznik>\n        <ObracunSastavio>\n            <Ime>Ivan</Ime>\n            <Prezime>Horvat</Prezime>\n        </ObracunSastavio>\n    </Zaglavlje>\n    <Tijelo>\n        <Racuni>\n            <R>\n                <R1>1</R1>\n                <R2>2354/1/1</R2>\n                <R3>2019-01-05</R3>\n                <R4>Ivan Horvat</R4>\n                <R5>Ilica 1, Zagreb</R5>\n                <R6>1</R6>\n                <R7>10000000000</R7>\n                <R8>0.00</R8>\n                <R9>0.00</R9>\n                <R10>0.00</R10>\n                <R11>0.00</R11>\n                <R12>0.00</R12>\n                <R13>0.00</R13>\n                <R14>0.00</R14>\n                <R15>0.00</R15>\n                <R16>0.00</R16>\n                <R17>0.00</R17>\n                <R18>0.00</R18>\n            </R>\n        </Racuni>\n        <Ukupno>\n            <U8>0.00</U8>\n            <U9>0.00</U9>\n            <U10>0.00</U10>\n            <U11>0.00</U11>\n            <U12>0.00</U12>\n            <U13>0.00</U13>\n            <U14>0.00</U14>\n            <U15>0.00</U15>\n            <U16>0.00</U16>\n            <U17>0.00</U17>\n            <U18>0.00</U18>\n        </Ukupno>\n    </Tijelo>\n</ObrazacURA>\n'
test_html_file_string = b'<!DOCTYPE html>\n<html>\n  <head>\n    <meta charset="utf-8"/>\n    <title>Mozilla logo title!</title>\n  </head>\n  <body>\n<p>Paragraph</p>\n</body>\n</html>\n'
test_xml_first_element_string = b'<meta:Naslov xmlns:meta="meta-ns-value" xmlns:xsi="xsi-ns-value" xmlns="none-ns-value" dc="http://purl.org/dc/elements/1.1/title">Knjiga primljenih (ulaznih) ra&#269;una</meta:Naslov>\n        \n'
test_xml_root_descendants = [
    "ObrazacURA",
    "Metapodaci",
    "Naslov",
    "Autor",
    "Datum",
    "Format",
    "Jezik",
    "Identifikator",
    "Uskladjenost",
    "Tip",
    "Adresant",
    "Zaglavlje",
    "Razdoblje",
    "DatumOd",
    "DatumDo",
    "Obveznik",
    "OIB",
    "Naziv",
    "Adresa",
    "Mjesto",
    "Ulica",
    "Broj",
    "DodatakKucnomBroju",
    "PodrucjeDjelatnosti",
    "SifraDjelatnosti",
    "ObracunSastavio",
    "Ime",
    "Prezime",
    "Tijelo",
    "Racuni",
    "R",
    "R1",
    "R2",
    "R3",
    "R4",
    "R5",
    "R6",
    "R7",
    "R8",
    "R9",
    "R10",
    "R11",
    "R12",
    "R13",
    "R14",
    "R15",
    "R16",
    "R17",
    "R18",
    "Ukupno",
    "U8",
    "U9",
    "U10",
    "U11",
    "U12",
    "U13",
    "U14",
    "U15",
    "U16",
    "U17",
    "U18",
]

test_edges_file_path = "tests/parser/data/edges.csv"

test_cache_path = ".testcache"

test_in_memory_database = "sqlite:///:memory:"
