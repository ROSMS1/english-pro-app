import streamlit as st
from gtts import gTTS
import os
import random

# 1. CONFIGURATION (Toujours en premier !)
st.set_page_config(page_title="English Pro - Rosly", page_icon="🇬🇧")

# 2. FONCTION AUDIO
def prononcer_anglais(texte):
    try:
        tts = gTTS(text=texte, lang='en')
        filename = "prononciation.mp3"
        tts.save(filename)
        audio_file = open(filename, "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")
        audio_file.close() # Important pour pouvoir réécrire le fichier après
    except Exception as e:
        st.error("Erreur de lecture audio.")

# 3. BASE DE DONNÉES
if 'data' not in st.session_state:
    st.session_state.data = [
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
        {"en": "As far as I'm concerned", "fr": "En ce qui me concerne", "ex": "As far as I'm concerned, the site is ready."}
    ]

# 4. INTERFACE
st.title("🚀 English Pro App")

menu = st.sidebar.selectbox("Menu", ["Flashcards", "Dictionnaire", "A propos"])

if menu == "Flashcards":
    st.subheader("Entraînement Rapide")
    if 'current_card' not in st.session_state:
        st.session_state.current_card = random.choice(st.session_state.data)
        st.session_state.show_ans = False

    card = st.session_state.current_card
    
    st.info(f"### {card['en']}")
    
    # BOUTON AUDIO (Placé ici pour écouter avant ou après la traduction)
    if st.button("Écouter l'accent 🔊"):
        prononcer_anglais(card['en'])

    if st.button("Traduire"):
        st.session_state.show_ans = True
        
    if st.session_state.show_ans:
        st.success(f"**Français :** {card['fr']}")
        st.warning(f"**Exemple :** {card['ex']}")
        
    if st.button("Suivant ➡️"):
        st.session_state.current_card = random.choice(st.session_state.data)
        st.session_state.show_ans = False
        st.rerun()

elif menu == "Dictionnaire":
    st.subheader("Rechercher une expression")
    search = st.text_input("Tapez un mot (Anglais ou Français)")
    results = [i for i in st.session_state.data if search.lower() in i['en'].lower() or search.lower() in i['fr'].lower()]
    
    for r in results:
        with st.expander(r['en']):
            st.write(f"**Traduction :** {r['fr']}")
            st.write(f"**Exemple :** {r['ex']}")
            # Audio aussi dans le dictionnaire
            if st.button(f"Écouter 🔊", key=r['en']):
                prononcer_anglais(r['en'])

else:
    st.write("Application de révision d'anglais professionnel basée sur le livre Eyrolles.")
    st.write("Développé pour Rosly.")
