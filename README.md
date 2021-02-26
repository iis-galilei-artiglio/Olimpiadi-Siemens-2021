<b><font color='blue' size='6'>IIS Galilei-Artiglio</font></b>


## Olimpiadi di Automazione Siemens


<b><font color='blue' size='4'>Progetto PVCorobot</font></b>

PVCorobot è un robot collaborativo autocostruito con materiali di recupero e a basso costo, controllato da un PLC Siemens S71200 a seguito delle informazioni in tempo reale ricevute da una rete neurale installata su una GPU Jetson Nano. Di seguito il video di presentazione del progetto **VIDEO ISTITUZIONALE ANCORA DA CARICARE**
 
<html lang="it"> 

<body>
    <div class="container">
         <!-- finestra popup 3 -->
        <a href="#x" class="overlay" id="win3"></a>
        <div class="popup">
            <div class="video">
         <!-- il link you tube deve essere selezionato dal link di rete lasciando la cartella embed -->
		    <iframe width="614" height="345" src="https://www.youtube.com/embed/2P0j74Kl6sE" ></iframe>
            </div>
            <a class="close" title="Chiudere" href="modal.html" onclick = "modal.html(); return false;"></a>
        </div>
       
    </div>
</body>
</html>

Scopo del progetto è quello di rendere possibile la costruzione del robot da parte delle scuole utilizzando pezzi di tubo in PVC innestato in curve e TEE facilmente reperibili sul mercato o addirittura da sfridi, per realizzare un prodotto didattico avanzato e facilmente repricabile per piu' postazioni di lavoro. La tecnologia impiegata nel robot è di tutto riguardo trattandosi di tecnologia Siemens (Tia Portal, PLC S71200) abbinata ad una rete neurale in Python personalizzata che gira su una GPU Jetson Nano

## Pubblicazione su GitHub Pages
Le classi dell'[IIS Galilei-Artiglio](http://www.iisgalileiartiglio.gov.it/) hanno deciso di sviluppare il progetto su GitHub sostanzialmente per due motivi: per condividere uno spazio di lavoro comune tra Liceo ed ITI durante la realizzazione del robot e per condividere il lavoro finito con altre scuole e/o persone interessate. 
Questa modalità di condivisione non è "unidirezionale" tipica di un sito Web, perchè i file presenti nella repository permettono a chiunque di migliorare il progetto attraverso proposte, suggerimenti correzioni nello spirito di collaborazione proprio di [GitHub](https://guides.github.com/activities/hello-world/)

Per accedere al repository dei file clicca su [View On GitHub](https://github.com/iis-galilei-artiglio/Olimpiadi-Siemens-2021)

## Organizzazione e fasi di lavoro
Le classi che hanno partecipato al progetto sono la classe 4BS del Liceo Scientifico Tecnologico e le classi 4FT e 5CT del corso di Elettrotecnica/Elettronica.

La classe 4BS del Liceo si è occupata dell'addestramento della rete neurale mediante [Google Colaboratory](https://research.google.com/colaboratory/faq.html) mentre le classi ITI hanno collaborato nella realizzazione pratica del robot e nella programmazione del Tia Portal. E' evidente che la situazione legata al Covid ha influenzato non poco la costruzione del robot. Tuttavia l'IIS Galilei Artiglio ha attivato da subito lezioni in presenza alternate con lezioni in DAD per le classi 4BS e 4FT, mentre per la classe 5CT le lezioni sono sempre state in presenza. Per quanto riguarda l'addestramento della rete neurale, l'alternarsi di didattica in presenza ed a distanza non ha influenzato piu' di tanto i lavori degli studenti. Infatti Google Colab è uno strumento molto potente che può essere utilizzato da chiunque e con PC non particolarmente performanti. L'importante è avere un collegamento alla rete.

Circa invece la costruzione del robot in presenza, i docenti hanno mostrato come è possibile realizzare il montaggio del braccio con estrema semplicità trattandosi di normali tubi da innestare tra loro secondo uno schema stabilito.

La parte di programmazione con il Tia Portal è stata sviluppata in parte in presenza ed in parte in DAD.

## Aspetti principali della comunicazione tra il PLC Siemens e Jetson Nano
La rete neurale presente su JN è in codice Python scaricabile direttamente dal repository. Per maggiori dettagli sull'addestramento della rete neurale si rimanda alla pagina di [NVIDIA JETSON](https://github.com/dusty-nv/jetson-inference) 
Il collegamento tra JN e PLC avviene via LAN tramite TCP/IP dopo aver settato nel TIA Portal l'indirizzo del partner ovvero di JN

<img src="connect_plc_JN.png" width=400>


## Attività di addestramento della rete neurale svolta dalla Classe 4BS Liceo Scientifico Tecnologico
Le ragazze ed i ragazzi del Liceo che hanno partecipato al progetto Siemens, hanno realizzato, **_in totale autonomia_**,  un [video](https://www.youtube.com/watch?v=2P0j74Kl6sE&feature=emb_imp_woyt) che, seppure con qualche imprecisione, fornisce la cifra dell'impegno dimostrato

