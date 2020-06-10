import Point from './point.model.js'

export function getMouseCoordsOnCanvas(e, canvas){
    let rect = canvas.getBoundingClientRect();
    let x = Math.round(e.clientX - rect.left);
    let y = Math.round(e.clientY - rect.top);
    return new Point(x, y);
}

export function findDistance(coord1, coord2){
    let exp1 = Math.pow(coord1.x - coord2.x, 2);
    let exp2 = Math.pow(coord1.y - coord2.y, 2);
    return Math.sqrt(exp1 + exp2);
}

