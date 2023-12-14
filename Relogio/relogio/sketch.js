const larguraCanvas = 800
const alturaCanvas = 600

const raio = 200
const raioHora = raio * 0.5
const raioMinutos = raio * 0.7
const raioSegundos = raio * 0.9

function setup() {
  createCanvas(larguraCanvas, alturaCanvas)
}

function obterGrausMinuto(minuto) {
  return map(minuto, 0, 60, -HALF_PI, TWO_PI - HALF_PI)
}

function obterGrausHora(hora) {
  return map(hora % 12, 0, 12, -HALF_PI, TWO_PI - HALF_PI)
}

function obterGrausSegundo(segundo) {
  return map(segundo % 60, 0, 60, -HALF_PI, TWO_PI - HALF_PI)
}

function draw() {
  background(1, 1, 1)
  translate(width / 2, height / 2)
  desenharMostradorRelogio()

  const horaAtual = hour() - 12
  const minutoAtual = minute()
  const segundoAtual = second()

  const anguloHora =
    obterGrausHora(horaAtual) + map(minutoAtual, 0, 60, 0, PI / 6)
  const anguloMinuto = obterGrausMinuto(minutoAtual)
  const anguloSegundo = obterGrausSegundo(segundoAtual)

  desenharPonteiroRelogio(raioHora, anguloHora, 5)
  desenharPonteiroRelogio(raioMinutos, anguloMinuto, 3)
  desenharPonteiroRelogio(raioSegundos, anguloSegundo, 1)
}

function desenharMostradorRelogio() {
  strokeWeight(3)
  circle(0, 0, raio * 2)
}

function desenharPonteiroRelogio(raioPonteiro, angulo, espessura) {
  strokeWeight(espessura)
  line(0, 0, raioPonteiro * cos(angulo), raioPonteiro * sin(angulo))
}
