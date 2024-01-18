# Projekta apraksts

## Ievads

Šis ir automatizācijas projekta darbs. Tajā lietoju web-scraping tehnoloģiju, lai autorizētos savā last.fm kontā un no tā saņemtu personalizētas mūzikas rekomendācijas, glabājot tās csv failā. Last.fm ir mājaslapa, kura caur lietotāja Spotify vai Apple Music kontu seko līdzi viņa mūzikas klausījumiem, pēc tam ģenerējot rekomendācijas, balstoties uz iekrāto informāciju. Mājaslapā rekomendācijas gan ir grūti pārskatāmas - dažas no tām ir dziesmas, kuras jau esi klausījies, dažas ir balstītas uz izpildītājiem, kurus neklausies bieži, un dažas atkārtojas vairāku dienu garumā. Šo iemeslu dēļ es izlēmu automatizēt šo rekomendāciju pārskates procesu ar programmu, kura ļauj saņemt specifisku vai jebkādu izpildītāju rekomendācijas, kuras vēl nav klausītas, un šo informāciju glabātu 'csv' tipa failā, lai varētu nodrošināt, ka citā dienā apskatītās rekomendācijas neatkārtotos, un lai to varētu viegli pārskatīt.

## Programmas izmantošanas iespējas

Programmu var lietot cilvēki, kuriem ir izveidots Last.fm konts, kas seko līdzi viņu mūzikas klausījumu vēsturei.

Lietotāji var izvēlēties, kāda formāta rekomendācijas var iegūt - jaunas dziesmas, albumus vai arī izpildītājus. Lietotāji arī var norādīt, kādu izpildītāju ņemt kā 'iespaidu' rekomendācijām, vai arī nenorādīt nevienu, kurā gadījumā tiks atgrieztas visas rekomendācijas, kuras ir saistošas un kuras lietotājs nav iepriekš klausījies.

Programma ģenerēs 'csv' formāta teksta dokumentu, kurš glabāsies programmas folderī. Faila nosaukums tiks veidots atkarībā no lietotāja izvēlēm. Ja programma tiks atkārtoti palaista ar vienām un tām pašām izvēlēm, tad netiks veidots jauns fails, bet gan papildināts esošais fails.
Šī ir viena no galvenajām programmas priekšrocībām - rekomendācijas failā parādās tikai vienu reizi un ne vairāk, kas ļauj viegli pārskatīt, vai tiešām last.fm lapā ir parādījušās jaunas rekomendācijas vai nē. Terminālī katra jaunā rekomendācija ir paziņota, kas ļauj viegli to ievērot.

## Izmantotās Python bibliotēkas

Projektā galvenā izmantotā bibliotēka ir Selenium Webdriver, kā arī 'time' un 'os.path'.\

1. No moduļa "selenium" importēju sekojošo :

- - #### **'webdriver'** - lai varētu lietot web-scraping funkcijas, autorizēties mājaslapā last.fm, un iegūt nepieciešamo informāciju
- - #### **'service'** -lai nodrošinātu pārlūka un programmas saziņu, ka pārlūks tiek automatizēts.
- - #### **'By'** - lai nodrošinātu elementu atrašanu HTML mājaslapās. Tā ļauj meklēt HTML elementus pēc dažādiem atribūtiem, kā class, tag-name vai ID.
- - #### **'NoSuchElementException"** - šī ir kļūda, kas parādās, kad selenium driver nevar atrast tam minēto elementu. Tas tika lietots, lai noķertu kļūdu, kad nevarēja konkrēti zināt, vai elements būs redzams lapā vai nē, vai arī, kad lietojamu elementu vajadzēja atšķirt no nelietojama(reklāmas) elementa.

2. izmantoju **'time'**, lai varētu uzpauzēt programmu, kamēr lapa ielādējas, lai nodrošinātu pareizu selenium webdriver darbību.

3. izmantoju **'os.path'**, lai pārbaudītu, vai konkrēts fails eksistē projekta folderī.
