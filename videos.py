import streamlit as st

def run():
    st.subheader("Tutoriais no YouTube")
    st.write("Abaixo você encontra links para os vídeos explicativos que criei sobre análise de dados com Python.")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <iframe width="350" height="197" src="https://www.youtube.com/embed/SoT8nKb-R38" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
            <iframe width="350" height="197" src="https://www.youtube.com/embed/UnslpMJm0sI" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
            <iframe width="350" height="197" src="https://www.youtube.com/embed/kCN6Rtupy0s" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <iframe width="350" height="197" src="https://www.youtube.com/embed/YkzwEA4DSuQ" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
            <iframe width="350" height="197" src="https://www.youtube.com/embed/3enyJoD2kUk" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
            <iframe width="350" height="197" src="https://www.youtube.com/embed/eO0pfs0gTTc" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
        """, unsafe_allow_html=True)

    st.write("---")

    st.subheader("Participações em Outros Canais")
    st.write("Aqui estão alguns vídeos onde participei de bate-papos e discussões em outros canais.")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <iframe width="350" height="197" src="https://www.youtube.com/embed/xNu5F6hcim0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <iframe width="350" height="197" src="https://www.youtube.com/embed/ievLc2kqCu8" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
        """, unsafe_allow_html=True)

    st.write("---")

    st.subheader("Bate-papos e Entrevistas")
    st.write("Aqui estão alguns vídeos onde convidei participantes para bate-papos e discussões no meu canal.")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <iframe width="350" height="197" src="https://www.youtube.com/embed/kfg9uGXQCfg" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
            <iframe width="350" height="197" src="https://www.youtube.com/embed/bfXWgrhYTYc" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
            <iframe width="350" height="197" src="https://www.youtube.com/embed/F4qx5XoSOKE" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
            <iframe width="350" height="197" src="https://www.youtube.com/embed/xTeqIYqSITU" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <iframe width="350" height="197" src="https://www.youtube.com/embed/BdbwJvPuuYM" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
            <iframe width="350" height="197" src="https://www.youtube.com/embed/LcqodKPqgTs" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
            <iframe width="350" height="197" src="https://www.youtube.com/embed/ZbJrLlGzxJA" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
            <iframe width="350" height="197" src="https://www.youtube.com/embed/OdRhHc1vQ8M" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
        """, unsafe_allow_html=True)
