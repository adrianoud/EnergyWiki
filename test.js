interact(".abc").resizable({
  edges: { left: true, right: true, bottom: true, top: true },
  modifiers: [
    interact.modifiers.snapSize({
      targets: [
        interact.snappers.grid({ width: 30, height: 30 }),
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