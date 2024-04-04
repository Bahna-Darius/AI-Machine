# Pasi de urmat pentru un proiect in Machine Learning !!
1. **Import the Data**
   Importarea datelor intr-un format CSV sau in formatul dorit.

2. **Clean the Data**
    Curatarea datelor presupune eliminarea datelor lipsa, a datelor duplicate, a datelor irelevante. Deoarece datele murdare pot duce la rezultate incorecte.

    2.1 **Encode the Data**
        Codificarea datelor presupune transformarea datelor in valori numerice. Deoarece algoritmii de Machine Learning lucreaza doar cu valori numerice.

3. **Split the Data into Training/Test Sets**
    Impartirea datelor in seturi de antrenament si testare. Setul de antrenament este folosit pentru a antrena modelul, iar setul de testare este folosit pentru a testa modelul.
- Deobicei se foloseste 80% din date pentru antrenament si 20% pentru testare.

- 3.1 **Feature Selection**
    Selectarea caracteristicilor care sunt relevante pentru problema pe care dorim sa o rezolvam. Deoarece prea multe caracteristici pot duce la overfitting si prea putine caracteristici pot duce la underfitting.

4. **Create a Model**
    Crearea unui model de Machine Learning. Acesta presupune selectarea unui algoritm si analiza datelor. Fiecare algoritm prezinta avantaje si dezavantaje in ceea ce priveste performanta si viteza.
- Alegerea unui algoritm depinde de tipul de date si de problema pe care dorim sa o rezolvam.

5. **Train the Model**
    Antrenarea modelului presupune folosirea setului de antrenament pentru a invata modelul. Acesta va incerca sa gaseasca relatii intre date si sa faca predictii.

6. **Make Predictions**
    Facerea de predictii folosind modelul antrenat. Acesta va folosi setul de testare pentru a face predictii si pentru a evalua performanta modelului.
- Predictiile nu sunt intotdeauna exacte, de fapt la inceput sunt rareori exacte. Cu cat modelul este mai antrenat, cu atat predictiile vor fi mai bune.

7. **Evaluate and Improve**
    Evaluarea modelului si imbunatatirea performantei(acuratetei). Acesta presupune analizarea rezultatelor si ajustarea modelului pentru a obtine rezultate mai bune.
- Putem fie selecta un alt algoritm, fie ajusta parametrii algoritmului actual. 
- - Fiecare algoritm are parametrii proprii care pot fi ajustati pentru a obtine rezultate mai bune.

Sikit-Learn
- fit() - Obtine formula
- transform() - Aplica formula
- fit_transform() - Obtine si aplica formula

# Problema de rezolvat:
- **Problema de rezolvat:** Avem o aplicatie care gasduieste mai multi Customers care ofera postarea de noi anunturi de transport de marfa. Fiecare Customer are o locatie dorita de plecare, o locatie dorita de sosire si un pret pe care este dispus sa il plateasca pentru transport. Customerii doresc sa ofere locatia de plecare si locatia de sosire si sa primeasca un pret pentru transport.



