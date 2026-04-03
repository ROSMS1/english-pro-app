import streamlit as st
from gtts import gTTS
import os
import random

# 1. CONFIGURATION
st.set_page_config(page_title="English Pro - Rosly", page_icon="🇬🇧", layout="wide")

# 2. FONCTION AUDIO AMÉLIORÉE
def prononcer_anglais(texte):
    try:
        # Nettoyage du texte pour gTTS (enlever les slashs ou parenthèses pour une meilleure voix)
        texte_propre = texte.split('/')[0].split('(')[0].strip()
        tts = gTTS(text=texte_propre, lang='en')
        filename = "prononciation.mp3"
        tts.save(filename)
        
        with open(filename, "rb") as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")
        
        os.remove(filename) # Nettoie le fichier temporaire
    except Exception as e:
        st.error("Erreur de lecture audio.")

# 3. BASE DE DONNÉES MASSIVE
if 'data' not in st.session_state:
    st.session_state.data = [
        # --- BASES EXISTANTES ---
        {"en": "Go on / Carry on", "fr": "Continuer, poursuivre une action", "ex": "Please carry on, I am listening."},
        {"en": "Go back / Come back", "fr": "Retourner / Revenir", "ex": "We decided to go back to the site."},
        {"en": "Set up", "fr": "Installer, configurer", "ex": "Can you help me set up the router?"},
        {"en": "Carry out", "fr": "Effectuer, réaliser", "ex": "We need to carry out a site survey."},
        {"en": "Work out", "fr": "Élaborer, mettre au point", "ex": "We must work out a new strategy."},
        {"en": "Point out", "fr": "Signaler, souligner", "ex": "He pointed out the error in the report."},
        {"en": "Find out", "fr": "Découvrir, enquêter", "ex": "I need to find out who is responsible."},
        {"en": "Actually / In fact", "fr": "En fait / En effet", "ex": "Actually, it is simpler than it looks."},
        {"en": "Let's get down to business", "fr": "Passons aux choses sérieuses", "ex": "Time is short, let's get down to business."},
        {"en": "What's your take on this?", "fr": "Quel est votre avis ?", "ex": "What's your take on this technical issue?"},
        {"en": "As far as I'm concerned", "fr": "En ce qui me concerne", "ex": "As far as I'm concerned, the site is ready."},

        # --- VERBES IRRÉGULIERS & TEMPS ---
        {"en": "To Make (make-made-made)", "fr": "Faire / Fabriquer (création)", "ex": "We have made a lot of progress this month."},
        {"en": "To Know (know-knew-known)", "fr": "Savoir / Connaître", "ex": "I knew he was right from the start."},
        {"en": "To Come (come-came-come)", "fr": "Venir", "ex": "My brother came home very late last night."},
        {"en": "To Say (say-said-said)", "fr": "Dire", "ex": "She said hello to me this morning."},
        {"en": "To Buy (buy-bought-bought)", "fr": "Acheter", "ex": "We bought a new car last month."},
        {"en": "To Speak (speak-spoke-spoken)", "fr": "Parler", "ex": "I spoke to the manager about the problem."},
        {"en": "To Give (give-gave-given)", "fr": "Donner", "ex": "He gave me a very useful advice."},
        {"en": "To Be (am/is/are - was/were - been)", "fr": "Être", "ex": "We have been friends for years."},
        {"en": "To Go (go-went-gone)", "fr": "Aller", "ex": "They have already gone to bed."},
        {"en": "To Have (have-had-had)", "fr": "Avoir", "ex": "I had a big breakfast this morning."},
        {"en": "To Do (do-did-done)", "fr": "Faire (activité)", "ex": "He did a great job on the project."},
        {"en": "To See (see-saw-seen)", "fr": "Voir", "ex": "I have never seen such a beautiful sunset."},
        {"en": "To Eat (eat-ate-eaten)", "fr": "Manger", "ex": "They eat lunch at noon."},
        {"en": "To Take (take-took-taken)", "fr": "Prendre", "ex": "She took a taxi to the airport."},
        {"en": "To Write (write-wrote-written)", "fr": "Écrire", "ex": "She has written three books so far."},

        # --- VIE QUOTIDIENNE & SALUTATIONS ---
        {"en": "What's up?", "fr": "Quoi de neuf ?", "ex": "Hey man, what's up?"},
        {"en": "Long time no see", "fr": "Ça fait un bail", "ex": "Oh, hi Mark! Long time no see."},
        {"en": "I’m starving", "fr": "Je meurs de faim", "ex": "Let's eat, I'm starving."},
        {"en": "It’s up to you", "fr": "C’est toi qui décides", "ex": "Pizza or pasta? It’s up to you."},
        {"en": "Never mind", "fr": "Laisse tomber / C’est pas grave", "ex": "Never mind, I found my keys."},
        {"en": "My bad", "fr": "C’est ma faute", "ex": "I forgot to call you, my bad."},
        {"en": "Anyway...", "fr": "Bref / De toute façon...", "ex": "Anyway, let’s talk about something else."},
        {"en": "To be honest...", "fr": "Pour être honnête...", "ex": "To be honest, I don't like this movie."},

        # --- TEMPS & FRÉQUENCE ---
        {"en": "So far, so good", "fr": "Jusqu'ici tout va bien", "ex": "How is the project? So far, so good."},
        {"en": "Once in a blue moon", "fr": "Rarement / Tous les 36 du mois", "ex": "He visits us once in a blue moon."},
        {"en": "Better late than never", "fr": "Mieux vaut tard que jamais", "ex": "You’re here! Better late than never."},
        {"en": "In the long run", "fr": "À long terme", "ex": "It’s worth it in the long run."},
        {"en": "As soon as possible (ASAP)", "fr": "Dès que possible", "ex": "Call me ASAP."},

        # --- BUSINESS & TRAVAIL ---
        {"en": "Keep me posted", "fr": "Tiens-moi au courant", "ex": "Keep me posted on the situation."},
        {"en": "In a nutshell", "fr": "En résumé / En un mot", "ex": "In a nutshell, we are losing money."},
        {"en": "Think out of the box", "fr": "Penser différemment", "ex": "We need to think out of the box to solve this."},
        {"en": "Call it a day", "fr": "Finir sa journée", "ex": "It’s 6 PM, let’s call it a day."},
        {"en": "To be on the same page", "fr": "Être sur la même longueur d'onde", "ex": "We need to be on the same page."},
        {"en": "Back to square one", "fr": "Retour à la case départ", "ex": "The plan failed, so we're back to square one."},
        {"en": "Piece of cake", "fr": "C'est du gâteau / Très facile", "ex": "That exam was a piece of cake."},

        # --- EMAILS PROFESSIONNELS ---
        {"en": "I hope this email finds you well", "fr": "J'espère que vous allez bien (Intro email)", "ex": "Dear Eric, I hope this email finds you well."},
        {"en": "Further to our conversation...", "fr": "Suite à notre conversation...", "ex": "Further to our conversation this morning, here is the report."},
        {"en": "Please find attached", "fr": "Veuillez trouver ci-joint", "ex": "Please find attached the site survey results."},
        {"en": "I look forward to hearing from you", "fr": "Dans l'attente de votre réponse", "ex": "I look forward to hearing from you soon. Best regards."},

        # --- NÉGOCIATION & PERSUASION ---
        {"en": "A win-win situation", "fr": "Une situation gagnant-gagnant", "ex": "It's a win-win situation for everyone."},
        {"en": "Could we meet halfway?", "fr": "Pourrions-nous faire un compromis ?", "ex": "I understand your budget, could we meet halfway?"},
        {"en": "I see where you’re coming from", "fr": "Je vois où vous voulez en venir", "ex": "I see where you’re coming from, but we have technical limits."},
        {"en": "The bottom line is...", "fr": "L'essentiel / Le résultat net est...", "ex": "The bottom line is we need more users."}
    ]

# 4. INTERFACE
st.title("🚀 English Pro App")
st.markdown("---")

menu = st.sidebar.selectbox("Menu", ["Flashcards", "Dictionnaire", "A propos"])

if menu == "Flashcards":
    st.subheader("🎯 Entraînement Rapide")
    
    if 'current_card' not in st.session_state:
        st.session_state.current_card = random.choice(st.session_state.data)
        st.session_state.show_ans = False

    card = st.session_state.current_card
    
    # Affichage de la carte
    st.info(f"## {card['en']}")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Écouter 🔊"):
            prononcer_anglais(card['en'])
    
    with col2:
        if st.button("Traduire 🔄"):
            st.session_state.show_ans = True
            
    with col3:
        if st.button("Suivant ➡️"):
            st.session_state.current_card = random.choice(st.session_state.data)
            st.session_state.show_ans = False
            st.rerun()

    if st.session_state.show_ans:
        st.success(f"**Français :** {card['fr']}")
        st.warning(f"**Exemple :** {card['ex']}")

elif menu == "Dictionnaire":
    st.subheader("📚 Bibliothèque d'expressions")
    search = st.text_input("Rechercher un mot ou une expression...")
    
    filtered_data = [i for i in st.session_state.data if search.lower() in i['en'].lower() or search.lower() in i['fr'].lower()]
    
    st.write(f"{len(filtered_data)} expressions trouvées.")
    
    for r in filtered_data:
        with st.expander(f"🇬🇧 {r['en']}"):
            st.write(f"**🇫🇷 Traduction :** {r['fr']}")
            st.write(f"**💡 Exemple :** {r['ex']}")
            if st.button(f"Écouter 🔊", key=f"dict_{r['en']}"):
                prononcer_anglais(r['en'])

else:
    st.subheader("ℹ️ À propos")
    st.write("Cette application est conçue pour aider **Rosly** à maîtriser l'anglais technique et professionnel.")
    st.write(f"Nombre total d'expressions chargées : **{len(st.session_state.data)}**")
    st.markdown("---")
    st.write("Source : Méthode Eyrolles et expressions Business.")
