# WANDERER
## Guia de finais, rotas e segredos
Edição para a versão 1.1 • Português brasileiro

Uma missão para salvar o Vale dos Salgueiros. Um trono vazio. E duas entidades que observam suas escolhas com interesse demais.

Este guia explica como encontrar os desfechos da versão 1.1, quais decisões mudam a rota e quais cenas secretas não são finais independentes. O foco são os pontos decisivos: não é um roteiro de todas as salas da Cidadela.

## SPOILERS COMPLETOS
As próximas páginas revelam a traição de Balthus, a identidade dos arautos, a condição do final verdadeiro e o significado da última conversa com o jogador. Para descobrir a história sozinho, guarde o guia para depois da primeira partida.

## O que existe nesta versão
- Cinco encerramentos principais: fracasso, submissão, alvorecer, novo Lorde do Caos e final verdadeiro.
- Um desfecho cíclico: perder para um arauto individual leva ao recomeço da história.
- Um encontro secreto: o nome “caçador de arautos” abre uma batalha alternativa, não um sexto encerramento independente.

## Onde encontrar cada assunto
2 — Preparação e mapa de decisões
3 — Os quatro finais tradicionais
4 — Como desbloquear o final verdadeiro
5 — Dartmol, Viniman e o recomeço
6 — Caçador de arautos: o segredo e sua armadilha
7 — Curiosidades e atalhos da Cidadela
8 — Checklist, limites e fontes

Base: roteiro da versão publicada no repositório Projeto_Wanderer. As instruções distinguem condições confirmadas no código de conclusões sobre o balanceamento. Não há promessa de vencer combates sujeitos à sorte.

---

# Antes de escolher seu destino
## Prepare saves úteis
Comece uma partida nova da versão 1.1. Saves antigos podem não conter variáveis de combate, como elixirHP_left. Preserve os arquivos antigos, mas não dependa deles para seguir este guia.

- Save A: antes de decidir o que fazer com as pequenas criaturas no quarto dos goblins. Este é o ponto mais importante para explorar os dois arautos.
- Save B: antes de escolher entre servir Balthus e lutar contra ele.
- Save C: antes de derrotar a primeira forma de Balthus. O ataque que dá o golpe final decide entre a continuação normal e o segredo.
- Save D: na escolha entre a varanda e o trono, após vencer a rota normal.

Use slots separados. Sobrescrever o save anterior ao quarto dos goblins pode obrigar você a refazer boa parte da aventura para trocar de arauto.

## Mapa dos finais
Ao encontrar Balthus:
- Servir Balthus → final de submissão.
- Lutar e vencer a primeira fase SEM o golpe final de Rugido do Dragão → segunda fase → vencer → escolher varanda ou trono.
- Varanda → final do alvorecer.
- Trono → final do novo Lorde do Caos.
- Lutar e vencer a primeira fase COM o golpe final de Rugido do Dragão → revelação de Balthus → rota dos arautos.

Na rota dos arautos:
- Matou as criaturas do quarto dos goblins → Dartmol → vencer leva ao final verdadeiro.
- Não matou essas criaturas → Viniman → aceitar a proposta leva ao final do lorde; recusar abre a batalha e vencer leva ao final verdadeiro.
- Perder para Dartmol ou Viniman nas batalhas individuais → recomeço.

## Um cuidado com o combate
Tomar um elixir também pode ser seguido por um ataque inimigo. Cure antes de ficar à beira da morte; não trate a cura como um turno gratuito. Os combates principais reinicializam seus próprios recursos, mas isso não torna saves de outra versão compatíveis.

Referências: script.rpy, linhas 2885–2907, 3362–3373, 4968–5066, 5827–5915 e 5994–6100.

---

# Os quatro finais tradicionais
## 1 • Fracasso da missão
Como acessar: perder nos combates que encaminham para final_ruim ou cair numa situação fatal específica. Balthus sobrevive e avança contra sua terra natal.

Duas mortes têm narração própria antes desse mesmo encerramento:
- Poço: quando você grita por ajuda, os supostos salvadores jogam óleo fervente, não uma corda. Falhar nos encantos de escalada também pode levar ao pedido de socorro.
- Ganjees: falsificar um artefato e falhar faz as criaturas sugarem sua alma. Na versão 1.1, o teste exige 8 ou mais num sorteio de 1 a 20: o risco é real. A chance de sucesso é de 65%.

Essas cenas são variantes de morte, não finais adicionais com epílogos separados.

## 2 • Submissão
Na primeira conversa com Balthus, escolha a opção que começa com “confessará que deseja servir o lorde do caos”. Não é necessário vencê-lo em combate.

O mago se alia a Balthus para escapar das antigas amarras, mas ajuda a espalhar a tirania. Mais tarde, Balthus o esfaqueia e descarta seus serviços. A promessa de liberdade termina em submissão e morte.

## 3 • Alvorecer
Escolha “Lutar contra Balthus”. Para manter a rota normal, NÃO dê o golpe que mata a primeira forma com “estilo yore rugido do dragao”. Tormenta das Espadas é uma opção simples para concluir essa fase sem acionar o segredo.

Vença também a segunda forma. No aposento final, escolha “Se dirige a varanda, e contempla a paz conquistada”. O protagonista contempla o mundo que salvou e decide voltar para casa.

## 4 • Novo Lorde do Caos
Siga a mesma rota normal, vença as duas fases e escolha “Se dirige ao trono, e planeja oque fará como novo lorde do caos”. O mago assume o poder, mas o texto descreve uma nova prisão: avareza e arrogância.

Há outra entrada para esse mesmo final: aceitar a proposta de Viniman na rota secreta. Muda o contexto da escolha; o epílogo reutiliza final_lorde.

Referências: script.rpy, label dois02; linhas 2987–3009, 3375–3429, 3577–3617 e 5901–5915.

---

# O caminho do final verdadeiro
## O gatilho é um golpe, não uma sequência de respostas
1. Chegue ao encontro com Balthus e escolha lutar.
2. Enfrente a PRIMEIRA forma. Você ainda está na batalha anterior à transformação dele.
3. Reduza a vida de Balthus sem matá-lo com outro ataque.
4. Termine essa fase usando “estilo yore rugido do dragao”. O ataque precisa reduzir o HP do inimigo a zero ou menos.
5. Acompanhe a revelação e vença o arauto da sua rota. No caso de Viniman, recuse a proposta antes de lutar.

## Como evitar perder o gatilho
Rugido do Dragão causa de 6 a 14 de dano e consome 6 de mana. Com Balthus abaixo de 15 HP, ele já pode encerrar a luta, mas o resultado depende do dano sorteado. Se ele sobreviver, mantenha o mago vivo e use o ataque de novo.

Se Balthus estiver com 6 HP ou menos, qualquer resultado de dano desse feitiço basta, desde que você tenha mana. Não é obrigatório deixá-lo exatamente nesse valor.

O detalhe decisivo: usar Rugido em algum momento não basta. Ele precisa ser o golpe final da primeira fase. Usá-lo na segunda forma não desbloqueia o segredo.

## A revelação de Balthus
Em vez de simplesmente continuar para a segunda fase normal, o roteiro entra em segredo. Balthus conta que os arautos prometeram elevá-lo a um deles se conquistasse a região. Ele percebeu tarde demais que havia se tornado um instrumento. Antes de morrer, deixa ao mago novos poderes e um aviso.

## O que o final revela
Depois de vencer um arauto, o outro permite que vocês escolham seu futuro. O mago fala diretamente com o jogador em um vazio. Uma presença misteriosa intervém, os cenários se sucedem e a jornada chega à antiga casa do protagonista.

A presença chama o mago de Tsugausa e o jogador de “invasor”. O encerramento oferece ao mago paz e liberdade de escolha, e termina nos créditos. O texto não explica completamente quem é essa presença: isso permanece uma pergunta da história, não um enigma com solução confirmada neste guia.

Referências: script.rpy, linhas 5008–5024, 5827–5853 e 6167–6382.

---

# Dois arautos, um mesmo encerramento
## Dartmol • Arauto da Destruição
Para escolhê-lo, passe pelo portal central e, no quarto com pequenas criaturas verdes e brinquedos, escolha “Desembainhará a sua espada e se preparará para lutar contra eles?”. A cena mata as criaturas sem resistência e registra morte_goblins = True.

Depois, desbloqueie o segredo com Rugido do Dragão na primeira fase de Balthus. Dartmol aparece e a luta começa; nessa conversa não há proposta de aliança.

Ao vencer, Viniman surge, recolhe o corpo do irmão e reconhece a liberdade do mago e do jogador. A próxima sequência é final_real.

## Viniman • Arauto da Criação
Não mate as pequenas criaturas. Você pode atravessar o quarto sem atacá-las ou oferecer amoras, caso tenha o item. Também pode chegar à torre por um desvio que não passe por essa matança.

Desbloqueie o mesmo segredo na batalha de Balthus. Viniman apresenta uma proposta:
- “juntar-se a eles” → aceitar terminar o que Balthus começou → final_lorde.
- “recusar a proposta” → batalha contra Viniman → vencer → Dartmol aparece e concede a escolha do próprio futuro → final_real.

Essas duas vitórias têm cenas intermediárias distintas, mas chegam ao mesmo final verdadeiro. Não são dois epílogos finais separados.

## Dicas para as batalhas individuais
Os dois confrontos começam com o arauto em 250 HP e o mago em 120 HP. Tormenta das Espadas causa 15 de dano sem gastar mana; Rugido permanece entre 6 e 14. Para dano direto por ação, a espada é mais forte que o Rugido nesses encontros.

Os elixires de vida curam 25 HP aqui. O arauto pode atacar depois da cura. Há sorte nos ataques e oportunidades automáticas de contra-ataque: nenhuma sequência de botões é uma garantia universal de vitória.

## Se você perder: o ciclo
A derrota individual leva a recomeco. Os arautos decidem tentar novamente e a introdução retorna, seguida pela aventura. Não há créditos nesse desfecho.

O roteiro usa um salto para recontar a história, não uma reinicialização completa de todas as variáveis. Para explorar outra rota a partir de um estado limpo, use uma nova partida ou um save anterior apropriado, não presuma que o ciclo apagou suas escolhas.

Referências: script.rpy, linhas 2885–2928, 5827–6165 e 6510–6599.

---

# O nome que abre outra porta
## “Caçador de arautos”
Comece uma nova partida. Quando o jogo pedir o nome, digite exatamente uma destas formas:
- caçador de arautos
- CAÇADOR DE ARAUTOS

O código compara essas duas grafias diretamente. Não conte com uma variação como “Caçador de Arautos”, sem cedilha ou com espaços extras.

Após a introdução, você é transportado para um plano de gelo e fogo e surpreende os dois arautos. Isso entra em final_alt e depois batalha_arautos.

## Por que não é outro final completo?
O nome do label engana: final_alt é uma entrada alternativa para um confronto. Se perder, o jogo usa final_ruim. O ramo escrito para uma vitória leva de volta à aventura em dois51, não a créditos nem ao final verdadeiro.

Este encontro também é diferente das batalhas individuais da rota secreta. Não use a senha esperando pular diretamente para final_real.

## Uma armadilha de balanceamento
A dupla tem 500 HP. O mago começa com 60 HP, recebe 10 elixires que curam 15 HP e sofre 10 de dano em cada resposta inimiga. Seu ataque mais forte nessa luta alcança no máximo 12 de dano.

Mesmo num limite generoso, ignorando o gasto de turnos com cura e os limites de mana, o total de vida inicial mais cura seria 210: caberiam no máximo 21 ações antes da derrota. Se cada uma causasse o máximo de 12 de dano, seriam apenas 252 de dano — abaixo dos 500 necessários.

Conclusão de análise do código: o ramo de vitória existe, mas não há recursos suficientes para uma vitória normal com essas regras, sem alterar o estado do jogo ou explorar algum comportamento externo a esse combate. O guia não atribui uma intenção ao autor; apenas distingue uma saída escrita de uma saída viável.

## Outra pista discreta
Na sacada dos três portais, o narrador descreve o desenho de um pássaro semelhante a uma andorinha e a trilha se chama “easter egg.mp3”. Essa cena, por si só, não abre uma escolha secreta nem comprova uma interpretação específica da referência.

Referências: script.rpy, linhas 300–303, 2798–2816 e 6384–6508. O limite de dano acima é uma dedução das regras dessa batalha.

---

# Curiosidades e atalhos da Cidadela
## Os três portais mudam mais que o cenário
Na sacada, o portal da esquerda leva à porta do quarto de Lucretia; o central leva ao quarto das pequenas criaturas; o da direita leva à sala da gárgula. Esses desvios convergem novamente para a subida da torre.

O quarto central é especialmente importante porque a matança ali escolhe Dartmol na rota secreta. Se quiser Viniman, não precisa procurar uma resposta “boa” em todos os diálogos: o teste desse desvio consulta especificamente morte_goblins.

## Racknee não é só um item
Ao mostrar a aranha no vidro aos Ganjees, eles a reconhecem como Racknee. Fazer um acordo leva à passagem negociada. Jogar o vidro no chão provoca uma batalha para vingar o amigo. É uma pequena história opcional dentro de uma escolha de inventário.

A opção de falsificar um artefato pode ser útil quando faltam itens, mas não é passagem garantida: exige 8 ou mais no d20 e a falha termina em morte.

## A hidra tem três soluções
- Espada: na abordagem inicial, um sorteio de 1 a 7 pode acertar a cabeça primordial se sair 3. Esse resultado permite passar sem o combate completo; os outros resultados levam à luta.
- Cópia de criatura: exige 13 ou mais no d20, uma chance de 40%. O sucesso invoca a hidra reversa, com aparência exótica, e abre uma batalha entre criaturas. A falha não encerra imediatamente a aventura: ainda há a escolha entre o véu e a espada.
- Véu de ouro: se você tiver o item, a hidra recua e permite alcançar a porta. Ela toma o véu durante a passagem.

## Dois jeitos de encenar a queda de Balthus
Na segunda fase normal, o golpe final direto de Tormenta das Espadas leva à cena facada: o mago rejeita a última proposta de Balthus e o apunhala. A outra saída da batalha leva à sequência morte_balthus, com animação própria.

Ambas chegam à mesma escolha de varanda ou trono. Uma cena de morte diferente não cria um final adicional. Um contra-ataque automático também pode encerrar a batalha pela saída comum, em vez da cena específica do ataque selecionado.

## Algumas armadilhas podem ser evitadas
No grande salão de jantar, a escada esquerda vira uma rampa e pede uma reação; a direita segue para a sacada sem esse teste. Investigar as armaduras rende um golpe surpresa, não um final secreto. Exploração nem sempre significa recompensa.

Referências: script.rpy, linhas 2726–2816, 2987–3164, 3275–3359, 3482–3575 e 5100–5177.

---

# Checklist de explorador
## Para ver os cinco encerramentos
- Fracasso: veja uma derrota que chega a final_ruim.
- Submissão: ofereça seus serviços a Balthus.
- Alvorecer: vença a rota normal e escolha a varanda.
- Novo Lorde: escolha o trono ou aceite o pacto de Viniman.
- Verdadeiro: mate a primeira forma de Balthus com Rugido do Dragão e vença um arauto individual; recuse o pacto se encontrar Viniman.

## Para conhecer as variações
- Veja o final verdadeiro tanto pela vitória sobre Dartmol quanto pela vitória sobre Viniman.
- Observe a diferença entre a cena da facada e a outra morte de Balthus.
- Experimente negociar por Racknee e compare com quebrar o vidro.
- Teste o nome secreto sabendo que ele abre outro combate, não um atalho ao final verdadeiro.
- Veja o recomeço ao perder para um arauto individual, sem confundi-lo com uma nova partida limpa.

## O que foi verificado
As condições descritas foram conferidas em game/script.rpy da versão 1.1. Testes automatizados anteriores percorreram do início aos créditos as rotas de submissão, alvorecer, lorde e verdadeiro via Dartmol. Esses testes automatizam diálogos e escolhas; não equivalem a uma inspeção visual de todas as ramificações.

O acesso via Viniman, as cenas opcionais e o balanceamento da batalha dupla foram analisados no código. O autor também confirmou uma partida completa na distribuição 1.1. O guia não afirma que todas as combinações de escolhas ou todos os saves antigos foram testados.

## Fonte e edição
Roteiro de referência: game/script.rpy, no commit c31b9076fb85befe99037878d3957a61884904fa do repositório viniman27/Projeto_Wanderer. Os intervalos de linhas nas páginas anteriores se referem a essa revisão.

Código e créditos: https://github.com/viniman27/Projeto_Wanderer
Roteiro de referência: https://github.com/viniman27/Projeto_Wanderer/blob/c31b9076fb85befe99037878d3957a61884904fa/game/script.rpy
Jogo pronto para Windows: https://github.com/viniman27/Projeto_Wanderer/releases/tag/v1.1.0

Este é um guia do projeto Wanderer, não um guia de todas as versões da obra que o inspirou. Os nomes, personagens e recursos mantêm os créditos e direitos de seus respectivos autores. As descrições dos desfechos foram resumidas para orientar a exploração.

Boa viagem pela Cidadela. O trono é opcional; as consequências, não.
