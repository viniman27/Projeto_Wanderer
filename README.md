# Projeto_Wanderer
Adaptação de uma obra de Steve Jackson para visual novel.

## Baixar e jogar (Windows)

**[Baixar Wanderer 1.1 para Windows — jogo completo](https://github.com/viniman27/Projeto_Wanderer/releases/download/v1.1.0/Wanderer-1.1-Windows.zip)**

1. Baixe o ZIP acima e extraia **todo** o conteúdo.
2. Abra `wanderer_shiroto.exe` na pasta extraída.
3. Se precisar da versão 32 bits, use `wanderer_shiroto-32.exe`.

O executável, o motor Ren'Py e os recursos já estão incluídos. Para jogar, não
é necessário instalar Python ou o SDK. Não mova o `.exe` sozinho para outra pasta.
Use o ZIP **Wanderer-1.1-Windows.zip** da
[página de Releases](https://github.com/viniman27/Projeto_Wanderer/releases/tag/v1.1.0),
não os downloads automáticos “Source code”. O pacote não contém saves pessoais;
se já jogou uma versão antiga, prefira iniciar uma nova partida.

## Guia de finais e rotas — contém spoilers

**[Baixar o guia em PDF](https://github.com/viniman27/Projeto_Wanderer/releases/download/v1.1.0/Guia-de-Finais-Wanderer-1.1.pdf)**

Guia de oito páginas com as condições dos cinco encerramentos, mapa das decisões,
rotas de Dartmol e Viniman, nome secreto, dicas de combate, curiosidades e pontos
úteis para salvar. Inclui limites conhecidos e referências ao código da versão 1.1.

Também disponível para [visualizar no GitHub](docs/Guia-de-Finais-Wanderer-1.1.pdf)
ou [ler em texto](docs/Guia-de-Finais-Wanderer-1.1.md).

## Abrir e editar o jogo

Este repositório contém o projeto editável de Wanderer 1.1: roteiros, imagens,
interface, fontes, músicas e efeitos sonoros. Os scripts e recursos ficam em
`game/`, na estrutura de projeto do Ren'Py.

1. Instale o SDK do [Ren'Py](https://www.renpy.org/). A distribuição original
   utiliza **Ren'Py 7.4.4.1439**; versões mais recentes podem exigir adaptação.
2. Clone este repositório na pasta de projetos configurada no launcher.
3. Atualize a lista de projetos, selecione `Projeto_Wanderer` e clique em
   **Launch Project / Iniciar projeto**. Edite os arquivos `.rpy` em `game/`.

O motor, executáveis, caches, arquivos compilados e saves pessoais não são
versionados. Não é necessário um `archive.rpa`: os recursos estão disponíveis
como arquivos editáveis. Para gerar uma distribuição, use **Build Distributions**
no SDK compatível.

## Validação e limitações conhecidas

- O autor confirmou uma partida nova do início ao fim na distribuição 1.1.
- Testes automatizados de lógica no motor original chegaram do início aos créditos
  nos finais de submissão, alvorecer, lorde e verdadeiro (rota de Dartmol).
  Esses testes não substituem a verificação visual nem cobrem todas as escolhas.
- Saves de versões anteriores podem falhar com
  `NameError: name 'elixirHP_left' is not defined`. Comece uma nova partida;
  a migração desses saves ainda não foi implementada.
- O lint do motor aponta referências de áudio ausentes no material original:
  `musics/musica tensao.mp3`,
  `music/yt1s.com - Magic Fantasy Music  The Mystic  Beautiful Violin.mp3` e
  `musics/efeito_sonoro/fantasma_sussuro.mp3`.

Os créditos originais seguem abaixo. A inclusão de recursos de terceiros não
altera os direitos de seus respectivos autores; confira as permissões aplicáveis
antes de redistribuir ou utilizar esses materiais em outro projeto.


objetivos do projeto:

- por meio desse projeto, queriamos expressar demonstrações artisticas (literatura, artes visuais, musica, entre outros) de forma divertida e acessivel a diversas pessoas.
- tambem queriamos um projeto que fosse divertido de ser feito, para que pudesse ser feito com carinho e amor, dessa forma, com uma qualidade maior.

Esse projeto só foi possivel graças ao material fornecido por:
Editora Marques Saraiva, GDC game audio, Ren'py engine, Breaking Copyrights, netFontes, pngWing, Fantasy Background Music, Rush Garcia, Hiroyuki Sawano e Steve Jackson.

integrantes do grupo:

- André Corrêa (Dartmol203) Product Owner
- Vinicius Assumpção (Viniman27) Scrum Team
- Cesar Umeda (CesarUmeda) Scrum Team
- João Pedro Vaz (JoaoPedro0803) Scrum Master
- Gabriel Roger (GabrielRoger07) Scrum Team

Professor avaliador:

-Sergio Antonio Andrade De Freitas
