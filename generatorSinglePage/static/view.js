import { TOOL_LINE,
    TOOL_RECTANGLE,
    TOOL_CIRCLE,
    TOOL_TRIANGLE,
    TOOL_PENCIL,
    TOOL_BRUSH,
    TOOL_PAINT_BUCKET,
    TOOL_ERASER
} from './tool.js';
import Paint from './paint.class.js';


var paint = new Paint('canvas');
paint.activeTool = TOOL_LINE;
paint.lineWidth = 1;
paint.brushSize = 4;
paint.selectedColor = "#000000";
paint.init();

// function get_position_relative_outer_element(x, y){
//     let parent_elem = document.elementFromPoint(x, y).parentNode;
//     let x_relative_elem = x - parent_elem.getBoundingClientRect().left;
//     let y_relative_elem = y - parent_elem.getBoundingClientRect().top;
//     return (x_relative_elem, y_relative_elem);
// }

// function check_proximity_border_window(x, y, delta_percent){
//     let our_elem = document.elementFromPoint(x, y);

//     let relat_left = get_position_relative_outer_element(x, y).x; // left
//     let relat_top = get_position_relative_outer_element(x, y).y; // top
//     let relat_right = our_elem.offsetWidth - get_position_relative_outer_element(x, y).x; // right
//     let relat_bottom = our_elem.offsetHeight - get_position_relative_outer_element(x, y).y; // bottom

//     if(relat_right < relat_left && ((relat_right / our_elem.offsetWidth) < delta_percent))
//         x = our_elem.offsetWidth;
//     if (relat_right > relat_left && (relat_left / our_elem.offsetWidth) < delta_percent)
//         x = 0;
//     if(relat_bottom < relat_top && ((relat_bottom / our_elem.offsetHeight) < delta_percent))
//         y = our_elem.offsetHeight;
//     if(relat_bottom > relat_top && ((relat_top / our_elem.offsetHeight) < delta_percent))
//         y = 0;

//     return (x, y);
// }

document.querySelectorAll("[data-command]").forEach(
    item => {
        item.addEventListener("click", e => {
            let command = item.getAttribute('data-command');
            if(command === "undo"){
                paint.undoPaint();
            } else if(command == "download"){
                var canvas = document.getElementById("canvas");
                var image = canvas.toDataURL("image/png", 1.0).replace("image/png", "image/octet-stream");
                var link = document.createElement("a");
                link.download = "image.png";
                link.href = image;
                link.click();
            }
        });
    }
);

document.querySelectorAll("[data-tool]").forEach(
    item => {
        item.addEventListener("click", e => {
            document.querySelector("[data-tool].active").classList.toggle("active");
            item.classList.toggle("active");

            let selectedTool = item.getAttribute('data-tool');
            paint.activeTool = selectedTool;

            switch(selectedTool){
                case TOOL_LINE:
                case TOOL_RECTANGLE:
                case TOOL_CIRCLE:
                case TOOL_TRIANGLE:
                case TOOL_PENCIL:
                    document.querySelector('.group.for-shapes').style.display = "block";
                    document.querySelector('.group.for-brush').style.display = "none";
                    break;
                case TOOL_BRUSH:
                case TOOL_ERASER:
                    document.querySelector('.group.for-shapes').style.display = "none";
                    document.querySelector('.group.for-brush').style.display = "block";
                    break
                default:
                    document.querySelector('.group.for-shapes').style.display = "none";
                    document.querySelector('.group.for-brush').style.display = "none";
            }
        });
    }
);

document.querySelectorAll("[data-line-width]").forEach(
    item => {
        item.addEventListener("click", e => {
            document.querySelector("[data-line-width].active").classList.toggle("active");
            item.classList.toggle("active");

            let linewidth = item.getAttribute("data-line-width");
            paint.lineWidth = linewidth;
        });
    }
);

document.querySelectorAll("[data-brush-size]").forEach(
    item => {
        item.addEventListener("click", e => {
            document.querySelector("[data-brush-size].active").classList.toggle("active");
            item.classList.toggle("active");

            let brushsize = item.getAttribute("data-brush-size");
            paint.brushSize = brushsize;
        });
    }
);

document.querySelectorAll("[data-color]").forEach(
    item => {
        item.addEventListener("click", e => {
            document.querySelector("[data-color].active").classList.toggle("active");
            item.classList.toggle("active");

            let color = item.getAttribute("data-color");
            paint.selectedColor = color;
        });
    }
);