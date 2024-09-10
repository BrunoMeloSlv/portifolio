### Portfólio - Bruno Melo

Este é o código-fonte do aplicativo de portfólio desenvolvido em Streamlit, que apresenta minha trajetória como Especialista em Data Science e Power BI, além de projetos e experiências profissionais relacionadas à análise de dados. O app é uma forma interativa de visualizar meu portfólio, contendo seções como "Início", "Projetos", "Vídeos", "Dashboards" e "Contato".

#### Funcionalidades
Início: Apresenta uma introdução com um resumo da minha formação, experiência profissional e habilidades em análise de dados.
Projetos: Lista detalhada de projetos já realizados na área de ciência de dados e business intelligence.
Vídeos: Conteúdo de vídeos educativos disponíveis no meu canal do YouTube sobre análise de dados.
Dashboards: Exibição de dashboards interativos desenvolvidos para análise e visualização de dados.
Contato: Informações para entrar em contato e links para minhas redes sociais.

#### Tecnologias Utilizadas

Python
Streamlit: Para a criação do front-end interativo.
Pillow (PIL): Para manipulação de imagens e criação de imagens com bordas arredondadas.
Requests: Para carregar a imagem de forma dinâmica a partir de uma URL externa.
Como Executar o Projeto
Clone este repositório:


Copiar código
git clone https://github.com/BrunoMeloSlv/portifolio.git

Instale as dependências necessárias:


Copiar código
pip install -r requirements.txt
Execute o aplicativo localmente:


Copiar código
streamlit run app.py
Acesse o aplicativo em https://brunomelo.streamlit.app/ no seu navegador.

Imagem de Perfil Arredondada
Uma das características interessantes deste projeto é o uso de uma função que arredonda a imagem de perfil. Isso é feito utilizando a biblioteca Pillow para criar uma máscara circular sobre a imagem e, assim, exibi-la de forma estilizada.

Contribuições
Sinta-se à vontade para abrir issues e enviar pull requests com melhorias ou correções. Toda contribuição é bem-vinda!
