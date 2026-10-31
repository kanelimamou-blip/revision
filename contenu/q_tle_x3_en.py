# QCM d'anglais de terminale, volume ×3 : transformations grammaticales produites à partir de tables de verbes et de phrases.
from q_tle_x3_calc import calc

# (sujet, base, prétérit, participe, complément, complément pluriel ?)
SVO = [("The farmers", "grow", "grew", "grown", "millet", False), ("Our teacher", "correct", "corrected", "corrected", "the exams", True),
       ("The fishermen", "catch", "caught", "caught", "a lot of fish", False), ("The company", "build", "built", "built", "new schools", True),
       ("Aminata", "write", "wrote", "written", "the report", False), ("The police", "arrest", "arrested", "arrested", "the thieves", True),
       ("The government", "sign", "signed", "signed", "the agreement", False), ("The students", "clean", "cleaned", "cleaned", "the classrooms", True)]


def cap(s):
    return s[0].upper() + s[1:]


def low(s):
    return s if s.startswith(("Aminata", "Our")) and s == "Aminata" else s[0].lower() + s[1:]


P = []
for s, b, pt, pp, o, pl in SVO:
    plur = s in ("The farmers", "The fishermen", "The police", "The students")
    be_pr, be_pt, hv = ("are", "were", "have") if pl else ("is", "was", "has")
    ag = low(s)
    act_pr = f"{s} {b if plur else (b + 'es' if b.endswith(('ch', 'sh')) else b + 's')} {o}."
    P += [
        (f"Passive voice: « {act_pr} »", f"{cap(o)} {be_pr} {pp} by {ag}.", f"{cap(o)} {be_pt} {pp} by {ag}.", f"{cap(o)} {be_pr} {b} by {ag}.", f"{cap(o)} {'is' if pl else 'are'} {pp} by {ag}.", f"Présent simple : be au présent ({be_pr}) + participe passé ; accord avec « {o} »."),
        (f"Passive voice: « {s} {pt} {o}. »", f"{cap(o)} {be_pt} {pp} by {ag}.", f"{cap(o)} {be_pr} {pp} by {ag}.", f"{cap(o)} {be_pt} {pt if pt != pp else b} by {ag}.", f"{cap(o)} {'was' if pl else 'were'} {pp} by {ag}.", f"Prétérit : {be_pt} + participe passé."),
        (f"Passive voice: « {s} will {b} {o}. »", f"{cap(o)} will be {pp} by {ag}.", f"{cap(o)} will {pp} by {ag}.", f"{cap(o)} will being {pp} by {ag}.", f"{cap(o)} would be {pp} by {ag}.", "Futur : will be + participe passé."),
        (f"Passive voice: « {s} {'have' if plur else 'has'} {pp} {o}. »", f"{cap(o)} {hv} been {pp} by {ag}.", f"{cap(o)} {hv} being {pp} by {ag}.", f"{cap(o)} {be_pr} been {pp} by {ag}.", f"{cap(o)} {'has' if pl else 'have'} been {pp} by {ag}.", f"Present perfect : {hv} been + participe passé."),
        (f"Passive voice: « {s} {'are' if plur else 'is'} {b}{'ing' if not b.endswith('e') else ''}{'' if not b.endswith('e') else ''} {o}. »".replace("writeing", "writing"), f"{cap(o)} {be_pr} being {pp} by {ag}.", f"{cap(o)} {be_pr} been {pp} by {ag}.", f"{cap(o)} {be_pr} {pp} by {ag}.", f"{cap(o)} {be_pr} being {b} by {ag}.", f"Présent en be + -ing : {be_pr} being + participe passé."),
    ]
P = [(q.replace(" write the", " writing the") if "is write" in q else q, *r) for q, *r in P]
P = [(q.replace("is write ", "is writing "), *r) for q, *r in P]

# Discours indirect : (direct, sujet, indirect correct, 3 erreurs)
RS = [("« I am tired, » said Fatou.", "Fatou said that she was tired.", "Fatou said that she is tired.", "Fatou said that I was tired.", "Fatou told that she was tired."),
      ("« We live in Thiès, » they said.", "They said that they lived in Thiès.", "They said that we lived in Thiès.", "They said that they live in Thiès.", "They told that they lived in Thiès."),
      ("« I will help you, » Moussa told me.", "Moussa told me that he would help me.", "Moussa told me that he will help you.", "Moussa said me that he would help me.", "Moussa told me that I would help him."),
      ("« I can swim, » said Ibrahima.", "Ibrahima said that he could swim.", "Ibrahima said that he can swim.", "Ibrahima said that he could swam.", "Ibrahima said that I could swim."),
      ("« I have finished my homework, » said Awa.", "Awa said that she had finished her homework.", "Awa said that she has finished her homework.", "Awa said that she finished my homework.", "Awa said that she had finish her homework."),
      ("« I saw the film yesterday, » he said.", "He said that he had seen the film the day before.", "He said that he saw the film yesterday.", "He said that he has seen the film the day before.", "He said that I had seen the film the day before."),
      ("« We are watching TV, » the children said.", "The children said that they were watching TV.", "The children said that they are watching TV.", "The children said that we were watching TV.", "The children said that they watched TV tomorrow."),
      ("« I must leave now, » said the doctor.", "The doctor said that he had to leave then.", "The doctor said that he must leave now.", "The doctor said that he has to leave now.", "The doctor said that I had to leave then."),
      ("« Close the door, » the teacher told me.", "The teacher told me to close the door.", "The teacher told me close the door.", "The teacher said me to close the door.", "The teacher told me that I close the door."),
      ("« Don't make noise, » the principal told us.", "The principal told us not to make noise.", "The principal told us to not making noise.", "The principal told us don't make noise.", "The principal said us not to make noise."),
      ("« Where do you live? » she asked me.", "She asked me where I lived.", "She asked me where did I live.", "She asked me where do you live.", "She asked me where I live?"),
      ("« Are you ready? » he asked us.", "He asked us if we were ready.", "He asked us are we ready.", "He asked us if were we ready.", "He asked us that we were ready."),
      ("« What time is it? » the tourist asked.", "The tourist asked what time it was.", "The tourist asked what time was it.", "The tourist asked what time it is.", "The tourist asked if what time it was."),
      ("« Did you pass the exam? » my uncle asked me.", "My uncle asked me whether I had passed the exam.", "My uncle asked me did I pass the exam.", "My uncle asked me whether I passed the exam?", "My uncle asked me if had I passed the exam."),
      ("« I may come tomorrow, » said Khady.", "Khady said that she might come the next day.", "Khady said that she may come tomorrow.", "Khady said that she might came the next day.", "Khady said that I might come the next day."),
      ("« Please help me, » the old man asked us.", "The old man asked us to help him.", "The old man asked us help him.", "The old man asked us to help me.", "The old man said us to help him."),
      ("« Why are you late? » the teacher asked Omar.", "The teacher asked Omar why he was late.", "The teacher asked Omar why was he late.", "The teacher asked Omar why are you late.", "The teacher asked Omar why he is late?"),
      ("« I don't like rice, » said Paul.", "Paul said that he didn't like rice.", "Paul said that he doesn't liked rice.", "Paul said that I didn't like rice.", "Paul said that he not liked rice."),
      ]
RS = [(f"Reported speech: {d}", ok, a, b, c, "Discours indirect : recul des temps, changement des pronoms et des repères de temps, ordre sujet-verbe affirmatif.") for d, ok, a, b, c in RS]

# Conditionnels : (si-proposition au type 1, verbe base, prétérit, participe, principale base)
CD = [("I", "study", "studied", "studied", "I", "pass", "the exam"), ("she", "save", "saved", "saved", "she", "buy", "a computer"), ("we", "leave", "left", "left", "we", "catch", "the bus"),
      ("they", "train", "trained", "trained", "they", "win", "the match"), ("he", "eat", "ate", "eaten", "he", "feel", "better"), ("you", "listen", "listened", "listened", "you", "understand", "the lesson"),
      ("it", "rain", "rained", "rained", "the crops", "grow", "faster"), ("Fatou", "work", "worked", "worked", "she", "get", "a good mark")]
PP = {"pass": "passed", "buy": "bought", "catch": "caught", "win": "won", "feel": "felt", "understand": "understood", "grow": "grown", "get": "got"}


def third(s, b):
    if s in ("she", "he", "it", "Fatou"):
        return b[:-1] + "ies" if b.endswith("y") and b[-2] not in "aeiou" else b + ("es" if b.endswith(("ch", "sh", "s")) else "s")
    return b


C = []
for s, b, pt, pp, ms, mv, rest in CD:
    w = lambda aux, v=mv: f"{ms} {aux} {v} {rest}."
    adv = {"study": "hard", "save": "money", "leave": "early", "train": "every day", "eat": "fruit", "listen": "carefully", "rain": "", "work": "regularly"}[b]
    C += [
        (f"Complete (type 1): If {s} {third(s, b)} {adv}, …".replace(" ,", ","), w("will"), w("would"), w("would have", PP[mv]), w("will have", PP[mv]), "Type 1 : if + présent, will + base verbale."),
        (f"Complete (type 2): If {s} {pt} {adv}, …".replace(" ,", ","), w("would"), w("will"), w("would have", PP[mv]), w("had", PP[mv]), "Type 2 : if + prétérit, would + base verbale (hypothèse sur le présent)."),
        (f"Complete (type 3): If {s} had {pp} {adv}, …".replace(" ,", ","), w("would have", PP[mv]), w("would"), w("will"), w("had", PP[mv]), "Type 3 : if + past perfect, would have + participe passé (regret sur le passé)."),
    ]
W = [("I am not rich.", "I wish I were rich.", "I wish I am rich.", "I wish I will be rich.", "I wish I had be rich."),
     ("I can't speak Chinese.", "I wish I could speak Chinese.", "I wish I can speak Chinese.", "I wish I could spoke Chinese.", "I wish I would can speak Chinese."),
     ("I didn't revise for the test.", "I wish I had revised for the test.", "I wish I revised for the test.", "I wish I have revised for the test.", "I wish I would revise for the test yesterday."),
     ("My brother doesn't live with us.", "I wish my brother lived with us.", "I wish my brother lives with us.", "I wish my brother had live with us.", "I wish my brother will live with us."),
     ("It is raining.", "I wish it weren't raining.", "I wish it isn't raining.", "I wish it didn't rained.", "I wish it won't rain."),
     ("I lost my phone.", "If only I hadn't lost my phone!", "If only I didn't lost my phone!", "If only I haven't lost my phone!", "If only I don't lose my phone!"),
     ("You make so much noise.", "I wish you would stop making so much noise.", "I wish you stop making so much noise.", "I wish you will stop making so much noise.", "I wish you had stop making so much noise."),
     ("We don't have a car.", "If only we had a car!", "If only we have a car!", "If only we would have had a car!", "If only we has a car!"),
     ("She told the secret.", "She wishes she hadn't told the secret.", "She wishes she didn't told the secret.", "She wishes she doesn't tell the secret.", "She wishes she hasn't told the secret."),
     ("I'm not tall enough to play basketball.", "I wish I were taller.", "I wish I am taller.", "I wish I was more tall.", "I wish I will be taller."),
     ]
C += [(f"Rewrite with « wish / if only »: « {a} »", ok, x, y, z, "Souhait sur le présent : prétérit ; regret sur le passé : past perfect ; agacement : would.") for a, ok, x, y, z in W]
C += [(f"Choose the right form: « Unless you {v}, you will fail. »", ok, a, b, c, "Unless = if … not : présent dans la subordonnée, sans négation.") for v, ok, a, b, c in [("___ harder", "work", "don't work", "worked", "will work"), ("___ your lessons", "revise", "won't revise", "revised", "don't revise")]]
C += [(f"« Provided that you {x}, you can go out. » Provided that means :", "à condition que", "bien que", "à moins que", "parce que", "Provided (that) / providing (that) = à condition que.") for x in ["finish your homework"]]
C += [(f"« {s} » The correct sentence is:", ok, a, b, c, e) for s, ok, a, b, c, e in [
    ("Mixed conditional (past condition, present result)", "If I had taken the medicine, I would feel better now.", "If I took the medicine, I would have felt better now.", "If I had taken the medicine, I will feel better now.", "If I take the medicine, I would felt better now.", "Condition passée (past perfect) + conséquence présente (would + base)."),
    ("Zero conditional (general truth)", "If you heat water to 100 °C, it boils.", "If you heat water to 100 °C, it would boil.", "If you will heat water to 100 °C, it boils.", "If you heated water to 100 °C, it will boil.", "Vérité générale : présent + présent."),
    ("Inverted type 3 conditional", "Had I known, I would have come.", "Did I know, I would have come.", "Had I knew, I would have come.", "Have I known, I would come.", "Had + sujet + participe passé = if + sujet + had + participe passé."),
    ("Inverted type 2 conditional", "Were I rich, I would travel the world.", "Was I rich, I would travel the world.", "Am I rich, I would travel the world.", "Were I rich, I will travel the world.", "Were + sujet = if + sujet + were."),
]]

# Temps : since / for, present perfect, past perfect, continuous
T = []
for d in ["2015", "last year", "Monday", "this morning", "my childhood", "January", "1960", "the beginning of the year"]:
    T.append((f"« I have lived here ___ {d}. »", "since", "for", "during", "ago", "Since + point de départ."))
for d in ["ten years", "two hours", "a long time", "three weeks", "six months", "ages", "a few days", "twenty minutes"]:
    T.append((f"« She has been waiting ___ {d}. »", "for", "since", "ago", "from", "For + durée."))
TV = [("they / work / in Dakar / since 2010", "They have been working in Dakar since 2010.", "They are working in Dakar since 2010.", "They work in Dakar since 2010.", "They were working in Dakar since 2010.", "Action commencée dans le passé et qui dure : present perfect (continuous)."),
      ("when I arrived, the film / already / start", "When I arrived, the film had already started.", "When I arrived, the film has already started.", "When I arrived, the film already started.", "When I arrived, the film was already start.", "Antériorité dans le passé : past perfect."),
      ("I / read / when the light went off", "I was reading when the light went off.", "I read when the light was going off.", "I am reading when the light went off.", "I have read when the light went off.", "Action en cours (past continuous) interrompue par une action brève (prétérit)."),
      ("by next June, she / finish / her studies", "By next June, she will have finished her studies.", "By next June, she will finish her studies.", "By next June, she has finished her studies.", "By next June, she finished her studies.", "Futur antérieur : will have + participe passé."),
      ("look! the children / play / football", "Look! The children are playing football.", "Look! The children play football.", "Look! The children have played football.", "Look! The children were playing football.", "Action en cours au moment où l'on parle : présent en be + -ing."),
      ("he / not / see / his father / for two years", "He hasn't seen his father for two years.", "He didn't see his father for two years.", "He doesn't see his father since two years.", "He hasn't saw his father for two years.", "Present perfect négatif + for."),
      ("she / be / tired because she / run", "She was tired because she had been running.", "She was tired because she has been running.", "She is tired because she had run.", "She was tired because she runs.", "Past perfect continuous : cause d'un état passé."),
      ("this time tomorrow, we / fly / to Paris", "This time tomorrow, we will be flying to Paris.", "This time tomorrow, we will fly to Paris.", "This time tomorrow, we are flying to Paris.", "This time tomorrow, we have flown to Paris.", "Futur continu : action en cours à un moment du futur."),
      ("I / just / finish / my homework", "I have just finished my homework.", "I just finish my homework.", "I had just finish my homework.", "I am just finished my homework.", "Just + present perfect : action qui vient de se produire."),
      ("how long / you / learn / English?", "How long have you been learning English?", "How long are you learning English?", "How long do you learn English?", "How long you have been learning English?", "How long + present perfect continuous."),
      ("it's the first time I / eat / thieboudienne", "It's the first time I have eaten thieboudienne.", "It's the first time I eat thieboudienne.", "It's the first time I ate thieboudienne.", "It's the first time I am eating thieboudienne.", "It's the first time + present perfect."),
      ("she / live / in Ziguinchor / before she moved", "She had lived in Ziguinchor before she moved.", "She has lived in Ziguinchor before she moved.", "She lives in Ziguinchor before she moved.", "She was live in Ziguinchor before she moved.", "Past perfect avant une autre action passée."),
      ("they / wait / for an hour when the bus came", "They had been waiting for an hour when the bus came.", "They have been waiting for an hour when the bus came.", "They waited since an hour when the bus came.", "They are waiting for an hour when the bus came.", "Past perfect continuous : durée jusqu'à un moment du passé."),
      ("I / never / visit / Saint-Louis", "I have never visited Saint-Louis.", "I never have visited Saint-Louis.", "I didn't never visit Saint-Louis.", "I have never visit Saint-Louis.", "Expérience : present perfect + never."),
      ("we / already / eat / when they phoned", "We had already eaten when they phoned.", "We have already eaten when they phoned.", "We already ate when they were phoning.", "We had already eat when they phoned.", "Past perfect + already."),
      ("she / study / all night, so she is tired", "She has been studying all night, so she is tired.", "She studied all night, so she was tired.", "She is studying all night, so she is tired.", "She had studying all night, so she is tired.", "Present perfect continuous : résultat visible au présent."),
      ]
T += [(f"Put the words in the right tense: « {w} »", ok, a, b, c, e) for w, ok, a, b, c, e in TV]
T += [(f"« I ___ him {t} » : choose the right form of « meet ».", ok, a, b, c, e) for t, ok, a, b, c, e in [
    ("two days ago.", "met", "have met", "had met", "meet", "Ago : prétérit."), ("yet.", "haven't met", "didn't meet", "don't meet", "hadn't met", "Yet (négation) : present perfect."),
    ("before the meeting started.", "had met", "have met", "meet", "am meeting", "Antériorité : past perfect."), ("tomorrow at 9.", "am meeting", "met", "have met", "had met", "Rendez-vous prévu : présent en be + -ing."),
    ("every Monday.", "meet", "am meeting", "have met", "had met", "Habitude : présent simple."), ("in 2019.", "met", "have met", "meet", "had been meeting", "Date passée précise : prétérit.")]]

# Gérondif, infinitif, causatifs
GER = ["enjoy", "avoid", "finish", "mind", "suggest", "keep", "deny", "admit", "consider", "practise", "can't stand", "give up", "look forward to", "be used to", "be fond of"]
INF = ["want", "decide", "hope", "refuse", "promise", "plan", "agree", "expect", "afford", "learn", "manage", "would like", "intend", "seem", "pretend"]
ACT = [("swim", "swimming"), ("read", "reading"), ("dance", "dancing"), ("travel", "travelling"), ("study", "studying"), ("cook", "cooking"), ("play", "playing"), ("drive", "driving"),
       ("sing", "singing"), ("write", "writing"), ("run", "running"), ("help", "helping"), ("go", "going"), ("work", "working"), ("speak", "speaking")]
SUB = {"afford": "They can't afford", "mind": "Do you mind", "can't stand": "I can't stand", "look forward to": "We look forward to", "be used to": "She is used to", "be fond of": "He is fond of", "would like": "I would like", "seem": "They seem"}
GI = []
for i, v in enumerate(GER):
    b, g = ACT[i]
    pre = SUB.get(v, "She gave up" if v == "give up" else "She " + {"deny": "denies", "finish": "finishes"}.get(v, v + "s"))
    GI.append((f"« {pre} ___ » : choose the right form ({b}).", g, f"to {b}", b, f"to {g}", f"« {v} » est suivi du gérondif (-ing)."))
for i, v in enumerate(INF):
    b, g = ACT[-1 - i]
    pre = SUB.get(v, "They " + v)
    GI.append((f"« {pre} ___ » : choose the right form ({b}).", f"to {b}", g, b, f"to {g}", f"« {v} » est suivi de l'infinitif avec to."))
GI += [(f"« {s} » means:", ok, a, b, c, e) for s, ok, a, b, c, e in [
    ("I stopped smoking.", "J'ai arrêté de fumer.", "Je me suis arrêté pour fumer.", "J'ai commencé à fumer.", "Je fume encore.", "stop + -ing : arrêter de faire."),
    ("I stopped to smoke.", "Je me suis arrêté pour fumer.", "J'ai arrêté de fumer.", "J'ai commencé à fumer.", "J'ai refusé de fumer.", "stop + to : s'arrêter pour faire."),
    ("I remember posting the letter.", "Je me souviens d'avoir posté la lettre.", "Je dois penser à poster la lettre.", "J'ai oublié de poster la lettre.", "Je posterai la lettre.", "remember + -ing : se souvenir d'une action passée."),
    ("Remember to post the letter.", "Pense à poster la lettre.", "Souviens-toi d'avoir posté la lettre.", "N'oublie pas la lettre que tu as postée.", "Tu as posté la lettre.", "remember + to : penser à faire."),
    ("She tried opening the window.", "Elle a essayé d'ouvrir la fenêtre (pour voir si ça aidait).", "Elle a réussi à ouvrir la fenêtre.", "Elle a refusé d'ouvrir la fenêtre.", "Elle a ouvert la fenêtre par habitude.", "try + -ing : tester un moyen."),
]]
CAUS = [("I / my hair / cut", "I had my hair cut.", "I had cut my hair.", "I had my hair cutting.", "I had my hair to cut.", "have + objet + participe passé : faire faire."),
        ("she / her car / repair", "She had her car repaired.", "She had repaired her car.", "She had her car repair.", "She had her car to repair.", "have something done."),
        ("we / our house / paint", "We got our house painted.", "We got painted our house.", "We got our house paint.", "We got our house to painting.", "get something done = have something done."),
        ("the teacher / the students / rewrite the essay (make)", "The teacher made the students rewrite the essay.", "The teacher made the students to rewrite the essay.", "The teacher made the students rewriting the essay.", "The teacher made rewrite the students the essay.", "make + personne + base verbale."),
        ("my parents / me / go out (let)", "My parents let me go out.", "My parents let me to go out.", "My parents let me going out.", "My parents let go me out.", "let + personne + base verbale."),
        ("I / the mechanic / check the engine (have)", "I had the mechanic check the engine.", "I had the mechanic to check the engine.", "I had the mechanic checked the engine.", "I had checked the mechanic the engine.", "have + personne + base verbale."),
        ("she / her brother / help her (get)", "She got her brother to help her.", "She got her brother help her.", "She got her brother helping her.", "She got helped her brother.", "get + personne + to + base verbale."),
        ("he / his photo / take", "He had his photo taken.", "He had taken his photo.", "He had his photo take.", "He had his photo taking.", "have + objet + participe passé.")]
GI += [(f"Causative: « {w} »", ok, a, b, c, e) for w, ok, a, b, c, e in CAUS]

# Question tags
QT = [("You are a student", "aren't you?"), ("She is tired", "isn't she?"), ("They were late", "weren't they?"), ("He can swim", "can't he?"), ("We will win", "won't we?"),
      ("You have finished", "haven't you?"), ("She doesn't like fish", "does she?"), ("They didn't come", "did they?"), ("He has never been to Kolda", "has he?"),
      ("Let's go to the beach", "shall we?"), ("Open the window", "will you?"), ("I am right", "aren't I?"), ("Nobody called", "did they?"), ("Everybody is here", "aren't they?"),
      ("You should rest", "shouldn't you?"), ("She would help us", "wouldn't she?"), ("They live in Matam", "don't they?"), ("He went to school", "didn't he?"),
      ("There is a problem", "isn't there?"), ("You had a car", "didn't you?"), ("She must leave now", "mustn't she?"), ("It rarely rains here", "does it?"), ("We could try", "couldn't we?"),
      ("You won't tell anyone", "will you?"), ("Fatou studies hard", "doesn't she?")]
NEG = {"aren't": "are", "isn't": "is", "weren't": "were", "can't": "can", "won't": "will", "haven't": "have", "shouldn't": "should", "wouldn't": "would", "don't": "do", "didn't": "did", "mustn't": "must", "couldn't": "could", "doesn't": "does", "hasn't": "has"}
POS = {v: k for k, v in NEG.items()}
PRON = ["you", "she", "he", "they", "we", "it", "I", "there"]
R = []
for i, (s, t) in enumerate(QT):
    aux, pr = t[:-1].split()
    flip = NEG.get(aux) or POS.get(aux) or {"shall": "will"}.get(aux, aux)
    other = [x for x in PRON if x != pr][i % 7]
    R.append((f"Question tag: « {s}, ___ »", t, f"{flip} {pr}?", f"{aux} {other}?", f"{flip} {other}?", "Auxiliaire de la phrase, polarité inverse, pronom sujet."))
REL = [("The boy ___ won the prize is my cousin.", "who", "which", "whose", "where"), ("The book ___ I bought is interesting.", "which", "who", "whose", "where"),
       ("The woman ___ son is a doctor lives next door.", "whose", "who", "which", "whom"), ("This is the village ___ I was born.", "where", "which", "who", "whose"),
       ("I remember the day ___ we met.", "when", "where", "which", "who"), ("The man to ___ I spoke was polite.", "whom", "who", "which", "whose"),
       ("Tell me ___ you want.", "what", "which", "that", "who"), ("The reason ___ he left is unknown.", "why", "where", "which", "whose"),
       ("Dakar, ___ is the capital, is very busy.", "which", "that", "where", "who"), ("The girl ___ bag was stolen called the police.", "whose", "who", "which", "that"),
       ("The people ___ we met were friendly.", "whom", "which", "whose", "where"), ("The house ___ roof is red belongs to my uncle.", "whose", "which", "where", "that")]
R += [(f"Relative pronoun: « {s} »", ok, a, b, c, "Who (personne sujet), which (chose), whose (possession), where (lieu), when (temps), whom (personne complément).") for s, ok, a, b, c in REL]
CON = [("He was ill. ___, he went to school.", "Nevertheless", "Because", "So that", "Unless", "Opposition : nevertheless, however."),
       ("She worked hard ___ she could pass.", "so that", "although", "however", "unless", "But : so that."), ("___ it was raining, we played football.", "Although", "Because", "So", "Therefore", "Concession : although, even though."),
       ("He didn't study; ___, he failed.", "therefore", "although", "whereas", "despite", "Conséquence : therefore, as a result."), ("___ the rain, the match went on.", "Despite", "Although", "Because", "However", "Despite + nom (pas de proposition)."),
       ("I stayed home ___ I was sick.", "because", "although", "whereas", "unless", "Cause : because, since, as."), ("My brother likes rice ___ my sister prefers couscous.", "whereas", "because", "so", "therefore", "Contraste : whereas, while."),
       ("___ studying, he also works in a shop.", "Besides", "Despite", "Although", "Unless", "Addition : besides, in addition to + -ing."), ("You won't succeed ___ you work harder.", "unless", "if", "although", "so", "Unless = if not."),
       ("___ of the bad weather, the plane took off.", "In spite", "Despite", "Although", "Because", "In spite of + nom.")]
R += [(f"Connector: « {s} »", ok, a, b, c, e) for s, ok, a, b, c, e in CON]

VOC = [("unemployment", "le chômage", "l'emploi", "la retraite", "la grève"), ("drought", "la sécheresse", "l'inondation", "la récolte", "la pluie"),
       ("brain drain", "la fuite des cerveaux", "le lavage de cerveau", "la migration rurale", "l'échec scolaire"), ("to raise awareness", "sensibiliser", "augmenter les prix", "se lever tôt", "élever des enfants"),
       ("the rural exodus", "l'exode rural", "la ville nouvelle", "le tourisme vert", "la réforme agraire"), ("a breadwinner", "un soutien de famille", "un boulanger", "un mendiant", "un héritier"),
       ("illiteracy", "l'analphabétisme", "la littérature", "l'alphabet", "l'éducation"), ("to drop out of school", "abandonner l'école", "redoubler", "passer en classe supérieure", "obtenir son diplôme"),
       ("child labour", "le travail des enfants", "l'accouchement", "la garderie", "les allocations familiales"), ("gender equality", "l'égalité des sexes", "la généalogie", "la parité monétaire", "l'égalité des chances scolaires"),
       ("a scholarship", "une bourse d'études", "une école", "un savant", "un diplôme"), ("to bribe", "corrompre (soudoyer)", "briller", "emprunter", "construire un pont"),
       ("desertification", "la désertification", "le désert", "la déforestation", "l'irrigation"), ("a polling station", "un bureau de vote", "un sondage", "un commissariat", "une station-service"),
       ("deforestation", "la déforestation", "le reboisement", "la forêt classée", "le feu de brousse"), ("a refugee", "un réfugié", "un réfrigérateur", "un rebelle", "un touriste"),
       ("to make ends meet", "joindre les deux bouts", "finir un travail", "se rencontrer", "faire des économies d'énergie"), ("sustainable development", "le développement durable", "le sous-développement", "la croissance rapide", "l'aide d'urgence"),
       ("a landlord", "un propriétaire (bailleur)", "un seigneur", "un agriculteur", "un locataire"), ("a tenant", "un locataire", "un propriétaire", "un tenancier de bar", "un voisin"),
       ("greenhouse gases", "les gaz à effet de serre", "les serres agricoles", "le gaz de cuisine", "l'énergie verte"), ("to go on strike", "faire grève", "frapper", "réussir", "aller au travail"),
       ("a dowry", "une dot", "un douanier", "un héritage", "un mariage"), ("peer pressure", "la pression des camarades", "la pression artérielle", "la paix sociale", "la peur de l'échec"),
       ("a healthcare system", "un système de santé", "une assurance auto", "une clinique privée", "un régime alimentaire"), ("to tackle a problem", "s'attaquer à un problème", "créer un problème", "ignorer un problème", "plaquer un adversaire"),
       ("overpopulation", "la surpopulation", "la dépopulation", "le recensement", "la natalité"), ("a slum", "un bidonville", "un quartier chic", "un marché", "un village"),
       ("the youth", "la jeunesse", "la vieillesse", "l'enfance", "les adultes"), ("to earn a living", "gagner sa vie", "apprendre à vivre", "dépenser son salaire", "vivre à la campagne")]
V = [(f"« {w} » means:", ok, a, b, c, "Vocabulaire des thèmes du BAC (société, environnement, développement).") for w, ok, a, b, c in VOC]
V += [(f"Which word means « {ok} »?", w, a, b, c, "Vocabulaire des thèmes du BAC.") for (w, ok, *_), (a, *_), (b, *_), (c, *_) in zip(VOC[:15], VOC[15:30], VOC[5:20], VOC[10:25])]

QCM_TLE_X3_EN = {"tle-anglais": {
    "Passif et discours indirect": calc(P + RS),
    "Conditionnels et souhaits": calc(C),
    "Les temps : perfect et continuous": calc(T),
    "Gérondif, infinitif et causatifs": calc(GI),
    "Relatifs, connecteurs et question tags": calc(R),
    "Vocabulaire et expressions": calc(V),
}}
