var oldValue;
function bringToTop(element) {
    oldValue = element.style.zIndex;
    element.style.zIndex = 3;
}

function resetPosition(element) {
    element.style.zIndex = oldValue;
}
