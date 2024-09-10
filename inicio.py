import streamlit as st
from PIL import Image, ImageDraw

def run():

    # Função para arredondar a imagem
    def make_rounded(image):
        image = image.convert("RGBA")
        mask = Image.new('L', image.size, 0)
        draw = ImageDraw.Draw(mask)
        width, height = image.size
        radius = min(width, height) // 2
        center = (width // 2, height // 2)
        draw.ellipse([center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius], fill=255)
        mask = mask.convert("L")
        rounded_image = Image.new("RGBA", image.size)
        rounded_image.paste(image, (0, 0), mask=mask)
        return rounded_image

    # Carrega a imagem e aplica a função para torná-la arredondada
    image = Image.open('https://github.com/BrunoMeloSlv/portifolio/blob/main/BrunoMelo.JPG?raw=true')
    rounded_image = make_rounded(image)

    # Exibe a imagem arredondada
    st.image(rounded_image, caption="Bruno Melo", use_column_width=False, width=150)
    st.title("Portfólio de Análise de Dados")
    st.write("""
    Sou Bruno Melo, Especialista em Data Science e Power BI, com uma jornada que combina formação acadêmica de excelência e experiência prática para transformar dados em soluções estratégicas e impactantes.

    🎲 Formação de Excelência:

    Mestrando no Programa de Pós-graduação em Informática na UFPR: Explorando novas fronteiras da ciência dos dados e da inteligência artificial.
    MBA em Data Science e Analytics pela USP (2022-2023)
    Pós-graduação em Administração de Banco de Dados pela Faculdade Anhanguera (2021-2022)
    Pós-graduação em Gestão de Negócios pela Faculdade Descomplica (2019-2020)
    Graduação em Ciências Atuariais pela Universidade Federal de Sergipe (2013-2019)

    🎲 Experiência Profissional:

    Analista de Dados na Skymail (2024): Transformando dados em soluções estratégicas que geram resultados tangíveis.
    Coordenador de BI na Rockfeller (2024): Liderando equipes e soluções estratégicas que geram resultados tangíveis com eficiência e precisão.
    Analista de Dados na SD Conecta (2024): Transformando dados em soluções estratégicas que geram resultados tangíveis.
    Coordenador de Cadastro e Contribuições no Postalis (2021-2024): Liderando equipes e otimizando processos para alcançar eficiência e precisão.
    Analista de Dados Socioeconômicos na Prefeitura Municipal de Aracaju (2018-2021): Estruturando e analisando dados para o Observatório Social, contribuindo para políticas públicas eficazes.
    Atuário no Hospital de Olhos de Sergipe (2017-2018): Aplicando ciência atuarial para decisões informadas e fundamentadas.
    🎲 Compartilhamento de Conhecimento:

    Professor de Power BI e Ciência de Dados: Oferecendo mentoria e conteúdo educativo no meu canal no YouTube Bruno Melo - YouTube.
    Autor do livro "Explorando Além dos Gráficos: Recursos Avançados e Truques no Power BI" disponível na Amazon.

    🎲 Habilidades e Projetos:

    Softwares e Ferramentas (linguagens): SPSS, Power BI (expert), R, Python, SQL
    Bases de Dados: Microdados do Censo Demográfico, PNAD
    Análise de Dados: Indicadores educacionais, CAGED, ENEM

    🎲 De Aracaju para o Mundo: 

    Sou natural de Aracaju, Sergipe, a charmosa cidade que também é conhecida como a "Suíça Brasileira" devido ao seu clima ameno, chocolates deliciosos, alta qualidade de vida e o irresistível caranguejo. Minha terra natal inspira minha abordagem ao trabalho e à vida, combinando o calor humano com a precisão dos dados.
    """)
