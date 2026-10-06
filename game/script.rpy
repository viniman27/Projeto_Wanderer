# The script of the game goes in this file.

init python:
    dinheiro       = False
    amoras         = False
    espelho        = False
    chave_cobre    = False
    escova_cabelo  = False
    vidro_ungento  = False
    aranha_garrafa = False
    velo_ouro      = False
    sabe_senha     = False
    essencia_porco = False
    morte_goblins  = False

define flash = Fade(.25, 0, .75, color="#fff")
transform flip:
    xzoom -1.0

init python:
    credits1 = ('Wanderer é uma produção grupo 7', 'UNB FGA'), ('PO(product owner)','André Corrêa'), ('Scrum master', 'João Pedro de Camargo Vaz'), ('Scrum team', 'Vinicius Assumpção'), ('Scrum team', 'César Umeda'),('Scrum team', 'Gabriel Roger'),('Artista Responsável', '@qEROsene'), ('Direção de arte', 'Dartmol203'), ('Direção de arte', 'Viniman27'), ('Edição', 'Cesarheroyuki')
    credits2 = ('formatação', 'Djonga'), ('formatação', 'Roger'), ('agradecimento ao material fornecido por', 'Editora Marques Saraiva'), ('agradecimento ao material fornecido por', 'GDC game audio'), ('agradecimento ao material fornecido por', "Ren'py engine"), ('agradecimento ao material fornecido por', 'Breaking Copyrights'), ('agradecimento ao material fornecido por', 'netFontes'), ('agradecimento ao material fornecido por', 'pngWing'), ('agradecimento ao material fornecido por', 'Fantasy Background Music'), ('agradecimento ao material fornecido por', 'Rush Garcia'), ('agradecimento ao material fornecido por', 'Hiroyuki Sawano')
    credits3 = ('E um muito obrigado a todos que participaram da beta aberta!', 'MARIANAR GAMER'), ('E um muito obrigado a todos que participaram da beta aberta!', 'Katsuia'), ('E um muito obrigado a todos que participaram da beta aberta!', 'quEROSene'), ('E um muito obrigado a todos que participaram da beta aberta!', 'Mikkhaelll'), ('E um muito obrigado a todos que participaram da beta aberta!', 'Pedro Henrique Elias Pereira'), ('E um muito obrigado a todos que participaram da beta aberta!', 'Neeko'), ('E um muito obrigado a todos que participaram da beta aberta!', 'HeregeD'), ('E um muito obrigado a todos que participaram da beta aberta!', 'Gabrielle'), ('E um muito obrigado a todos que participaram da beta aberta!', 'O Bram'), ('E um muito obrigado a todos que participaram da beta aberta!', 'Felpeldel')
    credits4 = ('E um muito obrigado a todos que participaram da beta aberta!', '(GS) Luw'), ('E um muito obrigado a todos que participaram da beta aberta!', 'Alamux'), ('E um muito obrigado a todos que participaram da beta aberta!', 'Akaeboshi'), ('E um muito obrigado a todos que participaram da beta aberta!', 'lulinha'), ('E um muito obrigado a todos que participaram da beta aberta!', 'Milton'), ('E um muito obrigado a todos que participaram da beta aberta!', 'Ada Amaris'), ('E um muito obrigado a todos que participaram da beta aberta!', 'Isabella'), ('E um muito obrigado a todos que participaram da beta aberta!', 'Srta Fooshang'), ('E um muito obrigado a todos que participaram da beta aberta!', 'Flávio'), ('E um muito obrigado a todos que participaram da beta aberta!', 'ITZdeath')
    credits5 = ('E um muito obrigado a todos que participaram da beta aberta!', 'Caio26'), ('E um muito obrigado a todos que participaram da beta aberta!', 'Furyjoker'), ('E um muito obrigado a todos que participaram da beta aberta!', 'Lucas Soares'), ('E um muito obrigado a todos que participaram da beta aberta!', 'Manuzini'), ('E um muito obrigado a todos que participaram da beta aberta!', 'Lucas Rodrigues Lopes'), ('E um muito obrigado a todos que participaram da beta aberta!', 'XXX_Lima_XXX'), ('E um muito obrigado a todos que participaram da beta aberta!', '404SkillNotFound'), ('E um muito obrigado a todos que participaram da beta aberta!', 'impunky_e'), ('E um muito obrigado a todos que participaram da beta aberta!', 'Nabiki'), ('E o autor que tornou esse projeto possivel', 'Steve Jackson')
    credits_s = "{size=80}Créditos\n\n"
    c1 = ''
    for c in credits1:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    for c in credits2:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    for c in credits3:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    for c in credits4:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    for c in credits5:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=60}Ren'py\n7.4.4.1239" #Don't forget to set this to your Ren'py version

init:
    image cred   = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}O Fim!", text_align=0.5)
    image thanks = Text("{size=80}obrigado por jogar!", text_align=0.5)

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n               = Character("narrador")
define mc              = Character("Mago")
define l               = Character("Lucretia")
define b               = Character("Balthus")
define V               = Character("Viniman, arauto da criação")
define A               = Character("Dartmol, arauto da destruição")
define U               = Character("???")
define a2              = Character("Os arautos")

image Mapa = "images/Mapa.png"

## personagens
image mc normal        = "images/mc a.png"
image mc bombado       = "images/mc.png"
image mc invertido     = "images/mc invertido.png"
image guarda1          = "images/mamaco.png"
image guarda2          = "images/lobinho2.png"
image gremlim1         = "images/gremlim1.png"
image tentaculo        = "images/tentaculos.png"
image hydra            = "images/hydra.png"
image hydra_shiny      = "images/hydra shiny.png"
image homem1           = "images/homem1.png"
image homem2           = "images/homem2.png"
image goblin1          = "images/goblin1.png"
image goblin2          = "images/goblin2.png"
image orquisa          = "images/orca.webp"
image anao             = "images/anao.png"
image velha            = "images/velha.png"
image porteiro         = "images/PW minotauro.png"
image oseamus          = "images/duende.png"
image cobra_esgoto     = "images/cobra.png"
image pedroso          = "images/pedra.png"
image morena           = "images/morena.png"
image morena 2         = "images/PW succubus4.png"
image goblins          = "images/Goblin_Troop.png"
image mordomo          = "images/mordomo macabro.png"
image gark             = "images/gark.png"
image bibliotecario    = "images/bibliotecario.png"
image orcs             = "images/orcs.png"
image maguito          = "images/maguito.png"
image leviata          = "images/leviata.png"
image heitoba          = "images/heitoba.png"
image calacorm         = "images/calacorm.png"
image balthus normal   = "images/balthus.png"
image balthus bombado  = "images/balthus 2.png"
image morte_balthus1   = "images/morte_balthus1.png"
image morte_balthus2   = "images/morte_balthus2.png"
image morte_balthus3   = "images/morte_balthus3.png"
image morte_balthus4   = "images/morte_balthus4.png"
image morte_balthus5   = "images/morte_balthus5.png"
image morte_balthus6   = "images/morte_balthus6.png"
image morte_balthus7   = "images/morte_balthus7.png"
image morte_balthus8   = "images/morte_balthus8.png"
image morte_balthus9   = "images/morte_balthus9.png"
image morte_balthus10  = "images/morte_balthus10.png"
image morte_balthus11  = "images/morte_balthus11.png"
image morte_balthus12  = "images/morte_balthus12.png"
image morte_balthus13  = "images/morte_balthus13.png"
image morte_balthus14  = "images/morte_balthus14.png"
image morte_balthus15  = "images/morte_balthus15.png"
image ganjee           = "images/ganjee.png"
image giras            = "images/giras.png"
image velha1           = "images/velha1.png"
image velha2           = "images/velha2.png"
image velha3           = "images/velha3.png"
image devlin           = "images/devlin.png"
image cria1            = "images/cria1.png"
image cria2            = "images/cria2.png"
image gargula          = "images/gargula.png"
image gargula_clone    = "images/gargula2.png"
image elfo_negro       = "images/PW elfo negro.png"
image mulher_roupa     = "images/mulher_roupa.png"
image fantasmagorico   = "images/fantasmagorico.png"
image golem_clone      = "images/golem clone.png"
image viniman          = "images/arauto cria.png"
image dartmol          = "images/arauto dest.png"

## backgrounds
image entrada_caos     = "images/PW entrada cidadela.jpg"
image caminho_cidadela = "images/PW campo escuro.jpg"
image cidadela1        = "images/PW cidadela.jpg"
image poco             = "images/fundo-poco.jpg"
image portao           = "images/portao.jpg"
image portao aberto    = "images/portao aberto.png"
image corredor         = "images/corredor.jpg"
image sala_oseamus     = "images/sala oseamus.jpg"
image game_over        = "images/game_over.jpeg"
image templo           = "images/temple.jpg"
image aposento         = "images/PW dentro fortaleza.jpg"
image templo_floresta  = "images/templo floresta.jpg"
image fumaca           = "images/fumaca.jpg"
image bg               = "images/bg.jpg"
image corredor_escuro  = "images/corredor escuro.png"
image esgoto           = "images/esgoto.jpg"
image passagem_esgoto  = "images/passagem esgoto.jpg"
image sala_golem       = "images/rodiney.jpg"
image sala_jantar      = "images/sala de jantar.jpg"
image portais          = "images/portais.jpg"
image quarto_morena    = "images/quarto morena.jpg"
image quarto_goblin    = "images/quarto goblins.jpg"
image bg2              = "images/bg2.jpg"
image bg3              = "images/PW dentro fortaleza3.jpg"
image bg5              = "images/bg5.jpg"
image biblioteca       = "images/biblioteca.jpg"
image salao            = "images/PW dentro fortaleza4.jpg"
image prisao           = "images/prisao.jpg"
image topo_torre       = "images/topo da torre.jpg"
image arena_final1     = "images/PW arena final.jpg"
image arena_final2     = "images/campo etereo.jpg"
image fim_sub          = "images/submissao.jpg"
image fim_lorde        = "images/trono lorde do caos.jpg"
image fim_alvor        = "images/alvorecer.jpg"
image escada           = "images/escadas.jpg"
image quarto_escuro    = "images/escuro.jpg"
image tutorial1        = "images/Tutorial Wanderer 1.png"
image tutorial2        = "images/Tutorial Wanderer 2.png"
image tutorial3        = "images/Tutorial Wanderer 3.png"
image tutorial4        = "images/Tutorial Wanderer 4.png"
image quarto_hydra     = "images/quarto hydra 3.jpg"
image entrada_balthus  = "images/original.jpg"
image bg6              = "images/bg6.jpg"
image bg7              = "images/bg7.jpg"
image bg8              = "images/bg8.jpg"
image bg9              = "images/bg9.jpg"
image bg10             = "images/bg10.jpg"
image bg11             = "images/bg11.jpg"
image bg12             = "images/bg12.jpg"
image sala_gargula     = "images/sala estatuas.jpg"
image bg13             = "images/porta adega.jpg"
image bg14             = "images/bg14.png"
image bg15             = "images/lava-roupa.jpg"
image criacao          = "images/criacao.jpg"
image destruicao       = "images/destruição.jpg"
image arautos          = "images/2 arautos.png"
image casa_prota       = "images/casa.jpg"
image creditos         = "images/creditos/creditos.png"

# The game starts here.

label start:

    stop music

    play music "musics/tutorial.mp3"

    scene tutorial1 at truecenter:
        zoom 1.3
    window hide
    $renpy.notify("clique na tela!")
    pause 7
    scene tutorial2 at truecenter:
        zoom 1.3
    window hide
    pause
    scene tutorial3 at truecenter:
        zoom 1.3
    window hide
    pause
    $renpy.notify("notificação exemplo!")
    scene tutorial4 at truecenter:
        zoom 1.3
    window hide
    pause

    $nome = renpy.input("Qual é o seu nome?")
    $Protagonista1 = nome

    play music "musics/inicio_epico.mp3" fadein 1
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene Mapa

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.

    n "O ordeiro e generoso povo do Vale dos Salgueiros vive há oito anos sob o terror e medo do
    feiticeiro Balthus Dire."

    n "Terror, porque o poder dele é realmente aterrorizante,  e medo causados
    pela notícia que acabou chegando aos ouvidos desse povo, vinda dos domínios do feiticeiro, de que
    seus ambiciosos planos de conquista começariam pelo próprio Vale."

    n "Um fiel Semi-Elfo enviado em uma missão de espionagem à Torre Negra voltou galopando para o
    Vale há três dias com uma mensagem desesperada."

    n "Do interior das cavernas de Rocha Escarpada,
    Balthus Dire tinha recrutado um exército de Caóticos e se preparava para atacar com eles o Vale
    dentro de uma semana."

    n "O bom Rei Salamon era um homem de ação. Foram enviados mensageiros por todo o Vale no
    mesmo dia para preparar as defesas e convocar os homens para a guerra."

    n "Foram enviados também cavaleiros à Grande Floresta de Yore para avisar aos Semi-Elfos que moravam lá e fazer um apelo
    para que se aliassem às forças. O Rei Salamon era também um homem sábio."

    n "Ele sabia muito bem que as notícias inevitavelmente chegariam aos ouvidos do Grande Mago de Yore, um mestre da
    magia branca de grandes poderes, que vivia nas profundezas da floresta. O mago era velho e não
    resistiria a uma batalha destas proporções."

    n " Mas ele havia ensinado suas artes a vários jovens magos, e talvez um de seus discípulos de magia ajudasse o rei e seus súditos com coragem e ambição."

    show mc normal at center:
        zoom 0.6
    with dissolve

    n "Você é o aluno brilhante do Grande Mago de Yore. Ele tem sido um Mestre duro, e sua própria
    impaciência muitas vezes foi mais forte do que você. Talvez um pouco precipitadamente, você
    partiu de imediato para a corte de Salamon. O rei recebeu-o entusiasticamente e explicou seu plano."

    n "A batalha poderia ser evitada sem derramamento de sangue se Balthus fosse assassinado antes que
    seu exército pudesse ser reunido."

    n "A missão que você tem pela frente é extremamente perigosa. Balthus Dire está cercado, em sua  Cidadela,
    por uma multidão de criaturas assombrosas. Embora a Magia seja a sua arma mais forte,  haverá momentos em que você terá que confiar em sua espada para sobreviver."

    n "O Rei Salamon expôs a você como seria a sua missão e o advertiu dos perigos que estavam à sua  frente.
    Há um caminho melhor para atravessar a Cidadela. Se você o descobrir, terá êxito com um  mínimo de risco para a sua pessoa.
    Talvez você precise de várias viagens para descobrir o caminho  mais fácil para atravessar a Cidadela"

    n "antes da sua saida, o rei te chama e entrega um saco de couro com um punhado de moedas de ouro para auxiliar na sua jornada."

    $renpy.notify("adquiriu dinheiro!")

    play sound "musics/efeito_sonoro/item encontrado.mp3"

    n "Você deixa o Vale dos Salgueiros na longa caminhada para a Torre Negra. No sopé da colina de  Rocha Escarpada,
    você pode ver sua silhueta contra o céu escuro... "

    $dinheiro = True

    if (nome == 'caçador de arautos' or nome == 'CAÇADOR DE ARAUTOS'):
        jump final_alt

    jump um

    return

label um:

    hide Mapa
    hide mc

    play music "musics/Keys of Moon - Enchanted.mp3"

    scene caminho_cidadela:
        zoom 1.5

    n "O sol se põe. Enquanto o crepúsculo se transforma em escuridão, você começa a subir a colina na  direção da ameaçadora forma que se desenha contra o céu noturno.
    A Cidadela fica a menos de uma  hora de escalada."

    n "A uma certa distância de seus muros, você pára para descansar - um erro, uma vez que, dessa  posição, ela parece um espectro medonho do qual não se pode escapar.
    Os cabelos no seu pescoço  se arrepiam enquanto você a observa."

    n "Mas você se envergonha de seus medos. Com inflexível decisão, você marcha adiante na direção do  portão principal, onde você sabe que encontrará guardas à sua espera.
    Você considera suas opções. "

    n " Já pensou em se apresentar como um especialista em plantas medicinais que veio tratar de um  guarda com febre. Poderia também se dizer um comerciante ou artesão talvez um carpinteiro.
    Poderia até mesmo ser um nômade que buscasse abrigo para a noite."

    scene entrada_caos:
        zoom 1.8

    n "Enquanto você pondera as possibilidades, e as histórias que terá que contar aos guardas, acaba  chegando à trilha principal que conduz aos portões.
    Duas lanternas brilham em cada um dos lados da porta levadiça. "

    play sound "musics/efeito_sonoro/macacor.mp3" volume 0.6

    show guarda1 at left:
        zoom 1.3
    with dissolve

    n "Você ouve grunhidos abafados ao se aproximar, e vê duas criaturas de aparência absurda. Do lado  esquerdo está uma criatura horrível, um grande macaco,
    flexionando seus braços fortíssimos."

    play sound "musics/efeito_sonoro/lobor.mp3"

    show guarda2 at right:
        zoom 0.9
    with dissolve

    n "Do outro lado, encontra-se de fato o seu oposto, um cachorro grande. Este último guarda se aproxima nas suas quatro  patas.
    Para a alguns metros de distância diante de você, ergue-se sobre as patas traseiras e dirige a  palavra a você. "

    n "Por qual das histórias você optará?"

    menu:
        "Você se apresentará como um especialista
        em plantas medicinais?":
            jump dois61
        "Você dirá que é um comerciante?":
            jump dois30
        "Você pedirá abrigo para pernoitar?":
            jump dois0

label dois61:
    n "O Macaco e o Cachorro pedem para ver as suas ervas. Por sorte, você tinha apanhado alguns punhados de ervas no caminho, e você mostra isso a eles."

    n "Inclinando a cabeça para um lado, as criaturas olham para você com desconfiança.
    Perguntam a você então o nome do guarda que veio tratar, uma coisa que não estava nos seus planos!"

    n "Você pensa rapidamente em um nome para enganar a criatura:"
    menu:
        "Kylltrog":
            jump oito1
        "Pincus":
            jump um75
        "Blag":
            jump tres94

label oito1:
    n "O Macaco e o Cachorro riem e dizem a você que Kylltrog é um preguiçoso que não serve para nada, e que não vale a pena salvá-lo.
    Você solta um suspiro de alívio quando eles caminham de volta e gritam para chamar o porteiro.
    Alguns momentos depois, o porteiro aparece e abre uma pequena porta para deixar você entrar."
    jump dois51

label um75:
    n "As criaturas nunca ouviram falar de nenhum Pincus no interior da Cidadela. O Cachorro que está segurando a clava rosna e dá um passo adiante."
    menu:
        "Escolher outro nome rapidamente (Teste de sorte)":
            jump um10
        "Lutar contra eles":
            jump dois88

label um10:

    $ d20roll = renpy.random.randint(1, 20)

    if (d20roll>= 10):
        $renpy.notify("sucesso de sorte")
        play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
        n "Você obteve sucesso para falar outro nome conhecido pelos guardas, e o porteiro permitiu a sua passagem."
        jump dois51

    else:
        $renpy.notify("fracasso de sorte")
        play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
        n "Você não teve sorte e terá que lutar contra os guardas."
        jump dois88

label tres94:
    n "As criaturas se olham, como se o nome não fosse estranho para eles, mas elas não conseguiram se lembrar exatamente de onde o conheciam.
    Você rapidamente acrescenta que ele está na turma do primeiro andar."
    n "Eles dão de ombros e acabam por decidir que você deve estar falando a verdade. O Macaco e o Cachorro chamam o porteiro, que finalmente aparece para deixar você entrar."
    jump dois51

label dois30:
    n "'Veio ganhar algum dinheiro, né?!', diz o Macaco. 'Bem, você pode dividir um pouco dos seus lucros conosco!'"
    n "Como você não tem nada para oferecer a eles:"
    menu:
        "Lançar um Encanto do Ouro dos Tolos sobre uma pedra e oferecer a eles (Teste de sorte)":
            jump nove6

        "Prepare-se para a batalha!":
            jump dois88

label dois0:

    n "O Macaco-Cachorro diz que não é permitido a ninguém entrar na Torre Negra depois que anoitece
    você terá que procurar abrigo em outro lugar."


    n "Você pode se resignar a lutar. Ou pode pegar uma pedra e lançar um Encanto do Ouro dos Tolos sobre ela, oferecendo-a como uma pepita
    de ouro, para suborná-los, convencendo-os a deixar você entrar"
    menu teste:
        "se preparar para lutar?":
            jump dois88
        "tentar suborno? ":
            if dinheiro:
                jump suborno
            else:
                $renpy.notify("você não possui esse item!")
                play sound "musics/efeito_sonoro/nao tem o item.mp3"
                jump teste
        "usar encanto? (teste de sorte)":
            jump nove6

label dois88:

    n "os guardas avançam em sua direçao!"

    play music "musics/Makai Symphony - Dragon Castle.mp3"
    #with fade

    jump batalha_guardas

label suborno:
    n "os guardas regojizam-se com o pequeno punhado de moedas de ouro que você entregou e o deixam passar"

    $renpy.notify("dinheiro retirado!")

    play sound "musics/efeito_sonoro/item perdido.mp3"

    jump dois51

label nove6:

    play sound "musics/efeito_sonoro/dados.mp3"

    $ d201roll = renpy.random.randint(1, 20)

    if (d201roll>=12):
        $renpy.notify("sucesso de sorte")
        play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
        n "Eles aceitam a sua oferta e convocam o porteiro, que abre uma pequena porta dentro da porta
        levadiça para deixar você entrar. Você os deixa discutindo por causa da pepita de ouro."
        jump dois51
    else:
        $renpy.notify("fracasso de sorte")
        play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
        n "os guardas nao caem na ilusão e partem em sua direção prontos para lutar"
        jump dois88

label dois51:

    play music "musics/yt1s.com - Magic Fantasy Music  The Mystic  Beautiful Violin.mp3"

    scene cidadela1:
        zoom 1.0

    n "Você caminha em frente, entrando em um pátio aberto e espaçoso, circundado por grandes muros.
    Há várias tochas queimando, e grupos de figuras se movimentam na escuridão."

    n "Há um monumento de algum tipo no centro do pátio - talvez uma fonte. Olhando para o outro lado do pátio, você
    consegue ver o que parece ser a entrada principal da torre. Você:"

    menu:
        "Esgueira-se pela parede na direção da torre, contornando o pátio?":
            jump um4
        "Caminha decididamente, atravessando o pátio? ":
            jump um79
        "Vai na ponta dos pés pelas sombras, na direção de um dos grupos? ":
            jump tres21

label um79:
    stop music
    play music "musics/sb_phoenix.mp3"
    n "Quando você sai das sombras na direção do centro do pátio, uma voz no vento grita: 'Pare! Fique onde está!'
    Você olha a sua volta, mas não consegue ver ninguém que esteja se dirigindo a você."
    n "Você dá mais dois passos. A voz sinistra ordena de novo que você pare, e, dessa vez, uma flecha zune pelo ar e cai próximo ao seu pé esquerdo.
    Você pula para trás. Porém, ainda assim não vê ninguém e não pode se mexer."
    n "Dessa forma, você: "
    menu:
        "Seguirá adiante, muito cuidadosamente":
            jump tres78
        "Disparará na direção do monumento no meio do pátio":
            jump um25
        "Lançará um Encanto do Escudo à sua volta e seguirá avançando":
            jump tres41

label um25:
    n "Quando você começa a correr, três flechas partem em sua direção, vindas de nenhum lugar, testando a sua sorte."
    $ d202roll = renpy.random.randint(1, 20)

    if (d202roll>= 14):
        $renpy.notify("sucesso de sorte")
        play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
        n "Você foi muito sortudo e todas as flechas não o acertaram, e, com isso, conseguiu chegar ileso sob a cobertura do monumento."
        jump dois09

    else:
        $renpy.notify("Fracasso de sorte")
        play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
        n "Ao correr, uma das flechas o acertou no ombro ao chegar atrás do monumento. Assim você descansa por uns minutos para se recuperar do ferimento."
        play sound "musics/efeito_sonoro/gemido-combate.mp3"
        jump dois09

label tres41:
    n "Você lança o Encanto em torno de si mesmo e avança. Quatro ou cinco flechas voam em sua direção, mas param no ar a um metro de distância antes de te atingirem, caindo inofensivamente
    no chão."
    n "Dessa forma, você consegue chegar atrás do monumento ileso."
    jump dois09

label tres78:
    n "Você dá alguns passos adiante, e uma outra flecha erra por pouco o seu pé."
    n "Mais uns poucos passos e uma flecha rasga a sua túnica, arranhando o seu antebraço.
    Você ainda não consegue ver ninguém, nem de onde as flechas estão vindo."
    n "Depois de alguns passos, surge mais uma flecha, mas essa rasga a sua perna. Você grita alto"
    play sound "musics/efeito_sonoro/gemido-combate.mp3"
    scene templo at truecenter:
        zoom 1.3
    n "Como você já estava perto do monumento, dá um salto para frente e se esconde atrás dele até as flechas pararem de vir."
    jump dois09

label dois09:
    scene templo at truecenter with fade:
        zoom 1.3
    n "Você pousa os olhos sobre a estranha estrutura. Não parece ser uma fonte, mas alguma espécie de templo, em que você:"
    menu:
        "Verá uma porta, de um lado, e poderá investigar":
            jump tres62
        "Poderá seguir em frente para a Cidadela propriamente dita.":
            jump um56

label tres62:
    scene aposento at truecenter:
        zoom 1
    show gremlim1 at center:
        ypos 1000
        zoom 0.7

    play sound "musics/efeito_sonoro/gremlin.mp3"


    n "A porta abre, e o pequeno aposento no interior é iluminado a luz de vela. Cautelosamente, você olha lá para dentro e vê uma cena estranha.
    Sobre uma mesa de madeira no canto do aposento, há três recipientes, cada um contendo um líquido de cor diferente: um claro, outro vermelho e outro leitoso."
    n "Há uma pequena criatura alada, semelhante a gremlin, que está em torno da mesa, chilreando excitadamente.
    De vez em quando, ele vai para a mesa e toma um gole do líquido leitoso."
    n "A porta aberta range nas dobradiças e assusta o ser. Ele dá uma volta para olhar você e fica muito excitado. Com isso, você:"

    menu:
        "Pode entrar no cômodo":
            jump cinco8
        "Fechar a porta rapidamente e prosseguir em direção à Cidadela":
            hide aposento with fade
            jump um56

label cinco8:
    "Quando você entra, o Gremlin esvoaça e guincha excitado, depois voa, passando por você e saindo pela porta noite adentro. Você agora está sozinho
    com os recipientes. Arriscará beber algum?"
    #hide gremlim1
    #hide gremlim2
    #hide gremlim3
    menu:
        "O líquido claro":
            jump dois98
        "O líquido vermelho":
            jump dois67
        "O líquido leitoso":
            jump nove2
        "Caso não, prosseguirá na direção da Cidadela":
            hide aposento with fade
            jump um56

label um56:
    #hide aposento with fade
    #hide gremlim1 with fade
    #hide gremlim2 with fade
    #hide gremlim3 with fade
    scene templo_floresta at truecenter with dissolve:
        zoom 2.7
    show mc normal at left:
        zoom 0.6
    with fade

    show tentaculo at right with dissolve:
        zoom 0.8
        ypos 1050

    n "Enquanto você caminha pelo pátio ao ar livre, repara que está andando ao longo de uma pequena elevação, quase que como um encanamento enterrado que fosse da Torre Negra para o templo."

    n "Você se abaixa para investigar isso, poderia ter sido feito por algum tipo de toupeira?"
    n "Quando você toca na elevação, ela se retrai e, para seu horror, um longo tentáculo cinzento irrompe do solo
    e se enrosca em torno de sua perna!"
    n "Como você lutará com esta 'coisa'?"
    menu:
        "Desembainhará a sua espada":
            jump sete1
        "Lançará um Encanto da Levitação":
            jump dois84
        "Lançara um Encanto do Fogo":
            jump um14

label dois98:
    n "Quando suas mãos se fecham em torno do cálice, ele começa a efervescer e a espumar, respingando em você quando você o ergue até seus lábios. Você tem certeza de quer experimentar isso?"
    menu:
        "Sim! Estou Determinado!":
            jump um41
        "Acho melhor não, vou tomar uma decisão melhor.":
            jump cinco8

label um41:
    n "O líquido tem um gosto salgado, e você começa a suar frio quando engole. Em seguida, você tem tremores e tenta se aprumar na mesa. Porém, você cai para frente, derrubando os outros dois recipientes
    no chão e derramando os outros líquidos."
    scene fumaca at truecenter with dissolve:
        zoom 4
    n "Você também acaba caindo no chão, sentindo-se extremamente mal e com a visão turva. Como em um sonho, você tem uma visão de uma estranha criatura musculosa várias cabeças,
    uma calda comprida e uma pele de escamas amareladas."
    show hydra at center with pixellate:
        zoom 2.5
        ypos 900
    n "Tem nas mãos um grande molho de chaves. Um rato atravessa a mesa em que ela está sentada e ela grita alto..."
    n "O grito acorda você com um sobressalto e você toma consciência de onde está. Você reúne suas forças e tateia em busca da maçaneta da porta."
    n "Você precisa de ar fresco! Assim, sai da câmara, descansa alguns momentos e parte em direção da Cidadela..."
    hide hydra
    hide fumaca
    hide aposento with fade
    jump um56

label dois67:
    n "Quando você segura o cálice, o líquido fica verde, e depois marrom sujo, diante de seus olhos. Cheira a podre, mas você toma um gole. Com uma careta, você cospe tudo, pois descobriu que é água lamacenta!!"
    n "Você sai da câmara e se dirige à Cidadela."
    hide aposento with fade
    jump um56

label nove2:
    n "O líquido leitoso cheira bem. Você toma um gole e começa a sorrir. Dá um gole maior e explode em gargalhadas, por motivo nenhum!"
    n "Não é de se estranhar que os pequenos Gremlins estivessem gostando tanto. Com a cabeça leve e de bom humorm você sai do aposento para continuar em seu caminho para a Cidadela."
    hide aposento with fade
    jump um56

label sete1:
    n "Você desembainha a espada e vai golpear o tentáculo! O tentáculo tenta te arrastar para o grande buraco que está se abrindo em torno da base dele!"
    jump batalha_tentaculo

label dois84:
    n "Você lança o encanto e começa a sair do chão. O tentáculo não solta, e a dor em sua perna se torna insuportável. Você resolve retornar ao solo antes que a sua perna seja arrancada do corpo."
    n "Você terá que escolher outra maneira de passar pelo tentáculo."
    $encanto_levitacao = False
    menu:
        "Desembainhar a espada e lutar contra o tentáculo":
            jump sete1
        "Lançar um feitiço de fogo":
            jump um14

label um14:
    n "Você aponta para a base do tentáculo e lança o encanto. Um rolo de fumaça e um clarão luminoso irrompem do buraco no solo. Um tremor percorre o tentáculo, e, felizmente, ele afrouxa."
    n "Quando ele retorna para dentro do solom você esfrega sua perna para recuperar a circulação e depois na direção da entrada principal da Cidadela novamente."
    $encanto_fogo = False
    jump dois18

label tres21:
    n "Cautelosamente, e mantendo-se fora da área visível, você se esgueira pelas bordas do pátio na escuridão. Há dois grupos de criaturas à sua frente."
    show homem2 at right:
        zoom 1.2
    show homem1 at center:
        xpos 1300
        zoom 1.9
    n "À direita, você pode ver duas figuras de aparência humana conversando sob uma tocha presa à parede."
    show orquisa at left:
        zoom 1.2
    show anao at left:
        zoom 0.5
        xpos 450
    show goblin1 at left
    show goblin2 at left:
        zoom 0.2
        ypos 1027
    n "À esquerda, um grupo criaturas, de variadas formas e de tamanhos, estão sentados em volta de uma fogueira comendo."
    n "Você irá abordar o grupo da esquerda ou a dupla da direita?"
    menu:
        "Grupo da esquerda":
            jump tres39
        "Dupla da direita":
            jump dois69

label dois69:
    hide orquisa
    hide anao
    hide goblin1
    hide goblin2
    n "Os dois homens estão sujos e maltrapilhos. Quando se aproxima, você pode ouvi-los discutindo em
    voz alta sobre o preço de um punhal. O mais alto deles está obviamente tentando vender o punhal
    para o outro."
    n "Ele argumenta que o punhal é encantado, e vale mais do que o outro está disposto a
    pagar por ele. Quando você chega mais perto, ele pega você pelo braço e pergunta sua opinião sobre
    o preço da arma. O que você dirá:"
    menu:
        "Cinco Peças de Ouro?":
            jump dois05
        "Dez Peças de Ouro?":
            jump dois25

label dois05:
    hide homem1 with fade
    n "O comerciante fica indignado com o baixo preço que você colocou para o punhal dele e desembainha a sua espada, você age da mesma forma e se prepara para a batalha."
    jump batalha_contra_um

label dois25:
    n "Os dois ficam nervosos com o tom que você usa ao falar, e acham que foi muito arrogante. Assim ambos vão te
    ameaçar e você age igualmente. Prepare-se para lutar contra os dois oponentes!"
    jump batalha_contra_dois

label tres39:
    hide homem1 with dissolve
    hide homem2 with dissolve
    n "Há um time eclético sentado em volta do fogo. Uma orquisa está distribuindo magros bocados de carne mal passada para os outros."
    n "Um anão de pele gastada rosna e reclama do tamanho do seu pedaço, enquanto dois globins, homem e mulher, estão se acariciando. Eles riem e se sacodem, e de
    vez em quando ela dá um tapa na cara feia do macho, causando ainda mais risos."
    n "Quando você se aproxima, eles param e olham para você com rostos poucos amigáveis. Olham com desprezo para a sua aparência asseada, e a Globin fêmea
    cochicha algum comentário para seu companheiro."
    n "Na frente do anão você pode ver uma caixa aberta e com dificuldade distingue um frasco de líquido dentro dela."
    n "Dessa forma, você:"
    menu:
        "Sentará com eles em torno do fogo":
            jump um34
        "Perguntará se você pode se unir a eles":
            jump um49

label um34:
    n "Eles ficam admirados com a sua audácia. Ao invés de esperar que eles falem, você age agressivamente e exige saber como entrar na Cidadela. Eles apontam para a entrada principal,
    obviamente um tanto espantados com seu modo confiante e cochicham entre eles."
    n "A orquisa diz a você que será preciso uma senha, 'CIMITARRA', para entrar. Você pergunta a respeito do frasco de líquido dentro da caixa, o que faz com que eles fiquem agitados, então você:"
    $sabe_senha = True
    play sound "musics/efeito_sonoro/item encontrado.mp3"
    $renpy.notify("agora você sabe a senha! mas aonde vai usar?")

    menu:
        "Os pressiona para obter mais informações sobre o frasco":
            jump seis0
        "Segue adiante na direção da Torre Negra":
            jump dois45

label seis0:
    n "As criaturas ficam desconfiadas quando você as pressiona buscando informações. O anão salta rapidamente de pé, brandindo uma clava de madeira, enquanto o goblin
    e a orquisa pegam espadas e olham com raiva de você."
    n "A namorada do goblin grita e recua vários passos, enquanto os outros avançam na sua direção. Você terá que lutar contra eles."
    jump batalha_criaturas

label dois45:

    play music "musics/Savfk - The Travelling Symphony.mp3"

    hide mc normal
    hide anao
    hide orquisa
    hide goblin1

    scene bg at truecenter:
        zoom 2
    n "Você parte na direção da Cidadela. Embora o ar da noite esteja calmo, você ouve um assobio fraco,
    que rapidamente fica cada vez mais alto, até que uma forte lufada de vento subitamente atinge você
    com tamanha força, que você mal consegue se mexer no sentido contrário."
    show velha at right
    n "Você protege os olhos, até que a ventania diminui um pouco, e, quando você os abre, vê uma face fantasmagórica de
    mulher dentro do que parece ser um Redemoinho vivo."
    n "Ela move os lábios, dizendo palavras que você não consegue distinguir, mas, alguns segundos depois de ela ter terminado de falar, a
    mensagem chega até você."
    n "Ela parece considerar a sua aparência como ofensiva e está desafiando você com palavras agressivas. Você segura a sua espada, mas ela ri. Assim:"
    menu:
        "Você conversará com ela":
            jump tres90
        "Usará a sua magia para se livrar dela":
            jump quatro7

label tres90:
    n "Estranhamente a conversa flui, e, após algum tempo, ela lhe deixa e você prossegue a sua jornada."
    jump dois18

label quatro7:
    n "Com a pressão gerada pela situação, teste sua sorte ao conjurar o Encanto."
    $ d203roll = renpy.random.randint(1, 20)

    if (d203roll>= 12):
        $renpy.notify("sucesso de sorte")
        play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
        n "Ela observa espantada o aparecimento de uma réplica perfeita dela mesma entre vocês dois. Ela recua um pouco, e você orienta a sua criação para o ataque."
        n "Mas, quando elas se aproximam uma da outra, acontece uma coisa estranha."
        n "Elas parecem ser incapazes de chegar perto uma da outra, como duas extremidades giratórias, e sempre separam-se bruscamente de um salto."
        n "Porém, sua própria cópia pelo menos forçou a criatura a se afastar de você para uma certa distância, permitindo quevocê corra para a entrada principal da Cidadela."
        jump dois18

    else:
        $renpy.notify("fracasso de sorte")
        play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
        n "Você recua em direção ao centro do pátio para se esconder dela."
        jump dois09

label um49:
    n "Eles não estão interessados em sua companhia e sugerem que você siga o seu caminho. Então você:"
    menu:
        "Prosseguirá em direção à Torre Negra":
            jump dois18
        "Sentará ao fogo de qualquer maneira":
            jump um34

label um4:
    n "A sombra do muro dificulta muito a visão. Uma pedra solta desliza, e você perde o equilíbrio,
    oscilando à beira do que você tem consciência de que deve ser um poço profundo."

    n "Teste a sua Sorte. Se você tiver sorte, recupera o equilíbrio e caminha em segurança."

    play sound "musics/efeito_sonoro/dados.mp3"

    $ d204roll = renpy.random.randint(1, 20)

    if (d204roll>= 11):
        $renpy.notify("sucesso de sorte")
        play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
        n "você vê uma corda e se segura nela, recobrando o equilíbrio"
        jump sete9

    else:
        $renpy.notify("fracasso de sorte")

        play sound "musics/efeito_sonoro/sorte-fracasso.mp3"

        jump um00

label um00:
    n "tente usar um feitiço de levitação para nao cair! teste sua sorte!"

    play sound "musics/efeito_sonoro/dados.mp3"

    $ d205roll = renpy.random.randint(1, 20)

    if (d205roll>= 14):
        $renpy.notify("sucesso de sorte")
        play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
        n "você volta para a fora do poço e segue seu caminho"
        jump sete9

    else:
        $renpy.notify("fracasso de sorte")
        play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
        jump dois76

label dois76:

    scene poco:
        zoom 2.0

    n "Você cai no fundo de um poço profundo – possivelmente um manancial de água tapado. Você se
    recompõe e parece estar inteiro."

    n "Mas como você vai sair? Cavar apoios para os pés nas paredes do
    poço com sua espada levaria um tempo enorme."

    n "Você poderia lançar um Encanto da Força para
    ajudá-lo nessa tarefa ou poderia gritar, pedindo ajuda."

    menu:

        "usar encanto! teste de sorte.":
            play sound "musics/efeito_sonoro/dados.mp3"

            $ d206roll = renpy.random.randint(1, 20)

            if (d206roll>= 11):
                $renpy.notify("sucesso de sorte")
                play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
                jump um65

            else:
                $renpy.notify("fracasso de sorte")
                play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
                n "voce fracassa no uso do feitiço e quando começa a escalar cai de volta torçendo o pé, apenas lhe restanto gritar por ajuda"
                jump dois02

        "gritar pedindo ajuda":
            jump dois02

label um65:
    n "Quando você sente a força se espalhar pelo seu corpo desembainha a espada e crava na muralha
    terrosa. Dessa forma você faz um apoio para os pés, para depois utilizá-lo enquanto cava o próximo,
    assim consegue subir pelas paredes bem rapidamente com o aumento de força que recebeu."

    n "Na metade do caminho, contudo, sua força começa a diminuir, e você compreende que está retornando
    ao normal. Se você deixar que isso aconteça, cairá para trás dentro do poço mais uma vez."

    n "Você pode lançar outro Encanto da Força para dar a energia suficiente para completar a sua escada ou gritar pedindo ajuda."

    menu:
        "usar encanto! teste de sorte.":
            play sound "musics/efeito_sonoro/dados.mp3"

            $ d207roll = renpy.random.randint(1, 20)

            if (d207roll>= 11):
                $renpy.notify("sucesso de sorte")
                play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
                jump tres98

            else:
                $renpy.notify("fracasso de sorte")
                play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
                n "voce fracassa no uso do feitiço e quando volta a escalar cai de volta quebrando a perna, apenas lhe restanto gritar por ajuda"
                jump dois02

        "gritar pedindo ajuda":
            jump dois02

label tres98:
    n "Você lança o encanto, e sua força retorna, permitindo que você acabe de subir os degraus. Quando
    você chega no alto, os efeitos desaparecem mais uma vez. Você pode agora seguir ao longo da
    muralha na direção da Torre Negra."

    jump sete9

label dois02:
    n "Depois de vários minutos de gritaria, você ouve vozes que se aproximam, falando em uma língua
    estranha. Para seu alívio, você vê quatro cabeças que espiam dentro do poço se desenharem contra o
    céu. Você berra para que eles consigam alguma corda."

    n "Eles conversam entre si e desaparecem.
    Finalmente, você ouve suas passadas rápidas retornando. Eles param mais uma vez no alto do poço
    e jogam sobre você, não uma corda de socorro, mas o conteúdo de um caldeirão de óleo fervente!"

    n "Você terá que olhar com mais cuidado por onde anda na sua próxima aventura, porque esta está
    terminada. E lembre-se - estranhos não são bem-vindos na Cidadela do Caos..."

    jump final_ruim

label sete9:

    scene cidadela1

    n "No canto mais distante do pátio, você encontra um arbusto diferente, com galhos contorcidos a
    partir da haste central, como se estivesse em agonia."

    n "As folhas têm a forma de diamantes, com pequenas amoras por baixo, chatas e com forma de pastilhas. Você pode levar algumas amoras com
    você na sua aventura e avançar um pouco mais ao longo do muro para a entrada principal da
    Cidadela."

    $renpy.notify("adquiriu amoras!")

    play sound "musics/efeito_sonoro/item encontrado.mp3"

    $amoras = True

    jump dois18

label dois18:

    play music "musics/sb_phoenix.mp3"

    scene portao

    n "Há uma grande porta de madeira à sua frente, firmemente trancada. Você pode bater três vezes para
    chamar o guarda ou usar um Encanto da Força para tentar abri-la."

    menu:
        "chamar o guarda":
            jump um18
        "encanto força(teste de sorte)":
            jump nove4

label um18:

    play sound "musics/efeito_sonoro/batendo-porta.mp3"

    scene portao aberto
    with dissolve

    n "A porta abre e uma criatura grande e abrutalhada sai. sua aparencia remete a de uma besta e
    sua pele parece ser recoberta de armadura."

    show porteiro at center:
        zoom 1.5
    with dissolve

    play sound "musics/efeito_sonoro/minotauro.mp3"

    n "Rosna para saber o que você quer e exige a senha antes
    de deixar que você entre. Você sabe a senha?"
    menu:
        "Ganjees":
            jump dois55
        "Kraken":
            jump quatro9
        "Cimitarra":

            n "o porteiro te indaga para saber quem te contou a senha"

            if(sabe_senha):
                n "você diz que é um convidado especial do bibliotecario e veio auxiliar em um estudo com uma lingua ancestral"
                jump tres71
            else:
                n "você gagueja, nao sendo capaz de explicar como sabe a senha!"
                jump dois90
        "tentar se passar como especialista em ervas":
            jump um98

label nove4:
    play sound "musics/efeito_sonoro/dados.mp3"

    $ d208roll = renpy.random.randint(1, 20)

    if (d208roll>=8):
        $renpy.notify("sucesso de sorte")
        play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
        n "Você sente o seu próprio poder crescendo. Você corre na direção da porta e a golpeia firme como
        ombro... mas ela nem se mexe! Você bate com força para chamar o guarda."
        jump um18
    else:
        $renpy.notify("fracasso de sorte")
        play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
        n "você erra algumas palavras do encanto e se joga na porta sem fazer nenhuma diferença!
        Você bate com força para chamar o guarda."
        jump um18

label dois55:
    n "A criatura olha para você. Seus olhos se estreitam. Há uma lança longa em suas mãos, que ela
    rapidamente aponta na sua direção. 'Esta não é a senha!' ela grita e sai para a batalha. Teste a sua
    Sorte."
    $ d209roll = renpy.random.randint(1, 20)

    if (d209roll>=15):
        $renpy.notify("sucesso de sorte")
        play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
        n "você pensa rapidamente em um blefe!"
        jump um98
    else:
        $renpy.notify("fracasso de sorte")
        play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
        n "você gagueja e a criatura avança para lutar!"
        jump dois90

label dois90:
    n "O porteiro dá um passo adiante e desfere uma estocada com sua lança na sua direção. Você
    pula rapidamente e se desvia. Embora ele não esteja usando uma armadura, seu couro grosso parece
    ser proteção suficiente."
    jump batalha_porteiro

label quatro9:
    n "A criatura fica olhando fixamente para você com ar inquisitivo, como se estivesse insegura em
    relação a você."
    jump dois55

label tres71:

    play sound "musics/efeito_sonoro/minotauro.mp3"

    n "A criatura grunhe e abre a porta para deixar você entrar."

    jump um77

label um98:
    n "Você pensa rapidamente, e depois enfia a mão em sua mochila e tira um punhado de ervas.
    Mostrando-as à criatura, você explica que é um especialista em plantas medicinais e veio tratar do
    bibliotecário do Senhor, que está doente, em estado crítico."
    n "O mensageiro não disse nada quanto a
    senhas. Será que ele vai acreditar em você? Teste a sua Sorte."
    $ d2010roll = renpy.random.randint(1, 20)

    if (d2010roll>=10):
        $renpy.notify("sucesso de sorte")
        play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
        n "o guarda acredita no seu blefe e te deixa passar!"
        jump um77
    else:
        $renpy.notify("fracasso de sorte")
        play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
        n "ele diz que nao pode deixar entrar sem senha e avança em sua direçao com a lança em riste!"
        jump dois90

label um77:

    play music "musics/the-medieval-banquet.mp3"

    scene corredor:
        zoom 1.8

    n "Você está em um corredor estreito. Ele continua por alguns metros e termina em uma porta."

    n " A meio caminho, descendo a passagem, pode-se ver um arco, de onde alguns degraus levam para baixo.
    Você vai prosseguir na direção da porta ou se arriscará a descer as escadas?"
    menu:
        "seguir na direção da porta":
            jump cinco
        "descer as escadas":
            jump tres44

label cinco:
    n "Você experimenta a maçaneta da porta e ela gira, abrindo para um outro corredor. Logo adiante, a
    passagem vira para a direita e termina pouco depois em outra porta. Nesta porta há um letreiro que
    diz 'Por Favor Toque a Campainha para Chamar o Mordomo'. Uma corda - evidentemente a
    campainha - pende ao lado da porta."
    menu:
        "Você toca a campainha conforme indicado":
            jump quatro0
        "Experimenta a maçaneta da porta":
            jump tres61

label tres61:
    n "A porta abre novamente mas, quando você faz isso, ouve o ruído ensurdecedor de uma campainha
    de alarme! Teste a sua Sorte."
    play sound "musics/efeito_sonoro/dados.mp3"

    $ d2011roll = renpy.random.randint(1, 20)

    if (d2011roll>=14):
        $renpy.notify("sucesso de sorte")
        play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
        n "..."
        jump dois97
    else:
        $renpy.notify("fracasso de sorte")
        play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
        n "..."
        jump um26

label dois97:
    hide corredor
    scene bg6 at truecenter:
        zoom 1.5
    n "Você bate a porta, fechando-a atrás de você, e, juntamente como alarme estridente, você ouve o som
    de passos, correndo rapidamente e se aproximando. Você conseguiu fugir a tempo e escapar das criaturas."
    jump dois20

label um26:
    hide corredor with fade
    show bg6 at truecenter:
        zoom 1.5
    show giras at left:
        xpos 220
        ypos 950
        zoom 1.3
    with dissolve
    n "Você para para considerar a situação, em pânico. À sua frente, a passagem se bifurca para a
    esquerda e para a direita. Enquanto você está tentando decidir que direção tomar, três criaturas
    surgem da passagem do lado esquerdo."
    n "Chamar os ruídos que você ouviu de 'passos' não é inteiramente preciso, como você verá."
    jump tres16

label tres16:
    n "As passadas que você ouviu - que realmente deveriam ser chamadas de 'mãozadas' – pertencem a
    três GIRAS, que agora rolam descendo a passagem na sua direção, o que faz com que você recue de
    volta para a porta."
    n "Estas criaturas são animais peculiares que têm, ao invés de pernas, um segundo
    par de mãos. Eles se deslocam dando cambalhotas a um ritmo bem acelerado. Suas cabeças - ou
    pelo menos seus rostos - estão colocados no centro do peito."
    n "Embora não sejam muito prático como
    espadachins, tendo em vista seus meios de movimentação inadequados, são excelentes lançadores de facas."
    n "Pegando facas em seus cintos enquanto se movimentam em círculos, eles podem dispará-
    las em velocidade de fogo rápido, como rodas-de-santa-catarina. No momento, três facas desse tipo
    estão cruzando o ar na sua direção."
    n "Você usará um Encanto do Escudo para se proteger (Teste de sorte)."
    play sound "musics/efeito_sonoro/dados.mp3"

    $ d2012roll = renpy.random.randint(1, 20)

    if (d2012roll>=15):
        $renpy.notify("sucesso de sorte")
        play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
        n "As facas atingem o seu escudo mágico e caem ao chão. Você conseguiu escapar das criaturas."
        jump dois20
    else:
        $renpy.notify("fracasso de sorte")
        play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
        n "sob pressão, você erra algumas palavras do encanto,
        fazendo com que ele não seja eficaz, e você parte para a batalha!"
        jump tres46

label tres46:
    n "Quando os Giras vêem você desembainhar a sua espada, param e tagarelam com muita agitação.
    Um deles - evidentemente o líder - manda o menor subir a passagem de volta (presumivelmente
    para buscar ajuda). Os outros dois puxam facas e rolam lentamente na sua direção."
    n "Prepare-se para a batalha!"

    jump batalha_giras

label dois20:
    play music "musics/Savfk - The Travelling Symphony.mp3"
    n "Você poderá tomar a passagem do lado esquerdo, ou a passagem do lado direito."
    menu:
        "Passagem pela esquerda":
            jump dois43
        "Passagem pela direita":
            jump dois

label dois:
    scene bg7 at truecenter:
        zoom 2.2
    n "Um pouco adiante na passagem há uma porta do lado direito. Esta porta está coberta por estranhos
    caracteres, em uma linguagem que você não compreende. Dessa forma, você:"
    menu:
        "Tentará abrir a porta":
            jump um42
        "Seguirá a passagem":
            jump tres43

label um42:
    n "Você experimenta a maçaneta, e ela gira. Você não consegue ouvir nada vindo do interior do
    aposento, por isso você abre a porta para dar uma olhada."
    n "O aposento é pequeno, com um castiçal dourado em cima de uma mesa... mas, de repente, você ouve um rangido vindo do assoalho! Tarde
    demais, você compreende que as pedras sob os seus pés estão se mexendo para revelar um alçapão!"
    n "Você cai primeiro em um poço. Quando atinge o fundo, você rola para o lado, descendo outra
    passagem, e continua rolando para baixo. Por mais que você tente, não consegue impedir que você
    role sem parar, até que acaba por chegar a uma pequena câmara, onde finalmente pára."
    n "Mas o choque foi demais para você. Enquanto o mundo escurece à sua volta, você ouve uma tagarelice
    excitada, e depois desmaia."
    jump dois34

label tres43:
    scene bg8 at truecenter:
        zoom 1.2
    n "Seguindo o caminho após a passagem. Você se depara com um beco sem saída. Dessa forma, você procura por passagens secretas."
    jump um0

label um0:
    n "Você tateia pela rocha e acaba por encontrar uma pequena alavanca. Ao puxar esta alavanca, a face
    da rocha esfarela um pouco e aparece uma pequena abertura."
    n "Você sobe por esta abertura e chega a uma passagem. Descendo a passagem para a esquerda, você pode ver uma porta e resolve
    investigar."
    jump dois49

label dois49:
    scene bg9 at truecenter:
        zoom 1.5
    n "A passagem termina à sua frente em uma porta de madeira. Há um letreiro afixado nela, dizendo
    'DESPENSA'. Você cola os ouvidos junto a ela, mas não ouve nada. A porta está trancada."
    menu:
        "Se você tiver uma Chave de Cobre, poderá tentar usá-la aqui":
            if (chave_cobre == True):
                n "a chave gira e a porta abre!"
                jump um96
            else:
                play sound "musics/efeito_sonoro/nao tem o item.mp3"
                $renpy.notify("você não possui esse item!")
                n "Você se lembra que não tem a chave e terá que arrombar a porta."
                jump dois31
        "Tentar arrombar a porta":
            jump dois31

label dois31:
    n "Você bate na porta com o ombro para derrubá-la (Teste de sorte)."
    play sound "musics/efeito_sonoro/dados.mp3"

    $ d2013roll = renpy.random.randint(1, 20)

    if (d2013roll>=13):
        $renpy.notify("sucesso de sorte")
        play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
        n "A porta cede e abre."
        jump um96
    else:
        $renpy.notify("fracasso de sorte")
        play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
        n "Mesmo a pancada sendo muito forte, a porta apenas tremeu e você machucou muito seu ombro!"
        jump nove99

label nove99:
    n "Após alguns instantes se recuperando, você ouve um estrondo."
    n "Milagrosamente, a porta cedeu e você conseguirá prosseguir a sua jornada."
    jump um96

label um96:
    scene bg10
    n "Ao entrar, o aposento é de fato uma despensa. Num primeiro momento, os cheiros estranhos - uma mistura de
    comida doce, temperada e azeda - pegam você de surpresa. Há vários tipos de carne pendurada sem
    ganchos ao longo de uma das paredes."
    n "Uma prateleira de queijos contém mais ou menos uma dúzia
    de variedades de queijo, e você torce o nariz de nojo como cheiro forte dos, digamos, que estão
    'maduros demais'."
    n "Você poderá sair pela porta na parede do lado esquerdo, ou pela porta na parede do lado direito"
    menu:
        "Porta do lado esquerdo":
            jump um3
        "Porta do lado direito":
            jump dois81

label um3:
    n "A maçaneta gira e você abre a porta para um outro aposento, onde há bastante atividade. Três
    velhas feias, com narizes e queixos compridos, circulam pelo aposento - que parece ser alguma
    espécie de cozinha - pegando vários ingredientes dos armários e acrescentando-os a um caldo
    dentro de um grande caldeirão."
    scene bg11 at truecenter
    show velha1 at center:
        zoom 0.5
        xpos 850
    show velha2 at center:
        zoom 0.3
        xpos 650
    show velha3 at center:
        xpos 1300

    n "Há um pedaço de carne assando em um espeto, embaixo de uma
    grande chaminé. Olhando mais atentamente, você descobre que a carne, na verdade, não é de um
    animal, mas sim um Anão inteiro que escurece ao fogo."
    n "Uma das mulheres olha para você e diz: 'Ah, você deve ser o novo empregado...ou é a próxima refeição?', com o que todas as três
    começam a dar gargalhadas e gritos enquanto riem."
    menu:
        "Você deixará que elas acreditem que você é o novo empregado que elas estão esperando":
            jump tres02
        "Investigar o aposento mais devagar":
            jump dois15

label tres02:
    n "Elas ordenam que você leve uma bandeja de comida por uma porta na parede do outro lado para o
    Grande Salão e a deixe na mesa, pois os Ganjees logo estarão lá para ceia."
    n "Elas também advertem
    você para que não espere pelo Ganjees, ou provavelmente você terminará sendo a próxima refeição.
    Você leva a bandeja e sai pela porta distante."
    n "Feliz por ter saído da repulsiva cozinha delas, você segue uma passagem adiante, pára para deixar a bandeja e continua para uma outra porta. Você
    experimenta a maçaneta e ela gira."
    jump um69

label dois15:
    n "Você terá que inventar alguma história para estas mulheres horrorosas. Você dirá a elas que o
    Capitão da Guarda ordenou que se fizesse uma inspeção na cozinha delas, depois de uns dois casos
    de intoxicação alimentar"
    jump um36

label um36:
    n "Todas elas protestam veementemente, mas você explica que tem suas ordens e começa a circular
    pela cozinha."
    n "Você investigará:"
    menu:
        "Inspecionar os armários":
            jump um7
        "O espeto sendo assado":
            jump tres89

label um7:
    play music "musics/musica tensao.mp3"
    hide devlin with dissolve
    hide mc normal
    n "Ao investigar os armários todos os tipos de alimentos estranhos podem ser encontrados. Globos oculares, línguas,
    lagartixas, frascos de líquidos, ervas e frutos silvestres de diferentes formas e tamanhos."
    n "Uma garrafa em especial, contendo um líquido verde transparente, chama a sua atenção. Você não tem
    tempo para ler o rótulo no momento, por isso você a põe no bolso rapidamente, enquanto elas não
    estão olhando."
    n "Você lhes diz que a cozinha parece estar em ordem e sai pela porta do lado oposto da cozinha."
    jump nove3

label nove3:
    n "Do lado de fora, você olha para sua garrafa. É uma garrafa de Essência de Erva de Porco,
    aparentemente útil para repelir criaturas de base em pedra."
    $essencia_porco = True

    $renpy.notify("adquiriu Essência de Erva de Porco!")

    play sound "musics/efeito_sonoro/item encontrado.mp3"

    n "Isso pode ser útil, e você a guarda cuidadosamente em sua mochila. Seguindo em frente pelo corredor, você chega a uma outra porta,
    que abre, deixando que você passe para um grande aposento."
    jump um69

label tres89:
    n "Quando você se aproxima do espeto, uma das velhas joga um pó no fogo, e as três se afastam,
    dando risadas. Você está em guarda. Você observa o fogo começando a rugir, e as chamas
    crescendo ameaçadoramente."
    hide velha1 with dissolve
    hide velha2
    hide velha3
    n "Subitamente, várias das labaredas saltam do fogo e tomam a forma de
    um DEVLIN, uma criatura do tamanho de um Anão, feita do próprio fogo! As três bruxas apontam
    para você, e o Devlin avança. Assim você:"
    show devlin at right:
        zoom 0.7
        xpos 2300
    menu:
        "Usa magia (Teste de sorte).":
            play sound "musics/efeito_sonoro/dados.mp3"

            $ d2014roll = renpy.random.randint(1, 20)

            if (d2014roll>=14):
                $renpy.notify("sucesso de sorte")
                play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
                n "Você lança o encanto com sucesso, e o Devlin se apaga. Você ganha a chance de inspecionar outro item da cozinha."
                jump um36
            else:
                $renpy.notify("fracasso de sorte")
                play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
                n "sob pressão, você erra algumas palavras do encanto,
                fazendo com que ele não seja eficaz, e você parte para a batalha!"
                jump batalha_devlin

label dois81:
    scene bg12 at truecenter:
        zoom 1.7
    show cria1 at right:
        xpos 1600
        ypos 820
        zoom 0.8
    show cria2 at right
    n "Você abre a porta para outro aposento e surpreende duas pequenas criaturas.
    Elas te olham rapidamente, chocadas com a sua chegada. Você:"
    menu:
        "Inicia um combate":
            jump tres82
        "Tenta entabular uma conversa":
            jump tres56
        "Diz que está só de passagem":
            jump dois85

label tres82:
    n "Eles correm pelo aposento em pânico, esbarrando uns nos outros e gritando: 'Ai, meu Deus, ai,
    minha nossa, este estranho parece malvado, onde estão as nossas armas?'"
    n "Você ri da desordem deles e guarda a sua espada. Eles se acalmam e ficam olhando para você. Você pode seguir adiante ou conversar com eles"
    menu:
        "Seguir adiante":
            jump dois85
        "Conversar com eles":
            jump tres56

label tres56:
    n "Eles ficam um tanto aliviados por saber que você não tem intenção de fazer mal a eles e voltam a
    sentar-se no chão, convidando você para se juntar a eles."
    n "O aposento é pequeno e simples, com folhagens espalhadas pelas paredes, possivelmente com o intuito de servir de decoração, embora as
    folhas estejam agora murchas e há muito tempo mortas. Um pequeno fogo arde em um dos cantos,
    embaixo de um orifício no teto."
    n "Há duas portas na parede de fronte a você; uma à esquerda, a outra
    à direita. Você senta para bater um papo. Você descobre que as pequenas criaturas magérrimas se
    denominam ESCOTEIROS e são de fato um grupo agradável, que brinca e ri com você."
    n "Você resolve não se arriscar a dizer muito sobre a sua missão, mas faz perguntas genéricas sobre o lugar.
    Balthus Dire é o senhor da casa e passa a maior parte do tempo lá no alto na Cidadela."
    n "A senhora sua esposa é uma feiticeira lindíssima que é muito vaidosa e aprecia as coisas que o dinheiro e o
    poder podem proporcionar. Há muitas criaturas cruéis no interior da Cidadela, mas é preciso tomar
    cuidado especial com os Ganjees, que vagueiam pela Torre à noite."
    n "Você acaba levantando, agradece pela conversa e se prepara para seguir adiante."
    n "Os Escoteiros oferecem também a você o direito de receber deles um favor antes de ir embora, pois eles também
    apreciaram a sua companhia. Você pode:"
    menu:
        "Levar a sério a oferta deles":
            jump um46
        "Não aceitar e seguir adiante":
            jump dois85

label um46:
    n "Como favor, você pergunta como pode derrotar Balthus Dire."
    jump dois47

label dois47:
    n "Eles ficam chocados com seu pedido. Você pragueja ao compreender que não deveria ter revelado
    sua verdadeira missão a eles. Todos eles tagarelam agitados, por algum tempo, depois voltam-se na
    sua direção. Juntos, todos eles sopram com força."
    n "Para sua surpresa, o sopro deles é como um vento de tempestade, e você é atirado para trás de encontro à parede. Sua cabeça bate na parede áspera e
    rochosa, e você perde os sentidos."
    hide bg12 with dissolve
    hide cria1
    hide cria2
    jump dois34

label dois85:
    n "Há duas portas na parede oposta. As pequenas criaturas dizem que você pode seguir adiante em seu caminho tanto por uma ponta
    quanto pela outra. Você escolhe a porta da esquerda ou a porta da direita"
    menu:
        "Porta da esquerda":
            jump um85
        "Porta da direita":
            jump dois3

label um85:
    hide cria1 with dissolve
    hide cria2
    n "A porta se abre para um corredor estreito, que faz uma curva fechada para a esquerda, continua por
    vários metros e então termina por fim em uma porta. Você põe a mão na maçaneta."
    jump um3

label dois3:
    hide cria1 with dissolve
    hide cria2
    n "Você abre a porta e sai em uma passagem que continua direto para frente por algum tempo. Vira
    para a esquerda, depois para a direita, até que você chega a um arco à sua frente que dá para um
    grande aposento. Você caminha na direção do aposento e entra nele."
    jump um69

label quatro0:
    scene bg2 at truecenter:
        zoom 1.5
    show mordomo at center:
        zoom 1.3
    n "Depois de vários minutos, a porta se abre lentamente, e uma criatura corcunda e deformada, com
    dentes podres, cabelos desgrenhados e roupas esfarrapadas, aparece na sua frente. 'Sim senhor (heh, heh) - o que posso
    fazer pelo senhor?' rosna a criatura semi-humana."
    n "'Estou sendo esperado', você responde e passa por ele, atravessando a porta com confiança. Ele fica um pouco surpreso com seu
    comportamento e gagueja, sem saber se entra em conflito com você ou não."
    n "'Onde é a recepção?' você pergunta. Ele olha para você de soslaio com um dos olhos e faz um gesto na direção de uma
    bifurcação para a esquerda, a pouca distância dali."
    n "Você, de maneira receosa, acreditará nele e tomará a bifurcação para a esquerda"
    hide mordomo
    jump dois43

label dois43:

    hide giras
    hide mc normal

    n "A passagem se estende por vários metros e depois termina em uma porta. Você escuta junto à porta
    e ouve uma respiração profunda e pesada vindo lá de dentro, como se alguma criatura de grande
    porte estivesse dormindo ali."
    n "Cuidadosamente, você experimenta a maçaneta, e a porta abre. Logo na entrada, embora o aposento
    esteja escuro, você consegue ver uma criatura muito grande, semelhante a um Goblin, adormecida no chão."
    n "Você pode se arriscar a entrar no aposento na ponta dos pés"
    jump tres52

label tres52:
    scene bg3
    show gark at right:
        zoom 1.3
    n "Você entra no aposento na ponta dos pés. Está escuro lá dentro, e o ar está úmido. Há um poste de
    madeira rústica pregado em uma das paredes, com diversos ganchos nele. Há duas portas na parede do outro
    lado que levam adiante."
    n "No poste, pendurado, há um espelho improvisado, mas, quando sua tocha ilumina o espelho,
    seu reflexo é projetado sobre os olhos do gigante adormecido, que grunhe e se mexe."
    n "Um dos olhos se abre, depois o outro, ele salta de pé! Ele pega uma acha, que usava como travesseiro, e
    rapidamente retira a bainha de couro, revelando uma afiada cabeça de bronze."
    n "Esta criatura gigantesca é um GARK! Grandes e brutos, os Garks são meio Goblins, meio
    Gigantes, cruzados por senhores feiticeiros por sua índole agressiva."
    n "Embora um tanto estúpidos, são criaturas bastante violentas e de natureza guerreira. Você:"
    menu:
        "Vai dar uma corrida na direção das portas?":
            jump dois03
        "Desembainhará a espada, pronto para a luta?":
            jump um6
        "Pedirá desculpas por perturbar a criatura?":
            jump dois16
        "Vai se preparar para usar um Encanto":
            jump um1

label dois03:
    n "Ao correr para as portas, você tropeça, permitindo que a criatura ganhe terreno. Ela agarra seu braço
    com uma das mãos e atira você para o outro lado do aposento."
    n "Dessa forma, não havendo outra saída, você se vê forçado à usar o Encanto da Fraqueza no Gark."
    jump um52

label um52:
    n "Você lança seu Encanto da Fraqueza, e a criatura interrompe seus passos, sem entender o que aconteceu com ela."
    n "Com algum esforço, ela apanha seu machado e vem na sua direção, mas evidentemente não é um
    adversário tão forte quanto era antes."
    jump um6

label um6:
    n "Ao desembainhar a espada, o gark parte em sua direção!"
    jump batalha_gark

label um1:
    n "Você opta por usar o Encanto da Fraqueza para tentar o atordoar e, assim, conseguirá seguir adiante em direção a porta."
    play sound "musics/efeito_sonoro/dados.mp3"

    $ d2015roll = renpy.random.randint(1, 20)

    if (d2015roll>=16):
        $renpy.notify("sucesso de sorte")
        play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
        n "você lança o encanto com sucesso, o gark fica fraco e cai, enquanto você parte em direção às portas."
        jump nove9
    else:
        $renpy.notify("fracasso de sorte")
        play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
        n "sob pressão, você erra algumas palavras do encanto,
        fazendo com que ele não seja eficaz, e você parte para a batalha!"
        jump um6

label dois16:
    n "Qual será sua tática?"
    menu:
        "Você dirá à criatura que você é um convidado":
            jump dois94
        "Tentará subornar o Gark, oferecendo três Peças de Ouro":
            jump tres91
        "Tentará lançar um Encanto de Ouro dos Tolos para subornar a criatura (Teste de sorte)":
            jump tres6

label dois94:
    n "O Gark se recompõe, abaixa o machado e começa a se desculpar com você por estar dormindo no
    posto."
    n "Por insistência dele, você concorda em não dizer nada a ninguém. A criatura se oferece para
    levar a sua túnica, mas você recusa o oferecimento e segue em frente."
    jump nove9

label tres91:
    n "O Gark pega as suas três Peças de Ouro, coloca-as em uma bolsa presa em volta da cintura e mostra
    o caminho para seguir na direção das portas."
    #$ dinheiro retirado (notify)
    jump nove9

label tres6:

    $ d2016roll = renpy.random.randint(1, 20)

    if (d2016roll>=6):
        $renpy.notify("sucesso de sorte")
        play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
        n "você lança o encanto com sucesso, o gark acredita no ouro falso e permite a sua passagem, apontando a direção das portas."
        jump nove9
    else:
        $renpy.notify("fracasso de sorte")
        play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
        n "sob pressao, você erra algumas palavras do encanto,
        fazendo com que ele não seja eficaz, e você parte para a batalha!"
        jump um6

label nove9:

    play music "musics/the-medieval-banquet.mp3"

    hide gark
    hide bg3

    scene bg5

    n "Ao chegar nas duas portas, você escolhe para qual entrar"
    menu:
        "Porta da direita (biblioteca)":
            jump tres8

        "Porta da esquerda (salão de jogos)":
            jump cinco2

label tres8:
    n "A porta abre para uma passagem curta, calçada com pedras pequenas. A uma pequena distância
    mais adiante, uma porta elaboradamente entalhada assinala o fim da passagem."
    n "Você se aproximada porta, tentando escutar quaisquer sinais de vida do lado de dentro.
    Quando sua mão toca a maçaneta, uma voz diz: 'Não bata; simplesmente entre!' vinda de dentro."
    n "Dessa forma, você:"
    menu:
        "Entrará no aposento conforme as instruções":
            jump um32
        "Resolverá desistir, voltar e entrar na porta da esquerda":
            jump cinco2

label um32:

    scene biblioteca
    show bibliotecario at right:

    n "Ao entrar, há livro do chão até o teto em cada uma das paredes, e diversas mesas e cadeiras
    estão alinhadas no centro do aposento. Do outro lado, há um homem de pele escura sentado, que levanta os olhos de um livro para olhar
    para você por cima de óculos estreitos."
    n "Há uma porta atrás dele. 'Sim, o que é?', ele diz. 'Que livro você está procurando?'. Você examina as várias
    estantes, que possuem legendas. Você pedirá a ele:"
    menu:
        "Biografias de Balthus Dire?":
            jump um8
        "Segredos da Torre Negra?":
            jump dois38
        "Criaturas do Reino da Rocha Escarpada?":
            jump tres75

label um8:
    n "Ele aponta para uma seção logo acima do chão, que você examina. Finalmente, você escolhe um
    volume e senta para ler."
    n "Balthus Dire aparentemente é o terceiro de uma linhagem de Feiticeiros Senhores da Guerra que governa a Torre
    Negra e o Reino da Rocha Escarpada. Chegou ao poder depois da morte de seu pai, Craggen Dire, há alguns anos atrás."
    n "Os Dires são mestres de Magia Negra há gerações, mas sua força e poder duram somente no período noturno; a luz do sol é uma
    espécie de veneno para eles."
    n "Pouco tempo depois da morte de seu pai, Balthus Dire casou-se com Lady Lucretia, ela também uma Feiticeira de Magia Negra, e desde então eles vem reinando juntos
    sobre o Reino da Rocha Escarpada."
    n "Ao terminar o livro, você repara que o bibliotecário está com a mão junto ao ouvido, aparentemente escutando alguma coisa. Ele dirige a você um olhar
    inquisitivo."
    menu:
        "Você pode procurar outro livro útil, que possa ajudá-lo na sua empreitada":
            hide bibliotecario
            jump oito4
        "Ou tentar sair da biblioteca pela porta atrás dele":
            hide bibliotecario
            jump tres1

label oito4:
    n "Ao examinar as prateleiras, você ouve uma grande movimentação atrás de você. Você se vira rapidamente, a tempo de ver criaturas
    semelhantes a orquisas, armadas e em guarda, materializaram-se uma após a outra diante de você."
    show orcs at center:
        zoom 0.5
    n "Elas avançam e cercam você. O mais alto chega o rosto perto do seu e solta um bafo de respiração diretamente sobre os seus olhos."
    n "O aposento gira e você desaba no chão, inconsciente."
    hide orcs
    hide biblioteca
    with fade
    jump dois34

label tres1:
    n "Você sai do aposento pela porta do outro lado, a qual abre para uma passagem curta que termina em uma grande porta de madeira.
    A maçaneta desta porta gira, deixando que você entre em uma grande câmara."
    jump um69

label dois38:
    n "Ele indica uma seção das estantes, e você leva um livro para uma das mesas para ler. O livro é extremamente informativo, traçando a história da Cidadela.
    A Torre Negra foi construída pelo avô de Balthus Dire."
    n "À medida em que foi se tornando um santuário para as forças do mal, a lei e a ordem foram gradualmente dando lugar ao caos, devido à luta das criaturas monstruosas para
    ascender na hierarquia do poder."
    n "O avô de Dire acabou se vendo na necessidade de se proteger de seus próprios seguidores, criando vários sistemas de segurança entre as criaturas e seus próprios
    aposentos, destacando-se entre eles a Armadilha do Poço da Perdição e uma Fechadura de Combinação mágica na porta de seu próprio quarto. A combinação da fechadura é 217."
    n "Você lê mais sobre a Cidadela e então escolhe perguntar ao homem:"
    menu:
        "Sobre a seção dedicada a Balthus Dire":
            jump um8
        "Sobre a seção das Criaturas de Rocha Escarpada":
            jump tres75
        "Ou simplesmente sai do aposento pela porta do outro lado":
            jump tres1

label tres75:
    n "Ele indica um livro na prateleira que é uma lista alfabética de todos os tipos de criaturas. Você
    consultará a seção sobre Ganjees"
    jump seis3

label seis3:
    n "Você vai até o índice remissivo e verifica a referência. Ao chegar à página correta, você fica
    decepcionado ao descobrir que a seção foi arrancada do livro!"
    n "Dessa forma, você decide sair do aposento pela porta do outro lado."
    jump tres1

label cinco2:
    scene salao at truecenter:
        zoom 1.5
    show maguito at left:
        xpos 500
        ypos 1000
        zoom 1.2
    show leviata at right:
        zoom 1.7
    show heitoba at center:
        ypos 1000
        zoom 0.2
    n "A porta abre e você segue adiante, batendo-a para que se feche atrás de você. Pouca distância à frente, você chega a um cruzamento de três caminhos,
    no qual você toma a passagem que vai na direção norte."
    n "Ela continua por vários metros, conduzindo a uma outra porta. Você pode ouvir risos e vozes alegres do outro lado. Cautelosamente, você abre
    a porta que dá para um grande aposento, onde um grupo de mais ou menos doze criaturas, de todas as formas, tamanhos e cores, estão se divertindo com jogos."
    n "Quando você entra no aposento, uma voz grita: 'Olhem esse deve ser Glaz-Doz-Fut!', com o que todos eles cumprimentam você,  convidando-o para juntar-se à
    brincadeira.Evidentemente eles estão esperando alguém e confundiram você com o convidado que está faltando."
    menu:
        "Você continua fingindo e junta-se a eles":
            jump tres85
        "Dirá a eles que estão enganados e tentará chegar até a porta do outro lado do aposento":
            jump dois27

label tres85:
    n "Você consegue se enturmar com sucesso e, após algum tempo, conseguirá sair pela porta do outro lado do salão."
    jump tres1

label dois27:
    n "Eles começam a ficar muito zangados com seus modos. Os ânimos se exaltam, e eles começam a gritar."
    n "Repentinamente, você é dominado por eles. Você luta, mas um deles golpeia você na cabeça com o cabo da espada. Sua cabeça roda, e
    o aposento escurece, quando você perde a consciência."
    jump dois34

label dois34:
    hide maguito
    hide leviata
    hide heitoba
    hide salao
    with fade
    scene prisao at truecenter:
        zoom 2.8
    n "Você acorda em um aposento sujo, com paredes ásperas cortadas na rocha. As barras de ferro na janela e na porta confirmam que você está em algum tipo de cela de prisão, conforme você
    desconfiava. Não há muito que você possa fazer, além de ficar sentado no colchão de palha que está em um canto até que alguém apareça."
    n "Mais ou menos uma hora depois, você ouve o barulho de alguma coisa que se arrasta do lado de fora. Olhando através das barras da porta, você pode ver uma
    criatura com aparência de lagarto que se arrasta descendo o corredor, trazendo nas mãos uma moringa e uma terrina."
    show calacorm at center:
        zoom 1.5
    n "O animal tem a pele alaranjada e coberta de escamas, e uma cauda longa se estende pela passagem atrás dele."
    n "Ele para na sua porta e empurra a moringa e a terrina por uma pequena abertura para dentro de sua cela, e depois se afasta para sentar-se a uma mesa do outro lado do corredor. Você recebeu pão e
    caldo."
    hide calacorm with dissolve
    menu:
        "Você vai comer e beber?":
            jump tres97
        "Ou irá chamar esta criatura, um CALACORM?":
            jump seis9

label tres97:
    n "Não é uma refeição muito farta, mas você estava com fome e com sede, sentindo-se renovado."
    n "O que fará em seguida?"
    menu:
        "Usar um Encanto para sair da situação (Teste de Sorte)":
            jump um93
        "Chamar o Calacorm":
            jump seis9

label um93:
    play sound "musics/efeito_sonoro/dados.mp3"

    $ d2017roll = renpy.random.randint(1, 20)

    if (d2017roll>=8):
        $renpy.notify("sucesso de sorte")
        play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
        n "Você oferece a ele as pedrinhas que se transformaram em ouro. Ele desabafa sobre a vida pacata que ele leva na prisão, e, rapidamente te libera de sua cela"
        show calacorm at center:
            zoom 1.5
        jump um74
    else:
        $renpy.notify("fracasso de sorte")
        play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
        n "Infelizmente, já tentaram subornar a criatura, e ela não cai no seu Encanto!"
        jump batalha_calacorm

label seis9:
    n "A criatura não é de muita conversa, mas você consegue descobrir que está nas masmorras dos subterrâneos da Torre Negra e que provavelmente nunca será libertado,
    a não ser que se já dado aos Ganjees para o divertimento deles."
    n "Dessa forma, você se lembra sobre um estudo que você fez e conclui que talvez se a ofendesse, isso te traria uma oportunidade."
    n "De maneira incessante, você consegue atingir seu objetivo e a criatura engaja com você num combate."
    jump batalha_calacorm

label um74:
    n "A porta de saída está logo ali!"
    jump sete

label tres44:
    n "Você desce os degraus. O ar está fresco e estagnado. Há uma porta ao pé da escadaria. Você tentará
    a porta ou subirá as escadas de volta para ir até a porta para o andar térreo?"
    menu:
        "abrir a porta":
            jump sete
        "subir as escadas e voltar":
            jump cinco

label sete:

    n "A porta está trancada. Você pode tentar pô-la abaixo, batendo nela com o ombro, ou
    pode lançar um Encanto da Força sobre você mesmo e tentar arrancar a porta das suas dobradiças."

    menu:
        "bater na porta com o ombro":
            jump dois68
        "usar encanto para arrancar a porta (teste de sorte)":
            play sound "musics/efeito_sonoro/dados.mp3"

            $ d20roll = renpy.random.randint(1, 20)

            $renpy.notify("sucesso de sorte")
            play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
            jump um16

label dois68:

    n"Quando você golpeia a porta, a madeira racha um pouco, mas não cede. Você tenta de novo, e dessa
    vez a madeira se parte ao meio. Você abre caminho e entra no aposento do outro lado."

    jump dois10

label um16:

    n "Suas mãos super poderosas agarram a maçaneta e puxam. Ela sai na sua mão. Você fecha a mão e
    desfere um soco no meio da porta. A madeira racha e quebra, permitindo que você entre no
    aposento do outro lado."

    jump dois10

label dois10:

    play music "musics/Nikos Spiliotis - Love Waltz.mp3"

    scene sala_oseamus at center:
        zoom 1.5

    n "Você agora está em um aposento grande. É Iluminado por algumas tochas, presa a uma
    das paredes. Não há mobília no aposento,exceto uma mesa de madeira rústica e uma cadeira no
    centro."

    show oseamus at center:
        zoom 0.8
        ypos 850

    n "Flutuando acima da mesa - dormindo profundamente - há um homem muito pequeno,
    vestido com pantalonas e camisa. Ele não chega a ter mais de um metro de altura, e você não
    consegue acreditar que ele esteja ainda dormindo depois de sua entrada barulhenta!"

    n "Você ouve um rangido e vira-se para a direita a tempo de ver uma pequena catapulta disparar um projétil de algum
    tipo direto na sua direção. Vai atingir você, a não ser que você use um Encanto do Escudo!"

    menu:
        "usar encanto de escudo (teste de sorte)":

            play sound "musics/efeito_sonoro/dados.mp3"

            $ d2018roll = renpy.random.randint(1, 20)

            if (d2018roll>=12):
                $renpy.notify("sucesso de sorte")
                play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
                n "você lança o encanto com sucesso"
                jump um92
            else:
                $renpy.notify("fracasso de sorte")
                play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
                n "sob pressao do projetil te atingir, você erra algumas palavras do encanto,
                fazendo com que ele seja ineficaz!"
                jump tres59

        "nao usar encanto de escudo":
            jump tres59

label um92:

    play sound "musics/efeito_sonoro/yt1s.com - Tomato Splat Sound Effect.mp3"

    n "Você lança o Encanto bem na hora. O projétil atinge o seu escudo mágico e se espatifa contra ele,
    escorrendo para o solo. Você examina a pasta que ficou no escudo para ver o que era."
    n "Você quase foi atingido por um tomate! No centro do aposento, a figura adormecida está se mexendo."

    jump dois9

label tres59:
    n "Você tenta se esquivar, mas não consegue evitar o impacto em cheio do projétil, que atinge você na
    testa e se derrama por toda a sua cara."

    play sound "musics/efeito_sonoro/yt1s.com - Tomato Splat Sound Effect.mp3"

    n "Você fica imóvel, esperando talvez pelo início de algum tipo de reação ácida, mas o líquido pastoso simplesmente pinga do seu rosto no chão. Cautelosamente,
    você o toca, primeiro com o dedo, depois com a língua."
    n "Você acaba de ser atingido por um tomate maduro! Mais uma vez, você se volta para enfrentar a figura adormecida."

    jump dois9

label dois9:
    n "Cautelosamente, você se aproxima do homenzinho. Ao chegar perto, um único olho se abre e olha
    diretamente no seu rosto. Um sorriso largo se espalha de orelha a orelha na criatura e ela
    desaparece!"
    n "'Bom dia para você!' diz uma vozinha chilreante atrás de você, e, ao voltar-se, você o
    vê ali, ainda sorrindo."
    n "'Sou O'Seamus, o Duende!', ele diz, dando risinhos, e estende a mão para
    você. Ele parece suficientemente amigável - você aperta a mão dele e tenta fazer amizade ou desembainha sua espada?"

    menu:
        "você aperta a mão dele e tenta fazer amizade":
            jump dois71
        "desembainha sua espada":
            jump um31

label dois71:
    n "Você aperta a mão dele e se apresenta - e grita quando os nervos da sua mão e braço ficam
    dormentes! O'Seamus se escangalha de rir. Você está ficando aborrecido, mas o homenzinho continua a
    apertar a sua mão e rir."

    n "Uma risada vem de trás de você, e você se vira e vê o brincalhão flutuando
    no ar, sorrindo. Mas você está ainda apertando a mão dele diante de você... ou não está?"

    n " Na realidade, você compreende agora que está freneticamente apertando a mão de um boneco
    empalhado que balança juntamente com seu braço enquanto você se movimenta.Você atira o
    boneco no chão - mas ele está grudado na sua mão!"

    n "A situação é ridícula, e você está ficando muito
    zangado. 'Só uma brincadeirinha', diz o Duende. 'Agora, o que posso fazer por você?' Você
    perguntará a ele o caminho para seguir adiante ou desembainhará a sua espada?"

    menu:
        "perguntar a ele o caminho":
            jump tres48
        "puxar sua espada!":
            jump um31

label um31:
    n "Você rapidamente desembainha a sua espada, apontando-a na direção do Duende. Ele lança um
    olhar para a lâmina e, para seu horror, ela verga molemente a partir do cabo, pendendo para baixo
    como se fosse um cinto de couro."
    n "Parece que você não irá muito longe agindo com agressividade.
    Talvez seja melhor você perguntar a ele o caminho para seguir adiante."

    jump tres48

label tres48:
    n "'Oh, eu não iria nesta direção', diz O'Seamus. 'Não é uma região agradável.' Estas três portas são
    o único caminho para seguir adiante. Duas delas são muito perigosas, e a terceira tem um cheiro
    muito forte. No lado oposto do aposento, há três portas."
    n " Uma tem uma maçaneta de latão, outra tem uma maçaneta de cobre, e a terceira tem uma maçaneta de bronze. Qual delas você escolherá:"
    n "o que você faz?"
    menu:
        "abrir a porta com maçaneta de latao?":
            jump dois07
        "abrir a porta com maçaneta de cobre?":
            jump dois2
        "abrir a porta com maçaneta de bronze?":
            jump tres54
        "pedir conselho ao doende?":
            jump seis8

label dois07:

    play music "music/yt1s.com - Magic Fantasy Music  The Mystic  Beautiful Violin.mp3"

    scene corredor_escuro at center:
        zoom 3.0

    n "Você abre a porta e espia a escuridão à sua frente. Você dá uns dois passos adiante, dando tempo
    para que seus olhos se acostumem ao escuro. Você fecha a porta atrás de você, dizendo adeus ao
    Duende."

    jump um88

label dois2:

    play music "music/yt1s.com - Magic Fantasy Music  The Mystic  Beautiful Violin.mp3"

    scene corredor_escuro at center:
        zoom 3.0

    n "Você abre a porta e sai em um corredor longo e escuro."

    jump um88

label tres54:

    play music "music/yt1s.com - Magic Fantasy Music  The Mystic  Beautiful Violin.mp3"

    scene corredor_escuro at center:
        zoom 3.0

    n "Você abre a porta e entra em outro aposento, feliz por ter deixado para trás a aborrecida criaturinha."

    jump um88

label seis8:
    n "'Por qual eu iria, hein?' ele considera. 'Vamos ver... eu não iria por uma das duas portas à esquerda
    da porta de maçaneta de cobre, nem a porta à direita da de maçaneta de bronze.' Qual delas você
    escolherá:"

    menu:
        "abrir a porta com maçaneta de latao?":
            jump dois07
        "abrir a porta com maçaneta de cobre?":
            jump dois2
        "abrir a porta com maçaneta de bronze?":
            jump tres54

label um88:

    scene corredor_escuro at center:
        zoom 3.0
    with flash

    n "Um clarão de luz súbito e intenso irrompe à sua frente. Você protege os olhos e depois os esfrega -
    mas não consegue ver nada!"
    n "Você entra em pânico ao ouvir um ruído como um rosnado baixo.
    Passos de pés peludos se aproximam, e você grita de dor quando esta criatura que você não pode
    ver ruge e crava seus dentes aguçados na sua perna.Você:"
    menu:
        "usa encanto de fraqueza? (teste de sorte)":
            play sound "musics/efeito_sonoro/dados.mp3"

            $ d2019roll = renpy.random.randint(1, 20)

            if (d2019roll>=14):
                $renpy.notify("sucesso de sorte")
                play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
                n "você lança o encanto com sucesso"

                jump um59
            else:
                $renpy.notify("fracasso de sorte")
                play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
                n "sob o efeito da dor extrema, você erra o feitiço, tornando a criatura mais forte ao inves de fraca!"

                jump dois80
        "puxa sua espada para atacar?":
            jump cinco1

label um59:
    n "Você lança seu Feitiço da Fraqueza e deixa transcorrer um tempo na esperança de que a força da
    criatura diminua. Mas, como seus dentes continuam a ferir você, você fica desalentado ao descobrir
    que o ataque da criatura está cada vez mais feroz. Você já não consegue sentir a perna."
    n "A dor é intensa. Você se sente fraco e perde a consciência quando as mandíbulas se fecham na sua garganta."
    jump tres23

label dois80:
    n "A criatura está atacando você impiedosamente, e não há nada que você possa fazer para evitar isso.
    Sua perna está coberta de sangue, e a dor é arrasadora. Você luta com a cabeça que não está vendo,
    mas não adianta nada."

    n "A criatura salta sobre o seu pescoço, e sua última lembrança, antes de perder
    os sentidos, é de suas mandíbulas se fechando sobre a sua garganta."

    jump tres23

label cinco1:
    n "Você distribui loucamente golpes com sua espada, mas não consegue atingir a criatura. Ou ela é
    extremamente rápida, ou não possui um corpo sólido que possa ser atingido."

    n "Seus dentes estão agora rasgando a sua carne, e você sente sangue na perna. Você terá que se proteger com sua
    mágica ou enfrentar uma morte certa, trazida por esta criatura que não se vê. Você lançará um Encanto da Fraqueza ou aceitará seu destino?"

    menu:
        "usar encanto de fraqueza? (teste de sorte)":
            play sound "musics/efeito_sonoro/dados.mp3"

            $ d2020roll = renpy.random.randint(1, 20)

            if (d2020roll>=14):
                $renpy.notify("sucesso de sorte")
                play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
                n "você lança o encanto com sucesso"

                jump um59
            else:
                $renpy.notify("fracasso de sorte")
                play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
                n "sob o efeito da dor extrema, você erra o feitiço, tornando a criatura mais forte ao inves de fraca!"

                jump dois80
        "aceitar seu destino e não resistir":
            jump dois80

label tres23:

    scene sala_oseamus at center:
        zoom 1.5

    show oseamus at center:
        zoom 0.8
        ypos 850
    with dissolve
    play music "musics/Nikos Spiliotis - Love Waltz.mp3"

    n "Você desperta e olha em torno de si. À medida que sua memória volta, você fica admirado de estar
    vendo. A sua perna está sensível, mas não há ferimento!"

    n "Você ouve um risinho frouxo vindo de um
    lugar acima de você e subitamente a coisa toda faz sentido..."

    n "Autuando acima de você está O'Seamus, agora rindo alto. A coisa toda foi uma grande brincadeira!
    Você fica furioso e salta de pé, mas, ao olhar para o engraçado homenzinho que rola pelo ar em
    gargalhadas histéricas, você não outra opção a não ser ver o lado engraçado da coisa também."
    n "Você dá um risinho, depois mais uma risada, e acaba rindo alto. Por algum tempo, vocês dois se acabam
    de dar gargalhadas, até que as lágrimas rolam pelos seus rostos."

    n "Quando os dois conseguem se controlar, vocês acabam se sentando para conversar. Ele é um
    homenzinho agradável. Antes de você sair, ele diz: 'Você é realmente um cara legal. O caminho à
    sua frente, porém, está cheio de perigos. Mas talvez isto possa ajudá-lo.'"
    n " Com um movimento da mão, ele faz com que apareça um prato na mesa. O prato é, na realidade, um Espelho de Prata de excelente
    qualidade. Saia do aposento pela:"

    $renpy.notify("adquiriu espelho!")

    play sound "musics/efeito_sonoro/item encontrado.mp3"

    $espelho = True

    menu sala_oseamus:
        "abrir a porta com maçaneta de latao?":
            jump tres86

        "abrir a porta com maçaneta de cobre?":
            jump um44

        "abrir a porta com maçaneta de bronze?":
            jump tres38

label tres86:

    scene esgoto at center:
    play music "musics/passagem esgoto.mp3"

    n "Do lado de fora da porta, a passagem continua em declive, e você a segue por algum tempo. Você
    repara que há um cheiro desagradável que fica cada vez mais forte à medida que você avança.
    Afinal, você chega a uma abertura."
    n "Olhando por ela, e tapando o nariz, você pode ver um grande
    esgoto a descoberto que corre transversalmente à passagem. Há uma corda que pende do teto."
    n "Você atravessará o esgoto ou tentará agarrar a corda e se valer dela para passar para o
    outro lado?"
    menu:
        "atravessar o esgoto?":
            jump dois04
        "agarrar a corda e se balançar para o outro lado?":
            jump um08

label um44:
    scene bg13 at truecenter:
        zoom 0.7
    play music "musics/adega.mp3"
    n "A porta abre e você entra em um corredor estreito. Você segue por ele algum tempo, até que
    finalmente chega a uma outra porta: desta vez é uma porta larga entalhada, com a inscrição 'Adega
    de Vinhos' gravada nela."
    n "Você experimenta a maçaneta e ela abre. Você espia do lado de dentro, esticando o pescoço,
    e vê filas e mais filas de prateleiras cheias de garrafas contendo... vinho? O
    aposento é pouco iluminado pela luz de várias velas."
    n "O fato de você abrir a porta fez com que uma
    pequena sineta soasse, e uma figura vem na sua direção por um dos corredores. Assim, você:"
    scene bg14 at truecenter:
        zoom 1.09
    show elfo_negro at center:
        zoom 0.8
    with dissolve
    menu:
        "Desembainhará a sua espada e se preparará para se defender":
            jump um54
        "Verá o que este sujeito pode ter a dizer":
            jump cinco6

label cinco6:
    n "O Elfo Negro que se aproxima de você é bem vestido. Ele pergunta se você é um
    convidado ou um aventureiro. Você diz que é um convidado que veio até embaixo para provar o
    vinho que ele guarda em sua famosa Adega de Vinhos."
    n "Com um certo orgulho, ele mostra a você as garrafas de safras que ele guarda para seu Senhor, o Feiticeiro.
    Algumas delas, ele afirma, possuem poderes mágicos. Ele pergunta se você não quer experimentar o vinho. Você prefere: "
    menu:
        "Provar o vinho tinto":
            jump um20
        "Provar o vinho rosé":
            jump tres34
        "Recusar a oferta dele e seguir adiante no seu caminho":
            jump nove5

label um20:
    n "Você prova o vinho e balança a cabeça afirmativamente. A safra é excelente de fato, com um sabor
    revigorante e rico. Você agradece ao Elfo e segue adiante."
    jump nove5

label tres34:
    n "Você toma dois goles. Não é ruim! Você enche a boca, mas, ao fazê-lo, fica imaginando porque o
    Elfo está rindo. De repente, ele pergunta se você é realmente um convidado."
    n "Embora sua mente esteja confirmando que você é de fato um convidado, sua voz está dizendo que não é, que você veio
    para pôr um fim nos planos de conquista de Balthus Dire! Você pragueja ao compreender que o
    vinho deve conter uma dose de Soro da Verdade."
    n "O Elfo Negro agora sabe da sua missão e deve ser impedido de dizer a outros.
    Você desembainha a sua espada e, ao fazê-lo, ele puxa um pequeno mecanismo metálico da bolsa presa em volta da cintura dele.
    Com um toque, isso se transforma em uma arma de lâmina em serra."
    jump dois75

label nove5:
    n "No lado mais distante da Adega de Vinhos, há uma porta de madeira, que você experimenta. Ela
    abre para uma passagem que conduz adiante por vários metros."
    jump tres67

label um54:
    n "Quando você puxa a espada, a figura para e pega alguma coisa da bolsa em sua cintura. Quando ele
    se aproxima mais, você pode ver que a criatura é um ELFO NEGRO; alto e magro."
    n "Na sua mão, ele traz um pequeno mecanismo de algum tipo.
    Ele vê você, manipula o mecanismo que subitamente se torna uma espada tipo estilete
    na sua mão! Você escolherá:"
    menu:
        "Avançar e lutar":
            jump dois75
        "Abaixar a espada e conversar com ele":
            jump cinco6

label dois75:
    n "Você reconhece o mecanismo como sendo uma Miríade de Bolso, um objeto encantado que pode se
    transformar em qualquer tipo de armas e outros artefatos úteis. Vocês dois se preparam para a
    batalha."
    jump batalha_elfo_negro

label dois72:
    $renpy.notify("dinheiro e miríade pilhados")
    play sound "musics/efeito_sonoro/item encontrado.mp3"
    play music "musics/'descoberta'.mp3"
    n "Você revista os bolsos dele e encontra oito Peças de Ouro. A Miríade de Bolso infelizmente foi
    danificada na luta, mas talvez você possa encontrar algum uso para ela, podendo levá-la com você. Você irá:"
    menu:
        "Investigar a Adega dos Vinhos":
            jump dois42
        "Atravessá-la e seguir adiante pela porta do outro lado do aposento":
            jump nove5

label dois42:
    n "As garrafas e barriletes contêm centenas de diferentes vinhos. Alguns são extremamente velhos e
    valiosos. Em um dos cantos do aposento, há uma mesa posta para a degustação, com duas garrafas e copos. Você irá:"
    menu:
        "Provar uma amostra do vinho tinto":
            jump dois4
        "Provar uma amostra do vinho branco":
            jump um05
        "Seguir adiante e não provar nenhum vinho":
            jump nove5

label dois4:
    n "Você prova o vinho e, enquanto está apreciando o seu sabor, ouve um ruído tilintante. Você se vira
    para olhar na direção de onde o ruído está vindo e fica horrorizado ao ver que as garrafas nas
    prateleiras estão se mexendo sozinhas."
    n "Uma garrafa voa do lugar onde está e se projeta na sua
    direção, errando por pouco a sua cabeça e se espatifando na parede atrás de você. Uma outra voa na
    sua direção, depois outra, até que você está recebendo uma chuva de garrafas vindas de todas as
    direções."
    n "Você toma consciência de que sua única defesa é usar o Encanto do Escudo."
    menu:
        "Usar Encanto do Escudo":
            jump tres72
        "Não usar Encanto do Escudo":
            jump dois19

label tres72:
    n "Ao lançar seu Encanto do Escudo, uma garrafa ainda atinge você no ombro. Você não sente nada.
    Alguma coisa não está muito certa, e você tenta cancelar o Encanto. Infelizmente, ele já foi lançado,
    e você pode ver as garrafas se quebrando de encontro a seu escudo mágico."
    n "A garrafa que acabou de atingir você desapareceu. Você xinga ao compreender que o vinho que você acabou de provar
    deveria ter algumas propriedades alucinógenas, e que você está imaginando o ataque das garrafas.
    Quando esta idéia lhe ocorre, as garrafas param de vir sobre você."
    n "Você pisca e olha de novo. Todas as garrafas estão em seus lugares nas estantes, como é normal!
    Você resolve seguir adiante."
    jump nove5

label dois19:
    n "Você se abaixa e protege a cabeça. Uma garrafa atinge você, depois outra e mais outra - mas você
    não sente nada! Como pode ser isso? Aí você compreende o que está acontecendo. O vinho devia
    conter alguma poção alucinógena que está fazendo você imaginar este ataque de garrafas."
    n "Num instante, o ruído cessa. Você levanta a cabeça para ver que, como você desconfiava, todas as
    garrafas estão em seus lugares nas estantes. Com grande alívio, você segue adiante e sai da Adega
    de Vinhos."
    jump nove5

label um05:
    n "O vinho é bastante amargo e, ao saboreá-lo em sua boca, você sente uma sensação de ardência.
    Você cospe o vinho no chão e, para sua surpresa, um jato de chamas irrompe dos seus lábios!"
    n "Você segue adiante na direção de uma porta que
    leva mais para o interior da adega."
    jump nove5

label tres38:
    n "A porta abre para uma passagem. Você segue a passagem sempre em frente por algum tempo,
    passando por muitas curvas na rocha. Você encontra outra passagem que vem da direita, mas segue
    adiante direto. Finalmente, o caminho acaba se alargando."
    jump nove0

label nove0:
    scene bg15 at truecenter:
        zoom 2.4
    with dissolve
    show mulher_roupa at right:
        zoom 0.41
        xpos 1500
    with dissolve
    n "A passagem se alarga, e você está agora andando ao longo de um rio que corre. Bem à frente, há
    uma mulher que parece estar lavando roupa."
    n "Ela tem uma cesta com roupas a seu lado, e há vários conjuntos de ceroula e camiseta de baixo
    pendurados em um varal atrás dela. Você:"

    play music "musics/medo.mp3"

    menu:
        "Desembainhará a sua espada e avançará":
            jump um76
        "Cumprimentará ela e tentará estabelecer uma conversa":
            jump dois1
        "Usará a sua percepção Extra-Sensorial para descobrir quem ela é":
            jump tres29

label um76:
    n "Quando você se aproxima, ela se volta para olhar para você. Sem se perturbar nem um pouco com a
    sua arma, ela diz: 'Abaixe sua arma, jovem forasteiro. Sou apenas uma velha. Não farei mal a você.' Você irá:"
    menu:
        "Ignorar as palavras dela e continuar avançando":
            jump um27
        "Abaixar a espada e conversar com ela":
            jump dois1
        "Parar e usar um Encanto de Percepção Extra-Sensorial":
            jump tres29

label dois1:
    n "'O que traz você a estas paragens?' ela pergunta. Você conta a ela sua história, evitando
    cuidadosamente revelar a sua verdadeira missão. Ela aconselha você a afastar-se desse lugar, caso
    conheça alguma magia."
    n "As criaturas que você encontrou até agora não se comparam com as que
    habitam o interior da Torre da Cidadela propriamente dita. Ela diz que você jamais encontrará o
    senhor sem conseguir primeiro o Velo e deseja sorte para você em sua missão."
    jump seis

label tres29:
    n "Você se concentra na mente dela e fica chocada ao descobrir que ela não está viva, como parece,
    mas que já morreu há muitos anos."
    n "Desde que um incêndio violento - uma maldição lançada sobre ela por Balthus Dire em pessoa, por ela
    não ter cumprido as ordens de lavar suas vestes a tempo para uma reunião importante - matou-a e às suas crianças,
    seu corpo espectral foi condenado a lavar roupas eternamente."
    n "Ela é de fato uma pobre miserável. Você agora repara que ela está ficando
    zangada e desconfiada com a sua presença. Ela está murmurando alguma cantilena muito baixo. Você irá: "
    menu:
        "Tentar conversar com ela":
            jump dois1
        "Tentar passar rapidamente por ela seguindo o caminho":
            jump dois21

label dois21:
    n "Quando você se adianta, ela faz um gesto peculiar com as mãos e abaixa a cabeça, resmungando
    muito baixo."
    jump um27

label um27:
    n "Ela levanta a cabeça e solta um chamado no ar e você interrompe seus passos."
    show fantasmagorico at right:
        zoom 2.0
        ypos 640
    with dissolve
    n "Após o ar ficar muito forte, você consegue distinguir um corpo fantasmagórico com rosto há muito já morto.
    'Proteja-me, meu filho!' ela grita, e de repente ele cerca você."
    n "Ele te ataca com pancadas de ar, que causam uma ardência dolorosa. O par de braços dele se enrosca em torno
    de seu pescoço, tornando a respiração difícil e apertando cada vez mais."
    n "Você distribui golpes com sua espada, mas isso causa pouco dano ao Fantasma. O aperto o estrangula cada vez mais, e você terá que usar a sua
    magia para se libertar, a não ser que tenha alguma coisa em sua mochila para oferecer à mulher. Você:"

    menu:
        "Oferecerá um Espelho de Prata a ela":
            if (espelho == True):
                $espelho = False
                $renpy.notify("item removido!")
                play sound "musics/efeito_sonoro/item perdido.mp3"
                jump tres87

            else:
                play sound "musics/efeito_sonoro/nao tem o item.mp3"
                $renpy.notify("você não possui esse item!")
                n "Ela fica irritada pois acha que você tentou enganá-la.
                Assim, o fantasma parte para cima e você desembainha sua espada"
                jump batalha_fantasmas

        "Usará um Encanto do Fogo (teste de sorte)":
            $ d2099roll = renpy.random.randint(1, 20)

            if (d2099roll>= 13):
                $renpy.notify("sucesso de sorte")
                play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
                n "você teve sucesso ao lançar o encanto"
                play sound "musics/efeito_sonoro/bola de fogo.mp3"
                jump dois40

            else:
                $renpy.notify("fracasso de sorte")
                play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
                n "Você não teve sucesso ao lançar o encanto"
                n "se prepare para lutar!"
                jump batalha_fantasmas
        "Desembainhará a sua espada":
            jump batalha_fantasmas

label tres87:
    n "À simples menção de um Espelho de Prata, ela se levanta, ergue as mãos e ordena ao Fantasma
    que pare. Você dá a ela o Espelho, e ela diz que você pode seguir o seu caminho. Você tem sorte
    de estar vivo."
    jump seis

label dois40:
    n "Você ergue uma mão flamejante, passando-a pelas costas do fantasma, que está apertando seu
    pescoço. A roupa se incendeia, e um grito silencioso sai da boca morta dentro dela. O
    Fantasma recua. Você ateia mais fogo enquanto ele bate em retirada."
    n "Andando cuidadosamente para a frente, você mantém o Fantasma à distância até passar em
    segurança pela mulher."
    jump seis

label seis:
    n "O caminho segue ao longo do rio por vários metros e depois volta a penetrar na rocha. Você segue o
    caminho por algum tempo."
    jump tres67

label um08:
    n "Você agarra a corda firmemente, recua e toma impulso na direção do rio pútrido. Subitamente, a
    corda passa a se movimentar e se contorcer com vontade própria! Você a larga rapidamente e cai no
    chão."
    show cobra_esgoto at truecenter
    n "A corda cai por cima de você e se enrola em volta de você. Você compreende que não é uma
    corda, mas, na realidade, uma longa COBRA DE ESGOTO, que se enrosca em torno do seu corpo e
    de seu pescoço."

    jump sete3

label sete3:
    n "voce pode lutar contra a criatura ou usar um encanto"
    menu:
        "preparar para lutar?":
            jump batalha_cobras
        "usar encanto de fogo? (teste de sorte)":

            $ d2021roll = renpy.random.randint(1, 20)

            if (d2021roll>= 12):
                $renpy.notify("sucesso de sorte")
                play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
                n "você teve sucesso ao lançar o encanto e as chamas vao em direção à cobra do esgoto"
                play sound "musics/efeito_sonoro/bola de fogo.mp3"
                jump dois82

            else:
                $renpy.notify("fracasso de sorte")
                play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
                n "Você não teve sucesso ao lançar o encanto e a cobra continua a pressionar seu pescoço"
                n "se prepare para lutar!"
                jump batalha_cobras

label dois82:
    n "Você lança uma pequena bola de fogo diretamente sobre a Cobra de Esgoto, que queima seu corpo,
    cortando-a em duas metades. As duas metades agora atacam você e estão esmagando o seu peito."
    n "Tentando uma estratégia diferente, você cria chamas que
    queimam em cada mão e as esfrega sobre os anéis de seu corpo enroscado. A criatura se contorce
    violentamente e afrouxa a pressão!"
    n "Você encontra sua cabeça e a espreme com as suas mãos
    flamejantes, queimando-a fatalmente."
    jump um12

label dois04:
    n "Você prende a respiração e dá um passo adiante, entrando na água lodosa. Pouco depois, você sente
    alguma coisa puxando a sua perna. Levantando a perna da água, você descobre que algum tipo de
    trepadeira se enroscou na sua perna."
    n "Você salta de volta para a margem, e a trepadeira continua agarrada. Saindo da água, uma das pontas da trepadeira se ergue, contorce-se no ar, como se
    estivesse olhando para você, e depois cai na água de volta com estrépito."
    show cobra_esgoto at truecenter
    n "Você compreende que não é uma trepadeira, mas sim uma longa COBRA DE ESGOTO, que agora está deslizando na sua
    direção."
    jump sete3

label um12:

    n "Você se desvencilha da Cobra de Esgoto morta e tenta atravessar a água. Você chega do outro lado
    sem maiores incidentes, mas está com certeza ansioso para tomar um banho rápido!"

    hide cobra_esgoto
    play music "musics/yt1s.com - D J Pinto  Tension EpicOrchestralCinematicMFY  No Copyright Music.mp3"

    n " Você continua ao longo da passagem até chegar a uma encruzilhada, onde pode seguir em frente ou tomar a
    passagem da esquerda."
    menu cobra:
        "ir para a esquerda?":
            jump dois12
        "seguir em frente?":
            jump tres67

label dois12:
    n "Tomando a bifurcação da esquerda, você segue um caminho que acaba por se juntar a uma outra
    passagem que conduz para a direção norte. Você segue este novo caminho por algum tempo, até
    que ele acaba por se alargar."
    jump nove0

label tres67:
    scene passagem_esgoto at center:
        zoom 2.0

    n "Alguma distância adiante na passagem, você chega a uma junção de quatro caminhos. Você toma o
    caminho do norte, que acaba chegando a uma grande porta de madeira."
    n "Você não consegue ouvir nada escutando pelo buraco da fechadura. Você tentará abrir a porta lentamente e sem ruído ou derrubá-la à força?"
    menu:
        "abrir a porta com cautela?":
            jump tres08
        "abrir a porta na força?":
            jump um21

label tres08:

    n "A maçaneta gira e você entra em um cômodo às escuras."
    jump dois57

label um21:

    n "Quando você parte para a porta, ela abre repentinamente à sua frente. Impossibilitado de travar seu
    impulso, você entra pelo aposento de cabeça e acaba tropeçando e rolando pelo chão até parar."
    jump dois57

label dois57:

    scene sala_golem:
        zoom 1.3

    show pedroso:
        ypos 100
        zoom 1.5
    with dissolve

    n "Você olha à sua volta no aposento. Está iluminado somente pela sua tocha. Embora seja um
    aposento bastante grande, possui pouca mobília, com apenas uma grande rocha, cortada de modo a
    servir de mesa, e uma rocha menor com o formato de uma banqueta."
    n "Em um dos cantos, há uma pilha de rochas unidas por uma camada de lama. Você não consegue imaginar qual é a serventia
    disso, embora haja três arcas de madeira sobre ela. Então, você pula de susto quando sua tocha
    ilumina uma grande criatura, aparentemente também ela própria feita de rocha, de pé junto a uma
    porta."
    n "Possui aproximadamente uma forma humana, ainda que um tanto maior. Seus olhos estão
    dirigidos diretamente para você, mas você não consegue ter certeza de que ela esteja de fato vendo
    você! Você:"
    menu sala_golem:
        "correr para a porta do outro lado do aposento?":
            jump dois37

        "tentar falar com a criatura?":
            jump tres57

        "avançar lentamente na direção das caixas no canto?":
            jump dois00

label dois37:

    n "Você abre a porta e sai em uma passagem que segue na direção leste por vários metros, terminando
    ao pé de uma escadaria. Você sobe as escadas e acaba chegando em uma passagem estreita."
    n "A uma pequena distância mais adiante, você pode ver uma abertura para um aposento grande e bem
    iluminado. Você segue nessa direção."

    jump um69

label tres57:
    n "A criatura é aparentemente surda-muda. Você a saúda em todas as línguas que conhece, mas ela
    continua de pé em silêncio. Você se desloca na direção do centro do aposento."
    jump dois00

label dois00:
    n "Ao seu primeiro movimento, a criatura parece sair de seu transe e caminha na sua direção. Ao ver
    isso, você irá:"
    menu:
        "Correr para a porta do outro lado do aposento":
            jump dois37
        "partir na direção das caixas e arriscar-se a enfrentar este gigante silencioso":
            jump nove8

label nove8:
    n "O Golem que avança na sua direção é uma criatura que se move com lentidão, e você alcança
    facilmente as caixas. Enquanto você luta com as fechaduras, o Golem chega até você. Você pode:"
    menu:
        "Desembainhar a sua espada e lutar contra a criatura":

            $ oponente_max_hp = 60
            $ oponente_hp = oponente_max_hp

            jump batalha_golem
        "Lançar um Encanto de Cópia de Criatura (teste de sorte)":
            $ d2098roll = renpy.random.randint(1, 20)

            if (d2098roll>= 14):
                $renpy.notify("sucesso de sorte")
                play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
                n "durante a conjuração da criatura, você se confunde colocando algumas palavras elementais junto ao encanto!"
                n "dessa forma, o seu golem sofreu uma transformação, se tornando um elemental misto de eletricidade e fogo!"
                jump batalha_golem_vs_golem
            else:
                $renpy.notify("fracasso de sorte")
                play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
                n "Você errou uma palavra do encanto e o golem parte para cima!"

                $ oponente_max_hp = 60
                $ oponente_hp = oponente_max_hp

                jump batalha_golem
        "Deixar as caixas de lado e correr para a porta":
            jump dois37

label um47:

    play music "musics/yt1s.com - Magic Fantasy Music  The Mystic  Beautiful Violin.mp3"

    n "O Golem desaba no chão e se parte em pedaços. Aliviado, você anda até as caixas e as examina.
    Você tentará abrir:"
    menu:
        "A primeira caixa":
            jump dois60
        "A segunda caixa":
            jump um29

label um29:
    n "Você luta com a caixa por algum tempo, tentando abri-la. Então puxa a espada e a golpeia,
    mas a única coisa que consegue é fazer sua espada perder o fio. Você não consegue abrir a caixa. O que irá fazer?: "
    menu:
        "Tentar abrir a primeira caixa":
            jump dois60
        "Deixar as caixas de lado e seguirá em frente":
            jump dois37

label dois60:
    n "Depois de alguma insistência, a caixa abre. Há uma chave de prata lá dentro. Você:"
    menu:
        "Tentará usar a chave na segunda caixa":
            jump tres4
        "Pegará a chave e partirá para a porta de saída?":
            jump dois37

label tres4:
    n "A chave gira e, retirando a tranca, você abre a caixa, encontrando outra chave, dessa vez talhada em
    um metal verde cintilante. Você irá:"
    menu:
        "Explorar um pouco mais o quarto":
            jump oito9
        "Sair do aposento com as duas chaves":
            jump dois37

label oito9:
    n "Lá dentro há um vidro grande que
    contém uma aranha. Mas não é uma aranha comum; esta criatura tem o rosto de um velho. Ele está
    falando com você, mas você não consegue entender o que ele está dizendo."
    n "Um barulho chama a sua atenção, você se vira e vê que a porta por onde você entrou está começando a abrir.
    Você põe o vidro na sua mochila e parte para a outra porta."
    $renpy.notify("aranha no frasco adquirida!!!")
    play sound "musics/efeito_sonoro/item encontrado.mp3"
    $aranha_garrafa = True
    jump dois37

label um69:

    scene sala_jantar
    n "O aposento em que você está é uma espécie de grande salão de jantar. Uma mesa longa, de tamanho
    suficiente para que quarenta ou cinquenta pessoas sentem, ocupa o centro, ladeada por cadeiras."
    n "Há várias portas e passagens que dão saída do aposento, mas você está particularmente interessado em
    duas escadarias largas que levam, uma por cada um dos lados, até uma sacada no alto de onde se
    pode observar o salão."
    n "Quadros e armaduras decoram as paredes. O aposento está vazio. Você:"
    menu:
        "toma escadaria do lado esquerdo e sobe?":
            jump um9
        "toma escadaria do lado direito e sobe?":
            jump um97
        "investiga os quadros?":
            jump tres17
        "investiga as armaduras?":
            jump um51

label um9:

    n "A escada geme quando você põe o pé nela. Você tenta subir o mais silenciosamente possível, mas a
    madeira velha range sob o seu peso."
    n "De repente, um dos degraus estala, como se acionasse um
    dispositivo de algum tipo. Para sua surpresa, todos os degraus: viram para baixo! Você está agora
    de pé em uma rampa lisa e inclinadíssima! Por mais que você tente, não consegue manter o
    equilíbrio e acaba escorregando pela rampa, rolando de ponta cabeça."
    n "Se você quiser usar um
    Encanto da Levitação, poderá voar e descer, fora de perigo, na sacada em cima."
    menu:
        "usar encanto de levitação? (teste de sorte)":
            $ d2022roll = renpy.random.randint(1, 20)

            if (d2022roll>= 13):
                $renpy.notify("sucesso de sorte")
                play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
                n "Você obteve sucesso ao conjurar o encanto e consegue subir a rampa!"
                jump tres63

            else:
                $renpy.notify("fracasso de sorte")
                play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
                n "Você errou uma palavra do encanto e começa a escorregar pela rampa mais rapido que o normal!"
                jump dois54

        "nao usar o encanto?":
            jump dois54

label dois54:

    n "Você rola escada abaixo, atravessa o aposento e finalmente se choca contra a parede do outro lado
    do salão. Você torce o cotovelo seriamente.depois sobe pela outra escadaria."

    jump um97

label um97:

    n "As escadas estão bastante gastas e estalam sob o seu peso. Cuidadosamente, você sobe até a sacada."
    jump tres63

label tres17:
    n "Os quadros são retratos de vários Senhores e Condes de destaque no Reino da Rocha Escarpada.
    Atrás de uma cadeira, na cabeceira da mesa, há um retrato do próprio Balthus Dire."

    show balthus normal at center:
        zoom 0.7
    with dissolve

    n "Ele realmente aparenta ser um adversário poderoso. Você pode agora continuar pela escadaria do lado esquerdo, ou pela escadaria do lado direito."
    hide balthus

    menu:
        "ir pela escadaria da esquerda?":
            jump um9
        "ir pela escadaria da direita?":
            jump um97

label um51:
    n "Os conjuntos de armaduras são de vários tamanhos e formatos, e você fica arrepiado de pensar nas
    criaturas estranhas para as quais eles devem ter sido feitos; talvez você ainda encontre algumas
    delas."
    n "Ao examinar um conjunto particularmente suntuoso, a manopla dele subitamente se ergue e
    bate forte em seu rosto! Você cambaleia para trás, cuspindo sangue."
    n "Mas a armadura não se mexe mais, e você resolve que pode ser prudente continuar
    subindo, seja pela escada do lado esquerdo ou pela escada do lado direito."
    menu:
        "ir pela escadaria da esquerda?":
            jump um9
        "ir pela escadaria da direita?":
            jump um97

label tres63:

    scene portais at center:
        zoom 2.0

    play music "musics/easter egg.mp3"

    n "Há três portais ao longo da sacada."

    n "você nota um estranho desenho de um pássaro, semelhante a uma andorinha, perto dos portais, o que será que ele significa?"

    n "Você experimentará:"
    menu portais:
        "o portal da esquerda?":
            jump dois28
        "o portal do centro?":
            jump seis4
        "o portal da direita?":
            jump tres04

label dois28:

    n "A porta trancada é muito forte e feita de carvalho sólido. Não é provável que você consiga arrombá-
    la, mas você pode tentar."
    n "Do contrário, você pode usar um Encanto da Força para arrebentá-la. A
    fechadura é de cobre, e você poderia tentar usar uma Chave de Cobre, se tiver uma. O que você
    escolherá:"

    menu porta:
        "tentar arrombar? (teste de sorte)":
            $ d2023roll = renpy.random.randint(1, 20)

            if (d2023roll>= 15):
                $renpy.notify("sucesso de sorte")
                play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
                n "a porta abre e voce acessa a sala!"
                jump dois92
            else:
                $renpy.notify("fracasso de sorte")
                play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
                n "você nao conseguiu abrir a porta e volta para a porta do centro"
                jump seis4
        "usar encanto de força? (teste de sorte)":
            $ d2024roll = renpy.random.randint(1, 20)

            if (d2024roll>= 6):
                $renpy.notify("sucesso de sorte")
                play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
                n "a porta abre e voce acessa a sala!"
                jump dois92
            else:
                $renpy.notify("fracasso de sorte")
                play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
                n "você nao conseguiu abrir a porta e volta para a porta do centro"
                jump seis4

        "usar chave de cobre?":
            if (chave_cobre == True):
                n "a chave gira e a porta abre!"
                jump dois92
            else:
                play sound "musics/efeito_sonoro/nao tem o item.mp3"
                $renpy.notify("você não possui esse item!")
                jump porta

label seis4:

    scene portais at center:
        zoom 2.0

    play music "musics/rota djonga.mp3"

    n "Você ouve junto à porta e consegue escutar vozes esganiçadas rindo e brigando. Você experimenta
    a maçaneta e a porta abre. O lado de dentro é um aposento de cores vivas."
    scene quarto_goblin

    n "Há umas poucas camas pequenas em um canto, e, espalhados pelo chão, há pequenos bonecos de várias criaturas brutas.
    Junto à parede do lado direito há uma caixa, e logo adiante da caixa uma porta."

    show goblins at center:
    with dissolve

    play sound "musics/efeito_sonoro/risada goblin.mp3"

    n "No meio do assoalho, e olhando para você com curiosidade, estão algumas pequenas criaturas. Têm aparência
    humana, mas possuem pele verde, orelhas pontudas e olhos muito apertados. Qual será a sua
    atitude? Você:"
    menu portal_centro:
        "Desembainhará a sua espada e se preparará para lutar contra eles?":
            jump dois86
        "oferecer um punhado de amoras para eles?":
            if(amoras):
                jump tres
            else:
                play sound "musics/efeito_sonoro/nao tem o item.mp3"
                $renpy.notify("você não possui esse item!")
                jump portal_centro
        "Caminhará confiantemente através do aposento para a porta do outro lado?":
            jump tres66

label dois86:

    n "As pequenas criaturas guincham e se amontoam quando você se aproxima. Você passa todas a fio
    de espada, mas eles não oferecem nenhuma resistência!"

    $ morte_goblins = True

    $renpy.notify("nossa você realmente fez isso...")

    $renpy.notify("os arautos vão se lembrar da sua escolha...")

    n "Você fica um pouco desconfiado com essa
    batalha tão fácil e dirige-se para a porta do outro lado do aposento."
    jump um40

label tres:
    n "Eles aceitam as suas Amoras de bom grado, jogando-as para dentro da boca e mastigando. Alguns
    segundos depois, eles adormecem um por um."
    n "Quando todos os três estão dormindo, você caminha
    até a caixa para investigar. A tampa se abre, revelando diversas outras bonecas do lado de dentro,
    iguais às que estão no chão, e vários outros brinquedos de madeira."
    n "Não parece haver nada
    verdadeiramente de valor ali, por isso você sai do aposento pela porta do outro lado."
    jump um40

label tres66:
    n "Quando você passa pelas pequenas criaturas, elas ficam olhando para você silenciosamente. Elas
    parecem simplesmente achar que você é interessante. Você sente que alguma coisa não vai bem por
    aqui."

    jump um40

label um40:

    play music "musics/'descoberta'.mp3"

    scene escadas at center

    n "Você sai do aposento e segue por um corredor curto. Alguns metros adiante, você se encontra ao pé
    de uma escada. É uma escada em espiral que leva diretamente ao interior da Torre da Cidadela."
    n "Você sobe os degraus cautelosamente e acaba chegando em uma pequena plataforma com duas
    portas à sua frente. você testa a porta da direita primeiro, esta que esta extremamente emperrada, apenas lhe restando seguir pela esquerda"
    jump um82

label um82:

    scene quarto_escuro at center:
        zoom 1.5

    play music "musics/medo.mp3" volume 2.0

    n "Você se sente sugado para o interior do aposento. Como que por um passe de mágica, sua tocha
    tremula e se apaga. O aposento está escuro como breu. De nenhum lugar, mas ainda assim de toda
    parte, vem um riso de escárnio que enche o aposento."
    n "'Aventureiro tolo', diz uma outra voz, que altera o tom de alto para baixo enquanto fala, 'Bem-vindo à casa dos GANJEES! Infelizmente, será
    o último lugar que você verá na sua vida... Ah, mas é claro, você não está vendo nada, está?"
    n "' Mas nós estamos vendo você, não estamos irmãos?' Vozes que riem chegam de toda parte à sua volta.
    De repente, um rosto luminoso, branco e fantasmagórico, vem voando na sua direção."

    show ganjee at truecenter
    with dissolve

    play sound "musics/efeito_sonoro/fantasma_sussuro.mp3"

    n "Você se encolhe horrorizado, atira-se no chão e começa a se sentir muito assustado. Por causa desse medo extremo, qualquer batalha contra essas criaturas vai ser de extrema dificuldade!"
    n "você pensa nas seguintes opções:"
    menu quarto_ganjee:
        "usar encanto?":
            jump oito5
        "se preparar para lutar":
            jump dois48
        "procurar um artefato na mochila?":
            jump tres22

label oito5:
    n "as ganjees riam da sua atitude e nao causa nenhum efeito! so lhe resta procurar um artefato na mochila!"
    jump tres22

label dois48:
    n "você desembainha sua espada e os inimigos começam a rir de você e partem em sua direção!"
    jump batalha_ganjees

label morte_ganjees:
    play music "musics/yt1s.com - D J Pinto  Tension EpicOrchestralCinematicMFY  No Copyright Music.mp3"

    n "após a derrota, as ganjees desaparecem, como se deixassem de existir, com um grito estridente que afeta um pouco a sua audição"
    n "dessa forma o caminho esta livre!"
    jump tres28

label tres22:

    n "O que você vai tirar de sua mochila?"
    menu ganjees:
        "aranha em um vidro?":
            if (aranha_garrafa == True):
                jump tres9
            else:
                play sound "musics/efeito_sonoro/nao tem o item.mp3"
                $renpy.notify("você não possui esse item!")
                jump ganjees
        "tentar falsificar um artefato? (teste de sorte)":
            $ d2025roll = renpy.random.randint(1, 20)

            if (d2025roll>= 8):
                $renpy.notify("sucesso de sorte")
                play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
                jump dois91
            else:
                $renpy.notify("fracasso de sorte")
                play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
                n "você nao consegue um artefato e as Ganjees te atacam sugando sua alma, esse foi seu fim!"
                jump final_ruim
        "vidro de ungento?":
            if (vidro_ungento == True):
                jump dois91
            else:
                play sound "musics/efeito_sonoro/nao tem o item.mp3"
                $renpy.notify("você não possui esse item!")
                jump ganjees

label tres9:
    n "as gajees gritam 'Racknee!' como se fosse um velho amigo delas e te ordenam a entregar o vidro a elas!"
    n "você pensa em jogar o vidro no chão ou usar ele como barganha para poder passar:"
    menu:
        "fazer um acordo para que elas te deixem passar":
            jump dois91
        "jogar o vidro no chão":
            n "as ganjees gritam com você fdalando que você matou o Racknee e partem em sua direção para vingar o amigo!"
            jump batalha_ganjees

label dois91:

    n "'O que é isso?' pergunta uma voz fantasmagórica. Você negocia com eles. Você deixará que eles
    fiquem com o frasco, se eles deixarem você passar pelo aposento, já que você não está
    interessado neles."
    n "Uma fantasmagórica mão aparece do nada e tenta arrancar o vidro da sua mão,
    mas você o guarda rapidamente. 'É de fato o Unguento da Cura', você ouve uma das vozes dizendo
    baixo."
    n "'Aceitamos a sua oferta', diz uma voz. 'Deixe o Vidro onde você está e saia do aposento por
    esta porta'. Uma porta do outro lado brilha suavemente. Você não confia neles e leva o Vidro com
    você até a porta."
    n "Quando você abre a porta, atira o Vidro para o outro lado do aposento e sai
    rapidamente."

    jump tres28

label tres28:

    hide ganjee

    scene quarto_hydra at truecenter:
        zoom 1.5

    n "Você fecha a porta atrás de você e chega ao pé de outra escadaria, que sobe em espirais para o
    interior da torre. Subindo os degraus, você chega a uma outra sacada, onde uma única porta é a
    alternativa que existe para seguir adiante."
    n "Ao experimentar a porta, ela abre facilmente. Mas,
    quando você empurra a porta, um ruído alto de silvos vem lá de dentro. Você entra e fica gelado, ao
    ver uma imensa HIDRA de sete cabeças se arrastando na sua direção sobre os corpos das vítimas
    anteriores!"
    show hydra at truecenter:
        zoom 2
    with dissolve
    n "Suas sete cabeças de serpente atacam você com seus dentes aguçados e cruéis. Você fica
    encurralado em um canto. O que você fará:"
    menu hidra:
        "Desembainhará a sua Espada e lutará contra a criatura?":
            $ d6roll = renpy.random.randint(1, 7)

            if (d6roll==3):
                $renpy.notify("sucesso de sorte")
                play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
                n "Você começa a sua luta contra a criatura. Seu primeiro golpe é certeiro e corta uma das seis
                cabeças. fazendo com que as outras comecem a definhar! parabens, cortou a cabeça primordial!"
                n "você segue em direção à porta rumo ao vinal da sua jornada!"
                jump dois29
            else:
                $renpy.notify("fracasso de sorte")
                play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
                n "Você começa a sua luta contra a criatura. Seu primeiro golpe é certeiro e corta uma das seis
                cabeças. As outras cinco avançam sobre você e, para seu horror, mais duas cabeças crescem onde
                estava antes a cabeça morta!"
                jump seis7

        "usar encanto copia de criatura?":
            jump um43
        "usar veu de ouro?":
            if (velo_ouro):
                jump tres7
            else:
                play sound "musics/efeito_sonoro/nao tem o item.mp3"
                $renpy.notify("você não possui esse item!")
                jump hidra

label dois29:

    play music "musics/passagem esgoto.mp3"

    hide hydra
    hide hydra_shiny
    hide mc
    scene entrada_balthus at center:
        zoom 2.0

    n "Você bate a porta, fechando-a ao passar. Você segue por uma passagem curta e estreita, que dá
    muitas voltas e conduz você ao pé de outra escadaria, levando diretamente ao topo da Cidadela. Um
    letreiro na parede diz: 'PARE. Ninguém poderá passar, a não ser com ordem de Balthus Dire.'"
    n"Você percebe que está chegando a seu objetivo. Cautelosamente, você sobe as escadas até o
    próximo patamar, penetrando na torre superior da Cidadela. Há uma porta de metal sólido à sua
    frente. Você tenta a maçaneta, mas a porta está trancada."
    n "Você levanta a sua mão em direção a porta e se concentra, gerando um poderoso raio arcano que estilhaça a fechadura,
    permitindo você seguir para o final da sua jornada. você vai ser capaz de salvar a sua terra?"
    jump dois17

label seis7:
    n "Uma das cabeças morde profundamente o seu braço. e você se prepara para uma batalha ate a morte com a hidra!"

    $ oponente_max_hp = 80
    $ oponente_hp = oponente_max_hp

    jump batalha_hidra

label um43:
    $ d2026roll = renpy.random.randint(1, 20)

    if (d2026roll>= 13):
        $renpy.notify("sucesso de sorte")
        play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
        n "Você se concentra e lança seu Encanto. aparece uma hidra que, para sua surpresa,
        ela surgiu com um padrao de cor exotico!"
        n "Você lembra de ter estudado com seu mestre, são chamadas de hidras reversas,
        essas que possuem o dobro da força das hidras normais!"
        n "a sua hidra avança em direção a hidra original"
        jump batalha_hidra_vs_hidra
    else:
        $renpy.notify("fracasso de sorte")
        play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
        n "Você falha na conjuração do feitiço, de forma que aparece apenas uma cabeça de hidra caida ao chão!"
        n "você fica extremamente nervoso e tem apenas duas opções, procurar algo na sua mochila ou tentar ir para a batalha você mesmo!"
        menu hidra2:
            "pegar veu de ouro?":
                if (velo_ouro):
                    jump tres7
                else:
                    play sound "musics/efeito_sonoro/nao tem o item.mp3"
                    $renpy.notify("você não possui esse item!")
                    jump hidra2
            "puxar sua espada da bainha e ir para a luta?":

                $ oponente_max_hp = 70
                $ oponente_hp = oponente_max_hp

                jump batalha_hidra

label tres7:
    n "Você puxa a pele e a criatura solta silvos altos. Todas as suas cabeças recuam,e ela permanece
    quieta, observando você. Há uma porta do outro lado do aposento, e você lentamente se desloca na
    direção dela."
    n "Quando você está na metade do caminho, uma das cabeças se projeta e arranca o velo
    das suas mãos. Mas, ao invés de atacar você, a Hidra se encolhe de volta em um dos cantos. Você
    segue para a porta cautelosamente."

    $renpy.notify("véu retirado!")

    play sound "musics/efeito_sonoro/item perdido.mp3"

    jump dois29

label dois92:

    scene quarto_morena at center:

    show morena at center:
        ypos 900

    n "O aposento é um elegante quarto de dormir suntuosamente decorado com rendas finas e um tapete
    de pele. No centro do aposento, há uma grande cama de quatro colunas."
    n "Sentada e recostada na cama, evidentemente acordada pela agitação toda, está uma linda mulher, com uma aparência de
    sílfide, longos cabelos negros e olhos profundos e penetrantes. 'Que direito você tem de entrar
    aqui?' ela grita."
    n "Com estas palavras seus olhos ficam vermelhos como sangue e dois jatos de fogo
    líquido jorram deles diretamente sobre você. Você:"

    menu quarto:
        "usar encanto de escudo para se proteger?":
            jump tres76
        "sai do aposento rapidamente e experimente a porta ao lado?":
            jump seis4
        "diz ter um presente especial para ela? (escova de cabelo)":
            if (escova_cabelo == True):
                n "ela aceita o presente"
                jump quatro2
            else:
                play sound "musics/efeito_sonoro/nao tem o item.mp3"
                $renpy.notify("você não possui esse item!")
                jump quarto

label tres76:

    n "Você lança seu Encanto do Escudo. Que lástima, este Encanto não faz efeito contra armas mágicas!"
    n "Você percebe que dialogo nao vai adiantar e se prepara para lutar"
    jump batalha_morena1

label despertar_morena:

    hide mc

    show morena at center
    with dissolve

    l "Você jamais chegará ao Balthus!"

    play sound "musics/efeito_sonoro/tranformacao Balthus.mp3"

    show morena 2 at truecenter:
    with flash
    with dissolve

    l "Essa será a ultima coisa que você verá!"

    jump batalha_morena2

label morte_morena:

    play music "musics/'descoberta'.mp3"

    hide morena
    hide mc

    n "você encontra um veu de ouro!"
    $velo_ouro = True
    $renpy.notify("adquiriu véu de ouro!")

    play sound "musics/efeito_sonoro/item encontrado.mp3"


    n "o caminho está limpo, avance com cautela!"

    jump um40

label quatro2:

    n "Ela olha para a sua oferta e seus olhos se arregalam. 'Deixe-me ver isso', ela ordena. Você avança
    cuidadosamente na direção dela e mostra a escova. Ela pega o objeto e passa vários minutos
    admirando-o."

    $renpy.notify("removeu escova de cabelo!!")
    play sound "musics/efeito_sonoro/item perdido.mp3"

    $ escova_cabelo = False

    n "'Isto é de fato uma obra de arte', ela diz, e se levanta da cama para experimentá-la
    em frente ao espelho. Ao escovar os cabelos dela, eles assumem um brilho incomum, cintilando
    suavemente. Ela fica fascinada com seu presente, e esta é a sua chance de sair sem ser notado pela
    porta existente no canto mais distante."
    n "Você pode tentar levar com você um Véu de Ouro que se
    encontra sobre a cama. Teste a sua Sorte."

    $ d2027roll = renpy.random.randint(1, 20)

    if (d2027roll>= 14):
        $renpy.notify("sucesso de sorte")
        play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
        n "voce teve sorte e conseguiu pegar o véu de ouro!"

        $velo_ouro = True
        $renpy.notify("adquiriu véu de ouro!")

        play sound "musics/efeito_sonoro/item encontrado.mp3"
        jump um40

    else:
        $renpy.notify("fracasso de sorte")
        play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
        n "Você não teve sorte e saiu sem o véu de ouro"
        jump um40

label tres04:
    scene sala_gargula at center:
        zoom 2.3

    n "voce passa pelo portal e penetra no aposento. É bastante grande e está decorado com vários entalhes.
    Parece ser alguma coisa como o estúdio de um artista, e há diversas estátuas inacabadas de pedra
    alinhadas na parede."
    show gargula at center
    with dissolve
    n "No centro do aposento, há um grande GÁRGULA de pedra sobre uma caixa
    entalhada em pedra. Quando você entra no aposento, a criatura faz ruído ao virar a cabeça na sua
    direção. Lentamente, ele desperta para a vida, descendo do seu pedestal."
    n "Está bloqueando o seu caminho pelo aposento para uma porta do outro lado. Você vai:"
    menu gargula:
        "desembainhar sua espada e avançar":
            jump um72
        "usar um encanto!(teste de sorte)":
            jump dois6
        "usar frasco de Essência de Erva de Porco":
            if(essencia_porco):
                jump dois14
            else:
                play sound "musics/efeito_sonoro/nao tem o item.mp3"
                $renpy.notify("você não possui esse item!")
                jump gargula
        "voltar rapidamente pelo portal e ir para o portal do centro":
            jump seis4

label um72:
    n "Você avança e desfere um golpe na criatura. Com um ruído estridente, sua espada repica no corpo
    de pedra. Compreendendo que não conseguirá causar danos a ela com sua arma, você pode lançar
    um Encanto, ou usar alguma coisa que esteja na sua mochila."
    menu gargula2:
        "usar um encanto!":
            jump dois6
        "usar frasco de Essência de Erva de Porco":
            if(essencia_porco):
                jump dois14
            else:
                play sound "musics/efeito_sonoro/nao tem o item.mp3"
                $renpy.notify("você não possui esse item!")
                jump gargula2

label dois6:
    n "você pensa em duas possibilidades de encanto:"
    menu:
        "usar encanto de fraqueza":
            $ d2010roll = renpy.random.randint(1, 20)

            if (d2010roll>=10):
                $renpy.notify("sucesso de sorte")
                play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
                n "A criatura geme quando o Encanto faz efeito. Seu enorme peso tornou-se agora um fardo terrível
                para ela. Ela ainda se arrasta na sua direção, mas você consegue desviar-se e contorná-la, partindo
                na direção da porta do outro lado do aposento."
                jump um40
            else:
                $renpy.notify("fracasso de sorte")
                play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
                n "o encanto não dá certo e só lhe resta fugir de volta para o portal do centro"
                jump seis4

        "usar encanto copia de criatura":
            $ d2010roll = renpy.random.randint(1, 20)

            if (d2010roll>=10):
                $renpy.notify("sucesso de sorte")
                play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
                n "Uma réplica da criatura se materializa entre vocês dois. A uma ordem sua, a batalha começa:"
                jump batalha_gargula
            else:
                $renpy.notify("fracasso de sorte")
                play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
                n "o encanto falha, aparecendo apenas uma rocha imovel na sua frente e so lhe resta fugir de volta para o portal do centro"
                jump seis4

label seis2:
    n "você parte em direção a porta do outro lado da sala!"
    jump um40

label dois14:
    n "Você tira a tampado Frasco e esparrama o líquido verde sobre a criatura. Ela rosna e grita no ar,
    pondo as mãos em volta do pescoço. O líquido parece estar queimando intensamente o Gárgula, e
    uma fumaça sobe pelo ar. Alguns momentos depois, a criatura jaz morta no chão."
    n "você segue em frente pela porta do outro lado do aposento!"
    jump um40

label dois17:
    scene topo_torre
    show balthus normal at center:
        zoom 0.7
    with dissolve
    n "Balthus dire finalmente está a sua frente,seu poder emana e sua pressão é enorme
    seu próximo passo definirá o destino do Vale do Salgueiro, e o seu futuro,o que você fará"
    menu:
        "confessará que deseja servir o lorde do caos e nao desafia-lo?":
            jump final_submissao
        "Lutar contra Balthus":
            jump despertar

label final_ruim:

    play music "musics/Savfk - Deep.mp3"

    scene game_over:
        zoom 1.5

    $renpy.notify("fim de jogo")

    n "voce falhou em sua missão e Balthus Dire agora avança em direção a sua terra natal, que destino a espera?"

    return

label final_submissao:

    play music "musics/yt1s.com - No Copyright Music Whisper In The Deep  Royalty Free Music.mp3"

    n "você abaixa sua arma e explica que na verdade voce nao buscava a morte do lorde do caos, mas servi-lo.A esperança era de obter a liberdade de decidir oque fazer com a sua vida,
    algo que voce nunca sentiu ter, com tudo sempre por decisão de seu antigo mestre, o grande mago de Yore."

    b "Ora ora... O unico capaz de adentrar não só minha cidadela mas minha torre deseja juntra-se a mim!!!
    HA HA HA HA HAAAAAAAAA!!! O destino favorece aos detentores do poder e você, meu jovem,entendeu isso muito bem!"

    b "Agora vamos,aquele vale patético tem muito gado esperando para ser controlado,e nós seremos seus pastores!"

    hide balthus normal

    scene fim_sub at center:
        zoom 1.5

    n "A tirania se espalhou e Balthus se tornou supremo graças a você,todos que conhecia foram mortos,você estava livre das suas antigas amarras,
    mas ainda se sentia acorrentado. Porquê?
    Você se aproxima para falar com Balthus sobre sua parceria com ele"

    show balthus normal at center:
        zoom 0.7
    with dissolve

    b "Ah, meu jovem nada tema!Sua ansiedade é injustificada,afinal..."

    play sound "musics/efeito_sonoro/facada.mp3"

    n "O lorde do caos invoca rapidamente uma adaga e te esfaqueia!"

    b "Um rei governa sozinho!Seus serviços nao são mais necessários! Lacaios,joguem esse corpo na vala!"

    n "Antes da morte,sua vida passa diante de seus olhos, você retribiu seus traumas da infância e juventude com violência, o vazio é tudo que lhe restou..."

    scene game_over:
        zoom 1.5

    $renpy.notify("fim de jogo")

    n "Sua jornada termina aqui..."
    jump creditos

label despertar:

    play music "musics/Makai Symphony - The Army of Minotaur.mp3" volume 0.5

    hide balthus normal
    show mc normal at center:
        zoom 0.7
    with dissolve


    n "Este é o momento para o qual você treinou tanto, sofreu tanto! Não importa o preco que terá de pagar,voce dará tudo de si!
    Você retira o colar do selamento, dado a você pelo seu antigo mestre, o grande mago de Yore."

    n "Seus poderes antes suprimidos para garantir sua discrição para infiltrar-se na cidadela agora são seus para utilizar!"

    play sound "musics/efeito_sonoro/poderes liberados.mp3"
    show mc bombado at center:
        zoom 0.7
    with flash
    with dissolve


    b "Quem diria! O desgracado que invade minha cidadela! minha torre! Ousa me desafiar com esse nível de poder?!Ridículo!"

    jump batalha_balthus1

label despertar_balthus:

    hide mc

    show balthus normal at center:
        zoom 0.7
    with dissolve

    b "Ridículo!!!! Não serei derrotado por um moleque arrogante!!!Biotáille ársa yore, oibrigh an fhoirm chinniúnach seo i ldabaoth!!!!!"

    play sound "musics/efeito_sonoro/tranformacao Balthus.mp3"

    show balthus bombado at center:
        ypos 1500
        zoom 1.5
    with flash
    with dissolve

    play music "musics/fase 2.mp3"

    n "O lorde do caos havia lancado um encantamento antigo e proibido, os anos de estudo do mago garatiram que ele sabia do que se tratava.
    'Antigos espirítos de Yore,transformem essa forma decadente em ldabaoth',Balthus havia desistido de sua forma humana para tentar a vitória,a luta continua!"

    jump batalha_balthus2

label morte_balthus:

    scene arena_final2:
        zoom 1.3
    with dissolve

    show balthus bombado at center:
        ypos 1500
        zoom 1.5
    with dissolve

    b "como isso pode acontecer?? eu era invencivel!!"

    play sound "musics/efeito_sonoro/balthus morrendo.mp3"

    show morte_balthus1 at center with dissolve:
        zoom 9.0
    pause 0.1
    show morte_balthus2 at center with dissolve:
        zoom 9.0
    pause 0.1
    show morte_balthus3 at center with dissolve:
        zoom 9.0
    pause 0.1
    show morte_balthus4 at center with dissolve:
        zoom 9.0
    pause 0.1
    show morte_balthus5 at center with dissolve:
        zoom 9.0
    pause 0.1
    show morte_balthus6 at center with dissolve:
        zoom 9.0
    pause 0.1
    show morte_balthus7 at center with dissolve:
        zoom 9.0
    pause 0.1
    show morte_balthus8 at center with dissolve:
        zoom 9.0
    pause 0.1
    show morte_balthus9 at center with dissolve:
        zoom 9.0
    pause 0.1
    show morte_balthus10 at center with dissolve:
        zoom 9.0
    pause 0.1
    show morte_balthus11 at center with dissolve:
        zoom 9.0
    pause 0.1
    show morte_balthus12 at center with dissolve:
        zoom 9.0
    pause 0.1
    show morte_balthus13 at center with dissolve:
        zoom 9.0
    pause 0.1
    show morte_balthus14 at center with dissolve:
        zoom 9.0
    pause 0.1
    show morte_balthus15 at center with dissolve:
        zoom 9.0
    pause 0.1


    hide balthus

    jump fim_batalha

label facada:
    hide screen batalha_balthus

    show balthus normal at right:
        zoom 0.7
    with flash
    with dissolve

    n "Balthus volta a a sua forma humana, no entanto degastado e ferido.Ele pateticamente cai de joelhos,olha para cima em sua direção e diz:"

    b "Mago! Você já provou seu valor,governe ao meu lado,aqueles porcos imundos do vale não merecem sua salvação,torne-se um lorde do caos ao meu lado!"

    n "O mago se aproxima a passos lentos de Balthus e com o olhar penetrante o examina"

    mc "..."
    mc "...."
    mc "Posso ter sido um escravo do meu destino Balthus,eu nunca escolhi ser um mago, eu não escolhi me arriscar na sua maldita cidadela! Mas agora..."
    mc "Eu escolho matá-lo! Ó 'lorde do caos'"

    play sound "musics/efeito_sonoro/facada.mp3"

    n "O mago invoca um punhal e apunha-la Balthus em sua jugular,enquanto o observa cair sem vida, um fim mortal para aquele que se dizia um deus"

    hide balthus

    hide mc

    jump fim_batalha

label fim_batalha:

    hide balthus



    scene topo_torre

    n "Voce se encontra novamente no aposento de Balthus na torre, o trono jaz vazio a sua frente. Há tambem uma varanda que indica um nascer do sol próximo.
    Agora que Balthus está morto, você se tornou o mago...não... o ser mais poderoso de todo o continente, o destino de tudo e todos é seu,entao:"
    menu:
        "Se dirige a varanda, e contempla a paz conquistada":
            jump final_alvorecer
        "Se dirige ao trono, e planeja oque fará como novo lorde do caos":
            jump final_lorde

label final_alvorecer:

    play music "musics/Neverland+-+320bit.mp3"

    scene fim_alvor:
        zoom 2.2
    n "Você se dirige a varanda e contempla, tudo isso seria destruido caso você tivesse falhado, tal realização te enche de orgulho,seu sofrimento não foi em vão,
    é hora de voltar para casa e abracar todos aqueles que ama!
    Sua jornada termina aqui,mas sempre que houver escuridao, o mago retornará!"

    $renpy.notify("fim de jogo")

    jump creditos

label final_lorde:

    scene fim_lorde

    play music "musics/final lorde.mp3"

    $renpy.notify("fim de jogo")

    n "Sua jornada jamais terá fim lorde do caos, para aqueles que anseiam pelo poder, as correntes da avareza, da arrogância jamais te deixarâo livre,vida longa ao novo governante!"

    jump creditos

label creditos:
    $ quick_menu = False

    play music "musics/trilha creditos.mp3"

    $renpy.notify("por favor, aprecie os créditos")

    $ credits_speed = 240 #scrolling speed in seconds
    scene creditos
    with dissolve
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide theend
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(5)
    hide thanks
    return

label batalha_guardas:

    hide guarda1
    hide guarda2

    show mc normal at left:
        zoom 0.6
    with fade

    show guarda1 at right:
        zoom 1.3
    with dissolve

    show guarda2:
        xpos 1050
        ypos 400
        zoom 0.9
    with dissolve

    $ oponente_max_hp = 45
    $ mago_max_hp = 60
    $ oponente_hp = oponente_max_hp
    $ mago_hp = mago_max_hp
    $ mago_max_mp = 50
    $ mago_mp = mago_max_mp
    $ elixirHP_left = 10
    $ elixirMP_left = 5


    show screen batalha_generica

    while (oponente_hp > 0):

        if mago_hp > 0:
            menu batalha1:

                "Ataque com espada (5 de dano)":

                    play sound "musics/efeito_sonoro/ataque espada.mp3"

                    $ oponente_hp -= 5
                    $mago_damage = 5
                    mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"


                "Bola de fogo (2 a 8 de dano)":
                    if(mago_mp >= 6):
                        play sound "musics/efeito_sonoro/bola de fogo.mp3"

                        $ mago_damage = renpy.random.randint(2, 8)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 6
                        mc "Bola de fogo!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha1

                "Raio arcano (1 a 12 de dano)":

                    if(mago_mp >= 10):
                        play sound "musics/efeito_sonoro/raio arcano.mp3" volume 0.7

                        $ mago_damage = renpy.random.randint(1, 12)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 10
                        mc "Raio arcano!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha1

                "tomar elixir da vida (tem [elixirHP_left] elixires)" if elixirHP_left > 0:
                    $ mago_hp = min(mago_hp+15, mago_max_hp)
                    $ elixirHP_left -= 1
                    n "{i}*você sente suas feridas cicatrizarem!*{/i} (vida curada - 15 hp)"

                "tomar elixir de mana (tem [elixirMP_left] elixires)" if elixirMP_left > 0:
                    $ mago_mp = min(mago_mp+14, mago_max_mp)
                    $ elixirMP_left -= 1
                    n "{i}*você sente suas forças voltarem!*{/i} (mana restaurada - 14 mp)"
        else:
            hide screen batalha_generica
            jump final_ruim

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(2, 6)

            $ mago_hp -= oponente_damage

            n " {i}*os guardas te atacam!*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    'oponentes derrotados!!!'
    jump dois51

label batalha_criaturas:
    play music "musics/Makai Symphony - Dragon Castle.mp3"
    #hide guarda1
    hide goblin2

    show mc normal at left:
        zoom 0.6
    with dissolve

    show orquisa at right:
        zoom 1.2
        ypos 1050
    show anao at right:
        zoom 0.5
        xpos 1600
    show goblin1 at right:
        xpos 2050

    $ oponente_max_hp = 90
    $ mago_max_hp = 60
    $ oponente_hp = oponente_max_hp
    $ mago_hp = mago_max_hp
    $ mago_max_mp = 50
    $ mago_mp = mago_max_mp
    $ elixirHP_left = 10
    $ elixirMP_left = 5

    show screen batalha_generica

    while (oponente_hp > 0):

        if mago_hp > 0:
            menu batalha2:

                "Ataque com espada ( 5 de dano)":

                    play sound "musics/efeito_sonoro/ataque espada.mp3"

                    $ mago_damage = 5
                    $ oponente_hp -= mago_damage
                    mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"


                "Bola de fogo (2 a 8 de dano)":

                    if(mago_mp >= 6):
                        play sound "musics/efeito_sonoro/bola de fogo.mp3"

                        $ mago_damage = renpy.random.randint(2, 8)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 6
                        mc "Bola de fogo!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha2

                "Raio arcano (1 a 12 de dano)":

                    if(mago_mp >= 10):
                        play sound "musics/efeito_sonoro/raio arcano.mp3" volume 0.7

                        $ mago_damage = renpy.random.randint(1, 12)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 10
                        mc "Raio arcano!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha2

                "tomar elixir da vida (tem [elixirHP_left] elixires)" if elixirHP_left > 0:
                    $ mago_hp = min(mago_hp+15, mago_max_hp)
                    $ elixirHP_left -= 1
                    n "{i}*você sente suas feridas cicatrizarem!*{/i} (vida curada - 15 hp)"

                "tomar elixir de mana (tem [elixirMP_left] elixires)" if elixirMP_left > 0:
                    $ mago_mp = min(mago_mp+14, mago_max_mp)
                    $ elixirMP_left -= 1
                    n "{i}*você sente suas forças voltarem!*{/i} (mana restaurada - 14 mp)"

        else:
            hide screen batalha_generica
            jump final_ruim

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(5, 8)

            $ mago_hp -= oponente_damage

            n " {i}*As criaturas te atacam!*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    'oponentes derrotados!!!'
    jump dois45

label batalha_porteiro:
    show mc normal at left:
        zoom 0.6
    with dissolve

    show porteiro at right:
        zoom 1.5
    with dissolve

    play music "musics/Makai Symphony - Dragon Castle.mp3"


    $ oponente_max_hp = 70
    $ mago_max_hp = 60
    $ oponente_hp = oponente_max_hp
    $ mago_hp = mago_max_hp
    $ mago_max_mp = 50
    $ mago_mp = mago_max_mp
    $ elixirHP_left = 10
    $ elixirMP_left = 5

    show screen batalha_generica

    while (oponente_hp > 0):

        if mago_hp > 0:
            menu batalha3:

                "Ataque com espada ( 5 de dano)":

                    play sound "musics/efeito_sonoro/ataque espada.mp3"

                    $ mago_damage = 5
                    $ oponente_hp -= mago_damage
                    mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"


                "Bola de fogo (2 a 8 de dano)":

                    if(mago_mp >= 6):
                        play sound "musics/efeito_sonoro/bola de fogo.mp3"

                        $ mago_damage = renpy.random.randint(2, 8)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 6
                        mc "Bola de fogo!!!!! (dano causado - [mago_damage]hp)"

                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha3

                "Raio arcano (1 a 12 de dano)":

                    if(mago_mp >= 10):
                        play sound "musics/efeito_sonoro/raio arcano.mp3" volume 0.7

                        $ mago_damage = renpy.random.randint(1, 12)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 10
                        mc "Raio arcano!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha3

                "tomar elixir da vida (tem [elixirHP_left] elixires)" if elixirHP_left > 0:
                    $ mago_hp = min(mago_hp+15, mago_max_hp)
                    $ elixirHP_left -= 1
                    n "{i}*você sente suas feridas cicatrizarem!*{/i} (vida curada - 15 hp)"

                "tomar elixir de mana (tem [elixirMP_left] elixires)" if elixirMP_left > 0:
                    $ mago_mp = min(mago_mp+14, mago_max_mp)
                    $ elixirMP_left -= 1
                    n "{i}*você sente suas forças voltarem!*{/i} (mana restaurada - 14 mp)"

        else:
            hide screen batalha_generica
            jump final_ruim

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(4, 8)

            $ mago_hp -= oponente_damage

            n " {i}*o oponente te ataca com a lança!!*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    'Fernando12000 derrotado!!!'
    jump um77

label batalha_tentaculo:

    play music "musics/Makai Symphony - Dragon Castle.mp3"

    $ oponente_max_hp = 60
    $ mago_max_hp = 60
    $ oponente_hp = oponente_max_hp
    $ mago_hp = mago_max_hp
    $ mago_max_mp = 50
    $ mago_mp = mago_max_mp
    $ elixirHP_left = 10
    $ elixirMP_left = 5

    show screen batalha_generica

    while (oponente_hp > 0):

        if mago_hp > 0:
            menu batalha4:

                "Ataque com espada ( 5 de dano)":

                    play sound "musics/efeito_sonoro/ataque espada.mp3"

                    $ mago_damage = 5
                    $ oponente_hp -= mago_damage
                    mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"


                "Bola de fogo (2 a 8 de dano)":

                    if(mago_mp >= 6):
                        play sound "musics/efeito_sonoro/bola de fogo.mp3"

                        $ mago_damage = renpy.random.randint(2, 8)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 6
                        mc "Bola de fogo!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha4

                "Raio arcano (1 a 12 de dano)":

                    if(mago_mp >= 10):
                        play sound "musics/efeito_sonoro/raio arcano.mp3" volume 0.7

                        $ mago_damage = renpy.random.randint(1, 12)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 10
                        mc "Raio arcano!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha4

                "tomar elixir da vida (tem [elixirHP_left] elixires)" if elixirHP_left > 0:
                    $ mago_hp = min(mago_hp+15, mago_max_hp)
                    $ elixirHP_left -= 1
                    n "{i}*você sente suas feridas cicatrizarem!*{/i} (vida curada - 15 hp)"

                "tomar elixir de mana (tem [elixirMP_left] elixires)" if elixirMP_left > 0:
                    $ mago_mp = min(mago_mp+14, mago_max_mp)
                    $ elixirMP_left -= 1
                    n "{i}*você sente suas forças voltarem!*{/i} (mana restaurada - 14 mp)"

        else:
            hide screen batalha_generica
            jump final_ruim

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(4, 8)

            $ mago_hp -= oponente_damage

            n " {i}*o oponente te arrasta para o seu covil!*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    'oponente derrotado!!!'
    jump dois18

label batalha_contra_um:

    play music "musics/Makai Symphony - Dragon Castle.mp3"

    show mc normal at left:
        zoom 0.6
    with fade

    $ oponente_max_hp = 70
    $ mago_max_hp = 60
    $ oponente_hp = oponente_max_hp
    $ mago_hp = mago_max_hp
    $ elixirHP_left = 10
    $ mago_max_mp = 50
    $ mago_mp = mago_max_mp
    $ elixirHP_left = 10
    $ elixirMP_left = 5

    show screen batalha_generica

    while (oponente_hp > 0):

        if mago_hp > 0:
            menu batalha5:

                "Ataque com espada ( 5 de dano)":

                    play sound "musics/efeito_sonoro/ataque espada.mp3"

                    $ mago_damage = 5
                    $ oponente_hp -= mago_damage
                    mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"


                "Bola de fogo (2 a 8 de dano)":

                    if(mago_mp >= 6):
                        play sound "musics/efeito_sonoro/bola de fogo.mp3"

                        $ mago_damage = renpy.random.randint(2, 8)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 6
                        mc "Bola de fogo!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha5

                "Raio arcano (1 a 12 de dano)":

                    if(mago_mp >= 10):
                        play sound "musics/efeito_sonoro/raio arcano.mp3" volume 0.7

                        $ mago_damage = renpy.random.randint(1, 12)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 10
                        mc "Raio arcano!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha5

                "tomar elixir da vida (tem [elixirHP_left] elixires)" if elixirHP_left > 0:
                    $ mago_hp = min(mago_hp+15, mago_max_hp)
                    $ elixirHP_left -= 1
                    n "{i}*você sente suas feridas cicatrizarem!*{/i} (vida curada - 15 hp)"

                "tomar elixir de mana (tem [elixirMP_left] elixires)" if elixirMP_left > 0:
                    $ mago_mp = min(mago_mp+14, mago_max_mp)
                    $ elixirMP_left -= 1
                    n "{i}*você sente suas forças voltarem!*{/i} (mana restaurada - 14 mp)"

        else:
            hide screen batalha_generica
            jump final_ruim

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(2, 6)

            $ mago_hp -= oponente_damage

            n " {i}*O vendedor te ataca!*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    'oponente derrotado!!!'
    n "Dessa forma, você prossegue a sua jornada para a Torre Negra"
    $renpy.notify("Punhal pilhado!")
    play sound "musics/efeito_sonoro/item encontrado.mp3"

    jump dois18

label batalha_contra_dois:

    play music "musics/Makai Symphony - Dragon Castle.mp3"

    show mc normal at left:
        zoom 0.6
    with fade

    $ oponente_max_hp = 90
    $ mago_max_hp = 60
    $ oponente_hp = oponente_max_hp
    $ mago_hp = mago_max_hp
    $ elixirHP_left = 10
    $ mago_max_mp = 50
    $ mago_mp = mago_max_mp
    $ elixirHP_left = 10
    $ elixirMP_left = 5

    show screen batalha_generica

    while (oponente_hp > 0):

        if mago_hp > 0:
            menu batalha6:

                "Ataque com espada ( 5 de dano)":

                    play sound "musics/efeito_sonoro/ataque espada.mp3"

                    $ mago_damage = 5
                    $ oponente_hp -= mago_damage
                    mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"


                "Bola de fogo (2 a 8 de dano)":

                    if(mago_mp >= 6):
                        play sound "musics/efeito_sonoro/bola de fogo.mp3"

                        $ mago_damage = renpy.random.randint(2, 8)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 6
                        mc "Bola de fogo!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha6

                "Raio arcano (1 a 12 de dano)":

                    if(mago_mp >= 10):
                        play sound "musics/efeito_sonoro/raio arcano.mp3" volume 0.7

                        $ mago_damage = renpy.random.randint(1, 12)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 10
                        mc "Raio arcano!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha6

                "tomar elixir da vida (tem [elixirHP_left] elixires)" if elixirHP_left > 0:
                    $ mago_hp = min(mago_hp+15, mago_max_hp)
                    $ elixirHP_left -= 1
                    n "{i}*você sente suas feridas cicatrizarem!*{/i} (vida curada - 15 hp)"

                "tomar elixir de mana (tem [elixirMP_left] elixires)" if elixirMP_left > 0:
                    $ mago_mp = min(mago_mp+14, mago_max_mp)
                    $ elixirMP_left -= 1
                    n "{i}*você sente suas forças voltarem!*{/i} (mana restaurada - 14 mp)"

        else:
            hide screen batalha_generica
            jump final_ruim

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(4, 9)

            $ mago_hp -= oponente_damage

            n " {i}*Os oponentes te atacam!*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    'oponentes derrotados!!!'
    $renpy.notify("Punhal pilhado!")
    play sound "musics/efeito_sonoro/item encontrado.mp3"
    n "Dessa forma, você prosseguirá com a sua jornada para a Torre Negra."
    jump dois18

label batalha_calacorm:

    show calacorm at right:
        zoom 1.5

    play music "musics/Makai Symphony - Dragon Castle.mp3"

    n "A criatura entra em seu aposento e parte para cima de você!"
    show mc normal at left:
        zoom 0.6
    with dissolve
    $ oponente_max_hp = 110
    $ mago_max_hp = 60
    $ oponente_hp = oponente_max_hp
    $ mago_hp = mago_max_hp
    $ elixirHP_left = 10
    $ mago_max_mp = 50
    $ mago_mp = mago_max_mp
    $ elixirHP_left = 10
    $ elixirMP_left = 5

    show screen batalha_generica

    while (oponente_hp > 0):

        if mago_hp > 0:
            menu batalha7:

                "Ataque com espada ( 5 de dano)":

                    play sound "musics/efeito_sonoro/ataque espada.mp3"

                    $ mago_damage = 5
                    $ oponente_hp -= mago_damage
                    mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"


                "Bola de fogo (2 a 8 de dano)":

                    if(mago_mp >= 6):
                        play sound "musics/efeito_sonoro/bola de fogo.mp3"

                        $ mago_damage = renpy.random.randint(2, 8)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 6
                        mc "Bola de fogo!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha7

                "Raio arcano (1 a 12 de dano)":

                    if(mago_mp >= 10):
                        play sound "musics/efeito_sonoro/raio arcano.mp3" volume 0.7

                        $ mago_damage = renpy.random.randint(1, 12)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 10
                        mc "Raio arcano!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha7

                "tomar elixir da vida (tem [elixirHP_left] elixires)" if elixirHP_left > 0:
                    $ mago_hp = min(mago_hp+15, mago_max_hp)
                    $ elixirHP_left -= 1
                    n "{i}*você sente suas feridas cicatrizarem!*{/i} (vida curada - 15 hp)"

                "tomar elixir de mana (tem [elixirMP_left] elixires)" if elixirMP_left > 0:
                    $ mago_mp = min(mago_mp+14, mago_max_mp)
                    $ elixirMP_left -= 1
                    n "{i}*você sente suas forças voltarem!*{/i} (mana restaurada - 14 mp)"

        else:
            hide batalha_generica
            jump final_ruim

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(4, 9)

            $ mago_hp -= oponente_damage

            n " {i}*ele investe em sua direção*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    "Oponente derrotado e você parte em fuga!"
    jump um74

label batalha_gark:

    play music "musics/Makai Symphony - Dragon Castle.mp3"

    show mc normal at left:
        zoom 0.6
    with dissolve
    $ oponente_max_hp = 90
    $ mago_max_hp = 60
    $ oponente_hp = oponente_max_hp
    $ mago_hp = mago_max_hp
    $ elixirHP_left = 10
    $ mago_max_mp = 50
    $ mago_mp = mago_max_mp
    $ elixirHP_left = 10
    $ elixirMP_left = 5

    show screen batalha_generica

    while (oponente_hp > 0):

        if mago_hp > 0:
            menu batalha8:

                "Ataque com espada ( 5 de dano)":

                    play sound "musics/efeito_sonoro/ataque espada.mp3"

                    $ mago_damage = 5
                    $ oponente_hp -= mago_damage
                    mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"


                "Bola de fogo (2 a 8 de dano)":

                    if(mago_mp >= 6):
                        play sound "musics/efeito_sonoro/bola de fogo.mp3"

                        $ mago_damage = renpy.random.randint(2, 8)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 6
                        mc "Bola de fogo!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha8

                "Raio arcano (1 a 12 de dano)":

                    if(mago_mp >= 10):
                        play sound "musics/efeito_sonoro/raio arcano.mp3" volume 0.7

                        $ mago_damage = renpy.random.randint(1, 12)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 10
                        mc "Raio arcano!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha8

                "tomar elixir da vida (tem [elixirHP_left] elixires)" if elixirHP_left > 0:
                    $ mago_hp = min(mago_hp+15, mago_max_hp)
                    $ elixirHP_left -= 1
                    n "{i}*você sente suas feridas cicatrizarem!*{/i} (vida curada - 15 hp)"

                "tomar elixir de mana (tem [elixirMP_left] elixires)" if elixirMP_left > 0:
                    $ mago_mp = min(mago_mp+14, mago_max_mp)
                    $ elixirMP_left -= 1
                    n "{i}*você sente suas forças voltarem!*{/i} (mana restaurada - 14 mp)"

        else:
            hide screen batalha_generica
            jump final_ruim

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(4, 9)

            $ mago_hp -= oponente_damage

            n " {i}*o oponente te da uma marretada!!*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    'Oponente derrotado e você parte em direção às portas!'
    jump nove9

label batalha_cobras:

    play music "musics/Makai Symphony - Dragon Castle.mp3"

    show mc normal at left:
        zoom 0.6
    with fade

    show cobra_esgoto at right:
        zoom 1.3
    with dissolve

    $ oponente_max_hp = 50
    $ mago_max_hp = 60
    $ oponente_hp = oponente_max_hp
    $ mago_hp = mago_max_hp
    $ elixirHP_left = 10
    $ mago_max_mp = 50
    $ mago_mp = mago_max_mp
    $ elixirHP_left = 10
    $ elixirMP_left = 5

    show screen batalha_generica

    while (oponente_hp > 0):

        if mago_hp > 0:
            menu batalha9:

                "Ataque com espada ( 5 de dano)":

                    play sound "musics/efeito_sonoro/ataque espada.mp3"

                    $ mago_damage = 5
                    $ oponente_hp -= mago_damage
                    mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"


                "Bola de fogo (2 a 8 de dano)":

                    if(mago_mp >= 6):
                        play sound "musics/efeito_sonoro/bola de fogo.mp3"

                        $ mago_damage = renpy.random.randint(2, 8)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 6
                        mc "Bola de fogo!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha9

                "Raio arcano (1 a 12 de dano)":

                    if(mago_mp >= 10):
                        play sound "musics/efeito_sonoro/raio arcano.mp3" volume 0.7

                        $ mago_damage = renpy.random.randint(1, 12)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 10
                        mc "Raio arcano!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha9

                "tomar elixir da vida (tem [elixirHP_left] elixires)" if elixirHP_left > 0:
                    $ mago_hp = min(mago_hp+15, mago_max_hp)
                    $ elixirHP_left -= 1
                    n "{i}*você sente suas feridas cicatrizarem!*{/i} (vida curada - 15 hp)"

                "tomar elixir de mana (tem [elixirMP_left] elixires)" if elixirMP_left > 0:
                    $ mago_mp = min(mago_mp+14, mago_max_mp)
                    $ elixirMP_left -= 1
                    n "{i}*você sente suas forças voltarem!*{/i} (mana restaurada - 14 mp)"

        else:
            hide screen batalha_generica
            jump final_ruim

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(2, 6)

            $ mago_hp -= oponente_damage

            n " {i}*a cobra te ataca!*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    'oponente derrotado!!!'
    jump um12

label batalha_morena1:

    play music "musics/Makai Symphony - Dragon Castle.mp3"

    show mc normal at left:
        zoom 0.6
    with fade

    show morena at right:
        zoom 1.3
    with dissolve

    $ oponente_max_hp = 60
    $ mago_max_hp = 60
    $ oponente_hp = oponente_max_hp
    $ mago_hp = mago_max_hp
    $ elixirHP_left = 10
    $ mago_max_mp = 50
    $ mago_mp = mago_max_mp
    $ elixirHP_left = 10
    $ elixirMP_left = 5

    show screen batalha_generica

    while (oponente_hp > 0):

        if mago_hp > 0:
            menu batalha10:

                "Ataque com espada ( 5 de dano)":

                    play sound "musics/efeito_sonoro/ataque espada.mp3"

                    $ mago_damage = 5
                    $ oponente_hp -= mago_damage
                    mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"


                "Bola de fogo (2 a 8 de dano)":

                    if(mago_mp >= 6):
                        play sound "musics/efeito_sonoro/bola de fogo.mp3"

                        $ mago_damage = renpy.random.randint(2, 8)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 6
                        mc "Bola de fogo!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha10

                "Raio arcano (1 a 12 de dano)":

                    if(mago_mp >= 10):
                        play sound "musics/efeito_sonoro/raio arcano.mp3" volume 0.7

                        $ mago_damage = renpy.random.randint(1, 12)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 10
                        mc "Raio arcano!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha10

                "tomar elixir da vida (tem [elixirHP_left] elixires)" if elixirHP_left > 0:
                    $ mago_hp = min(mago_hp+15, mago_max_hp)
                    $ elixirHP_left -= 1
                    n "{i}*você sente suas feridas cicatrizarem!*{/i} (vida curada - 15 hp)"

                "tomar elixir de mana (tem [elixirMP_left] elixires)" if elixirMP_left > 0:
                    $ mago_mp = min(mago_mp+14, mago_max_mp)
                    $ elixirMP_left -= 1
                    n "{i}*você sente suas forças voltarem!*{/i} (mana restaurada - 14 mp)"

        else:
            hide screen batalha_generica
            jump final_ruim

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(5, 8)

            $ mago_hp -= oponente_damage

            n " {i}*a morena te ataca!*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    'manuzini derrotada!!!'
    jump despertar_morena

label batalha_morena2:

    play music "musics/morena's battle.mp3"

    show mc normal at left:
        zoom 0.6
    with fade

    show morena 2 at right:
        zoom 0.9
    with dissolve

    $ oponente_max_hp = 90
    $ mago_max_hp = 60
    $ oponente_hp = oponente_max_hp
    $ mago_hp = mago_max_hp
    $ elixirHP_left = 10
    $ mago_max_mp = 50
    $ mago_mp = mago_max_mp
    $ elixirHP_left = 10
    $ elixirMP_left = 5

    show screen batalha_generica

    while (oponente_hp > 0):

        if mago_hp > 0:
            menu batalha11:

                "Ataque com espada ( 5 de dano)":

                    play sound "musics/efeito_sonoro/ataque espada.mp3"

                    $ mago_damage = 5
                    $ oponente_hp -= mago_damage
                    mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"


                "Bola de fogo (2 a 8 de dano)":

                    if(mago_mp >= 6):
                        play sound "musics/efeito_sonoro/bola de fogo.mp3"

                        $ mago_damage = renpy.random.randint(2, 8)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 6
                        mc "Bola de fogo!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha11

                "Raio arcano (1 a 12 de dano)":

                    if(mago_mp >= 10):
                        play sound "musics/efeito_sonoro/raio arcano.mp3" volume 0.7

                        $ mago_damage = renpy.random.randint(1, 12)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 10
                        mc "Raio arcano!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha11

                "tomar elixir da vida (tem [elixirHP_left] elixires)" if elixirHP_left > 0:
                    $ mago_hp = min(mago_hp+15, mago_max_hp)
                    $ elixirHP_left -= 1
                    n "{i}*você sente suas feridas cicatrizarem!*{/i} (vida curada - 15 hp)"

                "tomar elixir de mana (tem [elixirMP_left] elixires)" if elixirMP_left > 0:
                    $ mago_mp = min(mago_mp+14, mago_max_mp)
                    $ elixirMP_left -= 1
                    n "{i}*você sente suas forças voltarem!*{/i} (mana restaurada - 14 mp)"

        else:
            hide screen batalha_generica
            jump final_ruim

        if(oponente_hp > 0):

            $ chance_acerto = renpy.random.randint(1, 100)

            if (chance_acerto<70):

                $ oponente_damage = renpy.random.randint(7, 10)

                $ mago_hp -= oponente_damage

                play sound "musics/efeito_sonoro/morena2.mp3"

                n " {i}*a morena te ataca!*{/i} (dano recebido - [oponente_damage]hp)"

                play sound "musics/efeito_sonoro/gemido-combate.mp3"

            else:
                n "a morena lança um raio laser dos olhos que você consegue desviar, aproveitando isso para dar um contra ataque com sua espada!"
                play sound "musics/efeito_sonoro/ataque espada.mp3"

                $ mago_damage = 5
                $ oponente_hp -= mago_damage
                mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"

    hide screen batalha_generica
    'Lucretia derrotada!!!'
    jump morte_morena

label batalha_ganjees:
    play music "musics/Makai Symphony - Dragon Castle.mp3"

    show mc normal at left:
        zoom 0.6
    with fade

    show ganjee at right:
    with dissolve

    $ oponente_max_hp = 55
    $ mago_max_hp = 60
    $ oponente_hp = oponente_max_hp
    $ mago_hp = mago_max_hp
    $ elixirHP_left = 10
    $ mago_max_mp = 50
    $ mago_mp = mago_max_mp
    $ elixirHP_left = 10
    $ elixirMP_left = 5

    show screen batalha_generica

    while (oponente_hp > 0):

        if mago_hp > 0:
            menu batalha12:

                "Ataque com espada ( 5 de dano)":

                    play sound "musics/efeito_sonoro/ataque espada.mp3"

                    #$ mago_damage = 5
                    #$ oponente_hp -= mago_damage
                    #mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"
                    n "você ve sua espada atravessar o corpo da criatura sem causar dano algum!"
                    $renpy.notify("ataque ineficaz contra espectros!!")
                    play sound "musics/efeito_sonoro/nao tem o item.mp3"


                "Bola de fogo (2 a 8 de dano)":

                    if(mago_mp >= 6):
                        play sound "musics/efeito_sonoro/bola de fogo.mp3"

                        $ mago_damage = renpy.random.randint(2, 8)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 6
                        mc "Bola de fogo!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha12

                "Raio arcano (1 a 12 de dano)":

                    if(mago_mp >= 10):
                        play sound "musics/efeito_sonoro/raio arcano.mp3" volume 0.7

                        $ mago_damage = renpy.random.randint(1, 12)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 5
                        mc "Raio arcano!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha12

                "tomar elixir da vida (tem [elixirHP_left] elixires)" if elixirHP_left > 0:
                    $ mago_hp = min(mago_hp+15, mago_max_hp)
                    $ elixirHP_left -= 1
                    n "{i}*você sente suas feridas cicatrizarem!*{/i} (vida curada - 15 hp)"

                "tomar elixir de mana (tem [elixirMP_left] elixires)" if elixirMP_left > 0:
                    $ mago_mp = min(mago_mp+14, mago_max_mp)
                    $ elixirMP_left -= 1
                    n "{i}*você sente suas forças voltarem!*{/i} (mana restaurada - 14 mp)"

        else:
            hide screen batalha_generica
            jump final_ruim

        if(oponente_hp > 0):

            $ chance_acerto = renpy.random.randint(1, 100)

            if (chance_acerto < 65):

                $ oponente_damage = renpy.random.randint(2, 6)

                $ mago_hp -= oponente_damage

                n " {i}*a ganjee te ataca!*{/i} (dano recebido - [oponente_damage]hp)"

                play sound "musics/efeito_sonoro/gemido-combate.mp3"

            else:
                n "a ganjee parte em sua direção mas você consegue desviar!"

    hide screen batalha_generica
    "ganjees derrotados!"
    jump morte_ganjees

label batalha_hidra:

    show mc normal at left:
        zoom 0.6
    with dissolve

    show hydra at right:
        zoom 2
        ypos 900
    with dissolve

    play music "musics/Makai Symphony - Dragon Castle.mp3"


    #$ oponente_max_hp = 30
    $ mago_max_hp = 60
    #$ oponente_hp = oponente_max_hp
    $ mago_hp = mago_max_hp
    $ elixirHP_left = 10
    $ mago_max_mp = 50
    $ mago_mp = mago_max_mp
    $ elixirHP_left = 10
    $ elixirMP_left = 5

    show screen batalha_generica

    while (oponente_hp > 0):

        if mago_hp > 0:
            menu batalha13:

                "Ataque com espada ( 5 de dano)":

                    play sound "musics/efeito_sonoro/ataque espada.mp3"

                    $ mago_damage = 5
                    $ oponente_hp -= mago_damage
                    mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"


                "Bola de fogo (2 a 8 de dano)":

                    if(mago_mp >= 6):
                        play sound "musics/efeito_sonoro/bola de fogo.mp3"

                        $ mago_damage = renpy.random.randint(2, 8)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 30
                        mc "Bola de fogo!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha13

                "Raio arcano (1 a 12 de dano)":

                    if(mago_mp >= 10):
                        play sound "musics/efeito_sonoro/raio arcano.mp3" volume 0.7

                        $ mago_damage = renpy.random.randint(1, 12)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 5
                        mc "Raio arcano!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha13

                "tomar elixir da vida (tem [elixirHP_left] elixires)" if elixirHP_left > 0:
                    $ mago_hp = min(mago_hp+15, mago_max_hp)
                    $ elixirHP_left -= 1
                    n "{i}*você sente suas feridas cicatrizarem!*{/i} (vida curada - 15 hp)"

                "tomar elixir de mana (tem [elixirMP_left] elixires)" if elixirMP_left > 0:
                    $ mago_mp = min(mago_mp+14, mago_max_mp)
                    $ elixirMP_left -= 1
                    n "{i}*você sente suas forças voltarem!*{/i} (mana restaurada - 14 mp)"

        else:
            hide screen batalha_generica
            jump final_ruim

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(4, 10)

            $ mago_hp -= oponente_damage

            n " {i}*o oponente te arrasta para o seu covil!*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    'oponente derrotado!!!'
    jump dois29

label batalha_hidra_vs_hidra:
    show hydra_shiny at flip, left:
        zoom 0.7
        ypos 900
    with dissolve

    show hydra at right:
        zoom 2
        ypos 900
    with dissolve

    play music "musics/Makai Symphony - Dragon Castle.mp3"


    $ oponente_max_hp = 80
    $ mago_max_hp = 60
    $ oponente_hp = oponente_max_hp
    $ mago_hp = mago_max_hp
    $ elixirHP_left = 10
    $ mago_max_mp = 50
    $ mago_mp = mago_max_mp
    $ elixirHP_left = 10
    $ elixirMP_left = 5

    show screen batalha_generica

    while (oponente_hp > 0):

        if mago_hp > 0:
            menu batalha14:

                "Ataque com garras ( 7 de dano)":

                    play sound "musics/efeito_sonoro/garras hidra.mp3"

                    $ mago_damage = 5
                    $ oponente_hp -= mago_damage
                    "Raaaaah!!!!! (dano causado - [mago_damage]hp)"


                "Avanço das cabeças(3 a 9 de dano)":

                    play sound "musics/efeito_sonoro/hidra ataque cabeça.mp3"

                    $ mago_damage = renpy.random.randint(3, 8)
                    $ oponente_hp -= mago_damage
                    "Raaaah!!!!!!! (dano causado - [mago_damage]hp)"

                "Sopro flamejante (1 a 15 de dano)":

                    if(mago_mp >= 6):
                        play sound "musics/efeito_sonoro/bola de fogo.mp3"

                        $ mago_damage = renpy.random.randint(1, 15)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 6
                        "shushhhh (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha14

                #"tomar elixir da vida (tem [elixirHP_left] elixires)" if elixirHP_left > 0:
                #    $ mago_hp = min(mago_hp+15, mago_max_hp)
                #    $ elixirHP_left -= 1
                #    n "{i}*você sente suas feridas cicatrizarem!*{/i} (vida curada - 15 hp)"

                #"tomar elixir de mana (tem [elixirMP_left] elixires)" if elixirMP_left > 0:
                #    $ mago_mp = min(mago_mp+14, mago_max_mp)
                #    $ elixirMP_left -= 1
                #    n "{i}*você sente suas forças voltarem!*{/i} (mana restaurada - 14 mp)"

        else:
            hide screen batalha_generica

            hide hydra_shiny

            n "a sua hidra pereceu! cabe a você terminar o trabalho que ela começou"

            jump batalha_hidra

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(4, 10)

            $ mago_hp -= oponente_damage

            n " {i}*o oponente te arrasta para o seu covil!*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    'oponente derrotado!!!'
    jump dois29

label batalha_balthus1:

    scene arena_final1

    with dissolve

    show mc bombado at left:
        zoom 0.6
    with dissolve

    show balthus normal at right:
        zoom 0.7
    with dissolve

    $ oponente_max_hp = 120
    $ mago_max_hp = 100
    $ oponente_hp = oponente_max_hp
    $ mago_hp = mago_max_hp
    $ elixirHP_left = 10
    $ mago_max_mp = 80
    $ mago_mp = mago_max_mp
    $ elixirHP_left = 10
    $ elixirMP_left = 5

    show screen batalha_balthus

    while (oponente_hp > 0):

        if mago_hp > 0:
            menu batalha15:

                "estilo yore tormenta das espadas (10 de dano)":

                    play sound "musics/efeito_sonoro/ataque espada.mp3"

                    $ mago_damage = 10
                    $ oponente_hp -= mago_damage
                    mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"


                "estilo yore rugido do dragao (6 a 14 de dano)":

                    if(mago_mp >= 6):
                        play sound "musics/efeito_sonoro/bola de fogo.mp3"

                        $ mago_damage = renpy.random.randint(6, 14)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 6
                        mc "estilo yore! rugido do dragao!!!!! (dano causado - [mago_damage]hp)"

                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha15

                    if oponente_hp <= 0:
                        jump segredo

                "estilo yore desabrochar arcano (6 a 20 de dano)":

                    if(mago_mp >= 10):
                        play sound "musics/efeito_sonoro/raio arcano.mp3" volume 0.7

                        $ mago_damage = renpy.random.randint(6, 20)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 10
                        mc "estilo yore! desabrochar arcano!!!!! (dano causado - [mago_damage]hp)"

                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha15

                "tomar elixir da vida (tem [elixirHP_left] elixires)" if elixirHP_left > 0:
                    $ mago_hp = min(mago_hp+15, mago_max_hp)
                    $ elixirHP_left -= 1
                    n "{i}*você sente suas feridas cicatrizarem!*{/i} (vida curada - 15 hp)"

                "tomar elixir de mana (tem [elixirMP_left] elixires)" if elixirMP_left > 0:
                    $ mago_mp = min(mago_mp+14, mago_max_mp)
                    $ elixirMP_left -= 1
                    n "{i}*você sente suas forças voltarem!*{/i} (mana restaurada - 14 mp)"

        else:
            hide screen batalha_balthus
            jump final_ruim

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(6, 10)

            $ mago_hp -= oponente_damage

            n " {i}*o grande Balthus te ataca !*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_balthus
    'Balthus derrotado!!!'
    jump despertar_balthus

label batalha_balthus2:
    scene arena_final2:
        zoom 1.3
    with dissolve

    show mc bombado at left:
        zoom 0.6
    with dissolve

    show balthus bombado at right:
        ypos 1500
        xpos 2100
        zoom 1.5
    with dissolve

    $ oponente_max_hp = 180
    $ mago_max_hp = 100
    $ oponente_hp = oponente_max_hp
    $ mago_hp = mago_max_hp
    $ elixirHP_left = 10
    $ mago_max_mp = 80
    $ mago_mp = mago_max_mp
    $ elixirHP_left = 10
    $ elixirMP_left = 5

    show screen batalha_balthus

    while (oponente_hp > 0):

        if mago_hp > 0:
            menu batalha16:

                "estilo yore tormenta das espadas (10 de dano)":

                    play sound "musics/efeito_sonoro/ataque espada.mp3"

                    $ mago_damage = 10
                    $ oponente_hp -= mago_damage
                    mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"
                    if(oponente_hp <= 0):
                        jump facada

                "estilo yore rugido do dragao (6 a 14 de dano)":

                    if(mago_mp >= 6):
                        play sound "musics/efeito_sonoro/bola de fogo.mp3"

                        $ mago_damage = renpy.random.randint(6, 14)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 6
                        mc "estilo yore! rugido do dragao!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha16


                "estilo yore desabrochar arcano (6 a 20 de dano)":

                    if(mago_mp >= 10):
                        play sound "musics/efeito_sonoro/raio arcano.mp3" volume 0.7

                        $ mago_damage = renpy.random.randint(6, 20)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 10
                        mc "estilo yore! desabrochar arcano!!!!! (dano causado - [mago_damage]hp)"

                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha16

                "tomar elixir da vida (tem [elixirHP_left] elixires)" if elixirHP_left > 0:
                    $ mago_hp = min(mago_hp+15, mago_max_hp)
                    $ elixirHP_left -= 1
                    n "{i}*você sente suas feridas cicatrizarem!*{/i} (vida curada - 15 hp)"

                "tomar elixir de mana (tem [elixirMP_left] elixires)" if elixirMP_left > 0:
                    $ mago_mp = min(mago_mp+14, mago_max_mp)
                    $ elixirMP_left -= 1
                    n "{i}*você sente suas forças voltarem!*{/i} (mana restaurada - 14 mp)"

        else:
            hide screen batalha_balthus
            jump final_ruim

        if(oponente_hp > 0):

            $ chance_acerto = renpy.random.randint(1, 100)

            if (chance_acerto < 75):

                $ oponente_damage = renpy.random.randint(8, 15)

                $ mago_hp -= oponente_damage

                n " {i}*o grande Balthus te ataca !*{/i} (dano recebido - [oponente_damage]hp)"

                play sound "musics/efeito_sonoro/gemido-combate.mp3"
            else:
                n "balthus avança em sua direção com poder nas mãos, mas você consegue desviar aproveitando a chance para contraatacar com sua espada!"
                play sound "musics/efeito_sonoro/ataque espada.mp3"

                $ mago_damage = 10
                $ oponente_hp -= mago_damage
                mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"

    hide screen batalha_balthus
    'Balthus derrotado!!!'
    jump morte_balthus

label batalha_giras:
    play music "musics/Makai Symphony - Dragon Castle.mp3"
    show mc invertido at right:
        zoom 0.9
        xpos 2350
    with dissolve
    #show giras
    $ oponente_max_hp = 65
    $ mago_max_hp = 60
    $ oponente_hp = oponente_max_hp
    $ mago_hp = mago_max_hp
    $ elixirHP_left = 10
    $ mago_max_mp = 50
    $ mago_mp = mago_max_mp
    $ elixirHP_left = 10
    $ elixirMP_left = 5

    show screen batalha_generica1

    while (oponente_hp > 0):

        if mago_hp > 0:
            menu batalha17:

                "Ataque com espada ( 5 de dano)":

                    play sound "musics/efeito_sonoro/ataque espada.mp3"

                    $ mago_damage = 5
                    $ oponente_hp -= mago_damage
                    mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"


                "Bola de fogo (2 a 8 de dano)":

                    if(mago_mp >= 6):
                        play sound "musics/efeito_sonoro/bola de fogo.mp3"

                        $ mago_damage = renpy.random.randint(2, 8)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 6
                        mc "Bola de fogo!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha17

                "Raio arcano (1 a 12 de dano)":

                    if(mago_mp >= 10):
                        play sound "musics/efeito_sonoro/raio arcano.mp3" volume 0.7

                        $ mago_damage = renpy.random.randint(1, 12)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 10
                        mc "Raio arcano!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha17

                "tomar elixir da vida (tem [elixirHP_left] elixires)" if elixirHP_left > 0:
                    $ mago_hp = min(mago_hp+15, mago_max_hp)
                    $ elixirHP_left -= 1
                    n "{i}*você sente suas feridas cicatrizarem!*{/i} (vida curada - 15 hp)"

                "tomar elixir de mana (tem [elixirMP_left] elixires)" if elixirMP_left > 0:
                    $ mago_mp = min(mago_mp+14, mago_max_mp)
                    $ elixirMP_left -= 1
                    n "{i}*você sente suas forças voltarem!*{/i} (mana restaurada - 14 mp)"

        else:
            hide screen batalha_generica1
            jump final_ruim

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(2, 6)

            $ mago_hp -= oponente_damage

            n " {i}*os oponentes mordem seus braços!*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    #hide mc
    #hide giras
    'Oponente derrotado e você parte em direção às passagens!'
    jump dois20

label batalha_devlin:
    n "Você avança com sua espada e parte para a batalha!"
    show mc normal at left:
        zoom 0.6
    with dissolve
    $ oponente_max_hp = 60
    $ mago_max_hp = 60
    $ oponente_hp = oponente_max_hp
    $ mago_hp = mago_max_hp
    $ elixirHP_left = 10
    $ mago_max_mp = 50
    $ mago_mp = mago_max_mp
    $ elixirHP_left = 10
    $ elixirMP_left = 5

    show screen batalha_generica

    while (oponente_hp > 0):

        if mago_hp > 0:
            menu batalha18:

                "Ataque com espada ( 5 de dano)":

                    play sound "musics/efeito_sonoro/ataque espada.mp3"

                    #$ mago_damage = 5
                    #$ oponente_hp -= mago_damage
                    #mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"
                    n "você ve sua espada atravessar o corpo da criatura sem causar dano algum!"
                    $renpy.notify("ataque ineficaz contra espectros!!")
                    play sound "musics/efeito_sonoro/nao tem o item.mp3"


                "Bola de fogo (2 a 8 de dano)":

                    if(mago_mp >= 6):
                        play sound "musics/efeito_sonoro/bola de fogo.mp3"

                        $ mago_damage = renpy.random.randint(1, 4)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 6
                        mc "Bola de fogo!!!!! (dano causado - [mago_damage]hp)"
                        n "o ataque quase não causa dano! o inimigo é feito de puro fogo!"
                        $renpy.notify("ataque é ineficaz!!")
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha18

                "Raio arcano (1 a 12 de dano)":

                    if(mago_mp >= 10):
                        play sound "musics/efeito_sonoro/raio arcano.mp3" volume 0.7

                        $ mago_damage = renpy.random.randint(1, 12)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 10
                        mc "Raio arcano!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha18

                "tomar elixir da vida (tem [elixirHP_left] elixires)" if elixirHP_left > 0:
                    $ mago_hp = min(mago_hp+15, mago_max_hp)
                    $ elixirHP_left -= 1
                    n "{i}*você sente suas feridas cicatrizarem!*{/i} (vida curada - 15 hp)"

                "tomar elixir de mana (tem [elixirMP_left] elixires)" if elixirMP_left > 0:
                    $ mago_mp = min(mago_mp+14, mago_max_mp)
                    $ elixirMP_left -= 1
                    n "{i}*você sente suas forças voltarem!*{/i} (mana restaurada - 14 mp)"

        else:
            hide screen batalha_generica
            jump final_ruim

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(2, 6)

            $ mago_hp -= oponente_damage

            n " {i}*o oponente te arrasta para o seu covil!*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    'Oponente derrotado e você ganha a chance de inspecionar outro item da cozinha!'
    jump um7

label batalha_gargula:
    play music "musics/Makai Symphony - Dragon Castle.mp3"

    show gargula_clone at left:
        zoom 1.8
    with dissolve

    show gargula at right:
    with dissolve

    $ oponente_max_hp = 60
    $ mago_max_hp = 60
    $ oponente_hp = oponente_max_hp
    $ mago_hp = mago_max_hp
    $ elixirHP_left = 10
    $ mago_max_mp = 50
    $ mago_mp = mago_max_mp
    $ elixirHP_left = 0
    $ elixirMP_left = 0

    show screen batalha_generica

    while (oponente_hp > 0):

        if mago_hp > 0:
            menu batalha19:

                "Ataque com garra ( 8 de dano)":

                    play sound "musics/efeito_sonoro/ataque espada.mp3"

                    $ mago_damage = 8
                    $ oponente_hp -= mago_damage
                    mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"

                "Bola de fogo (2 a 8 de dano)":

                    if(mago_mp >= 6):
                        play sound "musics/efeito_sonoro/bola de fogo.mp3"

                        $ mago_damage = renpy.random.randint(2, 8)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 6
                        mc "Bola de fogo!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha19

                "choque do trovão (1 a 12 de dano)":

                    if(mago_mp >= 10):
                        play sound "musics/efeito_sonoro/raio arcano.mp3" volume 0.7

                        $ mago_damage = renpy.random.randint(1, 12)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 10
                        mc "Raio arcano!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha19

        else:
            hide screen batalha_generica
            n "você fica com medo de enfrentar a gargula sozinho e corre de volta para o portal do meio"
            jump seis4

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(5, 8)

            $ mago_hp -= oponente_damage

            n " {i}*a gargula te ataca!*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    hide gargula
    "gargula derrotado!"
    jump seis2

label batalha_elfo_negro:
    play music "musics/Makai Symphony - Dragon Castle.mp3"

    show mc normal at left:
        zoom 0.551111111
    with fade

    show elfo_negro at right:
        zoom 0.8
        ypos 1150
    with dissolve

    $ oponente_max_hp = 85
    $ mago_max_hp = 60
    $ oponente_hp = oponente_max_hp
    $ mago_hp = mago_max_hp
    $ elixirHP_left = 10
    $ mago_max_mp = 50
    $ mago_mp = mago_max_mp
    $ elixirHP_left = 10
    $ elixirMP_left = 5

    show screen batalha_generica

    while (oponente_hp > 0):

        if mago_hp > 0:
            menu batalha20:

                "Ataque com espada ( 5 de dano)":

                    play sound "musics/efeito_sonoro/ataque espada.mp3"

                    $ mago_damage = 5
                    $ oponente_hp -= mago_damage
                    mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"


                "Bola de fogo (2 a 8 de dano)":

                    if(mago_mp >= 6):
                        play sound "musics/efeito_sonoro/bola de fogo.mp3"

                        $ mago_damage = renpy.random.randint(2, 8)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 6
                        mc "Bola de fogo!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha20

                "Raio arcano (1 a 12 de dano)":

                    if(mago_mp >= 10):
                        play sound "musics/efeito_sonoro/raio arcano.mp3" volume 0.7

                        $ mago_damage = renpy.random.randint(1, 12)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 10
                        mc "Raio arcano!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha20

                "tomar elixir da vida (tem [elixirHP_left] elixires)" if elixirHP_left > 0:
                    $ mago_hp = min(mago_hp+15, mago_max_hp)
                    $ elixirHP_left -= 1
                    n "{i}*você sente suas feridas cicatrizarem!*{/i} (vida curada - 15 hp)"

                "tomar elixir de mana (tem [elixirMP_left] elixires)" if elixirMP_left > 0:
                    $ mago_mp = min(mago_mp+14, mago_max_mp)
                    $ elixirMP_left -= 1
                    n "{i}*você sente suas forças voltarem!*{/i} (mana restaurada - 14 mp)"

        else:
            hide screen batalha_generica
            jump final_ruim

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(4, 7)

            $ mago_hp -= oponente_damage

            n " {i}*o oponente te ataca!!*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    'oponente derrotado!!!'
    hide elfo_negro with dissolve
    hide mc normal with dissolve
    jump dois72

label batalha_golem:
    play music "musics/Makai Symphony - Dragon Castle.mp3"

    show mc normal at left:
        zoom 0.6
    with fade

    show pedroso:
        zoom 1.7
        ypos 100
        xpos 600
    with dissolve

    #$ oponente_max_hp = 60
    $ mago_max_hp = 60
    #$ oponente_hp = oponente_max_hp
    $ mago_hp = mago_max_hp
    $ elixirHP_left = 10
    $ mago_max_mp = 50
    $ mago_mp = mago_max_mp
    $ elixirHP_left = 10
    $ elixirMP_left = 5

    show screen batalha_generica

    while (oponente_hp > 0):

        if mago_hp > 0:
            menu batalha21:

                "Ataque com espada ( 5 de dano)":

                    play sound "musics/efeito_sonoro/ataque espada.mp3"

                    $ mago_damage = 5
                    $ oponente_hp -= mago_damage
                    mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"


                "Bola de fogo (2 a 8 de dano)":

                    if(mago_mp >= 6):
                        play sound "musics/efeito_sonoro/bola de fogo.mp3"

                        $ mago_damage = renpy.random.randint(2, 8)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 6
                        mc "Bola de fogo!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha21

                "Raio arcano (1 a 12 de dano)":

                    if(mago_mp >= 10):
                        play sound "musics/efeito_sonoro/raio arcano.mp3" volume 0.7

                        $ mago_damage = renpy.random.randint(1, 12)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 10
                        mc "Raio arcano!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha21

                "tomar elixir da vida (tem [elixirHP_left] elixires)" if elixirHP_left > 0:
                    $ mago_hp = min(mago_hp+15, mago_max_hp)
                    $ elixirHP_left -= 1
                    n "{i}*você sente suas feridas cicatrizarem!*{/i} (vida curada - 15 hp)"

                "tomar elixir de mana (tem [elixirMP_left] elixires)" if elixirMP_left > 0:
                    $ mago_mp = min(mago_mp+14, mago_max_mp)
                    $ elixirMP_left -= 1
                    n "{i}*você sente suas forças voltarem!*{/i} (mana restaurada - 14 mp)"

        else:
            hide screen batalha_generica
            jump final_ruim

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(7, 8)

            $ mago_hp -= oponente_damage

            n " {i}*o oponente te da um soco!!*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    'oponente derrotado!!!'
    hide pedroso with dissolve
    hide mc normal
    jump um47

label batalha_fantasmas:
    play music "musics/Makai Symphony - Dragon Castle.mp3"

    hide mulher_roupa
    with dissolve

    show mc normal at left:
        zoom 0.6
    with fade

    $ oponente_max_hp = 60
    $ mago_max_hp = 60
    $ oponente_hp = oponente_max_hp
    $ mago_hp = mago_max_hp
    $ elixirHP_left = 10
    $ mago_max_mp = 50
    $ mago_mp = mago_max_mp
    $ elixirHP_left = 10
    $ elixirMP_left = 5

    show screen batalha_generica

    while (oponente_hp > 0):

        if mago_hp > 0:
            menu batalha22:

                "Ataque com espada ( 5 de dano)":

                    play sound "musics/efeito_sonoro/ataque espada.mp3"

                    #$ mago_damage = 5
                    #$ oponente_hp -= mago_damage
                    #mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"
                    n "você ve sua espada atravessar o corpo da criatura sem causar dano algum!"
                    $renpy.notify("ataque ineficaz contra espectros!!")
                    play sound "musics/efeito_sonoro/nao tem o item.mp3"

                "Bola de fogo (2 a 8 de dano)":

                    if(mago_mp >= 6):
                        play sound "musics/efeito_sonoro/bola de fogo.mp3"

                        $ mago_damage = renpy.random.randint(2, 8)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 6
                        mc "Bola de fogo!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha22

                "Raio arcano (1 a 12 de dano)":

                    if(mago_mp >= 10):
                        play sound "musics/efeito_sonoro/raio arcano.mp3" volume 0.7

                        $ mago_damage = renpy.random.randint(1, 12)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 10
                        mc "Raio arcano!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha22

                "tomar elixir da vida (tem [elixirHP_left] elixires)" if elixirHP_left > 0:
                    $ mago_hp = min(mago_hp+15, mago_max_hp)
                    $ elixirHP_left -= 1
                    n "{i}*você sente suas feridas cicatrizarem!*{/i} (vida curada - 15 hp)"

                "tomar elixir de mana (tem [elixirMP_left] elixires)" if elixirMP_left > 0:
                    $ mago_mp = min(mago_mp+14, mago_max_mp)
                    $ elixirMP_left -= 1
                    n "{i}*você sente suas forças voltarem!*{/i} (mana restaurada - 14 mp)"

        else:
            hide screen batalha_generica
            jump final_ruim

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(4, 7)

            $ mago_hp -= oponente_damage

            n " {i}*o oponente te ataca!!*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    'oponente derrotado!!!'
    hide mc normal with fade
    hide fantasmagorico
    jump seis

label batalha_golem_vs_golem:
    play music "musics/Makai Symphony - Dragon Castle.mp3"

    show golem_clone at left:
        zoom 1.0
    with dissolve

    show pedroso:
        zoom 1.7
        ypos 100
        xpos 600
    with dissolve

    $ oponente_max_hp = 80
    $ mago_max_hp = 80
    $ oponente_hp = oponente_max_hp
    $ mago_hp = mago_max_hp
    $ elixirHP_left = 10
    $ mago_max_mp = 50
    $ mago_mp = mago_max_mp
    $ elixirHP_left = 0
    $ elixirMP_left = 0

    show screen batalha_generica

    while (oponente_hp > 0):

        if mago_hp > 0:
            menu batalha23:

                "soco de pedra ( 8 de dano)":

                    play sound "musics/efeito_sonoro/ataque espada.mp3"

                    $ mago_damage = 8
                    $ oponente_hp -= mago_damage
                    mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"



                "Bola de fogo (2 a 8 de dano)":

                    if(mago_mp >= 6):
                        play sound "musics/efeito_sonoro/bola de fogo.mp3"

                        $ mago_damage = renpy.random.randint(2, 8)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 6
                        mc "Bola de fogo!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha23

                "choque do trovão (1 a 12 de dano)":

                    if(mago_mp >= 10):
                        play sound "musics/efeito_sonoro/raio arcano.mp3" volume 0.7

                        $ mago_damage = renpy.random.randint(1, 12)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 10
                        mc "Raio arcano!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha23

                "tomar elixir da vida (tem [elixirHP_left] elixires)" if elixirHP_left > 0:
                    $ mago_hp = min(mago_hp+15, mago_max_hp)
                    $ elixirHP_left -= 1
                    n "{i}*você sente suas feridas cicatrizarem!*{/i} (vida curada - 15 hp)"

                "tomar elixir de mana (tem [elixirMP_left] elixires)" if elixirMP_left > 0:
                    $ mago_mp = min(mago_mp+14, mago_max_mp)
                    $ elixirMP_left -= 1
                    n "{i}*você sente suas forças voltarem!*{/i} (mana restaurada - 14 mp)"

        else:
            hide golem_clone
            hide screen batalha_generica
            n "o seu golem pereceu, agora cabe a você terminar o que ele começou!"
            jump batalha_golem

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(7, 8)

            $ mago_hp -= oponente_damage

            n " {i}*o golem te ataca!*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    hide pedroso
    hide golem_clone
    "golem derrotado!"
    jump um47

label segredo:
    hide screen batalha_balthus
    stop music
    n "balthus cai ao chão, ofegante e antes de seu ultimo suspiro, ele te conta o real objetivo dele:"

    b "durante meus anos de estudo duas entidades entraram em contato comigo, os arautos, eles disseram que eu tinha potencial e propuseram uma aposta comigo."
    b "caso eu dominasse toda a região, eles me tornariam um deles, me chamariam de arauto da morte, na época eu aceitei sem pensar duas vezes."
    b "entretanto, eu percebi que isso foi apenas uma grande mentira! que eles haviam me tornado apenas um escravo deles."
    b "e agora que você me derrotou, eles devem vir atras de você, não cometa o mesmo erro que eu."

    n "balthus levanta a mão em sua direção, como se fosse lançar uma magia em você."

    play sound "musics/efeito_sonoro/raio arcano.mp3" volume 0.7

    n "antes que você pudesse fazer qualquer coisa para se defender, a rajada de mana te atinge em cheio, a imagem dos arautos aparece na sua mente, esse é a prova de que balthus disse a verdade?"

    b "esse é o meu presente para você, espero que esses novos poderes lhe sirvam bem, faça a escolha correta."

    n "apos isso, ele cai ao chão sem vida"

    n "você sente uma tontura repentina e cai ao chão sem ter tempo de reação"

    scene black with fade
    if (morte_goblins):
        jump arauto_destruicao
    else:
        jump arauto_criacao

label arauto_destruicao:

    scene destruicao:
        zoom 2.4

    n "Você olha para cima e observa oque parece ser uma entidade enorme, em meio a um cenário desolador"

    show dartmol at right:
        zoom 0.5
        xpos 2200
        ypos 1500
    with dissolve

    "Ah olá,você gosta mesmo de dormir hein?"
    "Era pro Balthus estar aqui e tudo oque vejo é você..."
    "[Protagonista1]"
    "Parece que você destruiu meu brinquedo, mas o seu ainda está de pé..."
    "Depois de todo o trabalho que eu tive pra arrumar todas as peças..."
    "Bem isso não estava planejado, mas que seja! Farei jus ao meu nome como arauto da destruição!"
    play music "musics/andrids theme.mp3"
    A "Eu sou Dartmol, e serei seu adversário!!!"
    A "Agora vamos!!!"
    jump batalha_destruicao

label arauto_criacao:

    "acorde campeão, ja dormiu demais, tenho uma proposta pra você"
    n "você abre os olhos e nota que esta em um ambiente totalmente novo, aparentemente um reino etereo"

    scene criacao:
        zoom 2.5

    show viniman at right:
        zoom 1.3
    with dissolve

    n "voce olha pra cima e nota uma gigantesca entidade te observando, possivelmente ela que te trouxe aqui"
    "finalmente acordou, fazem 5 horas que te trouxe pra cá, esta cansado? quer um pedaço de bolo de limao e suco?"
    "temos um assunto importante a tratar"
    n "como num passe de magica, uma mesa com bolos e sucos aparece a sua frente."
    n "voce pega um pedaço e ao dar uma mordida, você entra em extase, é a comida mais saborosa da sua vida!"
    n "suas feridas e seu cansaço desaparecem, você esta em sua melhor forma!"
    "agora que você esta pronto, preciso me apresentar, sou viniman, o arauto da criação!"
    V "você tambem deve escutar, invasor, ou prefere que te chame de [Protagonista1]?"
    V "nós os arautos preparamos com tanto carinho as peças e vocês atrapalharam tudo!"
    V "mas eu encontrarei o perdão no meu coração, com uma condição, vocês dois terminarem o que Balthus começou, aceitam?"
    menu:
        "juntar-se a eles":
            n "vocês aceitam a proposta"
            V "muito bem, vocês fizeram a escolha correta!"
            play sound "musics/efeito_sonoro/estalo.mp3"
            V "agora vá e cumpra a sua promessa!"

            jump final_lorde

        "recusar a proposta":
            play music "musics/viniman.mp3"
            n "vocês rejeitam a proposta! falando que Balthus contou toda a verdade!"
            V "aquele ingrato nos traiu?!?"
            V "tudo bem... ja que é o que vocês querem, se preparem para sentir a minha ira!"
            jump batalha_criacao

label batalha_destruicao:

    show mc bombado at left:
        zoom 0.6
    with dissolve

    show dartmol at right:
        zoom 0.5
        xpos 2700
        ypos 1500


    $ oponente_max_hp = 250
    $ mago_max_hp = 120
    $ oponente_hp = oponente_max_hp
    $ mago_hp = mago_max_hp
    $ elixirHP_left = 10
    $ mago_max_mp = 80
    $ mago_mp = mago_max_mp
    $ elixirHP_left = 10
    $ elixirMP_left = 5

    show screen batalha_dartmol

    while (oponente_hp > 0):

        if mago_hp > 0:
            menu batalhadestru:

                "estilo yore tormenta das espadas (15 de dano)":

                    play sound "musics/efeito_sonoro/ataque espada.mp3"

                    $ mago_damage = 15
                    $ oponente_hp -= mago_damage
                    mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"

                "estilo yore rugido do dragao (6 a 14 de dano)":

                    if(mago_mp >= 6):
                        play sound "musics/efeito_sonoro/bola de fogo.mp3"

                        $ mago_damage = renpy.random.randint(6, 14)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 6
                        mc "estilo yore! rugido do dragao!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalhadestru


                "estilo yore desabrochar arcano (6 a 20 de dano)":

                    if(mago_mp >= 10):
                        play sound "musics/efeito_sonoro/raio arcano.mp3" volume 0.7

                        $ mago_damage = renpy.random.randint(6, 20)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 10
                        mc "estilo yore! desabrochar arcano!!!!! (dano causado - [mago_damage]hp)"

                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalhadestru

                "tomar elixir da vida (tem [elixirHP_left] elixires)" if elixirHP_left > 0:
                    $ mago_hp = min(mago_hp+25, mago_max_hp)
                    $ elixirHP_left -= 1
                    n "{i}*você sente suas feridas cicatrizarem!*{/i} (vida curada - 25 hp)"

                "tomar elixir de mana (tem [elixirMP_left] elixires)" if elixirMP_left > 0:
                    $ mago_mp = min(mago_mp+14, mago_max_mp)
                    $ elixirMP_left -= 1
                    n "{i}*você sente suas forças voltarem!*{/i} (mana restaurada - 14 mp)"

        else:
            hide screen batalha_dartmol
            jump recomeco

        if(oponente_hp > 0):

            $ chance_acerto = renpy.random.randint(1, 100)

            if (chance_acerto < 75):

                $ oponente_damage = renpy.random.randint(10, 20)

                $ mago_hp -= oponente_damage

                n " {i}*o grande arauto te ataca !*{/i} (dano recebido - [oponente_damage]hp)"

                play sound "musics/efeito_sonoro/gemido-combate.mp3"
            else:
                n "dartmol avança em sua direção atirando raios de gelo, mas você consegue desviar aproveitando a chance para contraatacar com sua espada!"
                play sound "musics/efeito_sonoro/ataque espada.mp3"

                $ mago_damage = 15
                $ oponente_hp -= mago_damage
                mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"

    hide screen batalha_dartmol
    hide dartmol
    'dartmol derrotado!!!'
    jump morte_destru

label batalha_criacao:

    show mc bombado at left:
        zoom 0.6
    with dissolve

    show viniman at right:
        zoom 1.3

    $ oponente_max_hp = 250
    $ mago_max_hp = 120
    $ oponente_hp = oponente_max_hp
    $ mago_hp = mago_max_hp
    $ elixirHP_left = 10
    $ mago_max_mp = 80
    $ mago_mp = mago_max_mp
    $ elixirHP_left = 10
    $ elixirMP_left = 5

    show screen batalha_viniman

    while (oponente_hp > 0):

        if mago_hp > 0:
            menu batalhacria:

                "estilo yore tormenta das espadas (15 de dano)":

                    play sound "musics/efeito_sonoro/ataque espada.mp3"

                    $ mago_damage = 15
                    $ oponente_hp -= mago_damage
                    mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"

                "estilo yore rugido do dragao (6 a 14 de dano)":

                    if(mago_mp >= 6):
                        play sound "musics/efeito_sonoro/bola de fogo.mp3"

                        $ mago_damage = renpy.random.randint(6, 14)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 6
                        mc "estilo yore! rugido do dragao!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalhacria


                "estilo yore desabrochar arcano (6 a 20 de dano)":

                    if(mago_mp >= 10):
                        play sound "musics/efeito_sonoro/raio arcano.mp3" volume 0.7

                        $ mago_damage = renpy.random.randint(6, 20)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 10
                        mc "estilo yore! desabrochar arcano!!!!! (dano causado - [mago_damage]hp)"

                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalhacria

                "tomar elixir da vida (tem [elixirHP_left] elixires)" if elixirHP_left > 0:
                    $ mago_hp = min(mago_hp+25, mago_max_hp)
                    $ elixirHP_left -= 1
                    n "{i}*você sente suas feridas cicatrizarem!*{/i} (vida curada - 25 hp)"

                "tomar elixir de mana (tem [elixirMP_left] elixires)" if elixirMP_left > 0:
                    $ mago_mp = min(mago_mp+14, mago_max_mp)
                    $ elixirMP_left -= 1
                    n "{i}*você sente suas forças voltarem!*{/i} (mana restaurada - 14 mp)"

        else:
            hide screen batalha_viniman
            jump recomeco

        if(oponente_hp > 0):

            $ chance_acerto = renpy.random.randint(1, 100)

            if (chance_acerto < 75):

                $ oponente_damage = renpy.random.randint(10, 20)

                $ mago_hp -= oponente_damage

                n " {i}*o arauto te ataca !*{/i} (dano recebido - [oponente_damage]hp)"

                play sound "musics/efeito_sonoro/gemido-combate.mp3"
            else:
                n "viniman avança em sua direção com bolas de fogo, mas você consegue desviar aproveitando a chance para contraatacar com sua espada!"
                play sound "musics/efeito_sonoro/ataque espada.mp3"

                $ mago_damage = 15
                $ oponente_hp -= mago_damage
                mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"

    hide screen batalha_viniman
    hide viniman
    'viniman derrotado!!!'
    jump morte_cria

label morte_cria:
    n "Em meio a uma névoa densa e fria, surge outro ser que emana grandiozidade, mais um arauto aparece diante de você"
    play music "musics/andrids theme.mp3"

    show dartmol at right:
        zoom 0.5
        xpos 2700
        ypos 1500

    A "Ora ora..."
    A "Parece que viniman foi derrotado."
    A " [Protagonista1], saiba que em condições normais eu destruiria você,meu irmão merecia muito mais que sua morte,junto de seu brinquedo patético..."
    A "Mas viniman era honrado, e na medida do possível piedoso,ele nao aprovaria mais sangue."
    A "Escolham seu próprio futuro,vocês fizeram por merecer."
    A "daqui a pouco 'Ele' deve vir ao encontro de vocês, espero que se deem bem..."
    A "Quem sabe nós voltemos a nos ver..."
    A "Até mais"
    A "..."
    A "...."
    jump final_real

label morte_destru:
    n "dartmol jaz morto no chão!"
    n "você escruta um grande estrondo! aparecendo uma outra entidade, a qual voce julga ser o outro arauto"

    play music "musics/viniman.mp3"

    show viniman at right:
        zoom 1.3

    V "Mago!"
    V "Invasor, ou devo dizer [Protagonista1]!"

    V "o que vocês fizeram com meu irmão?!? ele provavelmente nao deu outra opção para vocês certo?"
    V "ele sempre foi muito esquentadinho mesmo"
    V "parabéns, voces alcançaram a liberdade de escolher o proprio destino! 'Ele' deve cuidar do resto, até mais"
    n "viniman se retira, levando o corpo de seu irmão junto! quem seria esse tal de 'Ele'?"
    jump final_real

label final_real:

    stop music

    hide viniman
    with pixellate
    hide dartmol
    with pixellate

    scene black
    with dissolve

    U "..."
    U "...."
    U "....."

    play sound "musics/efeito_sonoro/andando.mp3"

    mc "Então esse é o limite..."
    mc "..."
    mc "...."

    show mc at center:
        zoom 0.6
    with dissolve

    play sound "musics/efeito_sonoro/batendo monitor.mp3"


    mc "Você,aí do outro lado do que quer que seja isso!"
    mc "Eu não sei oque diabos está acontecendo, tudo desapareceu, mas por algum motivo,você não."
    mc "Você nao me parece um arauto, eles temeram você, na verdade não parece com nada que já encontrei antes."
    mc "Eu estou preso neste vazio infernal a mais tempo do que gostaria, você é o tal [Protagonista1]?"

    menu:
        "sim":
            mc-"E você pode me ajudar?"

    menu:
        "Eu nao sei como":
            mc "Droga..."

    mc "Se os arautos deram tanta atencão a você, deve ter algo que pode ser feito!"

    U "Não se preocupem, mago, [Protagonista1], Já está acontecendo..."

    mc "Oque?"

    play music "musics/q lindo.mp3"
    scene entrada_balthus:
        zoom 2.0
    show mc at center:
        zoom 0.6
    pause 3

    scene quarto_hydra:
        zoom 1.5
    show mc at center:
        zoom 0.6
    pause 3

    scene arena_final1:
        zoom 1
    show mc at center:
        zoom 0.6
    pause 3

    scene topo_torre:
        zoom 1
    show mc at center:
        zoom 0.6
    pause 3

    scene entrada_caos:
        zoom 1.8
    show mc at center:
        zoom 0.6
    pause 3

    scene caminho_cidadela:
        zoom 1.5
    show mc at center:
        zoom 0.6
    pause 3

    scene cidadela1:
        zoom 1
    show mc at center:
        zoom 0.6
    pause 3

    scene portao:
        zoom 1
    show mc at center:
        zoom 0.6
    pause 3

    scene sala_oseamus:
        zoom 1.5
    show mc at center:
        zoom 0.6
    pause 3

    scene corredor_escuro:
        zoom 3
    show mc at center:
        zoom 0.6
    pause 3

    mc "Será que era disso que o Balthus estava falando?"

    scene esgoto:
        zoom 1
    show mc at center:
        zoom 0.6
    pause 2

    scene sala_golem:
        zoom 1.3
    show mc at center:
        zoom 0.6
    pause 2

    scene sala_jantar:
        zoom 1
    show mc at center:
        zoom 0.6
    pause 2

    scene portais:
        zoom 2.0
    show mc at center:
        zoom 0.6
    pause 2

    scene quarto_morena:
        zoom 1
    show mc at center:
        zoom 0.6
    pause 2

    scene quarto_goblin:
        zoom 1
    show mc at center:
        zoom 0.6
    pause 2

    scene biblioteca:
        zoom 1
    show mc at center:
        zoom 0.6
    pause 2

    scene salao at truecenter:
        zoom 1.5
    show mc at center:
        zoom 0.6
    pause 2

    scene prisao at truecenter:
        zoom 2.8
    show mc at center:
        zoom 0.6
    pause 2

    scene bg14 at truecenter:
        zoom 1.09
    show mc at center:
        zoom 0.6
    pause 2

    scene bg at truecenter:
        zoom 2.0
    show mc at center:
        zoom 0.6
    pause 2

    scene quarto_escuro:
        zoom 1.5
    show mc at center:
        zoom 0.6
    pause 2

    scene bg13 at truecenter:
        zoom 0.7
    show mc at center:
        zoom 0.6
    pause 2

    scene casa_prota:
        zoom 2.2
    show mc at center:
        zoom 0.6
    pause 2

    mc "Aquela é, minha antiga casa? Mas ela foi..."
    U "Você não precisa mais lutar ,tsugausa,nunca mais."
    mc "Meu nome?! Mas como..."
    U "E [Protagonista1], seu trabalho foi executado com exímio."
    U "Não esperaria menos do 'invasor'"
    U "..."
    U "...."
    mc "Parece que Ele se foi,eu nem tive a chance de perguntar quem ele era..."
    mc "Seja lá o que foi tudo isso, eu te devo um obrigado."
    mc "Caramba eu estou sendo um babaca, não sei se da pra confiar nisso tudo mas finalmente parece que eu tenho paz,que eu tenho escolha..."
    mc "Obrigado [Protagonista1],muito obrigado!"

    hide mc
    with dissolve
    play sound "musics/efeito_sonoro/andando.mp3"

    pause 4

    stop sound

    jump creditos

label final_alt:

    stop music

    scene arautos at center:
        zoom 3

    show dartmol at right:
        zoom 0.5
        xpos 2700
        ypos 1500

    show viniman at left:
        zoom 1.3

    n "você misteriosamente é teleportado a um plano etereo de gelo e fogo, há duas entidades a sua frente conversando entre si"

    n "eles notam a sua presença e olham para voce com um olhar inquisitivo"

    a2 "Como você chegou aqui?!"

    a2 "mas que Po..."

    a2 "você nao deveria estar aqui!"
    jump batalha_arautos

label batalha_arautos:
    play music "musics/batalha dupla.mp3"

    show mc normal:
        zoom 0.6
        xpos 0
        ypos 200
    with dissolve

    show dartmol:
        zoom 0.3
        xpos 2500
        ypos 1200
    with dissolve

    show viniman:
        xpos 900
        zoom 1
    with dissolve

    $ oponente_max_hp = 500
    $ mago_max_hp = 60
    $ oponente_hp = oponente_max_hp
    $ mago_hp = mago_max_hp
    $ mago_max_mp = 50
    $ mago_mp = mago_max_mp
    $ elixirHP_left = 10
    $ elixirMP_left = 5


    show screen batalha_generica

    while (oponente_hp > 0):

        if mago_hp > 0:
            menu batalha1:

                "Ataque com espada (5 de dano)":

                    play sound "musics/efeito_sonoro/ataque espada.mp3"

                    $ oponente_hp -= 5
                    $mago_damage = 5
                    mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"


                "Bola de fogo (2 a 8 de dano)":
                    if(mago_mp >= 6):
                        play sound "musics/efeito_sonoro/bola de fogo.mp3"

                        $ mago_damage = renpy.random.randint(2, 8)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 6
                        mc "Bola de fogo!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha1

                "Raio arcano (1 a 12 de dano)":

                    if(mago_mp >= 10):
                        play sound "musics/efeito_sonoro/raio arcano.mp3" volume 0.7

                        $ mago_damage = renpy.random.randint(1, 12)
                        $ oponente_hp -= mago_damage
                        $ mago_mp -= 10
                        mc "Raio arcano!!!!! (dano causado - [mago_damage]hp)"
                    else:
                        $renpy.notify("mana insuficiente!!")
                        play sound "musics/efeito_sonoro/sem mana.mp3"
                        jump batalha1

                "tomar elixir da vida (tem [elixirHP_left] elixires)" if elixirHP_left > 0:
                    $ mago_hp = min(mago_hp+15, mago_max_hp)
                    $ elixirHP_left -= 1
                    n "{i}*você sente suas feridas cicatrizarem!*{/i} (vida curada - 15 hp)"

                "tomar elixir de mana (tem [elixirMP_left] elixires)" if elixirMP_left > 0:
                    $ mago_mp = min(mago_mp+14, mago_max_mp)
                    $ elixirMP_left -= 1
                    n "{i}*você sente suas forças voltarem!*{/i} (mana restaurada - 14 mp)"
        else:
            hide screen batalha_generica
            a2 "eliminamos esse pequeno problema, onde estavamos mesmo?"
            jump final_ruim

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(10, 10)

            $ mago_hp -= oponente_damage

            n " {i}*os arautos te atacam com fogo e gelo!*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    'oponentes derrotados!!!'
    jump dois51

label recomeco:

    scene arautos at center:
        zoom 3
    with dissolve

    show dartmol at right:
        zoom 0.8
    with dissolve

    show viniman at left:
        zoom 1.3
    with dissolve

    A "é viniman... não alcançamos nosso objetivo novamente... o que acha de tentarmos de novo?"

    V "Pensando bem... porque não?"

    A "entao eu começo!"
    play sound "musics/efeito_sonoro/estalo.mp3"
    hide arautos
    with dissolve

    V "deixa comigo!"
    play sound "musics/efeito_sonoro/estalo.mp3"

    stop music
    hide arautos
    with dissolve

    scene mapa

    play music "musics/inicio_epico.mp3" fadein 1

    n "O ordeiro e generoso povo do Vale dos Salgueiros vive há oito anos sob o terror e medo do
    feiticeiro Balthus Dire."

    n "Terror, porque o poder dele é realmente aterrorizante,  e medo causados
    pela notícia que acabou chegando aos ouvidos desse povo, vinda dos domínios do feiticeiro, de que
    seus ambiciosos planos de conquista começariam pelo próprio Vale."

    n "Um fiel Semi-Elfo enviado em uma missão de espionagem à Torre Negra voltou galopando para o
    Vale há três dias com uma mensagem desesperada."

    n "Do interior das cavernas de Rocha Escarpada,
    Balthus Dire tinha recrutado um exército de Caóticos e se preparava para atacar com eles o Vale
    dentro de uma semana."

    n "O bom Rei Salamon era um homem de ação. Foram enviados mensageiros por todo o Vale no
    mesmo dia para preparar as defesas e convocar os homens para a guerra."

    n "Foram enviados também cavaleiros à Grande Floresta de Yore para avisar aos Semi-Elfos que moravam lá e fazer um apelo
    para que se aliassem às forças. O Rei Salamon era também um homem sábio."

    n "Ele sabia muito bem que as notícias inevitavelmente chegariam aos ouvidos do Grande Mago de Yore, um mestre da
    magia branca de grandes poderes, que vivia nas profundezas da floresta. O mago era velho e não
    resistiria a uma batalha destas proporções."

    n " Mas ele havia ensinado suas artes a vários jovens magos, e talvez um de seus discípulos de magia ajudasse o rei e seus súditos com coragem e ambição."

    show mc normal at center:
        zoom 0.6
    with dissolve

    n "Você é o aluno brilhante do Grande Mago de Yore. Ele tem sido um Mestre duro, e sua própria
    impaciência muitas vezes foi mais forte do que você. Talvez um pouco precipitadamente, você
    partiu de imediato para a corte de Salamon. O rei recebeu-o entusiasticamente e explicou seu plano."

    n "A batalha poderia ser evitada sem derramamento de sangue se Balthus fosse assassinado antes que
    seu exército pudesse ser reunido."

    n "A missão que você tem pela frente é extremamente perigosa. Balthus Dire está cercado, em sua  Cidadela,
    por uma multidão de criaturas assombrosas. Embora a Magia seja a sua arma mais forte,  haverá momentos em que você terá que confiar em sua espada para sobreviver."

    n "O Rei Salamon expôs a você como seria a sua missão e o advertiu dos perigos que estavam à sua  frente.
    Há um caminho melhor para atravessar a Cidadela. Se você o descobrir, terá êxito com um  mínimo de risco para a sua pessoa.
    Talvez você precise de várias viagens para descobrir o caminho  mais fácil para atravessar a Cidadela"

    n "antes da sua saida, o rei te chama e entrega um saco de couro com um punhado de moedas de ouro para auxiliar na sua jornada."

    $renpy.notify("adquiriu dinheiro!")

    play sound "musics/efeito_sonoro/item encontrado.mp3"

    n "Você deixa o Vale dos Salgueiros na longa caminhada para a Torre Negra. No sopé da colina de  Rocha Escarpada,
    você pode ver sua silhueta contra o céu escuro... "

    $dinheiro = True

    jump um
