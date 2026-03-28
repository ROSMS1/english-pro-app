import streamlit as st
import random

# Configuration Mobile
st.set_page_config(page_title="English Pro - Rosly", page_icon="🇬🇧")

# --- BASE DE DONNÉES COMPLÈTE ---
if 'data' not in st.session_state:
    st.session_state.data = [
        # Phrasal Verbs : Actions & Mouvements
        {"en": "Go on / Carry on", "fr": "Continuer, poursuivre une action", "ex": "Please carry on, I am listening."},
        {"en": "Go back / Come back", "fr": "Retourner / Revenir", "ex": "We decided to go back to the site."},
        {"en": "Go out / Come out", "fr": "Sortir / Paraître", "ex": "My new book comes out next week."},
        {"en": "Go down / Come down", "fr": "Descendre / Diminuer", "ex": "The temperature will come down tonight."},
        {"en": "Go up / Come up", "fr": "Monter / Se lever", "ex": "The sun comes up at 6 AM."},
        {"en": "Get in / Get out", "fr": "Entrer / Sortir", "ex": "Get in the car, we are late!"},
        {"en": "Get on / Get off", "fr": "Monter / Descendre (transport)", "ex": "I get off the bus at the next stop."},
        {"en": "Set up", "fr": "Installer, configurer", "ex": "Can you help me set up the router?"},
        {"en": "Set out / Set off", "fr": "Partir, se mettre en route", "ex": "We set off early to avoid traffic."},
        {"en": "Pick up", "fr": "Ramasser, récupérer", "ex": "I picked up a cold on my trip."},
        {"en": "Take off", "fr": "Décoller, enlever", "ex": "The plane is ready to take off."},
        {"en": "Turn back / Turn round", "fr": "Faire demi-tour / Se retourner", "ex": "We had to turn back because of the rain."},
        {"en": "Move on", "fr": "Passer à autre chose", "ex": "Let's move on to the next topic."},
        
        # Phrasal Verbs : Travail & Gestion
        {"en": "Carry out", "fr": "Effectuer, réaliser", "ex": "We need to carry out a site survey."},
        {"en": "Work out", "fr": "Élaborer, mettre au point", "ex": "We must work out a new strategy."},
        {"en": "Take over", "fr": "Reprendre la relève", "ex": "He will take over the project tomorrow."},
        {"en": "Take on", "fr": "Se charger de, défier", "ex": "I can't take on any more work right now."},
        {"en": "Point out", "fr": "Signaler, souligner", "ex": "He pointed out the error in the report."},
        {"en": "Find out", "fr": "Découvrir, enquêter", "ex": "I need to find out who is responsible."},
        {"en": "Bring about", "fr": "Provoquer, causer", "ex": "This will bring about big changes."},
        {"en": "Hold on", "fr": "Attendre, tenir bon", "ex": "Hold on a minute, I'm coming."},
        {"en": "Get back to", "fr": "Revenir vers quelqu'un", "ex": "I will get back to you with an answer."},

        # Adverbes de Temps & Fréquence
        {"en": "Always / Never", "fr": "Toujours / Jamais", "ex": "Always check the power supply first."},
        {"en": "Seldom / Barely", "fr": "Rarement / À peine", "ex": "I barely had time to finish."},
        {"en": "Recently / Yet", "fr": "Récemment / Encore", "ex": "I haven't seen the report yet."},
        {"en": "Meanwhile", "fr": "Entre-temps", "ex": "Meanwhile, the team is waiting."},
        
        # Adverbes de Logique & Manière
        {"en": "Actually / In fact", "fr": "En fait / En effet", "ex": "Actually, it is simpler than it looks."},
        {"en": "However / Nevertheless", "fr": "Cependant / Néanmoins", "ex": "However, we must be careful."},
        {"en": "Basically / Obviously", "fr": "En gros / Évidemment", "ex": "Basically, the system is offline."},
        {"en": "Perhaps / Maybe", "fr": "Peut-être", "ex": "Perhaps we should wait for the boss."},
        {"en": "Somehow", "fr": "En quelque sorte", "ex": "Somehow, we fixed the issue."},

        # Personnalité & Apparence
        {"en": "Reliable / Smart", "fr": "Fiable / Intelligent", "ex": "She is a very smart and reliable engineer."},
        {"en": "Brave / Selfish", "fr": "Courageux / Égoïste", "ex": "It was brave to admit the mistake."},
        {"en": "Tall / Thin", "fr": "Grand / Mince", "ex": "The tower is very tall and thin."},

        # Expressions du Livre (Eyrolles)
        {"en": "Pleased to meet you", "fr": "Ravi de vous rencontrer", "ex": "Pleased to meet you, welcome to Congo."},
        {"en": "Did you find us easily?", "fr": "Nous avez-vous trouvés facilement ?", "ex": "Welcome! Did you find us easily?"},
        {"en": "Let's get down to business", "fr": "Passons aux choses sérieuses", "ex": "Time is short, let's get down to business."},
        {"en": "What's your take on this?", "fr": "Quel est votre avis ?", "ex": "What's your take on this technical issue?"},
        {"en": "Please find attached", "fr": "Veuillez trouver ci-joint", "ex": "Please find attached the daily log."},
        {"en": "As far as I'm concerned", "fr": "En ce qui me concerne", "ex": "As far as I'm concerned, the site is ready."}
    ]

# --- INTERFACE ---
st.title("🚀 English Pro App")

menu = st.sidebar.selectbox("Menu", ["Flashcards", "Dictionnaire", "A propos"])

if menu == "Flashcards":
    st.subheader("Entraînement Rapide")
    if 'current_card' not in st.session_state:
        st.session_state.current_card = random.choice(st.session_state.data)
        st.session_state.show_ans = False

    card = st.session_state.current_card
    
    st.info(f"### {card['en']}")
    
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

else:
    st.write("Application de révision d'anglais professionnel basée sur le livre Eyrolles.")
    st.write("Développé pour Rosly.")
