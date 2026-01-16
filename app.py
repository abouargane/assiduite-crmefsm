import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="CRMEFSM | Assiduité EPS",
    page_icon="🏃‍♂️",
    layout="wide" # Utilisation de toute la largeur pour les colonnes
)

# Style CSS pour un rendu professionnel et coloré
st.markdown("""
    <style>
    .main {
        background-color: #f4f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s;
    }
    .class-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        text-align: center;
        border-top: 6px solid;
        margin-bottom: 20px;
    }
    .icon-circle {
        width: 70px;
        height: 70px;
        line-height: 70px;
        border-radius: 50%;
        margin: 0 auto 15px;
        font-size: 30px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    h4 {
        margin-top: 10px;
        color: #1e293b;
        font-size: 1.1em;
    }
    </style>
    """, unsafe_allow_html=True)

# En-tête
st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <h1 style="color: #004a99; margin-bottom: 0;">CRMEFSM</h1>
        <h3 style="color: #64748b; font-weight: 400;">Gestion de l'Assiduité - Section EPS</h3>
    </div>
    """, unsafe_allow_html=True)

# Définition des classes avec leurs couleurs et icônes
CLASSES = [
    {
        "title": "COLLÉGIAL / Classe 1",
        "icon": "🎯",
        "color": "#3b82f6", # Bleu
        "bg_icon": "#dbeafe",
        "form": "#",
        "sheet": "#"
    },
    {
        "title": "COLLÉGIAL / Classe 2",
        "icon": "⚽",
        "color": "#8b5cf6", # Violet
        "bg_icon": "#ede9fe",
        "form": "#",
        "sheet": "#"
    },
    {
        "title": "COLLÉGIAL / Classe 3",
        "icon": "🏀",
        "color": "#06b6d4", # Cyan
        "bg_icon": "#cffafe",
        "form": "#",
        "sheet": "#"
    },
    {
        "title": "QUALIFIANT",
        "icon": "🏆",
        "color": "#ef4444", # Rouge
        "bg_icon": "#fee2e2",
        "form": "#",
        "sheet": "#"
    }
]

# Création de la grille (2 colonnes x 2 lignes)
col1, col2 = st.columns(2, gap="large")

for i, cl in enumerate(CLASSES):
    # On alterne entre col1 et col2
    target_col = col1 if i % 2 == 0 else col2
    
    with target_col:
        st.markdown(f"""
            <div class="class-card" style="border-top-color: {cl['color']};">
                <div class="icon-circle" style="background-color: {cl['bg_icon']};">
                    {cl['icon']}
                </div>
                <h4>{cl['title']}</h4>
            </div>
            """, unsafe_allow_html=True)
        
        # Boutons d'action
        btn_form, btn_sheet = st.columns(2)
        with btn_form:
            st.link_button("📝 Enregistrer", cl['form'], use_container_width=True, type="primary")
        with btn_sheet:
            st.link_button("📊 Registre", cl['sheet'], use_container_width=True)
        
        st.markdown("<br>", unsafe_allow_html=True)

# Pied de page
st.divider()
st.markdown("""
    <div style="text-align: center; color: #94a3b8;">
        <small>Système d'Assiduité CRMEFSM © 2026 | Déployé via Streamlit</small>
    </div>
    """, unsafe_allow_html=True)