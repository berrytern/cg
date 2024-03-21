function drawLineDDA(x1, y1, x2, y2) {
    var dx = x2 - x1;
    var dy = y2 - y1;
    var steps = Math.max(Math.abs(dx), Math.abs(dy));
    var xIncrement = dx / steps;
    var yIncrement = dy / steps;
    
    var x = x1;
    var y = y1;

    var canvas = document.getElementById("myCanvas");
    var ctx = canvas.getContext("2d");

    ctx.clearRect(0, 0, canvas.width, canvas.height); // Limpa o canvas
    ctx.fillStyle = "red"; // Define a cor da linha como vermelha

    for (var i = 0; i <= steps; i++) {
        var pixelX = Math.round(x);
        var pixelY = Math.round(y);
        ctx.fillRect(pixelX, pixelY, 1, 1); // Desenha pixel

        x += xIncrement;
        y += yIncrement;
    }
}

function drawLine() {
    var x1 = parseInt(document.getElementById("x1").value);
    var y1 = parseInt(document.getElementById("y1").value);
    var x2 = parseInt(document.getElementById("x2").value);
    var y2 = parseInt(document.getElementById("y2").value);
    
    drawLineDDA(x1, y1, x2, y2);
}

// Desenha a linha quando a página é carregada
window.onload = function() {
    drawLine();
};
