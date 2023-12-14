let angulo
let comprimentoRamo

function setup() {
  createCanvas(800, 600)
  angulo = PI / 4
  comprimentoRamo = 100
}

function draw() {
  background(255)
  stroke(0)
  translate(width / 2, height)
  ramo(comprimentoRamo, 8)
}

function ramo(comprimento, espessura) {
  strokeWeight(espessura)
  line(0, 0, 0, -comprimento)

  translate(0, -comprimento)

  if (comprimento > 4) {
    push()
    rotate(angulo)
    ramo(comprimento * 0.67, espessura * 0.7)
    pop()

    push()
    rotate(-angulo)
    ramo(comprimento * 0.67, espessura * 0.7)
    pop()
  }
}
