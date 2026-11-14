import streamlit as st

st.set_page_config(
    page_title="LUNA BASE",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="collapsed"
)




if "page" not in st.session_state:
    st.session_state.page = "welcome"


if "oxygen" not in st.session_state:
    st.session_state.oxygen = 60

if "water" not in st.session_state:
    st.session_state.water = 70

if "food" not in st.session_state:
    st.session_state.food = 80

if "power" not in st.session_state:
    st.session_state.power = 70

if "health" not in st.session_state:
    st.session_state.health = 80


if "emergency_reserves" not in st.session_state:
    st.session_state.emergency_reserves = 2


if "emergency_resolved" not in st.session_state:
    st.session_state.emergency_resolved = False

if "emergency_message" not in st.session_state:
    st.session_state.emergency_message = ""



st.markdown("""
<style>

.stApp {
    background-color: #080D18;
    color: #FFFFFF;
}

.block-container {
    max-width: 1150px;
    padding-top: 3rem;
}

h1, h2, h3 {
    color: #FFFFFF;
}

p {
    color: #C5D0DF;
}

.stButton > button {
    background-color: #00A6C7;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 12px 20px;
    font-weight: bold;
    width: 100%;
}

.stButton > button:hover {
    background-color: #0086A3;
    color: white;
}

.info-panel {
    background-color: #111C2E;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #263B55;
    margin-bottom: 15px;
}

.small-label {
    color: #00C7E8;
    letter-spacing: 3px;
    font-size: 13px;
    font-weight: bold;
}

.tagline {
    color: #00C7E8;
    font-size: 20px;
    text-align: center;
}

.footer {
    color: #8191A8;
    text-align: center;
    font-size: 13px;
    margin-top: 50px;
}

</style>
""", unsafe_allow_html=True)



if st.session_state.page == "welcome":

    st.markdown(
        '<p class="small-label" style="text-align:center;">'
        'W.A.I.D. PRESENTS</p>',
        unsafe_allow_html=True
    )

    st.title("🌙 LUNA BASE")

    st.markdown(
        '<p class="tagline">'
        'Survive the Moon. Explore the Unknown. Build Beyond Earth.'
        '</p>',
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown("""
    <div style="text-align:center; padding:20px;">
        <h3>WELCOME, COMMANDER.</h3>
        <p>
        Your mission is to establish and maintain a lunar base.
        Manage resources, protect your crew, investigate the Moon
        and make decisions that will determine the future of your mission.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="info-panel">
            <h3>🫁 SURVIVAL</h3>
            <p>Manage oxygen, water, food and electricity.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-panel">
            <h3>🔬 EXPLORATION</h3>
            <p>Investigate lunar conditions and scientific discoveries.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="info-panel">
            <h3>🚀 PROGRESSION</h3>
            <p>Complete missions and unlock new challenges.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🚀 START CAMPAIGN"):
            st.session_state.page = "missions"
            st.rerun()

    with col2:
        if st.button("📖 HOW TO PLAY"):
            st.session_state.page = "instructions"
            st.rerun()

    with st.expander("ABOUT LUNA BASE"):
        st.write("""
        LUNA BASE is an educational lunar survival and scientific
        exploration simulator.

        Players experience fictional lunar mission scenarios,
        manage resources and make decisions with consequences.

        NASA scientific information can be used to help inform
        the educational gameplay.
        """)

    st.markdown(
        '<p class="footer">Developed by W.A.I.D. – Women in AI Development</p>',
        unsafe_allow_html=True
    )


elif st.session_state.page == "missions":

    st.markdown(
        '<p class="small-label">MISSION CONTROL</p>',
        unsafe_allow_html=True
    )

    st.title("🚀 MISSION SELECTION")

    st.write("Choose your mission, Commander.")

    st.markdown("""
    <div class="info-panel">
        <h3>MISSION 01: ESTABLISH THE LUNAR BASE</h3>
        <p><b>Duration:</b> 3 simulated days</p>
        <p><b>Difficulty:</b> Easy</p>
        <p><b>Objective:</b> Establish a functioning lunar base,
        maintain essential resources and protect the crew.</p>
        <p><b>Mission focus:</b> Survival and resource management.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("START MISSION 01"):
        st.session_state.emergency_resolved = False
        st.session_state.emergency_message = ""
        st.session_state.page = "emergency"
        st.rerun()

    st.write("")

    st.subheader("UPCOMING MISSIONS")

    st.markdown("""
    <div class="info-panel">
        🔒 <b>MISSION 02: LUNAR SURFACE EXPLORATION</b>
        <p>Duration: 4 simulated days | Difficulty: Medium</p>
    </div>

    <div class="info-panel">
        🔒 <b>MISSION 03: SEARCH FOR LUNAR WATER</b>
        <p>Duration: 5 simulated days | Difficulty: Hard</p>
    </div>

    <div class="info-panel">
        🔒 <b>MISSION 04: RESTORE BASE OPERATIONS</b>
        <p>Duration: 2 simulated days | Difficulty: Hard</p>
    </div>

    <div class="info-panel">
        🔒 <b>MISSION 05: SUSTAINABLE LUNAR SETTLEMENT</b>
        <p>Duration: To be determined | Difficulty: Advanced</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("← BACK TO HOME"):
        st.session_state.page = "welcome"
        st.rerun()



elif st.session_state.page == "instructions":

    st.markdown(
        '<p class="small-label">COMMANDER TRAINING</p>',
        unsafe_allow_html=True
    )

    st.title("📖 HOW TO PLAY")

    st.subheader("Your responsibilities")

    st.write("""
    1. Keep oxygen levels high enough to protect the crew.
    2. Monitor water and food supplies.
    3. Manage electricity carefully.
    4. Protect crew health.
    5. Respond to emergencies.
    6. Complete the objectives of each mission.
    """)

    st.subheader("Understanding resources")

    st.write("""
    - Oxygen: Supports the crew.
    - Water: Essential for the crew.
    - Food: Provides supplies for the crew.
    - Electricity: Powers base systems.
    - Crew Health: Represents the crew's overall condition.
    """)

    st.info("""
    Your decisions affect the condition of the lunar base.
    Poor resource management may lead to mission failure.
    """)

    if st.button("← BACK TO HOME"):
        st.session_state.page = "welcome"
        st.rerun()



elif st.session_state.page == "emergency":

    st.markdown(
        '<p class="small-label">LUNAR BASE ALERT SYSTEM</p>',
        unsafe_allow_html=True
    )

    st.title("⚠️ LIFE-SUPPORT EMERGENCY")

    st.error("OXYGEN PRODUCTION SYSTEM FAILURE!")

    st.write("""
    Commander, an unexpected malfunction has affected
    the oxygen production system.

    The crew needs an alternative oxygen supply.

    You must decide how to respond.
    """)

    st.divider()



    st.subheader("CURRENT BASE RESOURCES")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🫁 Oxygen", f"{st.session_state.oxygen}%")

    with col2:
        st.metric("⚡ Electricity", f"{st.session_state.power}%")

    with col3:
        st.metric("❤️ Crew Health", f"{st.session_state.health}%")

    col4, col5 = st.columns(2)

    with col4:
        st.metric("💧 Water", f"{st.session_state.water}%")

    with col5:
        st.metric("🍱 Food", f"{st.session_state.food}%")

    st.metric(
        "🛟 Emergency Oxygen Reserves",
        st.session_state.emergency_reserves
    )

    st.divider()

    st.subheader("COMMANDER, WHAT WILL YOU DO?")



    if not st.session_state.emergency_resolved:

        st.write("Select one of the available emergency responses.")



        if st.button(
            "🛟 USE EMERGENCY OXYGEN RESERVES",
            use_container_width=True
        ):

            if st.session_state.emergency_reserves > 0:

                st.session_state.oxygen = min(
                    100,
                    st.session_state.oxygen + 15
                )

                st.session_state.emergency_reserves -= 1

                st.session_state.health = min(
                    100,
                    st.session_state.health + 5
                )

                st.session_state.emergency_message = (
                    "Emergency oxygen reserves activated! "
                    "Oxygen levels have improved and the crew is protected."
                )

            else:

                st.session_state.emergency_message = (
                    "WARNING: No emergency oxygen reserves are available!"
                )

            st.session_state.emergency_resolved = True
            st.rerun()

 

        if st.button(
            "🔧 REPAIR OXYGEN PRODUCTION SYSTEM",
            use_container_width=True
        ):

            if st.session_state.power >= 15:

                st.session_state.power -= 15

                st.session_state.oxygen = min(
                    100,
                    st.session_state.oxygen + 10
                )

                st.session_state.health = min(
                    100,
                    st.session_state.health + 3
                )

                st.session_state.emergency_message = (
                    "The oxygen production system has been repaired. "
                    "Electricity was consumed."
                )

            else:

                st.session_state.emergency_message = (
                    "INSUFFICIENT ELECTRICITY! "
                    "The repair cannot be completed."
                )

            st.session_state.emergency_resolved = True
            st.rerun()

        # OPTION 3: IGNORE THE WARNING

        if st.button(
            "🚨 IGNORE WARNING",
            use_container_width=True
        ):

            st.session_state.oxygen = max(
                0,
                st.session_state.oxygen - 20
            )

            st.session_state.health = max(
                0,
                st.session_state.health - 15
            )

            st.session_state.emergency_message = (
                "The warning was ignored. Oxygen levels have decreased "
                "and crew health is at risk."
            )

            st.session_state.emergency_resolved = True
            st.rerun()

  

    else:

        st.success(st.session_state.emergency_message)

        st.subheader("UPDATED RESOURCE LEVELS")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("🫁 Oxygen", f"{st.session_state.oxygen}%")

        with col2:
            st.metric("⚡ Electricity", f"{st.session_state.power}%")

        with col3:
            st.metric("❤️ Crew Health", f"{st.session_state.health}%")

        st.metric(
            "🛟 Emergency Oxygen Reserves",
            st.session_state.emergency_reserves
        )

        st.write("")

        # Check for mission failure

        if st.session_state.health <= 0:

            st.error("MISSION FAILED: Crew health reached zero.")

        elif st.session_state.oxygen <= 0:

            st.error("MISSION FAILED: Oxygen reserves depleted.")

        else:

            st.info("Your emergency decision has been recorded.")

        st.subheader("MISSION COMMAND")

        if st.button("← RETURN TO MISSION SELECTION"):

            st.session_state.page = "missions"
            st.rerun()
