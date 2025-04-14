import streamlit as st
from datetime import date, timedelta
import random

# Challenge data
challenges = {
    1: {
        "environment": "Carry a reusable water bottle all day",
        "mindset": "Reflect on one area you'd like to grow spiritually",
        "reflection": "How did reducing plastic use make you feel? What growth area excites you?"
    },
    2: {
        "environment": "Turn off lights when not in use",
        "mindset": "Learn one new thing about environmental stewardship in Islam",
        "reflection": "What Quranic verse or Hadith about nature resonated with you today?"
    },
    3: {
        "environment": "Meat-free day (reduce carbon footprint)",
        "mindset": "Practice gratitude for three natural blessings",
        "reflection": "How does mindful consumption connect to spiritual growth?"
    },
    4: {
        "environment": "Collect and properly dispose of 10 pieces of litter",
        "mindset": "Identify a negative thought pattern to replace with growth",
        "reflection": "How does cleaning your environment mirror inner purification?"
    },
    5: {
        "environment": "Use a prayer mat made of sustainable materials",
        "mindset": "Challenge yourself to memorize an environmental ayah",
        "reflection": "How does connecting prayer with ecology deepen your worship?"
    },
    6: {
        "environment": "Reduce water usage during wudu by 25%",
        "mindset": "Journal about overcoming a recent difficulty",
        "reflection": "What lessons did water conservation teach you about moderation?"
    },
    7: {
        "environment": "Plant a tree or care for an existing plant",
        "mindset": "Teach someone one green practice from the Sunnah",
        "reflection": "How does nurturing life reflect your spiritual development?"
    },
    8: {
        "environment": "Use natural light instead of electric when possible",
        "mindset": "Visualize your ideal balanced, eco-conscious self",
        "reflection": "What inner light grew brighter through today's practice?"
    },
    9: {
        "environment": "Repurpose or repair something instead of discarding",
        "mindset": "Forgive one mistake (yours or others') and see it as growth",
        "reflection": "How does giving things second chances relate to tawbah?"
    },
    10: {
        "environment": "Create a personal sustainability pledge",
        "mindset": "Write a letter to your future self about continued growth",
        "reflection": "How has this combined journey impacted your connection to Creator and creation?"
    }
}

# Streamlit app
def main():
    st.set_page_config(page_title="Atikaf Eco-Growth Challenge", layout="wide")
    
    # Header with Islamic art style
    st.markdown("""
    <style>
    .header {
        font-size: 40px;
        color: #046A38;
        text-align: center;
        padding: 30px;
        background-color: #E8F5E9;
        border-radius: 10px;
        margin-bottom: 30px;
    }
    .day-card {
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        background-color: #F5F5F5;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.1);
    }
    .completed {
        border-left: 5px solid #2E7D32;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="header">🌿 10-Day Atikaf Environment & Growth Mindset Challenge 🌱</div>', unsafe_allow_html=True)
    
    # User info
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Your Name")
    with col2:
        start_date = st.date_input("Challenge Start Date", date.today())
    
    # Progress tracker
    st.subheader("Your Challenge Progress")
    progress = st.progress(0)
    
    # Calculate days
    today = date.today()
    current_day = (today - start_date).days + 1
    if current_day < 1 or current_day > 10:
        st.warning("The challenge runs for 10 days. Please adjust your start date.")
        current_day = min(max(current_day, 1), 10)
    
    # Display days
    completed_days = st.session_state.get("completed_days", set())
    
    tabs = st.tabs([f"Day {i}" for i in range(1, 11)])
    
    for i, tab in enumerate(tabs, start=1):
        with tab:
            day_date = start_date + timedelta(days=i-1)
            st.markdown(f"**{day_date.strftime('%A, %B %d, %Y')}**")
            
            container = st.container()
            container.markdown(f"### 🌍 Environmental Action:")
            container.markdown(f"> {challenges[i]['environment']}")
            
            container.markdown(f"### 🧠 Growth Mindset:")
            container.markdown(f"> {challenges[i]['mindset']}")
            
            container.markdown(f"### ✍️ Reflection Prompt:")
            container.markdown(f"> {challenges[i]['reflection']}")
            
            # Reflection text area
            reflection_key = f"reflection_{i}"
            user_reflection = container.text_area("Your Reflection", key=reflection_key,
                                               value=st.session_state.get(reflection_key, ""),
                                               height=150)
            
            # Mark as complete
            complete_key = f"day_{i}_complete"
            if container.checkbox("Mark as complete", key=complete_key,
                                value=st.session_state.get(complete_key, False)):
                completed_days.add(i)
                st.session_state.completed_days = completed_days
            else:
                completed_days.discard(i)
    
    # Update progress
    progress.progress(len(completed_days)/10)
    st.markdown(f"**Completed: {len(completed_days)}/10 days**")
    
    # Completion message
    if len(completed_days) == 10:
        st.balloons()
        st.success(f"Congratulations {name if name else 'participant'}! You've completed the 10-day Atikaf Eco-Growth Challenge!")
        
        # Generate certificate
        if st.button("Generate Completion Certificate"):
            st.markdown(f"""
            <div style="border: 2px solid #2E7D32; padding: 20px; text-align: center; border-radius: 10px;">
                <h1>Certificate of Completion</h1>
                <p>This certifies that</p>
                <h2>{name if name else 'The Participant'}</h2>
                <p>has successfully completed the</p>
                <h3>10-Day Atikaf Environment & Growth Mindset Challenge</h3>
                <p>from {start_date} to {start_date + timedelta(days=9)}</p>
                <p>By integrating environmental stewardship with spiritual growth, this participant has demonstrated commitment to holistic self-improvement during their Atikaf.</p>
                <br>
                <p>🌱 May your growth continue to benefit you and all creation. 🌍</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Resources section
    st.sidebar.title("Additional Resources")
    st.sidebar.markdown("""
    - [Environmental Teachings in Islam](https://www.iefworld.org/)
    - [Growth Mindset in Islamic Perspective](https://muslimmatters.org/)
    - [Sustainable Atikaf Guide](https://www.greenmuslims.org/)
    - [Daily Dua Journal Template](https://www.islamicreliefcanada.org/)
    """)
    
    st.sidebar.title("About This Challenge")
    st.sidebar.info("""
    This 10-day challenge combines environmental consciousness with personal growth during Atikaf - the spiritual retreat in the last 10 days of Ramadan. 
    
    Each day includes:
    - One actionable eco-friendly practice
    - One mindset growth exercise
    - A reflection prompt connecting both
    
    May this help you grow closer to Allah through caring for His creation.
    """)

if __name__ == "__main__":
    main()