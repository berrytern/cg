'use strict'

// tamanho da tela
const LARGURA = 600;
const ALTURA = 600;

//Eventos


// intervalo de entrada
// const INTERVALO_X_INPUT = [-parseInt(LARGURA / 2), parseInt(LARGURA / 2)];
// const INTERVALO_Y_INPUT = [-parseInt(ALTURA / 2), parseInt(ALTURA / 2)];

// intervalo NDC: [-1, 1] para X e Y
const INTERVALO_X_NDC = [-1, 1];
const INTERVALO_Y_NDC = [-1, 1];

// resolução de saída DC (screen)
const INTERVALO_X_DC = [0, LARGURA];
const INTERVALO_Y_DC = [0, ALTURA];

//Função da lib p5.js
function setup() {
    let canvas = createCanvas(LARGURA, ALTURA);
    canvas.parent('#plano');
    background(0);

};

function inp_to_ndc(x, y, intervalo_inp_x, intervalo_inp_y) {
    let [xmin, xmax] = intervalo_inp_x;
    let [ymin, ymax] = intervalo_inp_y;
    let ndcx = ((2 * (x - xmin)) / (xmax - xmin)) - 1;
    let ndcy = ((2 * (y - ymin)) / (ymax - ymin)) - 1;

    console.log([`ndcx: ${ndcx}`, `ndcy: ${ndcy}`]);
    return [ndcx, ndcy];
}

function ndc_to_dc(ndcx, ndcy, intervalo_dc_x, intervalo_dc_y) {
    let [ndh, ndv] = [intervalo_dc_x[1], intervalo_dc_y[1]];
    let dcx = Math.round(((ndcx + 1) * (ndh - 1)) / 2);
    let dcy = Math.round(((ndcy + 1) * (ndv - 1)) / 2);

    console.log([`dcx: ${dcx}`, `dcy: ${dcy}`]);
    return [dcx, dcy];
}

function inp_to_dc(x, y, intervalo_inp_x, intervalo_inp_y) {
    const [ndcx, ndcy] = [inp_to_ndc(x, y, intervalo_inp_x, intervalo_inp_y)[0], inp_to_ndc(x, y, intervalo_inp_x, intervalo_inp_y)[1]];

    return ndc_to_dc(ndcx, ndcy, INTERVALO_X_DC, INTERVALO_Y_DC);
}

function desenharPixel(x, y, cor = "red") {
    stroke(255, 0, 0);
    strokeWeight(2)
    point(x, y); 
}

//Função da lib p5.js
function draw() {
    document.querySelector('#desenhar').onclick = () => {
        background(0);
        // inputs do html
        const x = parseFloat(document.querySelector('#x').value);
        const xMax = parseFloat(document.querySelector('#xMax').value);
        const xMin = parseFloat(document.querySelector('#xMin').value);
        const y = parseFloat(document.querySelector('#y').value);
        const yMax = parseFloat(document.querySelector('#yMax').value);
        const yMin = parseFloat(document.querySelector('#yMin').value);

        let [xFinal, yFinal] = inp_to_dc(x, y, [xMin, xMax], [yMin, yMax]);

        if (xFinal && yFinal) {
            desenharPixel(xFinal, ALTURA - yFinal);
        }

        const [ndcx, ndcy] = inp_to_ndc(x, y, [xMin, xMax], [yMin, yMax]);
        const [dcx, dcy] = ndc_to_dc(ndcx, ndcy, INTERVALO_X_DC, INTERVALO_Y_DC);

        
        document.getElementById('inp_to_ndc_info').innerHTML = `inp_to_ndc:<br>x: ${ndcx.toFixed(2)}, y: ${ndcy.toFixed(2)}`;
        document.getElementById('ndc_to_dc_info').innerHTML = `ndc_to_dc:<br>x: ${dcx}, y: ${dcy}`;
        document.getElementById('inp_to_dc_info').innerHTML = `inp_to_dc:<br>x: ${xFinal}, y: ${yFinal}`;

        updatePixels();
    }
}

