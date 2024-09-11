import streamlit as st

import streamlit as st

def run():
    st.subheader("Contato")

    st.write("Para entrar em contato, por favor, envie um e-mail para: [brunomesilvads@gmail.com](mailto:brunomesilvads@gmail.com)")
    st.write("Ou me siga nas redes sociais:")

    # LinkedIn
    linkedin_url = "https://www.linkedin.com/in/bruno-melo-223817125/"
    st.markdown(f'<a href="{linkedin_url}" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="24"/> LinkedIn: @Bruno Melo</a>', unsafe_allow_html=True)

    # Instagram
    instagram_url = "https://www.instagram.com/datasciencebm/"
    st.markdown(f'<a href="{instagram_url}" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/174/174855.png" width="24"/> Instagram: @DataScienceBM</a>', unsafe_allow_html=True)

    # YouTube
    youtube_url = "https://www.youtube.com/@DataScienceBM"
    st.markdown(f'<a href="{youtube_url}" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/174/174883.png" width="24"/> YouTube: @DataScienceBM</a>', unsafe_allow_html=True)

    # WhatsApp
    whatsapp_url = "https://wa.me/61991744560"
    st.markdown(f'<a href="{whatsapp_url}" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/733/733585.png" width="24"/> WhatsApp: (61) 9 9174-4560 </a>', unsafe_allow_html=True)

    # GitHub
    github_url = "https://github.com/BrunoMeloSlv"
    st.markdown(f'<a href="{github_url}" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/733/733609.png" width="24"/> GitHub: @BrunoMeloSlv</a>', unsafe_allow_html=True)

if __name__ == "__main__":
    run()
