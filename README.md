# Calculador de Pot Odds para Poker

O `calculador-potodds-agent` é um agente desenvolvido para calcular as pot odds de uma mão de poker, ajudando jogadores a tomar decisões mais informadas durante o jogo. O agente avalia o tamanho do pot, o valor da aposta necessária para continuar na mão, a aposta atual e a força da mão (equity) para determinar as odds do pot, a rentabilidade de uma call e a equidade necessária para o break even.

## Instalação

Para utilizar o `calculador-potodds-agent`, é necessário ter o Node.js instalado em seu sistema. Siga os passos abaixo para instalar e executar o agente:

1. Clone o repositório do agente para sua máquina local:
```
git clone <URL_DO_REPOSITORIO>
```

2. Navegue até o diretório do agente clonado e instale as dependências:
```
cd calculador-potodds-agent
npm install
```

3. Inicie o agente:
```
npm start
```

## Uso

Após iniciar o agente, você pode enviar dados de entrada via uma requisição HTTP POST para o endpoint fornecido. O formato dos dados de entrada e saída é especificado abaixo.

### Formato de Entrada

Envie um JSON com as seguintes propriedades:

```json
{
  "pot_size": <number>,
  "call_amount": <number>,
  "current_bet": <number>,
  "hand_equity": <number> // opcional, valor entre 0.0 a 1.0
}
```

### Formato de Saída

O agente retorna um JSON com as seguintes propriedades:

```json
{
  "pot_odds_percent": "<string>",
  "is_call_profitable": "<string>",
  "break_even_equity": "<string>"
}
```

### Exemplo

**Entrada:**

```json
{
  "pot_size": 100,
  "call_amount": 10,
  "current_bet": 10,
  "hand_equity": 0.5
}
```

**Saída:**

```json
{
  "pot_odds_percent": "9.1%",
  "is_call_profitable": "Yes",
  "break_even_equity": "9.1%"
}
```

## Endpoint

O endpoint para cálculo de pot odds recebe os dados de entrada no formato especificado acima e retorna os cálculos de pot odds, rentabilidade de call e equidade necessária para break even. Certifique-se de enviar suas requisições para o endpoint correto conforme indicado na documentação de instalação.

## Contribuindo

Sua contribuição para melhorar o `calculador-potodds-agent` é muito bem-vinda. Se você encontrar algum bug ou tiver sugestões de melhorias, por favor, abra uma issue ou um pull request no repositório.

Agradecemos seu interesse e apoio!
