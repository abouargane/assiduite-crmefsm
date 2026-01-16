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
        "form": "https://docs.google.com/forms/d/e/1FAIpQLScm-4amoLVfl6r3fIKazUAr1djXRFmlYxrvIwxSAC_T4YaHjA/viewform?usp=pp_url&entry.1007979966=Pr%C3%A9sent&entry.1385971643=Pr%C3%A9sent&entry.1987222693=Pr%C3%A9sent&entry.1887929255=Pr%C3%A9sent&entry.455024699=Pr%C3%A9sent&entry.812780215=Pr%C3%A9sent&entry.361427837=Pr%C3%A9sent&entry.949700922=Pr%C3%A9sent&entry.1074772953=Pr%C3%A9sent&entry.1115980403=Pr%C3%A9sent&entry.1457065383=Pr%C3%A9sent&entry.230351923=Pr%C3%A9sent&entry.1940989520=Pr%C3%A9sent&entry.531465411=Pr%C3%A9sent&entry.1689540880=Pr%C3%A9sent&entry.686894759=Pr%C3%A9sent&entry.514224293=Pr%C3%A9sent&entry.92163942=Pr%C3%A9sent&entry.423639812=Pr%C3%A9sent&entry.1633304826=Pr%C3%A9sent&entry.113428221=Pr%C3%A9sent&entry.1955849253=Pr%C3%A9sent&entry.2067663889=Pr%C3%A9sent&entry.650958674=Pr%C3%A9sent&entry.1131637820=Pr%C3%A9sent&entry.2094542129=Pr%C3%A9sent&entry.728700713=Pr%C3%A9sent&entry.1038052564=Pr%C3%A9sent&entry.889627463=Pr%C3%A9sent&entry.2136813038=Pr%C3%A9sent&entry.1836105037=Pr%C3%A9sent&entry.1843164671=Pr%C3%A9sent&entry.1985831916=Pr%C3%A9sent&entry.10519350=Pr%C3%A9sent&entry.1335357810=Pr%C3%A9sent&entry.839748346=Pr%C3%A9sent&entry.641119159=Pr%C3%A9sent&entry.1084422824=Pr%C3%A9sent&entry.1726868224=Pr%C3%A9sent&entry.2024727228=Pr%C3%A9sent",
        "sheet": "https://docs.google.com/spreadsheets/d/1VmVo2rJhEmcKzDY1ASbIAXSpulDStW6e6ZdCrsgZOOw/edit?usp=sharing"
    },
    {
        "title": "COLLÉGIAL / Classe 2",
        "icon": "⚽",
        "color": "#8b5cf6", # Violet
        "bg_icon": "#ede9fe",
        "form": "https://docs.google.com/forms/d/e/1FAIpQLSfJKtAJV5GomvI67DfhWJUbVZ1fPn0sQ6-QZHqPSjxvHLbN4g/viewform?usp=pp_url&entry.2024727228=Pr%C3%A9sent&entry.215078296=Pr%C3%A9sent&entry.1978854833=Pr%C3%A9sent&entry.1995798027=Pr%C3%A9sent&entry.1345456164=Pr%C3%A9sent&entry.1837289749=Pr%C3%A9sent&entry.776652965=Pr%C3%A9sent&entry.130836278=Pr%C3%A9sent&entry.190418267=Pr%C3%A9sent&entry.1707877059=Pr%C3%A9sent&entry.930641701=Pr%C3%A9sent&entry.938295061=Pr%C3%A9sent&entry.707187884=Pr%C3%A9sent&entry.1831968273=Pr%C3%A9sent&entry.817717987=Pr%C3%A9sent&entry.2029267544=Pr%C3%A9sent&entry.1529589661=Pr%C3%A9sent&entry.911248793=Pr%C3%A9sent&entry.1881625481=Pr%C3%A9sent&entry.1373148559=Pr%C3%A9sent&entry.1901939998=Pr%C3%A9sent&entry.422216179=Pr%C3%A9sent&entry.1459208861=Pr%C3%A9sent&entry.942786572=Pr%C3%A9sent&entry.803606882=Pr%C3%A9sent&entry.98487844=Pr%C3%A9sent&entry.39493014=Pr%C3%A9sent&entry.2023420167=Pr%C3%A9sent&entry.2082049267=Pr%C3%A9sent&entry.714612561=Pr%C3%A9sent&entry.1652549927=Pr%C3%A9sent&entry.475008448=Pr%C3%A9sent&entry.699882270=Pr%C3%A9sent&entry.1910658620=Pr%C3%A9sent&entry.1993130080=Pr%C3%A9sent&entry.51865348=Pr%C3%A9sent&entry.2136657445=Pr%C3%A9sent&entry.406582727=Pr%C3%A9sent&entry.1476923264=Pr%C3%A9sent&entry.1836240291=Pr%C3%A9sent",
        "sheet": "https://docs.google.com/spreadsheets/d/1_TyM5GRZEN53zhwfUeHKyLuhskfMcBW3TmMyIvSCElU/edit?usp=sharing"
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
