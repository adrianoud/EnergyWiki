var targetElement;
$(document).ready(function(){
// 可以直接类选择使用 interact(“.draggable”) 省去使用ByClass和迭代
    targetElement =  document.getElementsByClassName("draggable");
//    alert(targetElement[1].getAttribute("id"))
    for(var k =0, length = targetElement.length; k< length; k++){
        interact(targetElement[k])
        .draggable({
            // enable inertial throwing
            modifiers: [
                interact.modifiers.snap({
                    targets: [
                        interact.snappers.grid({ x: 10, y: 10 })
                    ],
                    range: Infinity,
                    relativePoints: [ { x: 0, y: 0 } ]
                }),
            ],

            inertia: true,
            // keep the element within the area of it's parent
    //        modifiers: [
    //            interact.modifiers.restrictRect({
    //                restriction: 'parent',
    //                endOnly: true
    //            })
    //        ],
            // enable autoScroll
            autoScroll: true,

            listeners: {
                // call this function on every dragmove event
                move: dragMoveListener,

                // call this function on every dragend event
    //            end(event) {
    //                var textEl = event.target.querySelector('p')
    //
    //                textEl && (textEl.textContent =                           // 与运算，处理textEL 不存在情况，不存在即不执行
    //                    'moved a distance of ' +
    //                    (Math.sqrt(Math.pow(event.pageX - event.x0, 2) +
    //                        Math.pow(event.pageY - event.y0, 2) | 0))
    //                    .toFixed(2) + 'px')
    //            }
            }
        })
        .resizable({
                // resize from all edges and corners
            edges: { left: true, right: true, bottom: true, top: true },
            modifiers: [
                interact.modifiers.snapSize({
                    targets: [
                        interact.snappers.grid({ width: 10, height: 10 }),
                    ],
                }),
            ],
            listeners: {
              move (event) {
                var target = event.target
                var x = (parseFloat(target.getAttribute('data-x')) || 0)
                var y = (parseFloat(target.getAttribute('data-y')) || 0)

                // update the element's style
                target.style.width = event.rect.width + 'px'
                target.style.height = event.rect.height + 'px'

                // translate when resizing from top or left edges
                x += event.deltaRect.left
                y += event.deltaRect.top

                target.style.transform = 'translate(' + x + 'px,' + y + 'px)'

                target.setAttribute('data-x', x)
                target.setAttribute('data-y', y)
    //            target.textContent = Math.round(event.rect.width) + '\u00D7' + Math.round(event.rect.height)
              },
              end (event){
                if (event.target.getAttribute("id") == 'map'){
                    update_map();
                }
                else if(event.target.getAttribute("id") == 'bar'){
                    update_bar();
                }
              },
            },
        })
    }
})


// target elements with the "draggable" class


function dragMoveListener(event) {
    var target = event.target
        // keep the dragged position in the data-x/data-y attributes
    var x = (parseFloat(target.getAttribute('data-x')) || 0) + event.dx
    var y = (parseFloat(target.getAttribute('data-y')) || 0) + event.dy     // 或运算 处理空数据情况，设为0 ‘ ’|| 0 为 0

    // translate the element
    target.style.webkitTransform =
        target.style.transform =
        'translate(' + x + 'px, ' + y + 'px)'

    // update the position attributes
    target.setAttribute('data-x', x)
    target.setAttribute('data-y', y)
}

// this function is used later in the resizing and gesture demos
//window.dragMoveListener = dragMoveListener