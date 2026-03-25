import os

filepath = r'c:\Users\Kaike\Documents\projetos-pessoais\portfolio\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    '<html lang="pt-BR">': '<html lang="en">',
    '<title>Kaike Rodrigues — Portfólio</title>': '<title>Kaike Rodrigues — Portfolio</title>',
    'content="Portfólio de projetos pessoais de Kaike Rodrigues. Desenvolvedor com projetos em Python, JavaScript, HTML/CSS e mais."': 'content="Personal projects portfolio of Kaike Rodrigues. Developer with projects in Python, JavaScript, HTML/CSS and more."',
    'content="Kaike Rodrigues — Portfólio"': 'content="Kaike Rodrigues — Portfolio"',
    'content="Portfólio de projetos pessoais — Python, JavaScript, HTML/CSS e mais."': 'content="Personal projects portfolio — Python, JavaScript, HTML/CSS and more."',
    '<li><a href="#inicio">Início</a></li>': '<li><a href="#inicio">Home</a></li>',
    '<li><a href="#sobre">Sobre</a></li>': '<li><a href="#sobre">About</a></li>',
    '<li><a href="#projetos">Projetos</a></li>': '<li><a href="#projetos">Projects</a></li>',
    '<li><a href="#contato">Contato</a></li>': '<li><a href="#contato">Contact</a></li>',
    '<p class="hero__greeting">👋 Olá, eu sou</p>': '<p class="hero__greeting">👋 Hi, I am</p>',
    '<p class="hero__title"><span class="gradient-text">Desenvolvedor</span> apaixonado por tecnologia</p>': '<p class="hero__title"><span class="gradient-text">Developer</span> passionate about technology</p>',
    'Crio projetos pessoais para explorar novas ferramentas, linguagens e conceitos.\n          Aqui você encontra uma coleção dos meus trabalhos — de scripts e landing pages a aplicações completas.': 'I create personal projects to explore new tools, languages, and concepts.\n          Here you will find a collection of my work — from scripts and landing pages to full applications.',
    'Ver Projetos\n': 'View Projects\n',
    'Contato\n': 'Contact\n',
    '<span class="section-label">Sobre mim</span>': '<span class="section-label">About me</span>',
    '<h2 class="section-title">Transformando ideias em <span class="gradient-text">código</span></h2>': '<h2 class="section-title">Transforming ideas into <span class="gradient-text">code</span></h2>',
    'Sou um desenvolvedor que adora criar projetos no meu tempo livre. Este espaço reúne meus experimentos e aplicações,\n            servindo como um portfólio prático onde demonstro minhas habilidades e interesses em diferentes áreas da tecnologia.': 'I am a developer who loves creating projects in my spare time. This space gathers my experiments and applications,\n            serving as a practical portfolio where I demonstrate my skills and interests in different areas of technology.',
    'Cada projeto é uma oportunidade de aprender algo novo — seja uma nova linguagem, um framework diferente,\n            ou uma abordagem criativa para resolver problemas. Explore, clone e se inspire!': 'Each project is an opportunity to learn something new — whether it\'s a new language, a different framework,\n            or a creative approach to solve problems. Explore, clone, and get inspired!',
    '<div class="stat__label">Projetos</div>': '<div class="stat__label">Projects</div>',
    '<div class="stat__label">Tecnologias</div>': '<div class="stat__label">Technologies</div>',
    '<div class="stat__label">Curiosidade</div>': '<div class="stat__label">Curiosity</div>',
    '<span class="section-label">Tecnologias</span>': '<span class="section-label">Technologies</span>',
    '<span class="section-label">Portfólio</span>': '<span class="section-label">Portfolio</span>',
    '<h2 class="section-title">Meus <span class="gradient-text">Projetos</span></h2>': '<h2 class="section-title">My <span class="gradient-text">Projects</span></h2>',
    'alt="Simulador de Cartão de Crédito"': 'alt="Credit Card Simulator"',
    '<h3 class="project-card__title">Simulador de Cartão de Crédito</h3>': '<h3 class="project-card__title">Credit Card Simulator</h3>',
    'Simulação de gerenciamento de cartão via terminal com interface colorida e interativa. Inclui compras por categoria, extrato detalhado e regras de aumento de limite.': 'Terminal-based credit card management simulation with a colorful and interactive interface. Includes purchases by category, detailed statement, and limit increase rules.',
    'Ver projeto\n': 'View project\n',
    'alt="Sistema de Análise de Vendas"': 'alt="Sales Analysis System"',
    '<h3 class="project-card__title">Sistema de Análise de Vendas</h3>': '<h3 class="project-card__title">Sales Analysis System</h3>',
    'Dashboard web para gerenciar e analisar vendas com métricas automáticas, filtros, cadastro e API REST completa.': 'Web dashboard to manage and analyze sales with automatic metrics, filters, registration, and complete REST API.',
    'Carrossel interativo com diferentes versões do Homem-Aranha. Animações dinâmicas, trocas de imagem e textos informativos.': 'Interactive carousel with different versions of Spider-Man. Dynamic animations, image swaps, and informative texts.',
    'Card de produto elegante para um "Morning Set" de café e cookies, com design limpo e moderno usando tipografia Inter.': 'Elegant product card for a coffee and cookies "Morning Set", with a clean and modern design using Inter typography.',
    'Clone simplificado da interface da Apple com foco em layout limpo, tipografia característica e seções de produto como o iPhone 14.': 'Simplified clone of the Apple interface focusing on clean layout, characteristic typography, and product sections like the iPhone 14.',
    'alt="Login Minimalista"': 'alt="Minimalist Login"',
    '<h3 class="project-card__title">Login Minimalista</h3>': '<h3 class="project-card__title">Minimalist Login</h3>',
    'Tela de login moderna e minimalista com interface limpa e responsiva, utilizando Boxicons para ícones.': 'Modern and minimalist login screen with clean and responsive interface, using Boxicons for icons.',
    '<span class="section-label">Contato</span>': '<span class="section-label">Contact</span>',
    '<h2 class="section-title">Vamos <span class="gradient-text">conversar?</span></h2>': '<h2 class="section-title">Let\'s <span class="gradient-text">talk?</span></h2>',
    'Se tiver alguma dúvida, sugestão ou quiser bater um papo sobre tecnologia,\n          pode me encontrar nos canais abaixo.': 'If you have any questions, suggestions, or want to chat about technology,\n          you can find me on the channels below.',
    '© 2025 <span>Kaike Rodrigues</span>. Feito com 💜': '© 2025 <span>Kaike Rodrigues</span>. Made with 💜',
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Translation script executed successfully.")
