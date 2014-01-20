# Python: il web scraping fatto difficile

## Esempio 1 - Pagine Gialle

Con questo comando alle parole chiave del linguaggio aggiungiamo lo
spazio dei nomi di questa libreria e potremo utilizzare le funzioni in
essa presenti.

    # esempio1.1.py
    import requests

con il comando:

    dir(requests)

possiamo vedere cosa contiene la libreria. Se chi ha scritto la
libreria ha seguito le convenzioni stilistiche del python (e potrebbe
benissimo non averlo fatto) i nomi che iniziano con una lettera
maiuscola sono oggetti, quelli con la lettera minuscola sono funzioni
e ciò che inizia con il doppio underscore sono variabili speciali a
volte create automaticamente dall'interprete Python.

Per usare una funzione dovremo usare la notazione

    <libreria>.<nome>

ad esempio noi vogliamo usare la funzione get e useremo: `request.get`

Esiste anche un'altra forma con cui possiamo importare questo nome nello spazio di lavoro

    from requests import get

a questo punto potremo usare il nome 'get' senza il nome di libreria.

Quindi potremo fare:

    import requests 
    data = requests.get(...)

oppure

    from requests import get
    data = get(...)

Per ora la mia scelta è questa

    import requests
    data = requests.get("http://roma.paginegialle.it/lazio/roma/pizzeria.html")

nella variabile data ottengo il risultato che in questo caso è un Oggetto di tipo Response. Posso chiederlo sulla linea di comando

    In [22]: data
    Out[22]: <Response [200]>

Non è che si veda molto in effetti, ma anche qui possiamo usare la funzione dir

    dir(data)
    Out[23]: 
    ['__attrs__',
     '__bool__',
     '__class__',
     '__delattr__',
     '__dict__',
     '__doc__',
     '__format__',
     '__getattribute__',
     '__getstate__',
     '__hash__',
     '__init__',
     '__iter__',
     '__module__',
     '__new__',
     '__nonzero__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__setstate__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     '__weakref__',
     '_content',
     '_content_consumed',
     'apparent_encoding',
     'close',
     'connection',
     'content',
     'cookies',
     'elapsed',
     'encoding',
     'headers',
     'history',
     'iter_content',
     'iter_lines',
     'json',
     'links',
     'ok',
     'raise_for_status',
     'raw',
     'reason',
     'request',
     'status_code',
     'text',
     'url']

Non scendo nel dettaglio, vediamo alcuni campi. Ad esempio reason ci riporta in termini umani la ragione della risposta. In questo caso otteniamo un laconico

    In [33]: data.reason
    Out[33]: 'OK'

È andato tutto bene. Se c'è un errore' qui sarà scritto che errore è.

Questa risposta che abbiamo assegnato alla variabile 'data' è proprio
la risposta che io ottengo facendo la richiesta attraverso
internet. Non vi ho spiegato i dettagli del protocollo HTTP, basterà
dire che quando richiedo qualcosa posso ottenere quella cosa oppure un
errore. Quindi la risposta che ottengo può essere positiva o
negativa. Se il codice è 200 la risposta è positiva. Perciò quando
richiedo di stampare brevemente a video l'oggetto' ottengo quel
numero. Almeno mi dice che c'è' qualcosa di buono dentro.

Attenzione che c'è' errore ed errore (anzi per essere puntigliosi
esiste errore ed eccezione). Infatti se provassi a fare, prima cancello la variabile data dall'area di lavoro'

    del data 

e poi tento di scaricare una pagina da un server che proprio non esiste

    data = request.get('http://indirizzochenonesiste.non')

non ho ottenuto un risultato ma quella che in gergo si chiama
ECCEZIONE (una condizione d'errore' forte che impedisce l'esecuzione
del mio programma' infatti se si cerca di vedere il contenuto di data
proprio non esiste


è rimasto quello che era prima di chiamare la funzione. In generale
una eccezione all'interno' di uno script blocca l'esecuzione' dello
script (il che è ragionevole tante volte).

Invece se provo

    data = requests.get('http://www.repubblica.it/paginachenonce')

non ottengo un'eccezione' perché un server effettivamente esiste e ha
risposto con qualcosa che devo essere in grado di ispezionare. la
variabile data infatti viene effettivamente modificata e dentro ci
trovo:

    In [29]: data
    Out[29]: <Response [404]>

Il famoso errore 404 che i siti web forniscono all'utente' che cerca
di accedere ad una pagina che non esiste. Vediamo che è successo in parole umane:

    In [31]: data.reason
    Out[31]: 'Not Found'

Ripartiamo:

    import requests
    URL =  "http://roma.paginegialle.it/lazio/roma/pizzeria.html")
    data = requests.get(URL)

fin qui ha funzionato, abbiamo un codice 200 OK, ora mi prendo il
contenuto della risposta (ovvero la pagina Web che ho richiesto)

    html = data.content

ecco, ora nella variabile html c'è il testo, proprio come quello che
vedo in "Vedi sorgente del browser". Non ci credete.

potrei fare un

    print html

e vederlo a video. dato che è troppa roba lo metto in un file

    open('pizzerie.html','w').write(html)

ora lo apro con Emacs

ed ecco il file html che ho scaricato da internet (emacs mi fa anche
la colorazione del codice e mi riconosce che è xhtml. emacs lo capisce
dalla prima riga quella del DTD  ).

come si vede il 'modo' con cui emacs riconosce il file è XHTML questo
mette a disposizione un paio di menu appositi (HTML e SGML) - questo
mi dà modo di fare una parentesi per mostrarvi come il file che
abbiamo scaricato (che un browser mostra del tutto perfettamente sia
in effetti 'invalido' secondo lo standard)

Facciamo in modo che emacs lo veda come semplice XML

questo fa partire uno strumento di convalida in linea che prende la
definizione DTD e controlla il contenuto e ci dice che è Invalido e ci
segna come errori rossi in particolare possiamo vedere che
l'attributo' sizes è errato - vediamo cos'è l'attributo sizes e scopriamo che
è un nuovo attributo introdotto con la versione 5 di HTML 

http://www.w3schools.com/tags/att_link_sizes.asp

e non dovrebbe esserci in una pagina validata da HTML4.  L'autore
della pagina' ha quindi un po' pasticciato' tra le versioni di HTML -
poco male, dal punto di vista di chi 'vede' la pagina perché i browser
tentano comunque di 'mostrare' le cose che ricevono e, se nel caso,
dovessero formattare il link in una dimensione differente da quella
indicata da sizes tutt'al più' si spaginerebbe un po'
l'impaginazione. Se noi con un programma però deducessimo qualsiasi
tipo di informazione dal doctype verremmo tratti in errore. questo, se
ancora ce ne è bisogna, dimostra come si deve porre sempre un po'
attenzione in questo lavoro perché può essere reso problematico da
cose abbastanza impercettibili.

Nel nostro caso però, per ora, quest'errore non ci dà alcun fastidio.

Cosa vogliamo fare ora? Abbiamo detto che vogliamo estrarre i nomi
delle aziende sulla pagina.

Il primo approccio che vi mostro è quello che potrebbe adottare chi
non sa e non vuole sapere nulla di HTML, XML, XPAth, selettori CSS e
via dicendo. Si usano le "espressioni regolari". Nella teoria della
computer science e nella teoria dei linguaggi formali una espressione
regolare è una sequenza di caratteri che forma un pattern di ricerca
all'interno di un testo. È un linguaggio formale completo, è basato
su una solida base teorica definita dal matematico Stephen Cole
Kleene, negli anni '50 e funziona.

Ve lo mostro prima in Emacs che è più visibile abbiamo detto di avere il file HTML.

Noi sappiamo che quello che cerchiamo sta all'interno dell'attributo class=  di un tag a.

Facciamo così, nel primo passaggio manteniamoci in memoria tutto quello che è contenuto nei tag a.

    M-x keep-lines RETURN <a.*</a RETURN

A questo punto ho tutti i link, ma devo tenermi solo quelli che hanno la classe che mi interessa cioè

    M-x keep-lines RETURN class="_lms _noc"

A questo punto ad ogni riga di questo file corrisponde un nome di azienda.

Sempre con le espressioni regolari provvedo a pulire il tutto. Questa volta uso

    M-x query-replace-regexp RETURN ^.*title="Scheda Azienda \([^"]+\)".*$ RETURN \1 RETURN

Vediamo in python.

Prima importo la libreria delle espressioni regolari

    import re

Poi mi cerco tutti i link a

    links = re.findall(r'\<a.*\</a',html)

da questi filtro via tutti quelli che non rispettano la classe

    clinks = filter(lambda x: re.search(r'class="_lms _noc"',x), links)

ed infine ripulisco l'elenco ottenuto mantenendomi solo il nome che mi serve

    pizzerie = map(lambda x: re.sub(r'^.*title="Scheda Azienda ([^"]+)".*$','\\1',x), clinks)

alla fine nella variabile pizzerie ottengo quello che mi serviva

    ["THE VILLAGE PARCO DE' MEDICI",
     'PIZZERIA GRIGLIERIA CHICCO DI GRANO',
     'NAUMACHIA',
     'TERNO SECCO',
     'RISTORANTE LA MATRICIANA AI CONSOLI',
     'PIZZERIA LA GIANICOLENSE',
     'PIZZERIA ROMA SPARITA srl',
     'PIZZERIA PIZZA CIRO',
     'RISTORANTE PIZZERIA TRENTINO',
     'RISTORANTE BERNINETTA srl',
     'GAUCHOS PIZZA &amp; GRILL GAUCHO 69 srl',
     "L'ORA MAGICA",
     'RISTORANTE LO SCHIDIONE srl',
     'LA GALLINA BIANCA srl',
     'RISTORANTE DA BRUNO AI QUATTRO VENTI',
     'PUB KILL JOY KJ srl',
     'OTTAVIANI',
     "MARIO'S A TRASTEVERE",
     'DA OTELLO IN TRASTEVERE',
     'LA BALESTRA di RUGHI FERNANDO',
     'PICCOLA PAUSA di MOCCI ANNALISA &amp; C sas',
     "SCHIAVI D'ABRUZZO di NINO FALASCA",
     'TORCERVARA109',
     'AL GIARDINO DEL GATTO E LA VOLPE srl',
     'OSTERIA DEI PONTEFICI',
     'RISTORANTE PIZZERIA BIBO BAR',
     'LA MADIA',
     'EDEN MONTEVERDE RISTORANTE PIZZERIA ',
     'RISTORANTE PIZZERIA LA PIAZZETTA DE TRASTEVERE',
     'RISTORANTE IL BORGO DEGLI ULIVI di LIA ARBAU',
     'LA STIVA',
     'PORTO FLUVIALE FLUVIALE srl',
     'PIZZERIA RISTORANTE LE FINESTRE',
     'RAF srl',
     "L'ITALIA BUONA",
     'AL VECCHIO PIERROT S.M.P. srl',
     'ROSTI TREBIO srl',
     "FLANN O'BRIEN IRISH PUB",
     "RISTORANTE EDONE' EX ELMI",
     'HOTEL VILLA DELLE ROSE srl',
     'PIZZERIA ER PANONTO',
     'ARANCIO &amp; CANNELLA GIOVE srl',
     'TORCHIO SARDO',
     'RISTORANTE TUCCI',
     'RISTORANTE GIAPASI',
     'RISTORANTE NUOVO GUSTO',
     'GLI SPECIALISTI',
     'RISTORANTE FIORE DI ZUCCA',
     'COLUMBUS GES BAR srl',
     'RISTORANTE PIZZERIA LE VOLTE']


Questa volta l'ho fatto in python ma ho replicato perfettamente gli
stessi passi che ho fatto prima in EMACS

ho preso il file -come se fosse semplicemente un file di testo-
ho buttato via tutto quello che non fosse un link <a....</a
di questi ho tenuto solo quelli della classe buona
e infine ho buttato via tutti i caratteri che non mi servivano
e ho ottenuto il risultato.

Va notato che nel fare questa operazione non ho usato nessuno
strumento che 'capisce l'XML (o XPath o i selettori CSS), ho
semplicemente fatto un 'cerca e distruggi' di caratteri di testo.

Può andare bene per cose semplici… molto semplici

## Esempio 2 - PagineGialle / 2

>    http://arunrocks.com/easy-practical-web-scraping-in-python/

Facciamo un altro esempio altrettanto semplice ma questa volta
"capiamo l'XML"

Questa volta, abbiamo detto, vogliamo usare una libreria che capisce
l'XML, e non si limita a trattarlo come se fosse un testo.

Esistono due famiglie di librerie del genere secondo che vogliamo che,
nel capire l'XML, lo si voglia validare o meno. Nel nostro caso
abbiamo visto che il sito web ci risponde con qualcosa che potrebbe
non essere valido, quindi ci conviene usare una libreria che non
pretenda la validazione e che sia specializzato per l'html proprio.

Usiamo una funzione di libreria che si chiama fromstring dalla
libreria lxml.html

    from lxml.html import fromstring
    # URL =  "http://roma.paginegialle.it/lazio/roma/pizzeria.html"
    # data = requests.get(URL)
    # html = data.content

con questa libreria posso creare il DOM cioè il Document Object Model,
il modello in memoria del documento che ho letto, dove ogni pezzo
diventa un oggetto che può essere interrogato indipendentemente.

    dom = fromstring(html)

Questo è il primo passo per poi poter usare XPath o i selettori CSS,
che ci permette di navigare dentro il DOM. 


A questo punto possiamo selezionare i link di cui abbiamo bisogno e possiamo farlo indifferentemente con i selettori CSS, così:

    links_c = dom.cssselect("a._lms._noc")

oppure con XPath, così:

    links_x = dom.xpath("//a[@class='_lms _noc']")

Dovremmo verificare che sono uguali

    links_c == links_x

    In [124]: links_c == links_x
    Out[124]: True

ed infatti così è

A questo punto non ci resta che tirar fuori le informazioni:

    pizzerie_2 = [ link.attrib['title'][len("Scheda Azienda "):] for link in links_c ]

Questa cosa ve la spiego un po' più in dettaglio.

Quello che noi dobbiamo fare è questo:

    L = len("Scheda Azienda ") # Quanti caratteri eliminare davanti il nome
    pizzerie_2 = []            # Creo una lista di risultati vuota
    for link in links_c: # Per ogni link nella lista di ingresso
        title = link.attrib('title') # Prendo il valore dell'attributo title
        pizzerie_2.append(title[L:]) # Salvo il risultato

Il tutto il python si può scrivere (ma non di deve scrivere è solo una
cosa che potete trovare comoda)

    risultato = [ <funzione> for <variabile> in <lista> ]

Ed è quello che ho fatto: ho messo in pizzerie_2 l'attributo title, a
partire da un certo punto in poi di tutti i link indicati.

A questo punto dovrebbe risultare che:

    In [118]: pizzerie == pizzerie_2
    Out[118]: False

E invece no! Cosa è successo?

Cerchiamo di capirlo usando un filtro. Prendo i due array con i
risultati e li metto assieme in modo che al primo risultato del primo
corrisponda il primo del secondo. Lo faccio con la funzione 'zip'

    zip(pizzerie, pizzerie_2)

    [("THE VILLAGE PARCO DE' MEDICI", "THE VILLAGE PARCO DE' MEDICI"),
     ('PIZZERIA GRIGLIERIA CHICCO DI GRANO',
      'PIZZERIA GRIGLIERIA CHICCO DI GRANO'),
     ('NAUMACHIA', 'NAUMACHIA'),
     ('TERNO SECCO', 'TERNO SECCO'),

 Viene fuori un nuovo array con gli elementi accoppiati a due a due.

A questo punto filtro via quelli che non sono uguali con la funzione
filter usando una piccola funzione 'anonima' (una funzione così
semplice che non ha bisogno neppure di un nome), in questo caso
ritorna vero se i due elementi sono differenti. filter quindi produrrà
un nuovo array in cui ci sono solo gli elementi che tra loro due
risultano differenti. Si fa prima a farla questa cosa che a spiegarla.

    filter(lambda x: x[0]!=x[1], zip(pizzerie, pizzerie_2))

Alla fine il risultato è

    [('GAUCHOS PIZZA &amp; GRILL GAUCHO 69 srl',     'GAUCHOS PIZZA & GRILL GAUCHO 69 srl'),
     ('PICCOLA PAUSA di MOCCI ANNALISA &amp; C sas', 'PICCOLA PAUSA di MOCCI ANNALISA & C sas'),
     ('ARANCIO &amp; CANNELLA GIOVE srl',            'ARANCIO & CANNELLA GIOVE srl')]

Cos'è successo? In tutto l'array ci sono tre elementi differenti. E la
differenza sta nel carattere &. Beh, a "non capire l'XML" qualche
problema ce l'abbiamo.

Il carattere di testo & (E commerciale) è per il linguaggio XML un
carattere speciale. È proprio il carattere che serve a definire i
caratteri speciali! Ad esempio se in XML vogliamo definire il
carattere ™ (Trademark) in XML (che è progettato per usare solo un
alfabeto ristretto) bisogna usare il gruppo di caratteri &trade;

Quindi & da solo è un errore, e per definire il carattere & si usa
&amp; che è ciò che troviamo a sinistra (che sono le cose lette 'senza
capire l'XML'). A destra invece la libreria, che interpreta
correttamente l'XML, interpreta anche i caratteri speciali. È del
tutto logico il risultato quindi. Se non utilizziamo il metodo giusto
otteniamo il risultato corretto. Altrimenti dovremo fare
un'lavorazione per pulire i dati ottenuti.

## Esempio 3 - Ancora PagineGialle

Spero che fin qui siamo arrivati senza troppi traumi. Perché adesso viene il bello!

Usiamo un'altra libreria.

    from BeautifulSoup import BeautifulSoup

Si chiama così in onore della "mock turtle soup" di Lewis Carroll

> Bella Zuppa, così ricca e verde,
> che aspetti in una terrina bollente!
> Chi non si soffermerebbe su tali leccornie?
> Zuppa della sera, bella zuppa!
> Zuppa della sera, bella zuppa!

Riprendiamo il testo che è in html e facciamo la zuppa

    soup = BeautifulSoup(html)

a questo punto costruiamo la lista dei risultati

    pizzerie_3 = [ re.sub('^Scheda Azienda ',',h2['title']) for h2 in soup.findAll('a', attrs={'class': '_lms _noc'})]

e dovrebbe essere che

    pizzerie_3 == pizzerie_2

In definitiva il programma è così:

    from BeautifulSoup import BeautifulSoup

    soup = BeautifulSoup(html)

    pizzerie_3 = [ re.sub('^Scheda Azienda ','',h2['title']) for h2 in soup.findAll('a', attrs={'class': '_lms _noc'})]


## Esempio 4 - Linkedin

Tentiamo a questo punto di fare un passo oltre.

Diciamo di voler prendere un sito noto, ad esempio Linkedin, ed
estrarvi i dati relativi ad alcune aziende.

Immaginiamo di volere i dati di qualche grandi aziende
internazionale. Questa volta faremo un programma che si lancia dalla
linea di comando. Vogliamo una cosa del genere:

    getlinkedin1.py google microsoft oracle ibm facebook

per ottenere i dati che ci servono.

Introduciamo alcuni concetti nuovi.

Innanzitutto importiamo le funzioni e le librerie che ci servono

    from bs4 import BeautifulSoup
    import sys
    import requests

`bs4` è la versione 4 di BeutifulSoup. Ora creiamo un dizionario dove
inserire i risultati. 

    results = []

Creo una lista in cui mettere i risultati. 

A questo punto dobbiamo raccogliere dalla linea di comando la lista
dei nomi delle aziende. Si usa una particolare lista messa a
disposizione dalla libreria sys chiamata argv che contiene l'elenco
delle parole che abbiamo scritto sulla linea di comando. Poiché non ci
serve il nome del comando inizieremo a prenderla dal secondo elemento
in poi (in Python si inizia a contare da 0):

    companies = sys.argv[1:]

A questo punto possiamo iniziare il loop:

    for company in sys.argv[1:]:
         url = "http://www.linkedin.com/company/{}".format(company)
         raw = requests.get(url).content

         soup = BeautifulSoup(raw)

Questi sono più o meno gli stessi comandi che abbiamo visto finora. La
funzione `format` serve a sostituire le parentesi graffe nella stringa
con il contentuto della variabile `company`. Sembra strano che il nome
della funzione sia alla fine, vero? Ci saremmo aspettati qualcosa del
tipo:

    url = format("http://www.linkedin.com/company/{}",company)

Ok. Ne abbiamo già parlato. Questa è solo l'applicazione dei concetti
di linguaggio ad oggetti. La stringa:

     "http://www.linkedin.com/company/{}"

è un oggetto e quindi posso applicarci sopra dei metodi. Infatti posso
fare tranquillamente qualcosa del tipo:

     dir("pippo")

oppure

     help("pippo".format)
     Help on built-in function format:
     
     format(...)
          S.format(*args, **kwargs) -> string
    
          Return a formatted version of S, using substitutions from args and kwargs.
          The substitutions are identified by braces ('{' and '}').

Andiamo avanti:

    node = soup.find(attrs = {"class" : "grid-f"})

L'obiettivo adesso è buttar via tutto della pagina e tenersi solo il
pezzo che ci interessa, quindi andiamo a cercare la sezione della
pagine html dove c'è il quadro delle informazioni. La sezione è in
fondo alla pagina e inizia con un `div` che ha classe `grid-f`. In
mezzo alla zuppa vado a prendere proprio quest'elemento.

    if node!=None:
        info = node.find(attrs = {"class" : "basic-info"})
        titles = [item.get_text(strip=True) for item in info.findAll("dt")]
        data = [item.get_text(strip=True) for item in info.findAll("dd")]    
        output = dict(zip(titles,data))
    else:
        output = {}

Se lo trovo, a partire da quel nodo lì mi cerco la sezione delle
informazioni (`class="basic-info"`) e dentro questo prendo i titoli
dai tag `dt` e i valori da quelli `dd`. Dopo mi creo un dizionario
accoppiando gli elementi di una lista e dell'altra e usando la
funzione che crea i dizionari.  Nel caso in cui il nodo non esiste
semplicemente restituisco un dizionario vuoto.  Un 'dizionario'
(chiamato anche hash o mappa) è una collezione in cui è possibile
accedere agli oggetti attraverso una chiave qualsiasi (una stringa o
un numero). A differenza di una lista non è ordinata e soprattutto non
esiste un concetto di adiacenza delle chiavi. Per definirla si fa
semplicemente così:

    output['company']=company

Aggiungo al dizionario delle informazioni della singola azienda anche
il nome dell'azienda.

    results.append(output)

E salvo tutto nella lista dei risultati. E il loop è finito.

In realtà, per essere un po' buono nei confronti di Linkedin, posso
adottare un accorgimento: attendere un periodo di tempo casuale da 5 a
10 secondi prima di fare il prossimo giro del loop.

    import random, time
    sleep_time = random.uniform(5,10)
    time.sleep(sleep_time)

importo le librerie necessarie (questo avrei potuto metterlo
all'inizio, ma comunque anche mettendolo qui non cambia molto, non
saranno reimportate ad ogni giro di loop, ma solo la prima volta.

Estraggo un valore casuale da una distribuzione uniforme con limiti 5
e 10, e *dormo* per questo tempo.

Quando il loop è finito devo mostrare il risultato. Per esempio posso
fare così:

    import json
    print json.dumps(results, indent=2)

importo la libreria che gestisce il formato json e faccio un `dump`
del dizionario. Tutto qui.

Per usarlo posso fare una cosa simile a quella che mi ero ripromesso all'inizio:

    python getlinkedin1.py google microsoft oracle ibm facebook

oppure introdurre queste due righe all'inizio del programma:

	#! /usr/bin/env python
	# -*- coding: utf-8 -*-

poi renderlo eseguibile con

	chmod a+x getlinkedin1.py

e finalmente usarlo come:

	./getlinkedin1.py google microsoft oracle ibm facebook

e il risultato è:

     {
       "oracle": {
         "Website": "http://www.oracle.com", 
         "Company Size": "10,001+ employees", 
         "Industry": "Information Technology and Services", 
         "Founded": "1977", 
         "Type": "Public Company", 
         "company": "oracle"
       }, 
       "google": {
         "Website": "http://www.google.com", 
         "Company Size": "10,001+ employees", 
         "Industry": "Internet", 
         "Founded": "1998", 
         "Type": "Public Company", 
         "company": "google"
       }, 
       "facebook": {
         "Website": "http://www.facebook.com/", 
         "Company Size": "5001-10,000 employees", 
         "Industry": "Internet", 
         "Founded": "2004", 
         "Type": "Public Company", 
         "company": "facebook"
       }, 
       "microsoft": {
         "Website": "http://www.microsoft.com/", 
         "Company Size": "10,001+ employees", 
         "Industry": "Computer Software", 
         "Founded": "1975", 
         "Type": "Public Company", 
         "company": "microsoft"
       }, 
       "ibm": {
         "Company Size": "10,001+ employees", 
         "Website": "http://www.ibm.com", 
         "Industry": "Information Technology and Services", 
         "Type": "Public Company", 
         "company": "ibm"
       }
     }


Se avessi i nomi delle aziende in un file, uno per riga, invece di

    companies = sys.argv[1:]

potrei usare:

    companies = open(sys.argv[1],'r').readlines()

Se invece di visualizzare i dati in formato JSON vogliamo scriverli su
CSV possiamo usare una funzione così definita.


     import unicodecsv
     def write_csv_file(fname,content,delimiter=';'):
       try:
         with open(fname, 'wb') as csvfile:
             writer = unicodecsv.writer(csvfile, delimiter, encoding='utf-8')
             keys = content[0].keys()
             writer.writerow(keys)
             for element in content:          
               writer.writerow(element.values())
       except:
         raise

E poi usarla come:

     write_csv_file('linkedin_companies.csv',results)

Che scriverà i dati in un file csv chiamato csv.

## Esempio 5 - Enoteca Bulzoni


http://www.enotecabulzoni.it/en/view/Vini%20%20Bianchi/Pinot+Bianco+%22Penon%22/5439


## Esempio 6 - Mecanize

> http://stockrt.github.io/p/emulating-a-browser-in-python-with-mechanize/

Primo esempio.

Abbiamo visto la pagina informativa su Google messa a disposizione da
Linkedin. Quella è la pagina che un utente non autenticato a Linkedin
può vedere.

Questa è quella che invece può vedere un utente autenticato. È molto
differente, ci sono molte più informazioni a cui non abbiamo accesso
se non siamo autenticati.

Secondo Esempio.

Questa è normattiva, la collezione (purtroppo ancora parziale) delle
leggi nazionali. Se si preme quel pulsante lì in alto si può esportare
la legge in formato XML, ma prima bisogna passare per un test di
Turing (un capcha), poi si giunge in una pagina di selezione in cui
indicare a che data di vigenza si vuole scaricare la legge e poi
premere il pulsante "Esporta".

Qui non bisogna autenticarsi, ma se non si fa tutto il percorso
semplicemente non si raggiunge il risultato.

Per farla breve, non sempre se vediamo qualcosa su un browser è
semplice o possibile scaricare quella pagina attraverso un indirizzo
Internet. In generale questa cosa diventa sempre più rara.

Per questo motivo abbiamo bisogno di costruire programmi che emulano i
percorsi del browser proprio come se ci fosse un uomo a guidarli.

Questo è esattamente il punto in cui un linguaggio moderno come python
supera gli altri. Quello che abbiamo fatto fino ad adesso, con qualche
complicazione, sarebbe stato possibile anche farlo con R, questo no.

L'idea è di usare delle librerie apposite che colloquiano con i server
web proprio come se fossero dei browser. È un po' come se voi foste
nella pancia di browser e invece di cliccare a caso sullo schermo come
si fa di solito doveste dargli i comandi scrivendo linee di codice.

Come si fa?

Si inizia importando la libreria `mechanize`e creando un browser:

    import mechanize
    br = mechanize.Browser()

Diciamo al browser di gestire alcune opzioni comuni

    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

Se vogliamo possiamo definire alcune opzioni per il debug

    br.set_debug_http(True)
    br.set_debug_redirects(True)
    br.set_debug_responses(True)

Poi ci occupiamo di creare la sessione di lavoro, per questo abbiamo
bisogno di gestire i `cookie` di sessione:

    import cookielib
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)

Definiamo lo user-agent (e questo È barare):

    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

A questo punto facciamo qualcosa, prendo un sito a caso:

    r = br.open('http://google.com')
    html = r.read()

Oh… siamo più o meno dove eravamo prima.



    print br.title()

Stampo le forms disponibili:

    for f in br.forms():
        print f

C'è una sola form e quindi ottengo questo risultato:

    <f GET http://www.google.it/search application/x-www-form-urlencoded
      <HiddenControl(hl=it) (readonly)>
      <HiddenControl(source=hp) (readonly)>
      <TextControl(q=)>
      <SubmitControl(btnG=Cerca con Google) (readonly)>
      <SubmitControl(btnI=Mi sento fortunato) (readonly)>
      <HiddenControl(gbv=1) (readonly)>>

Questa è la rappresentazione della classica form di Google. Ci sono
sei controlli (pensate ad un controllo come ad un elemento con il
quale potete interagire come una casella di testo). Di questi 3 sono
nascosti e contengono dei valori preimpostati (ad esempio la
lingua). Poi c'è un controllo chiamaot `q` che è la casella di ricerca
(_query_) e i due classici pulsanti di Google ("Cerca con Google" e
"Mi sento fortunato").

Seleziono la prima form (quella della ricerca):

    br.select_form(nr=0)

Inserisco una chiave di ricerca:

    br.form['q']='data science'

E lancio la ricerca:

    r = br.submit()

A questo punto la mia pagina è cambiata. Se mi interessa posso avere
l'html della nuova pagina con:

    html = r.read()

Così a titolo di esempio facciamo una cosa così:

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html)
    nres = soup.find('div',attrs={'id':'resultStats'}).text
    print nres

E così è possibile verificare quanti risultati ha una certa ricerca di Google.

Oppure posso andare a selezionare all'interno dei risultati quelli
nella cui URL c'è `wikipedia`:

    wlinks =  [ w for w in br.links(url_regex='wikipedia') ]
    
    for l in wlinks:
        print l.url

Guardando il risultato:

    /url?q=http://en.wikipedia.org/wiki/Data_science&sa=U&ei=OXTRUp3wAcfJ4gS07oDIDA&ved=0CCYQFjAA&usg=AFQjCNE9mU0tkp8RMHL_B97WUs6rx91ZmQ
    /url?q=http://webcache.googleusercontent.com/search%3Fhl%3Dit%26q%3Dcache:9-f2bTZhGx8J:http://en.wikipedia.org/wiki/Data_science%252Bdata%2Bscience%26gbv%3D1%26ct%3Dclnk&sa=U&ei=OXTRUp3wAcfJ4gS07oDIDA&ved=0CCcQIDAA&usg=AFQjCNEWnaHGZ9SQvXa7x7EDyd7zOrpPbg
    /search?hl=it&gbv=1&q=related:en.wikipedia.org/wiki/Data_science+data+science&tbo=1&sa=X&ei=OXTRUp3wAcfJ4gS07oDIDA&ved=0CCgQHzAA
    /url?q=http://en.wikipedia.org/wiki/Data_science%23Origins&sa=U&ei=OXTRUp3wAcfJ4gS07oDIDA&ved=0CCoQ0gIoADAA&usg=AFQjCNHDhSHntwY3aajUKMncFR-HlQ5hPg
    /url?q=http://en.wikipedia.org/wiki/Data_science%23History&sa=U&ei=OXTRUp3wAcfJ4gS07oDIDA&ved=0CCsQ0gIoATAA&usg=AFQjCNFl6AxwELTborUNTf2ziJlZJaYhOw
    /url?q=http://en.wikipedia.org/wiki/Data_science%23Domain_Specific_Interests&sa=U&ei=OXTRUp3wAcfJ4gS07oDIDA&ved=0CCwQ0gIoAjAA&usg=AFQjCNEl_rKBUGT2-bVFnbLfDfWSZ6jYzQ
    /url?q=http://en.wikipedia.org/wiki/Data_science%23Research_Areas&sa=U&ei=OXTRUp3wAcfJ4gS07oDIDA&ved=0CC0Q0gIoAzAA&usg=AFQjCNHmxByaL4fxn220tvSSpIZKY2cF3A
    /url?q=http://en.wikipedia.org/wiki/Data_science&sa=U&ei=OXTRUp3wAcfJ4gS07oDIDA&ved=0CDUQ9QEwAg&usg=AFQjCNE9mU0tkp8RMHL_B97WUs6rx91ZmQ

si può notare che in una pagina dei risultati di google i link
indicati non rimandano VERAMENTE alle pagine trovate, ma ad un altro
link interno di Google che poi trasferirà l'utente. Probabilmente per
registrare informazioni di natura statistica o per il tracciamento
degli utenti.

Prendiamo il primo risultato

    w0 = wlinks[0]
    r = br.open(w0.url)

E verifichiamo di essere stato trasportato effettivamente sulla pagina di Wikipedia.

    print br.title()
    print br.geturl()

Per fare qualcosa con questa pagina riportiamo l'elenco delle lingue in cui la pagina è tradotta:

    html = r.read()
    soup = BeautifulSoup(html)
    a_li = soup.select('.interlanguage-link')
    print ('\n'.join([ li.a['lang']+" "+li.text for li in a_li])).encode('utf-8')

Così otteniamo:

    fa فارسی
    fr Français
    lv Latviešu
    ja 日本語
    ru Русский

## Esempio 7 - Un crawler

> https://github.com/creeveshft/Web_Scraping


Adesso vedremo l'implementazione di un particolare programma che è al
cuore della realizzazione dei motori di ricerca il `Web Crawler`. Il
crawler, che è chiamato anche spider o ant o scutter, raggiunge una
pagina Web e ne estrare tutti gli hyperlink che poi frequenta ad uno
ad uno per fare la stessa operazione. Alla fine avrà creato un grande
indice delle pagine disponibili.

Per l'implementazione di un crawler abbiamo bisogno di queste librerie:

    import sys
    from bs4 import BeautifulSoup
    import urlparse
    import mechanize

Partiamo da un indirizzo che forniamo sulla riga di comando:

    url = sys.argv[1]

Attiviamo il browser di mechanize:

    br = mechanize.Browser()

Creaiamo tre insiemi, uno con le url da visitare:

    urls = set()
    urls.add(url)

e uno con quelle già visitate:

    visited = set()

creiamone anche uno con le url che non si possono leggere

    errors = set()

E così iniziamo il loop:

    while len(urls)>0:

estraiamo un url:

        this = urls.pop()

e proviamo ad aprirlo:

        try:
            br.open(this)

poi per ognuno dei link presenti:

            for link in br.links():

creiamo una url assoluta 
                newurl =  urlparse.urljoin(link.base_url,link.url)

se non è già stata visitata, e non è già previsto di visitarla la
aggiungiamo all'elenco delle url da visitare

            if url in newurl and newurl not in visited:
                urls.add(newurl)
            visited.add(this)

Se qualcosa va male e c'è una eccezione inseriamo la url nella lista
degli errori:

        except:
            errors.add(this)

Poiché il processo può essere molto lungo inseriamo una stampa ogni
1000 url visitate:

    if len(visited) % 1000 == 0:
        print "E",len(errors),"U",len(urls),"V",len(visited)

L'operatore `%` è il modulo.

Alla fine salviamo due file, uno con le url visitate `links.txt` e uno
con gli errori `errors.txt`:

    open('links.txt','w').write('\n'.join(visited))
    open('errors.txt','w').write('\n'.join(errors))



# Webscraping con Python reso semplice

## Esempio 8 - Webscraping / 1

Finora abbiamo utilizzato librerie python generiche per la gestione
delle pagine Web. Con il passare del tempo questi metodi sono stati
sistematizzati in librerie di più alto livello realizzate proprio per
lo scopo di costruire programmi di webscraping.

Una di queste si chiama semplicemente `webscraping` e funziona grossomodo così:


Prima si importano le funzioni che ci interessano:

    from webscraping import download, xpath

poi si crea un motore per il download delle pagine

    engine = download.Download()

e si ottiene la pagina HTML:

    html = D.get('http://code.google.com/p/webscraping')

e fin qui stiamo più o meno dove eravamo con la libreria `requests`,
ma questo punto si può usare l'oggetto xpath per acquisire le informazioni.

    project_title = xpath.get(html, '//div[@id="pname"]/a/span')

## Esempio 9 - Webscraping / Pagine Gialle

Se vogliamo affrontare lo stesso problema dell'esempio 1 e 2 possiamo fare così:

Importiamo le librerie
    from webscraping import download, xpath

Creiamo il motore per il fetch della pagina

    engine = download.Download()

Definiamo la pagina e la scarichiamo:
    URL =  "http://roma.paginegialle.it/lazio/roma/pizzeria.html"
    html = engine.get(URL)

Creiamo l'oggetto da interrogare con xpath:

    doc = xpath.Doc(html)

Questo è un po' l'equivalente del `soup` di BeautifulSoup, ma potrò
essere interrogato solo con xpath.

Infine estraiamo le pizzerie:

    pizzerie = doc.search("//a[@class='_lms _noc']/@title")

Per la verità vogliamo eliminare la parte iniziale del titolo ('Scheda Azienda'), quindi:

    pizzerie = [ x[15:] for x in doc.search("//a[@class='_lms _noc']/@title")]

Allo stesso modo potranno essere estratti i numeri di telefono:

    tel = doc.search("//div[@class='tel']/span[@class='value']/text()")]

Prendiamo anche l'indirizzo:

    address = doc.search("//div[@class='address']/span[@class='street-address']/text()")

Mettiamo assieme queste due informazioni:

    info = zip(tel,address)

E aggreghiamo tutto in una specie di elenco telefonico:

    elenco_tel = dict(zip(pizzerie,info))

Se vogliamo interrogarlo possiamo fare una cosa del genere:

    print elenco_tel['OSTERIA DEI PONTEFICI']
    ('06 5896848', '53, V. Gregorio VII')

E se vogliamo invece inserire solo una stringa parziale usiamo la libreria `re`. Creiamo una funzione `cerca`:

    import re
    def cerca(cosa):
        match = filter(lambda x: re.search(cosa,x,re.I), elenco_tel)
        for p in match:
            print p,":",' - '.join(elenco_tel[p])

E quindi possiamo ottenere:

    cerca('ponte')
    OSTERIA DEI PONTEFICI : 06 5896848 - 53, V. Gregorio VII

Invece con:

    cerca('pizz')
    TRATTORIA PIZZERIA DA ARMANDO : 06 39378219 - 1/6, Pl. Tiburtino
    ANTICA PIZZERIA EST EST EST F.LLI RICCI : 06 4881107 - 32, V. Genova
    RISTORANTE PIZZERIA TRENTINO : 06 58233605 - 21/31, V. Sacconi
    PIZZERIA GRIGLIERIA CHICCO DI GRANO : 06 47825033 - 6/7/8, V. Zingari
    EDEN MONTEVERDE RISTORANTE PIZZERIA : 06 66152514,06 66156591,06 66154866 - 14/A, P. Ottavilla
    PIZZERIA ROMA SPARITA srl : 06 76900646,06 7615517 - 24, P. S. Cecilia
    PIZZERIA LA GIANICOLENSE : 06 39733477 - 238, Circonv. Gianicolense
    PIZZERIA PIZZA CIRO : 06 76900646 - 43/45, V. Mercede
    GAUCHOS PIZZA &amp; GRILL GAUCHO 69 srl : 06 3236806,06 3208402 - 606, V. M. Battistini
    RISTORANTE PIZZERIA LA PIAZZETTA DE TRASTEVERE : 06 66156591 - 16/B, V. Merry Del Val
    PIZZERIA ER PANONTO : 06 8551076 - 8/10, V. Cravero
    RISTORANTE PIZZERIA BUONO LES srl : 06 5818413 - 1, V. Albenga
    PIZZERIA RISTORANTE LE FINESTRE : 06 39378219,06 635206 - 80/86, V. Chiana
    RISTORANTE PIZZERIA BIBO BAR : 06 8555127,339 2229692 - 58, P. Ss. Apostoli

## Esempio 10 - Webcraping con screenshot

La libreria webscraping permette di meccanizzare l'interazione con il
web come abbiamo visto anche con mechanize. Le modalità sono simili.


Innanzitutto importo il `webkit` da `webscraping`:

	from webscraping import webkit
    w = webkit.WebkitBrowser(gui=True)

Prendo un sito internet (duckduckgo è un motore di ricerca meno conosciuto di google):

	w.get('http://duckduckgo.com')

Riempio la casella di ricerca:

    w.fill('input[id=search_form_input_homepage]', 'webscraping')


A questo punto premo il pulsante di ricerca:

    w.click('input[id=search_button_homepage]')

Aspetto un po' per assicurarmi che i risultati sono correttamente stati caricati

    w.wait(10)

E a questo punto posso prendere il risultato della pagina:

    html = w.current_html()

ed usarlo come abbiamo già visto, ad esempio attraverso l'oggetto
`xpath` della stessa libreria.

Ma, ad esempio, posso anche fare uno screenshot della pagina e poi
salvarlo in un file JPG:

    w.screenshot('duckduckgo_results.jpg')

# Webscraping fatto più semplice

    import scraperwiki
    import requests
    import lxml.html
    import pprint
    
    html = requests.get("http://intenseminimalism.com/").content
    dom = lxml.html.fromstring(html)
    
    for entry in dom.cssselect('.article'):
        post = {
            'title': entry.cssselect('h1 a')[0].text_content(),
            'date': entry.cssselect('.time')[0].text_content(),
            'url': entry.cssselect('h1 a')[0].get('href'),
        }
        pprint.pprint(post)
    
    scraperwiki.sql.save(['url'], post)



## Elezioni Senato

https://classic.scraperwiki.com/scrapers/elezioni_senato_2006-2008_-_basilicata/

select * from `swdata` where candidate like '%BERSANI% ' and votes>0 limit 10

select * from `swdata` where candidate like '%PANNELLA% ' and votes>0 limit 10


## Scioperi

https://classic.scraperwiki.com/scrapers/scioperi_it/

http://www.cgsse.it/web/guest/home

## Anagrafe Biblioteche

https://classic.scraperwiki.com/scrapers/anagrafebiblioteche/

## Opendata Gov.IT

https://classic.scraperwiki.com/scrapers/datigovit_1/

## Elenco Aziende

https://classic.scraperwiki.com/scrapers/tutorial_paginegialle/

## EU Balance Sheets

https://classic.scraperwiki.com/scrapers/balance-sheets/

## ExtractTable

http://www.whitehouse.gov/sites/default/files/omb/budget/fy2014/assets/tables.pdf


