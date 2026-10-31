# QCM d'espagnol de terminale, volume ×3 : conjugaisons calculées à partir de tables, concordance, discours indirect, relatifs.
from q_tle_x3_calc import calc

# infinitif : (radical du passé simple 3e pl. sans -ron, radical futur/conditionnel, imparfait 1re sg, passé simple 1re pl, sens)
V = {"hablar": ("habla", "hablar", "hablaba", "hablamos", "parler"), "comer": ("comie", "comer", "comía", "comimos", "manger"),
     "vivir": ("vivie", "vivir", "vivía", "vivimos", "vivre"), "tener": ("tuvie", "tendr", "tenía", "tuvimos", "avoir"),
     "hacer": ("hicie", "har", "hacía", "hicimos", "faire"), "poder": ("pudie", "podr", "podía", "pudimos", "pouvoir"),
     "decir": ("dije", "dir", "decía", "dijimos", "dire"), "ser": ("fue", "ser", "era", "fuimos", "être"),
     "estar": ("estuvie", "estar", "estaba", "estuvimos", "être (état)"), "venir": ("vinie", "vendr", "venía", "vinimos", "venir"),
     "querer": ("quisie", "querr", "quería", "quisimos", "vouloir"), "saber": ("supie", "sabr", "sabía", "supimos", "savoir"),
     "poner": ("pusie", "pondr", "ponía", "pusimos", "mettre"), "dar": ("die", "dar", "daba", "dimos", "donner"),
     "traer": ("traje", "traer", "traía", "trajimos", "apporter"), "leer": ("leye", "leer", "leía", "leímos", "lire"),
     "dormir": ("durmie", "dormir", "dormía", "dormimos", "dormir"), "pedir": ("pidie", "pedir", "pedía", "pedimos", "demander"),
     "ir": ("fue", "ir", "iba", "fuimos", "aller")}
ACC = str.maketrans("aeiou", "áéíóú")


def acc_last(st):
    i = max(st.rfind(v) for v in "aeiou")
    return st[:i] + st[i].translate(ACC) + st[i + 1:]


def subj(v, p):
    st = V[v][0]
    return {"yo": st + "ra", "tú": st + "ras", "él": st + "ra", "nosotros": acc_last(st) + "ramos", "vosotros": st + "rais", "ellos": st + "ran"}[p]


def imparf(v, p):
    b = V[v][2]
    root, end = (b[:-3], "aba") if b.endswith("aba") else (b[:-2], "ía") if b.endswith("ía") else (b[:-1], "a")
    if v == "ir":
        root, end = "ib", "a"
    if end == "aba":
        return root + {"yo": "aba", "tú": "abas", "él": "aba", "nosotros": "ábamos", "vosotros": "abais", "ellos": "aban"}[p]
    if end == "ía":
        return root + {"yo": "ía", "tú": "ías", "él": "ía", "nosotros": "íamos", "vosotros": "íais", "ellos": "ían"}[p]
    return root + {"yo": "a", "tú": "as", "él": "a", "nosotros": "amos", "vosotros": "ais", "ellos": "an"}[p].replace("amos", "amos") if v != "ser" else {"yo": "era", "tú": "eras", "él": "era", "nosotros": "éramos", "vosotros": "erais", "ellos": "eran"}[p]


def cond(v, p):
    return V[v][1] + {"yo": "ía", "tú": "ías", "él": "ía", "nosotros": "íamos", "vosotros": "íais", "ellos": "ían"}[p]


def pret3(v):
    return V[v][0] + "ron"


PERS = ["yo", "nosotros", "ellos", "tú"]
CJ = []
for i, v in enumerate(V):
    for p in (PERS[i % 4], PERS[(i + 2) % 4]):
        ok = subj(v, p)
        d3 = pret3(v) if p == "ellos" else (V[v][3] if p == "nosotros" else cond(v, "ellos"))
        CJ.append((f"Subjonctif imparfait de « {v} » ({V[v][4]}), personne « {p} » :", ok, imparf(v, p), cond(v, p), d3, f"Radical du passé simple 3e personne du pluriel ({pret3(v)}) + -ra, -ras, -ra, -ramos, -rais, -ran."))

CONC = [("Quiero que tú ___ (venir) mañana.", "vengas", "vinieras", "vienes", "vendrás", "Principale au présent → subjonctif présent."),
        ("Quería que tú ___ (venir) conmigo.", "vinieras", "vengas", "venías", "vendrías", "Principale au passé → subjonctif imparfait."),
        ("El profesor nos pidió que ___ (estudiar) más.", "estudiáramos", "estudiemos", "estudiábamos", "estudiaríamos", "Pedir que + subjonctif imparfait après un passé."),
        ("Me gustaría que ___ (hacer) buen tiempo.", "hiciera", "haga", "hacía", "haría", "Conditionnel dans la principale → subjonctif imparfait."),
        ("Si ___ (tener) dinero, compraría una casa.", "tuviera", "tengo", "tendría", "tenga", "Si + subjonctif imparfait, conditionnel (hypothèse)."),
        ("Si ___ (poder), te ayudaría.", "pudiera", "puedo", "podría", "pueda", "Si + subjonctif imparfait."),
        ("Te lo digo para que lo ___ (saber).", "sepas", "supieras", "sabes", "sabrás", "Para que + subjonctif ; principale au présent."),
        ("Te lo dije para que lo ___ (saber).", "supieras", "sepas", "sabías", "sabrías", "Para que + subjonctif imparfait après un passé."),
        ("Ojalá ___ (llover) mañana.", "llueva", "lloviera", "llueve", "lloverá", "Ojalá + subjonctif présent : souhait réalisable."),
        ("Ojalá ___ (ser) rico ahora.", "fuera", "sea", "era", "sería", "Ojalá + subjonctif imparfait : souhait irréel."),
        ("Era necesario que todos ___ (llegar) a tiempo.", "llegaran", "lleguen", "llegaban", "llegarían", "Era necesario que + subjonctif imparfait."),
        ("Es importante que los jóvenes ___ (leer).", "lean", "leyeran", "leen", "leerían", "Es importante que + subjonctif présent."),
        ("Cuando ___ (terminar) el bachillerato, iré a la universidad.", "termine", "terminara", "termino", "terminaré", "Cuando + subjonctif pour une action future."),
        ("Mis padres no querían que yo ___ (salir) de noche.", "saliera", "salga", "salía", "saldría", "Volonté au passé → subjonctif imparfait."),
        ("Habla como si lo ___ (saber) todo.", "supiera", "sepa", "sabe", "sabría", "Como si + toujours subjonctif imparfait."),
        ("Busco un amigo que ___ (hablar) francés.", "hable", "hablara", "habla", "hablaría", "Antécédent indéterminé → subjonctif."),
        ("Le aconsejé que ___ (dormir) más.", "durmiera", "duerma", "dormía", "dormiría", "Aconsejar que + subjonctif imparfait après un passé."),
        ("No creo que ___ (ser) verdad.", "sea", "fuera", "es", "será", "No creer que + subjonctif."),
        ("Aunque ___ (llover) mañana, saldremos.", "llueva", "lloviera", "llueve", "lloverá", "Aunque + subjonctif : hypothèse."),
        ("Esperaba que me ___ (escribir).", "escribieras", "escribas", "escribías", "escribirías", "Esperar que au passé → subjonctif imparfait.")]
CONC = [(f"Concordance des temps : « {s} »", ok, a, b, c, e) for s, ok, a, b, c, e in CONC]

DI = [("Juan dice: « Estoy cansado. »", "Juan dice que está cansado.", "Juan dice que estaba cansado.", "Juan dice que estoy cansado.", "Juan dice si está cansado."),
      ("Juan dijo: « Estoy cansado. »", "Juan dijo que estaba cansado.", "Juan dijo que está cansado.", "Juan dijo que estoy cansado.", "Juan dijo que estuviera cansado."),
      ("María dijo: « Iré a Dakar. »", "María dijo que iría a Dakar.", "María dijo que irá a Dakar.", "María dijo que iré a Dakar.", "María dijo que fuera a Dakar."),
      ("El profesor dijo: « Cerrad los libros. »", "El profesor dijo que cerráramos los libros.", "El profesor dijo que cerramos los libros.", "El profesor dijo que cerrad los libros.", "El profesor dijo que cerraremos los libros."),
      ("Mi madre me dijo: « Haz los deberes. »", "Mi madre me dijo que hiciera los deberes.", "Mi madre me dijo que hago los deberes.", "Mi madre me dijo que haz los deberes.", "Mi madre me dijo que hacía los deberes."),
      ("Pedro preguntó: « ¿Dónde vives? »", "Pedro preguntó dónde vivía yo.", "Pedro preguntó dónde vives.", "Pedro preguntó que dónde vivas.", "Pedro preguntó si dónde vivía."),
      ("Ana preguntó: « ¿Vienes mañana? »", "Ana preguntó si yo iba al día siguiente.", "Ana preguntó que vienes mañana.", "Ana preguntó si vienes mañana.", "Ana preguntó si fuera mañana."),
      ("Dijeron: « Hemos ganado. »", "Dijeron que habían ganado.", "Dijeron que han ganado.", "Dijeron que hemos ganado.", "Dijeron que hubieran ganado."),
      ("Fatou dijo: « Ayer compré un libro. »", "Fatou dijo que el día anterior había comprado un libro.", "Fatou dijo que ayer compré un libro.", "Fatou dijo que el día anterior compra un libro.", "Fatou dijo que mañana había comprado un libro."),
      ("El médico me dijo: « No fumes. »", "El médico me dijo que no fumara.", "El médico me dijo que no fumes.", "El médico me dijo que no fumaba.", "El médico me dijo no fumar que."),
      ("Dice: « Puedo ayudarte. »", "Dice que puede ayudarme.", "Dice que podía ayudarte.", "Dice que puedo ayudarte.", "Dice que pudiera ayudarme."),
      ("Dijo: « Aquí hace calor. »", "Dijo que allí hacía calor.", "Dijo que aquí hace calor.", "Dijo que allí hiciera calor.", "Dijo que allí hará calor."),
      ("Les pregunté: « ¿Qué queréis? »", "Les pregunté qué querían.", "Les pregunté qué queréis.", "Les pregunté que qué quieran.", "Les pregunté si qué querían."),
      ("Me dijo: « Tengo que irme. »", "Me dijo que tenía que irse.", "Me dijo que tengo que irme.", "Me dijo que tuviera que irse.", "Me dijo que tenía que irme."),
      ("Los alumnos dijeron: « Mañana tenemos examen. »", "Los alumnos dijeron que al día siguiente tenían examen.", "Los alumnos dijeron que mañana tenemos examen.", "Los alumnos dijeron que al día siguiente tengan examen.", "Los alumnos dijeron que ayer tenían examen.")]
DI = [(f"Discours indirect : {s}", ok, a, b, c, "Après un verbe introducteur au passé : recul des temps, impératif → subjonctif imparfait, changement des personnes et des repères (aquí → allí, mañana → al día siguiente).") for s, ok, a, b, c in DI]

REL = [("El chico ___ vive aquí es mi primo.", "que", "quien", "cuyo", "donde"), ("La mujer con ___ hablé es médica.", "quien", "que", "cuya", "donde"),
       ("El hombre ___ hijo estudia en Francia es mi vecino.", "cuyo", "cuya", "que", "quien"), ("La ciudad ___ nací es Kaolack.", "donde", "que", "cuya", "quien"),
       ("La chica ___ madre es profesora saca buenas notas.", "cuya", "cuyo", "que", "quien"), ("Los libros ___ compré son caros.", "que", "quienes", "cuyos", "donde"),
       ("No entiendo ___ dices.", "lo que", "que", "el que", "cuyo"), ("Los amigos con ___ viajo son simpáticos.", "quienes", "que", "cuyos", "donde"),
       ("Es la razón por la ___ me fui.", "cual", "que lo", "cuya", "quien"), ("___ estudia, aprueba.", "Quien", "Cuyo", "Donde", "Lo cual")]
REL = [(f"Pronom relatif : « {s} »", ok, a, b, c, "Que (général), quien (personne après préposition), cuyo/cuya (possession, accord avec le nom qui suit), donde (lieu), lo que (ce que).") for s, ok, a, b, c in REL]
PAS = [("Los alumnos escriben la redacción.", "La redacción es escrita por los alumnos.", "La redacción está escrito por los alumnos.", "La redacción es escribida por los alumnos.", "La redacción fue escrito por los alumnos."),
       ("El gobierno construyó el puente.", "El puente fue construido por el gobierno.", "El puente es construyó por el gobierno.", "El puente fue construida por el gobierno.", "El puente estuvo construyendo por el gobierno."),
       ("La policía detendrá a los ladrones.", "Los ladrones serán detenidos por la policía.", "Los ladrones serán detenido por la policía.", "Los ladrones están detenidos por la policía.", "Los ladrones serían detienen por la policía."),
       ("Venden casas.", "Se venden casas.", "Se vende casas.", "Son vendido casas.", "Se venden las casas por."),
       ("Hablan español en Guinea Ecuatorial.", "Se habla español en Guinea Ecuatorial.", "Se hablan español en Guinea Ecuatorial.", "Es hablado de español en Guinea Ecuatorial.", "Español habla en Guinea Ecuatorial."),
       ("Todos respetan al presidente.", "El presidente es respetado por todos.", "El presidente está respetando por todos.", "El presidente es respetada por todos.", "Al presidente es respetado por todos."),
       ("Mi abuela hizo esta tela.", "Esta tela fue hecha por mi abuela.", "Esta tela fue hecho por mi abuela.", "Esta tela fue hacida por mi abuela.", "Esta tela es hizo por mi abuela."),
       ("Abrieron las puertas a las ocho.", "Se abrieron las puertas a las ocho.", "Se abrió las puertas a las ocho.", "Fueron abierto las puertas a las ocho.", "Se abrieron por las puertas a las ocho.")]
PAS = [(f"Voix passive : « {s} »", ok, a, b, c, "Ser + participe accordé (+ por) ; ou passive avec se, verbe accordé avec le sujet.") for s, ok, a, b, c in PAS]

ARG = [("Pour introduire une idée : « ___, la educación es la clave del desarrollo. »", "En primer lugar", "Sin embargo", "Por lo tanto", "A pesar de"),
       ("Pour ajouter : « La emigración es peligrosa; ___, separa a las familias. »", "además", "sin embargo", "en cambio", "aunque"),
       ("Pour opposer : « Es caro; ___, lo compro. »", "sin embargo", "además", "por eso", "porque"),
       ("Pour conclure : « ___, hay que proteger el medio ambiente. »", "En conclusión", "Por ejemplo", "En primer lugar", "Además"),
       ("Pour donner un exemple : « Hay muchos deportes populares, ___ la lucha. »", "por ejemplo", "sin embargo", "en conclusión", "aunque"),
       ("Pour la cause : « No vino ___ estaba enfermo. »", "porque", "aunque", "sin embargo", "además"),
       ("Pour la conséquence : « Llovió mucho; ___, se inundaron las calles. »", "por consiguiente", "aunque", "en cambio", "por ejemplo"),
       ("Pour la concession : « ___ es difícil, lo intentaré. »", "Aunque", "Porque", "Por eso", "Además"),
       ("Pour exprimer son avis : « ___, el turismo trae ventajas. »", "En mi opinión", "Sin embargo", "Por lo tanto", "Al final de"),
       ("Pour le contraste : « Mi hermano es alto; ___, yo soy bajo. »", "en cambio", "además", "por consiguiente", "porque"),
       ("« A pesar de » est suivi :", "d'un nom ou d'un infinitif", "d'un verbe conjugué au subjonctif", "toujours de « que » + indicatif", "d'un adverbe seulement"),
       ("« Es preciso que » est suivi :", "du subjonctif", "de l'indicatif", "de l'infinitif", "du gérondif"),
       ("« Cabe destacar que » signifie :", "il faut souligner que", "il est interdit de", "il suffit que", "il semble que"),
       ("« Hoy en día » signifie :", "de nos jours", "aujourd'hui seulement", "chaque jour", "un jour"),
       ("« Llevar a cabo » signifie :", "réaliser, mener à bien", "porter un câble", "arriver au bout du chemin", "emmener quelqu'un"),
       ("« Por un lado… por otro lado » sert à :", "présenter deux aspects d'un problème", "conclure", "donner un exemple", "exprimer une cause"),
       ("Une bonne introduction d'expression écrite :", "présente le thème et annonce le plan", "donne directement la conclusion", "raconte une anecdote sans lien", "recopie le sujet"),
       ("« Desde mi punto de vista » signifie :", "de mon point de vue", "depuis ma fenêtre", "à première vue", "à mon avis contraire"),
       ("« No solo… sino también » signifie :", "non seulement… mais aussi", "ni… ni", "soit… soit", "pas seulement… mais pas"),
       ("Pour exprimer le but : « Trabajo ___ ayudar a mi familia. »", "para", "por", "porque", "aunque"),
       ("« Es una lástima que » est suivi :", "du subjonctif", "de l'indicatif", "de l'infinitif seul", "du futur"),
       ("« Cada vez más » signifie :", "de plus en plus", "chaque fois", "plus jamais", "au plus tard"),
       ("Pour reformuler : « ___, la sequía afecta a los campesinos. »", "Es decir", "Sin embargo", "Aunque", "Por ejemplo"),
       ("« Hacer frente a » signifie :", "faire face à", "faire la fête", "tourner le dos", "mettre en avant")]
ARG = [(s, ok, a, b, c, "Connecteurs et expressions de l'expression écrite argumentée.") for s, ok, a, b, c in ARG]

QCM_TLE_X3_ES = {"tle-espagnol": {
    "Concordance des temps et subjonctif imparfait": calc(CJ + CONC),
    "Le discours indirect": calc(DI),
    "Relatifs et voix passive": calc(REL + PAS),
    "Expression écrite : argumenter": calc(ARG),
}}
